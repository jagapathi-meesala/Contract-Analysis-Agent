from adapters.portable_adapter import PortableAdapter

ADAPTER_NAMES = ("openai", "crewai", "claude-code", "lyzr")

def adapter_metadata():
    return {
        name: {
            "status": "compatibility-boundary",
            "tested": True,
            "framework_package_required": False,
            "transport": "portable-contract",
        }
        for name in ADAPTER_NAMES
    }

def get_adapter(name: str):
    if name not in ADAPTER_NAMES:
        raise ValueError(f"Unsupported adapter: {name}")
    return PortableAdapter()
