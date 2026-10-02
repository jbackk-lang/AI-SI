import importlib.util,tempfile,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('release_guard',Path(__file__).resolve().parents[1]/'tools/release/check_public.py');guard=importlib.util.module_from_spec(spec);spec.loader.exec_module(guard)
class ReleaseTests(unittest.TestCase):
    def test_weight_and_private_path_rejected(self):
        self.assertTrue(guard.check(['models/base.gguf']))
        self.assertTrue(guard.check(['src/ai_si/independent_timdr_core.py']))
    def test_private_class_inside_allowed_file_rejected(self):
        previous=guard.ROOT
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);file=root/'src/ai_si/server.py';file.parent.mkdir(parents=True);file.write_text('class IndependentCore: pass',encoding='utf-8');guard.ROOT=root
            try:self.assertTrue(guard.check(['src/ai_si/server.py']))
            finally:guard.ROOT=previous
if __name__=='__main__':unittest.main()
