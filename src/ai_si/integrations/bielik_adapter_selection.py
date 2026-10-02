"""Activate only an accepted, checksum-bound local adapter."""
import hashlib,json,os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]

def select_active(root=ROOT):
    root=Path(root).resolve();directory=root/'artifacts/bielik_coding_adapter';pointer=directory/'active.json'
    if not pointer.exists():return None
    data=json.loads(pointer.read_text(encoding='utf-8'));path=Path(data['path']).resolve(strict=True);report_path=Path(data['report']).resolve(strict=True)
    if not path.is_relative_to(directory.resolve()) or not report_path.is_relative_to(directory.resolve()):raise ValueError('Adapter pointer outside experiment directory')
    report=json.loads(report_path.read_text(encoding='utf-8'))
    if report.get('status')!='ACCEPTED' or not report.get('candidate_active') or not report.get('base_unchanged'):raise ValueError('Adapter has not passed acceptance gate')
    if report['after']['coding_passed']<=report['before']['coding_passed'] or report['after']['polish_passed']<report['before']['polish_passed']:raise ValueError('Adapter scores do not meet acceptance gate')
    with path.open('rb') as stream:digest=hashlib.file_digest(stream,'sha256').hexdigest()
    if digest!=data['sha256']:raise ValueError('Adapter checksum mismatch')
    model=Path(os.environ.get('SI_MODEL_PATH',str(root/'models/Bielik-1.5B-v3.0-Instruct-GGUF/Bielik-1.5B-v3.0-Instruct.Q8_0.gguf')))
    with model.open('rb') as stream:base_digest=hashlib.file_digest(stream,'sha256').hexdigest()
    if base_digest!=data['base_sha256']:raise ValueError('Base model checksum mismatch')
    return path
