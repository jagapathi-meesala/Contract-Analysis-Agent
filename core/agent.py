from tools.registry import build_registry

class ContractAnalysisAgent:
    def __init__(self):
        self.registry = build_registry()

    def analyze(self, contract_text: str) -> dict:
        clauses = self.registry.execute("extract-clauses", {"contract_text": contract_text})
        risk = self.registry.execute("assess-risk", {"contract_text": contract_text})
        if not clauses["ok"]:
            raise ValueError(clauses["error"]["message"])
        if not risk["ok"]:
            raise ValueError(risk["error"]["message"])
        return {"clauses": clauses["result"], "risk": risk["result"]}

    def compare(self, original_contract: str, revised_contract: str) -> dict:
        result = self.registry.execute(
            "compare-contracts",
            {"original_contract": original_contract, "revised_contract": revised_contract},
        )
        if not result["ok"]:
            raise ValueError(result["error"]["message"])
        return result["result"]
