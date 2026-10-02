"""Stream public Q8_0 weights into RAM; never save a duplicate full model."""
import gc,json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'runtime/pydeps'));sys.path.insert(0,str(ROOT/'src'))
def load_base():
    import numpy as np,torch,gguf
    from transformers import AutoConfig,AutoModelForCausalLM,AutoTokenizer
    from transformers.modeling_gguf_pytorch_utils import load_gguf_checkpoint,get_gguf_hf_weights_map,LlamaTensorProcessor
    from ai_si.integrations.bielik_polish import MODEL
    metadata=load_gguf_checkpoint(str(MODEL),return_tensors=False)
    if metadata['config']['model_type']!='llama':raise ValueError('Only tested Llama mapping supported')
    cache=ROOT/'artifacts/bielik_training_tokenizer';cache.mkdir(parents=True,exist_ok=True)
    reader=gguf.GGUFReader(str(MODEL));tensor_names={t.name for t in reader.tensors}
    conf=dict(metadata['config']);conf.pop('model_type');conf['attention_bias']=any('.attn_q.bias' in name for name in tensor_names);conf['mlp_bias']=any('.ffn_gate.bias' in name for name in tensor_names);config=AutoConfig.for_model('llama',**conf);config.architectures=['LlamaForCausalLM'];config.save_pretrained(cache)
    if (cache/'tokenizer.json').exists():tokenizer=AutoTokenizer.from_pretrained(cache,local_files_only=True)
    else:
        print('Preparing tokenizer once...',flush=True)
        tokenizer=AutoTokenizer.from_pretrained(MODEL.parent,gguf_file=MODEL.name,local_files_only=True)
        tokens=metadata['tokenizer']['tokens']
        tokenizer.eos_token=tokens[config.eos_token_id];tokenizer.bos_token=tokens[config.bos_token_id];tokenizer.pad_token=tokens[config.pad_token_id]
        tokenizer.save_pretrained(cache)
    torch.set_num_threads(2)
    with torch.device('meta'):model=AutoModelForCausalLM.from_config(config,dtype=torch.bfloat16,attn_implementation='eager')
    mapping=get_gguf_hf_weights_map(model);processor=LlamaTensorProcessor(metadata['config']);loaded=set()
    from accelerate.utils import set_module_tensor_to_device
    start=time.perf_counter()
    for i,tensor in enumerate(reader.tensors):
        if tensor.name not in mapping:raise ValueError('Unmapped tensor '+tensor.name)
        weights=gguf.dequantize(tensor.data,tensor.tensor_type)
        weights=processor.process(weights,tensor.name).weights
        value=torch.from_numpy(np.ascontiguousarray(weights)).to(torch.bfloat16)
        name=mapping[tensor.name];set_module_tensor_to_device(model,name,'cpu',value=value);loaded.add(name)
        del weights,value
        if i%30==0:print('Loaded',i,'/',len(reader.tensors),flush=True)
    expected=set(dict(model.named_parameters()))
    if expected-loaded:raise ValueError('Missing weights '+str(expected-loaded))
    from transformers.models.llama.modeling_llama import LlamaRotaryEmbedding
    model.model.rotary_emb=LlamaRotaryEmbedding(config=config,device='cpu')
    del reader;gc.collect();model.eval()
    print('Public GGUF loaded for adapter training:',round(time.perf_counter()-start,1),'s',flush=True)
    return model,tokenizer,cache
