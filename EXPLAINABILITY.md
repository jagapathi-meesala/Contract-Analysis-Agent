## Inputs and Data Sources

The agent accepts contract text supplied directly to its framework-independent tools. Its data source is the text provided by the caller; it does not silently retrieve external legal databases or invent missing contract language.

The clause extractor uses section headings and explicit phrase families to locate recognizable clause types. The risk assessor consumes the extracted observations and the original text, while the comparison tool consumes two contract texts.

### Input Requirements

Contract text must be a non-empty string. Tool options are validated against explicit schemas, and unsupported or malformed values are rejected before domain logic executes.

### Failure Handling

Invalid input returns a structured validation error through the tool layer rather than being treated as an empty contract. Empty evidence is never converted into a positive finding.

## Decision and Reasoning

The agent makes decisions by applying deterministic text-matching and normalization rules. Each finding records a rule identifier, clause type or signal type, evidence, and a review-priority level where applicable.

A risk level is derived from the count and severity of predefined review signals, not from a model's private judgment. The output therefore explains which observed patterns contributed to the result and does not claim that a pattern is legally defective.

### Decision Rules

The extractor recognizes clause families such as termination, confidentiality, payment, liability, governing law, indemnity, renewal, and dispute resolution when their configured phrase patterns are present. The risk assessor maps detected signals to predefined severities and aggregates those severities into a review-priority label.

### Expected Outputs

Every successful tool response contains a stable structured result and traceable rule identifiers. Evidence snippets are bounded excerpts from the supplied input so a reviewer can locate the source text.

### Worked Example

If a contract contains a termination section with language indicating termination without notice, the extractor records a termination clause and the risk assessor may emit a corresponding review signal. The result identifies the phrase evidence and the rule identifier; it does not state that the clause is unenforceable.

## Limits and Constraints

The agent is limited to deterministic analysis of supplied text and cannot determine legal effect without jurisdiction, governing law, facts, negotiation history, and professional interpretation. It should therefore be treated as a review aid rather than a legal decision-maker.

The implementation does not claim comprehensive coverage of every contract clause or every legal drafting convention. OCR errors, unusual wording, ambiguous language, multilingual text, tables, scanned documents, and context spread across distant provisions can reduce detection quality.

### Execution Constraints

No external legal database is queried by the core tools. No tool executes contract text as code, and no tool signs, sends, approves, rejects, or modifies a contract.

### Provenance

Findings are derived only from the caller-supplied contract text and the versioned deterministic rule set in this repository. Tool outputs identify the rule responsible for each observation so that a reviewer can trace the result back to the input evidence.
