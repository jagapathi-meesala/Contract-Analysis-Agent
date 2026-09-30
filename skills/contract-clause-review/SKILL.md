---
name: contract-clause-review
description: Extract recognizable contract clause families from supplied contract text using deterministic phrase and section rules.
---

# Contract Clause Review

## Inputs

Accept a non-empty contract text string.

## Behavior

Run the clause extraction tool and preserve its rule identifiers and evidence snippets. Do not infer a clause when no configured pattern is present.

## Outputs

Return structured clause findings with clause type, rule identifier, and evidence.

## Invalid Inputs

Reject missing, non-string, or empty contract text.
