import hashlib,json,tempfile,unittest
from pathlib import Path
from ai_si.integrations.bielik_adapter_selection import select_active
class SelectionTests(unittest.TestCase):
    def fixture(self,root,accepted=True):
        directory=root/'artifacts/bielik_coding_adapter/run';directory.mkdir(parents=True);adapter=directory/'adapter.gguf';adapter.write_bytes(b'fixture')
        model=root/'models/Bielik-1.5B-v3.0-Instruct-GGUF/Bielik-1.5B-v3.0-Instruct.Q8_0.gguf';model.parent.mkdir(parents=True);model.write_bytes(b'base')
        report=directory/'report.json';report.write_text(json.dumps({'status':'ACCEPTED' if accepted else 'REJECTED_NO_PROVEN_IMPROVEMENT','candidate_active':accepted,'base_unchanged':True,'before':{'coding_passed':2,'polish_passed':3},'after':{'coding_passed':3,'polish_passed':3}}))
        (directory.parent/'active.json').write_text(json.dumps({'path':str(adapter),'report':str(report),'sha256':hashlib.sha256(b'fixture').hexdigest(),'base_sha256':hashlib.sha256(b'base').hexdigest()}));return adapter
    def test_no_candidate_and_accepted(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);self.assertIsNone(select_active(root));adapter=self.fixture(root);self.assertEqual(select_active(root),adapter)
    def test_rejected_and_tampered(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);self.fixture(root,False)
            with self.assertRaises(ValueError):select_active(root)
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);adapter=self.fixture(root);adapter.write_bytes(b'changed')
            with self.assertRaises(ValueError):select_active(root)
    def test_language_regression_blocks(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);adapter=self.fixture(root);report=adapter.parent/'report.json';data=json.loads(report.read_text());data['after']['polish_passed']=2;report.write_text(json.dumps(data))
            with self.assertRaises(ValueError):select_active(root)
if __name__=='__main__':unittest.main()
