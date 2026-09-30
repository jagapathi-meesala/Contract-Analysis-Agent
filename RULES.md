# Deterministic Rules

1. Empty or whitespace-only contract text is rejected.
2. Clause extraction uses explicit phrase families and section markers; it does not infer clauses from unrelated text.
3. Review signals are observations triggered by configured phrase patterns.
4. A signal is not a legal conclusion.
5. Risk levels are rule-derived labels: `low`, `medium`, or `high`; they describe review priority within this tool only.
6. Missing evidence produces a missing/unknown state rather than an invented value.
7. Results include rule identifiers so findings are traceable.
8. Inputs are treated as untrusted text and are never executed as code.
