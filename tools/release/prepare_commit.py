"""Prepare public index on a fresh checkout; never commit or push automatically."""
import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
EXPECTED='https://github.com/jbackk-lang/AI-SI.git'
def git(*args,check=True):return subprocess.run(['git',*args],cwd=ROOT,text=True,capture_output=True,check=check)
def main():
    subprocess.run([sys.executable,str(ROOT/'tools/release/check_public.py')],cwd=ROOT,check=True)
    remote=git('remote','get-url','origin',check=False)
    if remote.returncode:git('remote','add','origin',EXPECTED)
    elif remote.stdout.strip()!=EXPECTED:raise ValueError('Unexpected origin; publication stopped')
    # OpenSSL verifies certificates normally; avoids the Windows Schannel credential error seen in the sandbox.
    git('-c','http.sslBackend=openssl','fetch','origin','main')
    head=git('rev-parse','--verify','HEAD',check=False)
    if head.returncode:
        # Adopt GitHub initial history; --mixed keeps every working file intact.
        git('reset','--mixed','origin/main')
    elif git('merge-base','--is-ancestor','origin/main','HEAD',check=False).returncode:
        raise ValueError('Remote has new history; integrate it before preparing this commit')
    git('add','--','README.md','.gitignore','requirements-training.txt','run_ui.py','Uruchom_AI_SI.bat','src','web','tools','tests','data','docs','scripts')
    subprocess.run([sys.executable,str(ROOT/'tools/release/check_public.py'),'--staged'],cwd=ROOT,check=True)
    print(git('diff','--cached','--stat').stdout)
    print('Ready for your git commit and git push. No commit or push was performed.')
if __name__=='__main__':
    try:main()
    except subprocess.CalledProcessError as error:
        print(error.stderr or str(error),file=sys.stderr);raise SystemExit(1)
    except (ValueError,OSError) as error:
        print(str(error),file=sys.stderr);raise SystemExit(1)
