import re
from typing import Any

CLAUSE_PATTERNS = {
    "termination": [r"\btermination\b", r"terminate this agreement", r"termination for convenience"],
    "confidentiality": [r"\bconfidential", r"non[- ]disclosure", r"confidential information"],
    "payment": [r"\bpayment terms?\b", r"payment due", r"invoice"],
    "liability": [r"\blimitation of liability\b", r"liable for", r"liability"],
    "governing-law": [r"governing law", r"laws of the (state|country|jurisdiction)"],
    "indemnity": [r"\bindemnif", r"indemnification"],
    "renewal": [r"automatic renewal", r"renewal term", r"renews automatically"],
    "dispute-resolution": [r"dispute resolution", r"arbitration", r"mediation"],
}

RISK_SIGNALS = [
    ("termination-without-notice", "termination", [r"terminate.*without notice", r"termination.*without notice"], 3),
    ("unlimited-liability", "liability", [r"unlimited liability", r"liable.*without limitation"], 3),
    ("automatic-renewal", "renewal", [r"automatic renewal", r"renews automatically"], 2),
    ("broad-indemnity", "indemnity", [r"indemnify.*any and all", r"indemnify.*all claims"], 2),
    ("mandatory-arbitration", "dispute-resolution", [r"mandatory arbitration", r"binding arbitration"], 1),
]

def validate_text(value: Any, field: str = "contract_text") -> None:
    if not isinstance(value, str):
        raise ValueError(f"{field} must be a string")
    if not value.strip():
        raise ValueError(f"{field} must not be empty")

def _snippet(text: str, start: int, end: int, radius: int = 90) -> str:
    left = max(0, start - radius)
    right = min(len(text), end + radius)
    return " ".join(text[left:right].split())[:240]

def extract_clauses(contract_text: str) -> dict[str, Any]:
    validate_text(contract_text)
    findings = []
    for clause_type, patterns in CLAUSE_PATTERNS.items():
        for pattern in patterns:
            match = re.search(pattern, contract_text, re.IGNORECASE)
            if match:
                findings.append({
                    "clause_type": clause_type,
                    "rule_id": f"clause-{clause_type}",
                    "evidence": _snippet(contract_text, match.start(), match.end()),
                })
                break
    return {"contract_length": len(contract_text), "clauses": findings, "rule_version": "1.0"}

def assess_risk(contract_text: str) -> dict[str, Any]:
    validate_text(contract_text)
    signals = []
    total = 0
    for rule_id, category, patterns, weight in RISK_SIGNALS:
        for pattern in patterns:
            match = re.search(pattern, contract_text, re.IGNORECASE | re.DOTALL)
            if match:
                signals.append({
                    "signal_id": rule_id,
                    "category": category,
                    "severity_weight": weight,
                    "evidence": _snippet(contract_text, match.start(), match.end()),
                    "rule_id": f"risk-{rule_id}",
                })
                total += weight
                break
    level = "low" if total <= 1 else "medium" if total <= 3 else "high"
    return {"risk_level": level, "score": total, "signals": signals, "rule_version": "1.0"}

def compare_contracts(original: str, revised: str) -> dict[str, Any]:
    validate_text(original, "original_contract")
    validate_text(revised, "revised_contract")
    old = {item["clause_type"] for item in extract_clauses(original)["clauses"]}
    new = {item["clause_type"] for item in extract_clauses(revised)["clauses"]}
    return {
        "added_clause_types": sorted(new - old),
        "removed_clause_types": sorted(old - new),
        "unchanged_clause_types": sorted(old & new),
        "rule_version": "1.0",
    }
