"""Fail closed before publication: explicit files, no private core or weights."""
import argparse,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
TOP={'.gitignore','README.md','requirements-training.txt','run_ui.py','Uruchom_AI_SI.bat'}
EXACT={
'src/ai_si/__init__.py','src/ai_si/server.py','src/ai_si/integrations/__init__.py','src/ai_si/integrations/bielik_polish.py','src/ai_si/integrations/bielik_adapter_selection.py',
'web/index.html','tools/training/run_bielik_coding_adapter.py','tools/training/bielik_training_base.py','tools/training/prepare_runtime.py','tools/training/validate_bielik_adapter_fresh.py',
'tools/testing/coding_checks.py','tools/testing/coding_worker.py','tools/release/check_public.py','tools/release/prepare_commit.py','scripts/Prepare-Commit.ps1',
'tests/__init__.py','tests/test_coding_checks.py','tests/test_bielik_adapter_selection.py','tests/test_public_gateway.py','tests/test_release_guard.py',
'data/coding_adapter/train.json','data/coding_adapter/holdout.json','data/coding_adapter/polish_regression.json',
'docs/BIELIK_CODING_PROTOCOL.md','docs/PUBLIC_SCOPE.md','docs/TRAINING_RESULT.md'}
IGNORED_ROOTS={'.git','artifacts','runtime','models','private','local','.venv','venv','__pycache__'}
DENIED_SUFFIXES={'.pt','.pth','.gguf','.safetensors','.bin','.zip','.log','.pyc'}
PRIVATE_CLASSES={'IndependentCore','CompositionalStatus','AssociativeKnowledge','LanguageCore','ProgrammingCore','LearningConversation','NeuralConversation','BilingualConversation','DeliberativeCore'}
def check(paths):
    errors=[]
    for relative in paths:
        normalized=relative.replace('\\','/');file=ROOT/normalized
        if normalized not in TOP|EXACT:errors.append('Not in publication allowlist: '+normalized);continue
        if file.suffix.lower() in DENIED_SUFFIXES:errors.append('Weight/artifact file: '+normalized);continue
        if not file.is_file() or file.stat().st_size>2000000:errors.append('Missing or oversized file: '+normalized);continue
        if file.suffix=='.py':
            import ast
            tree=ast.parse(file.read_text(encoding='utf-8'))
            if any(isinstance(n,ast.ClassDef) and n.name in PRIVATE_CLASSES for n in ast.walk(tree)):errors.append('Private core class found: '+normalized)
    return errors

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--staged',action='store_true');args=parser.parse_args()
    if args.staged:
        process=subprocess.run(['git','ls-files','-z','--cached'],cwd=ROOT,capture_output=True)
        if process.returncode:raise SystemExit('Cannot inspect Git index; publication blocked')
        paths=[p for p in process.stdout.decode('utf-8').split('\x00') if p]
    else:
        paths=[p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and not any(part in IGNORED_ROOTS for part in p.relative_to(ROOT).parts)]
    errors=check(paths)
    if errors:print('\n'.join(errors));raise SystemExit(1)
    print('Public files checked:',len(paths),'- no private core or large weights.')
if __name__=='__main__':main()
