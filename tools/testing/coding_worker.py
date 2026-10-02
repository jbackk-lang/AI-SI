"""Private bounded worker for AST-filtered code. No arbitrary execution API."""
import builtins,json,os,sys

def limit():
    if os.name!='nt':
        import resource
        resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2));resource.setrlimit(resource.RLIMIT_CPU,(2,2));return None
    import ctypes
    from ctypes import wintypes
    class Basic(ctypes.Structure):
        _fields_=[('process_time',ctypes.c_int64),('job_time',ctypes.c_int64),('flags',wintypes.DWORD),('min_ws',ctypes.c_size_t),('max_ws',ctypes.c_size_t),('active',wintypes.DWORD),('affinity',ctypes.c_size_t),('priority',wintypes.DWORD),('scheduling',wintypes.DWORD)]
    class IO(ctypes.Structure):_fields_=[(n,ctypes.c_uint64) for n in ('read_ops','write_ops','other_ops','read_bytes','write_bytes','other_bytes')]
    class Extended(ctypes.Structure):_fields_=[('basic',Basic),('io',IO),('process_memory',ctypes.c_size_t),('job_memory',ctypes.c_size_t),('peak_process',ctypes.c_size_t),('peak_job',ctypes.c_size_t)]
    k=ctypes.WinDLL('kernel32',use_last_error=True);k.CreateJobObjectW.restype=wintypes.HANDLE;k.CreateJobObjectW.argtypes=[ctypes.c_void_p,wintypes.LPCWSTR]
    k.SetInformationJobObject.argtypes=[wintypes.HANDLE,ctypes.c_int,ctypes.c_void_p,wintypes.DWORD];k.AssignProcessToJobObject.argtypes=[wintypes.HANDLE,wintypes.HANDLE];k.GetCurrentProcess.restype=wintypes.HANDLE
    job=k.CreateJobObjectW(None,None);info=Extended();info.basic.flags=0x100|0x2|0x2000;info.basic.process_time=2*10000000;info.process_memory=512*1024**2
    if not job or not k.SetInformationJobObject(job,9,ctypes.byref(info),ctypes.sizeof(info)) or not k.AssignProcessToJobObject(job,k.GetCurrentProcess()):raise RuntimeError('Windows resource sandbox unavailable')
    return job

def main():
    sys.path.insert(0,os.path.dirname(__file__))
    from coding_checks import validate,BUILTINS
    data=json.load(sys.stdin);validate(data['code']);job=limit()
    scope={'__builtins__':{name:getattr(builtins,name) for name in BUILTINS}}
    exec(compile(data['code'],'<generated educational code>','exec'),scope)
    results=[]
    for case in data['cases']:
        try:value=scope['solve'](*case['args']);results.append(value==case['expected'])
        except Exception:results.append(False)
    print(json.dumps({'passed':all(results),'cases_passed':sum(results),'total_cases':len(results)}))
if __name__=='__main__':
    try:main()
    except Exception as e:print(json.dumps({'passed':False,'reason':str(e)}))
