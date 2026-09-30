from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]

def test_manifest():
    m = yaml.safe_load((ROOT / "agent.yaml").read_text())
    assert m["spec_version"] == "0.1.0"
    assert m["name"] == "contract-analysis-agent"
    assert re.fullmatch(r"[a-z][a-z0-9-]*", m["name"])
    assert m["skills"] == ["contract-clause-review", "contract-risk-assessment"]
    assert m["tools"] == ["extract-clauses", "assess-risk", "compare-contracts"]

def test_explainability_headings():
    doc = (ROOT / "EXPLAINABILITY.md").read_text()
    assert "## Inputs and Data Sources" in doc
    assert "## Decision and Reasoning" in doc
    assert "## Limits and Constraints" in doc
    assert "## Inputs\n" not in doc
    assert "## Decision\n" not in doc
    assert "## Limits\n" not in doc

def test_no_env_file():
    assert not (ROOT / ".env").exists()
