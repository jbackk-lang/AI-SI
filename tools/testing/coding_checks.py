"""Restricted educational subset. Not a sandbox for arbitrary Python."""
import ast,json,re,subprocess,sys
from pathlib import Path
ALLOWED_METHODS={'append','get','items','keys','values','join','split','lower','upper','strip','casefold','count','index','reverse','sort','pop'}
BUILTINS={'len','range','sum','min','max','sorted','enumerate','zip','list','tuple','dict','set','int','float','str','bool','abs','all','any','reversed'}
NODES={ast.Module,ast.FunctionDef,ast.arguments,ast.arg,ast.Return,ast.Assign,ast.AugAssign,ast.Expr,ast.If,ast.For,ast.While,ast.Break,ast.Continue,ast.Pass,ast.List,ast.Tuple,ast.Dict,ast.Set,ast.ListComp,ast.SetComp,ast.DictComp,ast.GeneratorExp,ast.comprehension,ast.Name,ast.Load,ast.Store,ast.Constant,ast.BinOp,ast.UnaryOp,ast.BoolOp,ast.Compare,ast.IfExp,ast.Subscript,ast.Slice,ast.Call,ast.keyword,ast.Attribute,ast.Add,ast.Sub,ast.Mult,ast.BitAnd,ast.Pow,ast.Div,ast.FloorDiv,ast.Mod,ast.USub,ast.UAdd,ast.Not,ast.And,ast.Or,ast.Eq,ast.NotEq,ast.Lt,ast.LtE,ast.Gt,ast.GtE,ast.In,ast.NotIn,ast.Is,ast.IsNot}
def extract(text):
    match=re.search(r'```(?:python)?\s*\n(.*?)```',text,re.S)
    return match.group(1).strip() if match else text.strip()
def validate(code):
    if len(code)>6000:raise ValueError('Code too long')
    tree=ast.parse(code)
    if len(tree.body)!=1 or not isinstance(tree.body[0],ast.FunctionDef) or tree.body[0].name!='solve':raise ValueError('Exactly one function solve required')
    if tree.body[0].decorator_list or tree.body[0].returns or tree.body[0].args.defaults or tree.body[0].args.kw_defaults:raise ValueError('No decorators, annotations or defaults')
    calls=BUILTINS|{'solve'}
    for node in ast.walk(tree):
        if type(node) not in NODES:raise ValueError('Unsupported syntax: '+type(node).__name__)
        if isinstance(node,(ast.Name,ast.arg)) and getattr(node,'id',getattr(node,'arg','')).startswith('_'):raise ValueError('Private names forbidden')
        if isinstance(node,ast.FunctionDef) and node is not tree.body[0]:raise ValueError('Nested functions forbidden')
        if isinstance(node,ast.Constant) and isinstance(node.value,(int,float)) and abs(node.value)>1000000:raise ValueError('Oversized numeric constant')
        if isinstance(node,ast.BinOp) and isinstance(node.op,ast.Pow) and (not isinstance(node.right,ast.Constant) or type(node.right.value) is not int or not 0<=node.right.value<=4):raise ValueError('Only small constant powers are supported')
        if isinstance(node,ast.Attribute) and node.attr not in ALLOWED_METHODS:raise ValueError('Unsupported attribute')
        if isinstance(node,ast.Call):
            if isinstance(node.func,ast.Name) and node.func.id not in calls:raise ValueError('Unsupported call: '+node.func.id)
            if not isinstance(node.func,(ast.Name,ast.Attribute)):raise ValueError('Indirect calls forbidden')
    return code

def assess(text,cases):
    try:code=validate(extract(text))
    except (SyntaxError,ValueError) as e:return {'passed':False,'reason':str(e),'code':extract(text)}
    try:
        result=subprocess.run([sys.executable,'-I','-B',str(Path(__file__).with_name('coding_worker.py'))],input=json.dumps({'code':code,'cases':cases}),capture_output=True,text=True,timeout=5,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        if result.returncode:return {'passed':False,'reason':'Worker stopped: '+str(result.returncode),'code':code}
        payload=json.loads(result.stdout);return {**payload,'code':code}
    except (subprocess.TimeoutExpired,json.JSONDecodeError) as e:return {'passed':False,'reason':type(e).__name__,'code':code}
