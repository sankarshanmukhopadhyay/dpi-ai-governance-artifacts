# Suggested adoption pathways

This guide provides three pragmatic adoption pathways, optimized for different organizational realities.

Each pathway follows the same principle: **start with one workflow that creates defensible evidence**, then expand.

---

## Pathway A — Startup / small team

**Goal:** Ship faster *without* accumulating unpayable governance debt.

### 0–2 weeks: establish a thin governance slice
- Adopt a minimal **risk register** and scoring approach (`controlled/risk/*`).
- Implement **decision receipts** for key automated decisions (schemas/templates).
- Pick one **redress path** for users/customers (`controlled/redress/redress-and-remediation.md`).

**Outputs:**
- A living risk register
- Decision receipt format + owner
- A basic appeal/remediation workflow

### 2–6 weeks: operationalize and standardize
- Standardize incident handling using playbooks (`playbooks/*`).
- Start producing an evidence bundle snapshot for internal review (`conformance/evidence-bundle.md`).

### 6–12 weeks: harden and automate
- Validate key artifacts using schemas.
- Add governance triggers (when risk scores require escalation).

---

## Pathway B — Enterprise / regulated environment

**Goal:** Reduce audit friction and integration cost across many teams.

### 0–4 weeks: establish enterprise baseline
- Adopt controlled governance commitments (risk + redress + assurance).
- Define “minimum artifact set” per product/system.
- Standardize templates for teams to use.

### 4–10 weeks: integrate into SDLC and operations
- Bind artifacts to delivery gates (design review, launch review, incident review).
- Integrate schemas into CI validation or internal tooling.
- Use evidence bundle expectations for quarterly assurance.

### 10–16 weeks: scale assurance
- Establish a portfolio-level transparency scorecard.
- Institutionalize audits via recurring evidence bundle sampling.

---

## Pathway C — State / DPI program / public agency

**Goal:** Create procurement- and oversight-grade governance posture.

### 0–6 weeks: governance front door
- Choose a baseline governance posture and publish commitments.
- Create procurement requirements aligned to evidence expectations.
- Establish redress and accountability mechanisms.

### 6–12 weeks: enforce via procurement and oversight
- Require vendor artifacts (capability attestations, dependency inventories, incident response plans).
- Require periodic evidence bundle submissions.
- Stand up an oversight review cadence.

### 12+ weeks: ecosystem alignment
- Create interoperability expectations across programs.
- Use maturity alignment to drive phased uplift across departments and vendors.

---

## Expansion strategy

Once one pathway is in motion, expand along two axes:
1. **Coverage:** more workflows (risk, redress, transparency, procurement)
2. **Depth:** higher maturity level (more mandatory artifacts, tighter evidence)

For a concrete maturity progression, see `docs/guides/maturity-model-alignment.md`.
