# Governance Risk Register (Meta-Governance)

This artifact captures **second-order risks**: risks in the *governance system itself* (not only in the AI system being governed).

Use this register alongside:
- `artifacts/dpi-ai-risk-scoring-matrix.md` (Tiering)
- `schemas/audit-finding.schema.json` (Oversight findings)
- `schemas/appeal-*.schema.json` (Contestability signals)

## Risk taxonomy

| Risk category | What it looks like | Leading indicators | Mitigations / controls | Evidence artifacts |
|---|---|---|---|---|
| Regulatory capture | Governance outcomes align with a sponsor/vendor over public purpose | Repeated favorable exceptions; low transparency; revolving door | Independence rules; `oversight-review` peer checks; funding disclosures | `schemas/oversight-review.schema.json` |
| Delegation sprawl | Unbounded proliferation of authorities and sub-authorities | Duplicate mandates; unclear owners; conflicting rules | Delegation ledger; mandatory review intervals; sunset clauses | `schemas/governance-authority-delegation.schema.json` |
| Procedural opacity | No clear path to understand *why* rules exist or changed | Missing rationale; no consultation record | Rulebook provenance requirements; change control discipline | `templates/rulebook-change-control.template.md` |
| Governance drift | Silent changes that shift policy posture without review | Rulebook changes not linked to triggers; ad‑hoc exceptions | Triggered governance updates; approvals and logs | `schemas/governance-trigger.schema.json` |
| Oversight failure | Audits are symbolic or compromised | No sampling; no follow-up; conflicts not declared | Audit-of-auditor reviews; independence scoring | `schemas/oversight-review.schema.json` |
| Appeal bottleneck | Contestability exists on paper but not in throughput | SLA breaches; backlog; low resolution rate | SLAs; staffing; automated intake; triage | `templates/correction-sla-metrics.md` |
| Fragmentation | Multiple overlapping rulebooks create incoherence | Divergent reason codes; inconsistent outcomes | Harmonized reason code vocab; interoperability mapping | `schemas/reason-codes.vocab.json` |

## Operating rhythm (minimum viable)

1. Review this register quarterly (or when a **governance trigger** fires).
2. For each “high” risk, require an **evidence bundle** (audit notes, change controls, delegation records).
3. Publish a transparency scorecard snapshot (see `artifacts/governance-transparency-scorecard.md`).
