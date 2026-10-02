$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)
python tools/release/check_public.py
if ($LASTEXITCODE -ne 0) { throw 'Public file check failed' }
$remote = git remote get-url origin 2>$null
if ($LASTEXITCODE -ne 0) { git remote add origin https://github.com/jbackk-lang/AI-SI.git }
elseif ($remote -ne 'https://github.com/jbackk-lang/AI-SI.git') { throw 'Unexpected origin; inspect before publication' }
git fetch origin main
if ($LASTEXITCODE -ne 0) { throw 'Fetch failed; no commit or push performed' }
git rev-parse --verify HEAD 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) {
    # This checkout was created empty; adopt existing remote history without replacing working files.
    git reset --mixed origin/main
    if ($LASTEXITCODE -ne 0) { throw 'Cannot adopt existing remote history' }
}
else {
    git merge-base --is-ancestor origin/main HEAD
    if ($LASTEXITCODE -ne 0) { throw 'Remote changed; integrate it before preparing this commit' }
}
git add -- README.md .gitignore requirements-training.txt run_ui.py Uruchom_AI_SI.bat src web tools tests data docs scripts
if ($LASTEXITCODE -ne 0) { throw 'git add failed' }
python tools/release/check_public.py --staged
if ($LASTEXITCODE -ne 0) { throw 'Git index contains prohibited files; commit blocked' }
git diff --cached --stat
Write-Host 'Po przejrzeniu zmian: git commit -m "Dodaj publiczny interfejs SI i narzedzia treningu bez prywatnego rdzenia"'
Write-Host 'Nastepnie: git push -u origin main'
