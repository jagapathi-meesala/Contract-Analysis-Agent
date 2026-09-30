---
name: contract-risk-assessment
description: Identify predefined contract review signals and calculate a deterministic review-priority label from their configured weights.
---

# Contract Risk Assessment

## Inputs

Accept a non-empty contract text string.

## Behavior

Run the risk-assessment tool. Report signals as review observations, not legal conclusions.

## Outputs

Return a review-priority label, numeric rule score, signal list, evidence, and rule version.

## Invalid Inputs

Reject missing, non-string, or empty contract text.
