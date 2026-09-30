from contracts.tool_contract import ToolContract
from core.analysis import extract_clauses, assess_risk, compare_contracts, validate_text

def _validate_contract_text(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be an object")
    validate_text(data.get("contract_text"))

def _validate_compare(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be an object")
    validate_text(data.get("original_contract"), "original_contract")
    validate_text(data.get("revised_contract"), "revised_contract")

class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, ToolContract] = {}

    def register(self, contract: ToolContract):
        if contract.name in self._tools:
            raise ValueError(f"Tool already registered: {contract.name}")
        self._tools[contract.name] = contract

    def discover(self):
        return sorted(self._tools)

    def validate(self, name, inputs):
        self._get(name).validate(inputs)

    def execute(self, name, inputs):
        try:
            tool = self._get(name)
            tool.validate(inputs)
            return {"ok": True, "tool": name, "result": tool.execute(inputs), "error": None}
        except (ValueError, TypeError) as exc:
            return {"ok": False, "tool": name, "result": None, "error": {"type": "validation_error", "message": str(exc)}}
        except Exception as exc:
            return {"ok": False, "tool": name, "result": None, "error": {"type": "execution_error", "message": str(exc)}}

    def _get(self, name):
        if name not in self._tools:
            raise ValueError(f"Unknown tool: {name}")
        return self._tools[name]

def build_registry():
    registry = ToolRegistry()
    registry.register(ToolContract(
        name="extract-clauses",
        purpose="Extract recognizable clause families from contract text.",
        input_schema={"type": "object", "required": ["contract_text"]},
        output_schema={"type": "object"},
        validate=_validate_contract_text,
        execute=lambda data: extract_clauses(data["contract_text"]),
    ))
    registry.register(ToolContract(
        name="assess-risk",
        purpose="Apply deterministic review-signal rules to contract text.",
        input_schema={"type": "object", "required": ["contract_text"]},
        output_schema={"type": "object"},
        validate=_validate_contract_text,
        execute=lambda data: assess_risk(data["contract_text"]),
    ))
    registry.register(ToolContract(
        name="compare-contracts",
        purpose="Compare clause-family observations between two contract texts.",
        input_schema={"type": "object", "required": ["original_contract", "revised_contract"]},
        output_schema={"type": "object"},
        validate=_validate_compare,
        execute=lambda data: compare_contracts(data["original_contract"], data["revised_contract"]),
    ))
    return registry
