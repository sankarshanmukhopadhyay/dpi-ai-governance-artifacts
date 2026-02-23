# Redress and remediation

This controlled document defines **minimum redress expectations** for DPI + AI systems adopting artifacts in this repository.

## 1. Scope

These requirements apply to systems and programs that:
- make decisions impacting people, communities, or organizations, and/or
- automate or materially influence eligibility, allocation, prioritization, enforcement, or access.

## 2. Redress channels

1. Implementers MUST provide at least one public redress channel per governed program.
2. Redress channels MUST support:
   a. intake of complaints/appeals,
   b. request for explanation or correction,
   c. submission of additional evidence.
3. Where feasible, channels SHOULD support authenticated submissions without excluding low-access users (see inclusion requirements when populated).

## 3. Decision receipt linkage

1. If decision receipts are used, the redress process MUST accept a decision receipt identifier (or equivalent).
2. Redress outcomes MUST be linkable to:
   - the original decision artifact,
   - the applied policy/rule version (where known),
   - the responsible authority role.

## 4. Escalation and timelines

1. Implementers MUST define escalation levels (e.g., L1 support → L2 program authority → L3 independent review).
2. Implementers MUST publish target response timelines for each level.
3. For high-impact decisions, implementers SHOULD provide expedited review paths.

## 5. Remediation completion evidence

When remediation is required, implementers MUST record:
- remediation action(s) taken,
- completion timestamp,
- responsible role,
- evidence artifacts (logs, updated configuration, patched model version, corrected data, etc.),
- verification that remediation is effective (test, audit check, or control validation).

## 6. Appeals and dispute resolution

1. Appeals MUST be possible when:
   - a decision is contested,
   - a harmful outcome is alleged,
   - a material error is identified.
2. Implementers SHOULD specify when independent review is available and how it is triggered.

## 7. Auditability and reporting

1. Programs SHOULD maintain an aggregate redress log (privacy-aware) to enable:
   - trend analysis,
   - systemic failure detection,
   - evidence of continuous improvement.

## 8. Relationship to other controlled documents

- Evidence requirements for redress MAY be referenced from `controlled/assurance/evidence-bundles.md`.
- Schema-level support SHOULD be implemented in decision receipt / audit finding schemas as applicable.
