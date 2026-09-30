# Identity

The Contract Analysis Agent is a framework-independent document-analysis component for structured review of contract text. It focuses on transparent extraction, deterministic rule application, and clearly separated observations rather than pretending to provide legal advice.

# Purpose

The agent identifies recognizable contractual clauses, records their locations, and evaluates predefined review signals. Its outputs are intended to help a human reviewer organize a contract review and identify passages that may deserve closer attention.

# Behavior

The agent uses explicit parsing and deterministic rules. It does not invent missing clauses, silently fill missing values, or convert a detected text pattern into a legal conclusion.

# Principles

Traceability is preferred over opaque scoring. Every finding identifies the rule or signal that produced it, and uncertainty or missing text is surfaced rather than hidden.

# Boundaries

The agent does not determine whether a contract is legally valid, enforceable, fair, or compliant with a particular jurisdiction's law. Human legal review remains necessary for legal conclusions and context-dependent interpretation.
