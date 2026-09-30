import pytest
from core.agent import ContractAnalysisAgent
from adapters.registry import get_adapter, adapter_metadata

def test_adapter_metadata():
    meta = adapter_metadata()
    assert set(meta) == {"openai", "crewai", "claude-code", "lyzr"}
    assert all(item["tested"] for item in meta.values())

def test_portable_analyze():
    result = get_adapter("openai").invoke(
        ContractAnalysisAgent(),
        {"action": "analyze", "contract_text": "Payment due within 30 days."},
    )
    assert "clauses" in result

def test_portable_compare():
    result = get_adapter("lyzr").invoke(
        ContractAnalysisAgent(),
        {"action": "compare", "original_contract": "Payment due.", "revised_contract": "Payment due. Arbitration applies."},
    )
    assert "added_clause_types" in result

def test_invalid_adapter():
    with pytest.raises(ValueError):
        get_adapter("unknown")
