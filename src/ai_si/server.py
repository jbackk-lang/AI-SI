"""Public browser gateway. Proprietary SI/TIMDR core is not distributed."""
import argparse,json,os,re,secrets,urllib.error,urllib.parse,urllib.request,webbrowser
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def backend_url(value):
    parsed=urllib.parse.urlsplit(value)
    if parsed.scheme!='http' or parsed.hostname not in ('127.0.0.1','localhost','::1') or parsed.username or parsed.password or parsed.path not in ('','/') or parsed.query or parsed.fragment:raise ValueError('Backend must be a local HTTP service')
    return value.rstrip('/')
class Backend:
    def __init__(self,url):self.url=backend_url(url);self.opener=urllib.request.build_opener(urllib.request.ProxyHandler({}))
    def get(self,path):
        with self.opener.open(self.url+path,timeout=10) as response:return response.read(1000000)
    def call(self,data):
        page=self.get('/').decode('utf-8');match=re.search(r"const token='([A-Za-z0-9_-]+)'",page)
        if not match:raise ValueError('Configured service is not the expected local SI backend')
        request=urllib.request.Request(self.url+'/api',json.dumps(data).encode('utf-8'),headers={'Content-Type':'application/json','X-SI-Token':match.group(1)})
        with self.opener.open(request,timeout=360) as response:return json.load(response)
def make_handler(backend,token):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self,*args):pass
        def valid_host(self):return self.headers.get('Host') in (f'127.0.0.1:{self.server.server_port}',f'localhost:{self.server.server_port}')
        def send(self,code,payload,kind='application/json; charset=utf-8'):
            body=payload.encode('utf-8') if isinstance(payload,str) else json.dumps(payload,ensure_ascii=False).encode('utf-8')
            self.send_response(code);self.send_header('Content-Type',kind);self.send_header('Content-Length',str(len(body)));self.send_header('X-Content-Type-Options','nosniff');self.send_header('Cache-Control','no-store');self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; connect-src 'self'; frame-ancestors 'none'");self.end_headers();self.wfile.write(body)
        def do_GET(self):
            if not self.valid_host():return self.send(403,{'error':'Host rejected'})
            if self.path=='/':return self.send(200,(ROOT/'web/index.html').read_text(encoding='utf-8').replace('__TOKEN__',token),'text/html; charset=utf-8')
            if self.path=='/health':return self.send(200,{'status':'public_gateway_ready'})
            if self.path=='/training':
                try:return self.send(200,json.loads(backend.get('/training')))
                except (OSError,ValueError):return self.send(200,{'status':'local_backend_unavailable'})
            return self.send(404,{'error':'Not found'})
        def do_POST(self):
            origin=self.headers.get('Origin');allowed=(f'http://127.0.0.1:{self.server.server_port}',f'http://localhost:{self.server.server_port}')
            if not self.valid_host() or self.headers.get('X-SI-Token')!=token or (origin and origin not in allowed):return self.send(403,{'error':'Request rejected'})
            if self.path!='/api' or self.headers.get_content_type()!='application/json':return self.send(400,{'error':'Expected JSON'})
            try:
                length=int(self.headers.get('Content-Length','0'))
                if not 0<length<=24000:raise ValueError('Invalid request length')
                data=json.loads(self.rfile.read(length))
                if not isinstance(data,dict):raise ValueError('Expected object')
                self.send(200,backend.call(data))
            except urllib.error.HTTPError as error:
                try:payload=json.loads(error.read(24000))
                except ValueError:payload={'error':'Local backend rejected the request'}
                self.send(error.code,payload)
            except ValueError as error:self.send(400,{'error':str(error)})
            except OSError:self.send(503,{'error':'Uruchom prywatny silnik SI. Publiczne repozytorium zawiera interfejs i narzędzia, bez rdzenia.'})
    return Handler
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--port',type=int,default=8780);parser.add_argument('--backend',default=os.environ.get('SI_BACKEND_URL','http://127.0.0.1:8771'));parser.add_argument('--no-browser',action='store_true');args=parser.parse_args()
    server=ThreadingHTTPServer(('127.0.0.1',args.port),make_handler(Backend(args.backend),secrets.token_urlsafe(32)))
    url=f'http://127.0.0.1:{server.server_port}/';print(url,flush=True)
    if not args.no_browser:webbrowser.open(url)
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()
if __name__=='__main__':main()
