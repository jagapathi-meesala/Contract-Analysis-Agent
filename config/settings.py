import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    agent_env: str
    log_level: str

def load_settings() -> Settings:
    agent_env = os.environ.get("AGENT_ENV")
    log_level = os.environ.get("LOG_LEVEL")
    missing = [name for name, value in (("AGENT_ENV", agent_env), ("LOG_LEVEL", log_level)) if not value]
    if missing:
        raise RuntimeError("Missing required environment variables: " + ", ".join(missing))
    normalized = log_level.upper()
    if normalized not in {"DEBUG", "INFO", "WARNING", "ERROR"}:
        raise ValueError("LOG_LEVEL must be one of DEBUG, INFO, WARNING, ERROR")
    return Settings(agent_env=agent_env, log_level=normalized)
