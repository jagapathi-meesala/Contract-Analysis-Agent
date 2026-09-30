from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]

def fail(msg):
    raise SystemExit("FAIL: " + msg)

required = [
    "agent.yaml", "SOUL.md", "AGENTS.md", "DUTIES.md", "RULES.md",
    "README.md", "EXPLAINABILITY.md", ".env.example", "requirements.txt",
]
for item in required:
    if not (ROOT / item).exists():
        fail(f"missing {item}")

manifest = yaml.safe_load((ROOT / "agent.yaml").read_text())
allowed_top = {"spec_version","name","version","description","author","license","model",
               "extends","dependencies","skills","tools","agents","delegation","runtime",
               "a2a","compliance","tags","metadata"}
unknown = set(manifest) - allowed_top
if unknown:
    fail(f"unsupported manifest properties: {sorted(unknown)}")
if manifest.get("spec_version") != "0.1.0":
    fail("wrong spec_version")
if not re.fullmatch(r"[a-z][a-z0-9-]*", manifest["name"]):
    fail("invalid agent name")

for skill in manifest.get("skills", []):
    if not (ROOT / "skills" / skill / "SKILL.md").exists():
        fail(f"missing skill: {skill}")

for tool in manifest.get("tools", []):
    if not (ROOT / "tools" / f"{tool}.yaml").exists():
        fail(f"missing tool: {tool}")

doc = (ROOT / "EXPLAINABILITY.md").read_text()
for heading in [
    "## Inputs and Data Sources",
    "## Decision and Reasoning",
    "## Limits and Constraints",
]:
    if heading not in doc:
        fail(f"missing heading: {heading}")
for bad in ["## Inputs\n", "## Decision\n", "## Limits\n"]:
    if bad in doc:
        fail(f"conflicting heading: {bad.strip()}")
print("PASS: structural audit")
