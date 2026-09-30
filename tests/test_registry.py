from tools.registry import build_registry

def test_registry_discovers_tools():
    registry = build_registry()
    assert registry.discover() == ["assess-risk", "compare-contracts", "extract-clauses"]

def test_registry_validation_error():
    result = build_registry().execute("assess-risk", {"contract_text": ""})
    assert result["ok"] is False
    assert result["error"]["type"] == "validation_error"

def test_unknown_tool():
    result = build_registry().execute("missing-tool", {})
    assert result["ok"] is False
