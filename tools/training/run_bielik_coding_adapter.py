"""CPU LoRA from public GGUF, executable holdout and Polish regression gate."""
import os,json,time,hashlib,types,subprocess,sys,gc
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
os.environ['HF_HUB_OFFLINE']='1';os.environ['TRANSFORMERS_OFFLINE']='1';os.environ['TOKENIZERS_PARALLELISM']='false';os.environ['OMP_NUM_THREADS']='2';os.environ['MKL_NUM_THREADS']='2'
sys.path.insert(0,str(ROOT/'runtime/pydeps'));sys.path.insert(0,str(ROOT/'src'));sys.path.insert(0,str(ROOT/'tools/testing'))
from coding_checks import assess

def dump(path,data):path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
def sha(path):
    with Path(path).open('rb') as stream:return hashlib.file_digest(stream,'sha256').hexdigest()

def main():
    import torch,psutil
    from peft import LoraConfig,TaskType,get_peft_model
    from ai_si.integrations.bielik_polish import PolishLanguage,MODEL
    datasets={key:json.loads((ROOT/'data/coding_adapter'/filename).read_text(encoding='utf-8')) for key,filename in [('train','train.json'),('holdout','holdout.json'),('polish','polish_regression.json')]}
    assert not {r['prompt'] for r in datasets['train']}&{r['prompt'] for r in datasets['holdout']}
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--resume',type=Path);args=parser.parse_args()
    run=args.resume.resolve() if args.resume else ROOT/'artifacts/bielik_coding_adapter'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    if args.resume and not run.is_relative_to((ROOT/'artifacts/bielik_coding_adapter').resolve()):raise ValueError('Resume outside experiment directory')
    run.mkdir(parents=True,exist_ok=bool(args.resume))
    plan={'seed':42,'epochs':3,'learning_rate':.0003,'rank':4,'alpha':8,'layers':[28,29,30,31],'target_modules':['q_proj','v_proj'],'max_train_seconds':900,'max_sequence_tokens':256,'generation_tokens':160,'dataset_hashes':{f:sha(ROOT/'data/coding_adapter'/f) for f in ('train.json','holdout.json','polish_regression.json')},'base_sha256':sha(MODEL),'acceptance':'More fully correct holdout tasks AND no fewer passing Polish checks; otherwise candidate stays inactive. Single pilot, no tuning on final holdout.','checker_sha256':sha(ROOT/'tools/testing/coding_checks.py'),'worker_sha256':sha(ROOT/'tools/testing/coding_worker.py'),'protocol_note':'Small constant powers enabled after initial baseline rejected a valid square expression. Aborted initial run remains archived; no training used those results.','base_reconstruction':'Q8_0 dequantization into bfloat16 RAM; full base never saved or updated.'}
    if args.resume:
        original=json.loads((run/'plan.json').read_text(encoding='utf-8'))
        if original!=plan:raise ValueError('Resume plan changed')
        report=json.loads((run/'report.json').read_text(encoding='utf-8'))
        if report.get('steps') or 'coding_passed' not in report.get('before',{}):raise ValueError('Only pre-training resume with complete baseline supported')
    else:
        dump(run/'plan.json',plan);dump(run/'dataset.json',datasets)
        report={'status':'BASELINE','run':str(run),'plan':plan,'steps':[]};dump(run/'report.json',report)
    print('RUN',run,flush=True)
    def evaluate(language,stage):
        results={'coding':[],'polish':[]};report[stage]=results
        for row in datasets['holdout']:
            answer=language.reply(row['prompt'],max_tokens=plan['generation_tokens']);result={'id':row['id'],'answer':answer,'assessment':assess(answer,row['cases'])};results['coding'].append(result);dump(run/'report.json',report);print(stage,row['id'],result['assessment']['passed'],flush=True)
        for row in datasets['polish']:
            answer=language.reply(row['prompt'],max_tokens=32);results['polish'].append({'id':row['id'],'answer':answer,'passed':row['contains'].casefold() in answer.casefold()});dump(run/'report.json',report)
        results['coding_passed']=sum(r['assessment']['passed'] for r in results['coding']);results['polish_passed']=sum(r['passed'] for r in results['polish']);dump(run/'report.json',report)
    if not args.resume:
        language=PolishLanguage()
        try:evaluate(language,'before')
        finally:language.close()
    report['status']='PREPARING_TRAINING';dump(run/'report.json',report)
    from bielik_training_base import load_base
    model,tokenizer,cache=load_base()
    torch.manual_seed(42);torch.set_num_threads(2)
    def portable(layer,inputs):
        return torch.nn.functional.linear(inputs.float(),layer.weight.float(),layer.bias.float() if layer.bias is not None else None).to(inputs.dtype)
    for layer in model.modules():
        if isinstance(layer,torch.nn.Linear):layer.forward=types.MethodType(portable,layer)
    model.config.use_cache=False
    model=get_peft_model(model,LoraConfig(task_type=TaskType.CAUSAL_LM,r=plan['rank'],lora_alpha=plan['alpha'],lora_dropout=0,target_modules=plan['target_modules'],layers_to_transform=plan['layers'],bias='none'))
    trainable=[v for v in model.parameters() if v.requires_grad];report['trainable_parameters']=sum(v.numel() for v in trainable);report['frozen_parameters']=sum(v.numel() for v in model.parameters() if not v.requires_grad)
    batches=[]
    for row in datasets['train']:
        messages=[{'role':'system','content':'Odpowiadaj po polsku, krótko i jasno. Nie udawaj, że sprawdziłeś internet. Gdy brakuje informacji, powiedz o tym.'},{'role':'user','content':row['prompt']}]
        prompt=tokenizer.apply_chat_template(messages,tokenize=True,add_generation_prompt=True)
        full=tokenizer.apply_chat_template(messages+[{'role':'assistant','content':row['code']}],tokenize=True,add_generation_prompt=False)
        if full[:len(prompt)]!=prompt:raise ValueError('Answer mask mismatch')
        if len(full)>plan['max_sequence_tokens']:raise ValueError('Training sequence too long')
        ids=torch.tensor([full]);labels=ids.clone();labels[:,:len(prompt)]=-100;batches.append({'input_ids':ids,'attention_mask':torch.ones_like(ids),'labels':labels})
    optimizer=torch.optim.AdamW(trainable,lr=plan['learning_rate'],weight_decay=0);started=time.monotonic();report['status']='TRAINING';dump(run/'report.json',report)
    import random
    for epoch in range(plan['epochs']):
        order=list(range(len(batches)));random.Random(42+epoch).shuffle(order)
        for index in order:
            if time.monotonic()-started>plan['max_train_seconds'] or psutil.virtual_memory().available<.5*2**30:
                report['stop_reason']='RESOURCE_LIMIT';break
            tick=time.perf_counter();model.train();optimizer.zero_grad(set_to_none=True);loss=model(**batches[index]).loss
            if not torch.isfinite(loss):raise ValueError('Non-finite loss')
            loss.backward();torch.nn.utils.clip_grad_norm_(trainable,1,error_if_nonfinite=True);optimizer.step()
            result={'step':len(report['steps'])+1,'task':datasets['train'][index]['id'],'epoch':epoch+1,'loss':float(loss.detach()),'seconds':time.perf_counter()-tick,'rss_bytes':psutil.Process().memory_info().rss};report['steps'].append(result);dump(run/'report.json',report);print('STEP',json.dumps(result),flush=True)
        if report.get('stop_reason'):break
    if not report['steps']:raise RuntimeError('No training steps completed')
    adapter=run/'adapter';model.save_pretrained(adapter,safe_serialization=True,save_embedding_layers=False)
    report['adapter_bytes']=sum(p.stat().st_size for p in adapter.rglob('*') if p.is_file())
    state={name:value.detach().clone() for name,value in model.named_parameters() if value.requires_grad}
    # Reload exact saved adapter before export and compare learned tensors.
    model.load_adapter(str(adapter),adapter_name='reload',is_trainable=False)
    from peft.utils.save_and_load import get_peft_model_state_dict
    a=get_peft_model_state_dict(model,adapter_name='default');b=get_peft_model_state_dict(model,adapter_name='reload')
    for name in a:torch.testing.assert_close(a[name],b[name],rtol=0,atol=0)
    report['serialization_verified']=True;report['adapter_weight_sha256']=sha(adapter/'adapter_model.safetensors')
    del optimizer,trainable,model,state,a,b;gc.collect()
    env=os.environ.copy();env['PYTHONPATH']=str(ROOT/'runtime/pydeps');env['NO_LOCAL_GGUF']='1'
    gguf_path=run/'adapter.gguf'
    command=[sys.executable,str(ROOT/'runtime/lora_export/convert_lora_to_gguf.py'),str(adapter),'--base',str(cache),'--outfile',str(gguf_path),'--outtype','f32']
    converted=subprocess.run(command,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=120);(run/'export.log').write_text(converted.stdout+'\n'+converted.stderr,encoding='utf-8')
    if converted.returncode:raise RuntimeError('Adapter GGUF export failed; see export.log')
    report['status']='FINAL_EVALUATION';report['adapter_gguf_bytes']=gguf_path.stat().st_size;dump(run/'report.json',report)
    language=PolishLanguage(adapter_path=gguf_path)
    try:evaluate(language,'after')
    finally:language.close()
    unchanged=sha(MODEL)==plan['base_sha256'];report['base_unchanged']=unchanged
    accepted=unchanged and report['after']['coding_passed']>report['before']['coding_passed'] and report['after']['polish_passed']>=report['before']['polish_passed']
    report['status']='ACCEPTED' if accepted else 'REJECTED_NO_PROVEN_IMPROVEMENT';report['candidate_active']=accepted
    if accepted:dump(ROOT/'artifacts/bielik_coding_adapter/active.json',{'path':str(gguf_path),'sha256':sha(gguf_path),'report':str(run/'report.json'),'base_sha256':plan['base_sha256']})
    dump(run/'report.json',report);print('FINAL',report['status'],'before',report['before']['coding_passed'],'after',report['after']['coding_passed'],flush=True)
if __name__=='__main__':main()
