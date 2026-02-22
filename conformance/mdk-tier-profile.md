# Minimum Digital Kernel Conformance Profile

This profile maps DPI–AI risk tiers to operational requirements for Minimum Digital Kernel primitives.

The intent is procurement-ready clarity: what must exist at each tier to make outcomes auditable, contestable, and remediable.

## Tier 0 (Minimal)

Tier 0 covers **non-consequential** decisions where a full signed receipt is not required, but **portable logging** is mandatory for audit sampling, monitoring, and incident response.

Required
- Log entry per decision execution and system error
- Internal traceability from request to outcome (trace_id / correlation id)
- Retain logs for a policy-defined period (implementation-specific)

**Tier 0 log entry format**
- Use `schemas/tier0-log-entry.schema.json` as the minimum portable record:
  - `event_id`, `timestamp`, `service_id`, `rulebook.rulebook_id`, `rulebook.version`, `outcome_code`, `trace_id`
  - Optional: `inputs_hash`, `receipt_ref` (when a receipt is produced)

Recommended
- Decision receipts for denials and revocations (upgrade path into Tier 1+)


## Tier 1 (Moderate)

Required
- Decision receipts for denials, revocations, and material eligibility determinations
- Published reason code vocabulary for all decision receipts
- Authority directory entries for each authority issuing receipts

Recommended
- Basic correction request interface for core registries

## Tier 2 (High)

Required
- Decision receipts for all consequential outcomes
- Versioned rulebooks with a rulebook manifest
- Registry correction request and response interfaces, including signed responses
- Recompute trigger semantics for affected decisions

Recommended
- Structured appeals filing interface for denials and revocations
- Evidence bundle pointers for outcomes with higher risk exposure

## Tier 3 (Critical)

Required
- Decision receipts for all consequential outcomes, including partial approvals and prioritization outcomes
- Mandatory appeals interface and appeal decisions that can issue orders (correction, recompute, manual review)
- Independent audit function producing structured findings and remediation orders
- Evidence pointers sufficient to support replay and audit without requiring privileged, informal access

Recommended
- Incident-to-appeal linkage and retrospective review for systemic failures
- Continuous monitoring of receipt issuance, signature verification, and reason code coverage

## Implementation notes

- Treat these requirements as interface contracts. Implementations can vary, but the outputs and verification semantics should not.
- Minimize personal data in receipts. Use hashes and durable references.
- Ensure keys and authority status are machine-verifiable through the authority directory.
