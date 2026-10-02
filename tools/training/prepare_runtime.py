"""Download official conversion scripts only; model/runtime weights stay external."""
import hashlib,json,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
    folder=ROOT/'runtime/lora_export';folder.mkdir(parents=True,exist_ok=True);manifest={}
    for name in ('convert_lora_to_gguf.py','convert_hf_to_gguf.py'):
        url='https://raw.githubusercontent.com/ggml-org/llama.cpp/b5473/'+name
        data=urllib.request.urlopen(url,timeout=30).read();(folder/name).write_bytes(data);manifest[name]={'source':url,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
    (folder/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8');print('Official conversion scripts ready')
if __name__=='__main__':main()
