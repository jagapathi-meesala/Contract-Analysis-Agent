from pathlib import Path
from core.analysis import extract_clauses

def test_text_is_not_executed():
    payload = "__import__('os').system('touch SHOULD_NOT_EXIST')"
    extract_clauses(payload)
    assert not Path("SHOULD_NOT_EXIST").exists()
