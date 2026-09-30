import pytest
from core.analysis import extract_clauses, assess_risk, compare_contracts

def test_clause_extraction_is_deterministic():
    text = "Payment due within 30 days. Confidential information must remain confidential."
    assert extract_clauses(text) == extract_clauses(text)

def test_risk_signal():
    result = assess_risk("The parties agree to unlimited liability.")
    assert result["risk_level"] == "medium"
    assert result["signals"][0]["signal_id"] == "unlimited-liability"

def test_compare():
    result = compare_contracts("Confidentiality applies.", "Confidentiality applies. Arbitration applies.")
    assert "dispute-resolution" in result["added_clause_types"]

@pytest.mark.parametrize("value", [None, "", "   ", 123])
def test_invalid_text(value):
    with pytest.raises(ValueError):
        extract_clauses(value)
