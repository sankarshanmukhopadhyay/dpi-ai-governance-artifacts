# Maturity model alignment

This repository supports staged adoption. The purpose of a maturity model here is not bureaucracy — it is **coordination**: teams need a shared definition of “baseline” versus “assurance-grade.”

The levels below are deliberately simple and map to concrete artifact expectations.

---

## Level 0 — Ad hoc
**Signal:** Decisions are made, but documentation is inconsistent.

**Minimum uplift:**
- Start a risk register (even if rough).
- Start capturing decision receipts for critical automated decisions.

---

## Level 1 — Documented
**Signal:** Key governance artifacts exist and are consistently used.

**Expected artifacts:**
- Risk register + scoring matrix (`controlled/risk/*`)
- Redress & remediation procedure (`controlled/redress/redress-and-remediation.md`)
- Basic incident playbooks (`playbooks/*`)

**Evidence:**
- Snapshot evidence bundle showing these artifacts exist and are used.

---

## Level 2 — Operationalized
**Signal:** Governance artifacts are integrated into delivery and operations.

**Expected artifacts:**
- Decision receipts and authority/ownership mapping
- Governance triggers (when issues must escalate)
- Evidence bundle expectations defined and used (`controlled/assurance/evidence-bundles.md`)

**Evidence:**
- Evidence bundles produced on a cadence (release, quarterly, incident-based)

---

## Level 3 — Assured
**Signal:** Governance posture is testable, reviewable, and auditable.

**Expected artifacts:**
- Conformance guidance adopted (`conformance/*`)
- Repeatable review cadence (oversight review, audit findings, remediation completion)
- Portfolio transparency scorecard (`controlled/assurance/transparency-scorecard.md`)

**Evidence:**
- Completed evidence bundles and remediation closure records

---

## Level 4 — Interoperable
**Signal:** Governance artifacts are portable across vendors and programs.

**Expected artifacts:**
- Consistent schema usage for key artifacts (`schemas/*`)
- Standardized vendor attestations and dependency inventories (`templates/*`)
- Cross-program comparability via traceability and scorecards (`docs/traceability*`, `controlled/assurance/*`)

**Evidence:**
- Multi-system evidence bundles that can be reviewed externally

---

## How to use this maturity model

- Use it as a **portfolio planning tool**: which systems must be Level 3 vs Level 1?
- Use it in **procurement**: vendors must demonstrate Level 2+ artifacts.
- Use it as an **internal roadmap**: uplift a system one level per quarter.

---

## Alignment to TRACE and assurance tiers

This repo also includes TRACE methodology alignment artifacts and tier profiles (e.g., MDK tier profile). The maturity model provides an *adoption lens*, while tiers/profiles provide an *assurance lens*.

A practical mapping:
- Levels 1–2: establish baseline governance and operational use.
- Level 3: bind governance to conformance and evidence.
- Level 4: make it portable, comparable, and procurement-grade.
