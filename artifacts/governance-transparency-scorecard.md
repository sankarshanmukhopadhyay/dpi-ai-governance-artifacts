# Governance Transparency Scorecard (Meta-Governance)

A lightweight scorecard to make governance **observable**. This is not a vanity dashboard — it is a control surface.

## Scorecard snapshot template

| Metric | Definition | Target | Current | Evidence |
|---|---|---:|---:|---|
| Decision receipts coverage | % consequential decisions issuing signed receipts | 100% |  | `schemas/decision-receipt.schema.json` |
| Appeal accessibility | % decisions that include appeal routes + deadlines | 100% |  | `schemas/appeal-filing.schema.json` |
| Appeal SLA compliance | % appeals resolved within SLA | ≥ 95% |  | `templates/correction-sla-metrics.md` |
| Rulebook provenance | % rule changes with rationale + approvals recorded | 100% |  | `templates/rulebook-change-control.template.md` |
| Delegation clarity | % authorities with active delegation records + review interval | 100% |  | `schemas/governance-authority-delegation.schema.json` |
| Oversight independence | % auditors with valid oversight-review in last period | 100% |  | `schemas/oversight-review.schema.json` |
| Trigger responsiveness | % governance triggers reviewed within defined window | ≥ 95% |  | `schemas/governance-trigger.schema.json` |

## Notes

- Where metrics are not measurable yet, treat the gap as a governance risk.
- Publish the scorecard internally at minimum; publish externally where feasible.
