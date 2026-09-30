# Contract Analysis Agent

A framework-independent OpenGAP agent for deterministic contract-text analysis.

## What it does

- Extracts recognizable clause families from contract text.
- Detects predefined review signals.
- Produces structured findings with rule identifiers and evidence snippets.
- Compares two contract texts using normalized clause findings.

## What it does not do

It does not provide a legal opinion, determine enforceability, or decide whether a contract should be signed.

## Local validation

Run:

```bash
pytest -q
python verification/structural_audit.py
```

If the `opengap` CLI is installed in the target environment, additionally run:

```bash
opengap validate
```

This repository does not claim OpenGAP CLI validation unless that command is actually executed successfully.
