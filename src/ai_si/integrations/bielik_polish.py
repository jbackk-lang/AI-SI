"""Local Polish language generation, separate from verified SI facts."""
from pathlib import Path
import atexit,json,socket,subprocess,time,urllib.request,os
ROOT=Path(__file__).resolve().parents[3]
MODEL=Path(os.environ.get('SI_MODEL_PATH',str(ROOT/'models/Bielik-1.5B-v3.0-Instruct-GGUF/Bielik-1.5B-v3.0-Instruct.Q8_0.gguf')))
class PolishLanguage:
    def __init__(self,adapter_path=None,use_active=False):
        if use_active and adapter_path is None:
            from ai_si.integrations.bielik_adapter_selection import select_active
            adapter_path=select_active()
        with socket.socket() as s:
            s.bind(('127.0.0.1',0)); port=s.getsockname()[1]
        self.url=f'http://127.0.0.1:{port}'
        logdir=ROOT/'artifacts/bielik_polish';logdir.mkdir(parents=True,exist_ok=True)
        self.log=(logdir/'server.log').open('w',encoding='utf-8')
        command=[str(Path(os.environ.get('SI_LLAMA_SERVER',str(ROOT/'runtime/llama-cpu/llama-server.exe')))),'-m',str(MODEL),'-c','4096','-t','4','--host','127.0.0.1','--port',str(port)]
        if adapter_path is not None:
            candidate=Path(adapter_path).resolve(strict=True)
            if not candidate.is_relative_to((ROOT/'artifacts/bielik_coding_adapter').resolve()):raise ValueError('Adapter outside experiment artifacts')
            command.extend(['--lora',str(candidate)])
        self.process=subprocess.Popen(command,stdout=self.log,stderr=self.log,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        atexit.register(self.close)
        deadline=time.monotonic()+180
        while time.monotonic()<deadline:
            if self.process.poll() is not None:
                self.close();raise RuntimeError('Bielik server failed; see artifacts/bielik_polish/server.log')
            try:
                with urllib.request.urlopen(self.url+'/health',timeout=2) as response:
                    if response.status==200:return
            except (OSError,urllib.error.URLError):pass
            time.sleep(.5)
        self.close();raise TimeoutError('Bielik loading timeout')
    def close(self):
        if self.process.poll() is None:
            self.process.terminate()
            try:self.process.wait(timeout=10)
            except subprocess.TimeoutExpired:self.process.kill();self.process.wait()
        self.log.close()
    def reply(self,text,history=None,max_tokens=160):
        messages=[{'role':'system','content':'Odpowiadaj po polsku, krótko i jasno. Nie udawaj, że sprawdziłeś internet. Gdy brakuje informacji, powiedz o tym.'}]+(history or [])+[{'role':'user','content':text}]
        data=json.dumps({'messages':messages,'max_tokens':max_tokens,'temperature':0}).encode('utf-8')
        request=urllib.request.Request(self.url+'/v1/chat/completions',data=data,headers={'Content-Type':'application/json'})
        with urllib.request.urlopen(request,timeout=300) as response:result=json.load(response)
        return result['choices'][0]['message']['content']
