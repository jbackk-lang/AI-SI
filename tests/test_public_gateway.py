import json,threading,unittest,urllib.request,urllib.error
from http.server import ThreadingHTTPServer
from ai_si.server import backend_url,make_handler
class Fake:
    def call(self,data):return {'answer':'local reply','status':'fixture'}
    def get(self,path):return json.dumps({'status':'TRAINING','steps':3}).encode()
class GatewayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=ThreadingHTTPServer(('127.0.0.1',0),make_handler(Fake(),'fixture-token'));cls.url=f'http://127.0.0.1:{cls.server.server_port}';cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
    @classmethod
    def tearDownClass(cls):cls.server.shutdown();cls.server.server_close();cls.thread.join()
    def test_local_backend_only(self):
        self.assertEqual(backend_url('http://127.0.0.1:8771/'),'http://127.0.0.1:8771')
        for url in ('https://example.com','http://user:secret@localhost:8771','http://localhost:8771/elsewhere'):
            with self.assertRaises(ValueError):backend_url(url)
    def test_page_and_training(self):
        with urllib.request.urlopen(self.url) as response:self.assertIn('SI — lokalny warsztat',response.read().decode())
        with urllib.request.urlopen(self.url+'/training') as response:self.assertEqual(json.load(response)['steps'],3)
    def test_proxy_and_cross_origin_guard(self):
        data=json.dumps({'mode':'chat','text':'hello'}).encode();headers={'Content-Type':'application/json','X-SI-Token':'fixture-token'}
        with urllib.request.urlopen(urllib.request.Request(self.url+'/api',data,headers)) as response:self.assertEqual(json.load(response)['answer'],'local reply')
        headers['Origin']='https://evil.test'
        with self.assertRaises(urllib.error.HTTPError) as error:urllib.request.urlopen(urllib.request.Request(self.url+'/api',data,headers))
        self.assertEqual(error.exception.code,403)
if __name__=='__main__':unittest.main()
