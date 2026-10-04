"""Additional frozen sanity validation after correcting the AST checker."""
import json,hashlib
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'src'));sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'tools/testing'))
from ai_si.integrations.bielik_polish import PolishLanguage
from coding_checks import assess
ROOT=Path(__file__).resolve().parents[2]
RUN=None
CASES=[
{'id':'common_letters','prompt':'Write Python code only: one function solve(a, b), no imports. Return a sorted list of unique letters appearing in both strings a and b, ignoring case.','cases':[{'args':['Abca','CAD'],'expected':['a','c']},{'args':['xyz','ABC'],'expected':[]},{'args':['','A'],'expected':[]}]},
{'id':'negative_count','prompt':'Write Python code only: one function solve(xs), no imports. Count integers strictly below zero in list xs.','cases':[{'args':[[-1,0,2,-3]],'expected':2},{'args':[[]],'expected':0},{'args':[[0,1]],'expected':0}]},
{'id':'first_positive','prompt':'Write Python code only: one function solve(xs), no imports. Return the first strictly positive integer from xs, or None if no such integer exists.','cases':[{'args':[[-2,0,5,3]],'expected':5},{'args':[[]],'expected':None},{'args':[[0,-2]],'expected':None}]}]
def dump(path,data):path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
def main():
    global RUN
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('run',type=Path);args=parser.parse_args();RUN=args.run.resolve(strict=True)
    if not RUN.is_relative_to((ROOT/'artifacts/bielik_coding_adapter').resolve()):raise ValueError('Run outside experiment artifacts')
    dump(RUN/'fresh_validation_plan.json',{'cases':CASES,'scope':'New sanity tasks authored after previous outputs, frozen before this comparison; no new training or hyperparameter tuning.'})
    results={}
    for stage,adapter in [('base',None),('candidate',RUN/'adapter.gguf')]:
        language=PolishLanguage(adapter_path=adapter)
        try:
            rows=[];results[stage]=rows
            for case in CASES:
                response=language.reply(case['prompt'],max_tokens=160);row={'id':case['id'],'response':response,'assessment':assess(response,case['cases'])};rows.append(row);dump(RUN/'fresh_validation_report.json',results);print(stage,case['id'],row['assessment']['passed'],flush=True)
        finally:language.close()
    print('Fresh comparison complete',flush=True)
if __name__=='__main__':main()
