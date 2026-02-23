# Operationalising Meta-Governance of AI Systems

This guide translates the **meta-governance** idea (“governance of governance”) into portable, auditable artifacts that can be used in DPI + AI programs.

## What meta-governance adds

Most governance programs define controls for an AI system (rulebooks, receipts, appeals, audits). Meta-governance adds controls for the *governance system itself*:

- Who has the mandate to govern (and who delegated it)?
- How are rule changes approved and traced?
- Who audits the auditors, and how is independence evidenced?
- When does governance adapt (triggers), and how fast?

## Repository artifacts to adopt

### 1) Delegation ledger (who can do what)
- `schemas/governance-authority-delegation.schema.json`

Minimum viable use:
- Require an active delegation record for every “authority directory entry” used as a verifier input.
- Set review intervals and sunset dates to reduce delegation sprawl.

### 2) Oversight review (audit of the auditor)
- `schemas/oversight-review.schema.json`

Minimum viable use:
- For each audit body, maintain a review covering independence, funding, conflicts, and peer review.

### 3) Governance triggers (when governance must adapt)
- `schemas/governance-trigger.schema.json`

Minimum viable use:
- Define 5–10 triggers that force review: appeal spikes, SLA breaches, bias signals, major model changes, major policy changes.

### 4) Meta-governance risk register
- `controlled/risk/risk-register.md`

Minimum viable use:
- Review quarterly, and whenever a governance trigger fires.

### 5) Transparency scorecard
- `controlled/assurance/transparency-scorecard.md`

Minimum viable use:
- Publish internally monthly; publish externally where possible.

### 6) Constitutional constraints
- `templates/governance-constitutional-constraints.template.md`

Minimum viable use:
- Adopt as a hard guardrail layer for emergency powers, automation limits, and delegation constraints.

## Practical sequencing

1. Stand up delegation records for existing authorities.
2. Define governance triggers and connect them to your change control runbooks.
3. Run one “audit of the auditor” review cycle.
4. Publish a baseline transparency scorecard.
5. Institutionalize the risk register review cadence.

## Acknowledgement

These additions were motivated by the essay “Meta-governance of AI systems” (Shru14stack / Substack). See `REFERENCES.md`.
