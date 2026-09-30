from typing import Any

class PortableAdapter:
    """Framework-neutral boundary for agent invocation."""

    def invoke(self, agent, payload: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(payload, dict):
            raise ValueError("Adapter payload must be an object")
        action = payload.get("action", "analyze")
        if action == "analyze":
            return agent.analyze(payload["contract_text"])
        if action == "compare":
            return agent.compare(payload["original_contract"], payload["revised_contract"])
        raise ValueError("Unsupported action")
