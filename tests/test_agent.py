import pytest
from core.agent import ContractAnalysisAgent

TEXT = """
Governing law: State law.
Termination for convenience is permitted.
The parties agree to confidentiality.
There is an automatic renewal term.
"""

def test_agent_analyze():
    result = ContractAnalysisAgent().analyze(TEXT)
    assert "termination" in {x["clause_type"] for x in result["clauses"]["clauses"]}
    assert result["risk"]["risk_level"] in {"medium", "high"}

def test_agent_rejects_empty():
    with pytest.raises(ValueError):
        ContractAnalysisAgent().analyze("")
