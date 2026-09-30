# Architecture

The project separates domain logic from tool contracts, registration, configuration, and framework adapters. The core analyzer depends only on local contracts and deterministic Python logic.

# Development Rules

Keep tool input/output contracts explicit. Prefer small deterministic functions, validate inputs before execution, and preserve stable output keys.

# Testing Rules

Every domain rule must have positive, negative, and invalid-input tests where applicable. Documentation structure and manifest references are also audited.

# Portability

Adapters translate a framework-neutral invocation into the same core contract. Framework packages are intentionally not required for the core test suite.
