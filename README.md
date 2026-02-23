# DPI–AI Governance Artifacts

![License](https://img.shields.io/badge/license-CC--BY--SA--4.0-blue)
![Release](https://img.shields.io/badge/release-v0.6.0-green)
![Focus](https://img.shields.io/badge/focus-DPI%20%2B%20AI%20governance-orange)

**Operational packs** for DPI + AI systems: portable schemas, templates, playbooks, and conformance checklists that turn “governance” from a slide deck into **interfaces you can procure, implement, test, and audit**.

This repo has grown beyond a single pack. It now ships a **full governance surface area**:
- **Decision and accountability contracts** (decision receipts, appeals, audit findings)
- **Authority and delegation contracts** (who can do what, with what limits, and how oversight works)
- **Policy-as-code release discipline** (rulebook manifests, test vectors)
- **Incident and notification interfaces** (so failures have a standard shape)
- **Assurance and evidence bundles** (TRACE-aligned conformance artifacts)
- **Operational playbooks** for recurring failure modes

---

## Where this fits (portfolio view)

This repository is the **operational layer** for the DPI–AI Governance Lab methodology.

- **Normative methodology + evaluation workflow:** `dpi-ai-governance-lab`
- **Operational artifacts you can embed into programs and systems:** this repo

See:
- Methodology alignment: `docs/methodology-alignment.md`
- Traceability map: `docs/traceability.md` and `docs/traceability.json`

---

## What you can do with this repo (practical outcomes)

Use these artifacts to harden delivery and de-risk adoption:

1. **Procurement-ready requirements**  
   Turn “must be transparent” into a schema-backed requirement: *emit a signed decision receipt*, *support appeals*, *publish a rulebook manifest*, *log Tier 0 events*, etc.

2. **Implementation contracts**  
   Give engineering teams explicit JSON contracts for governance surfaces (instead of vague policy docs).

3. **Audit and assurance acceleration**  
   Use conformance profiles + evidence bundle checklists to reduce audit ambiguity and the “interpretive dance” tax.

4. **Interoperability across vendors and ministries**  
   Standard shapes for receipts, delegations, incidents, and notifications reduce bespoke integrations.

---

## What’s inside (high signal inventory)

### Baseline risk tiering
- `artifacts/dpi-ai-risk-scoring-matrix.md`  
  A Tier 0–3 risk model with governance bindings.

### Minimum Digital Kernel pack (core interoperability + redress)
Key contracts that frequently become mandatory once systems become consequential:

- Decision and redress:
  - `schemas/decision-receipt.schema.json`
  - `schemas/appeal-filing.schema.json`
  - `schemas/appeal-decision.schema.json`
  - `schemas/audit-finding.schema.json`

- Trust/authority directories:
  - `schemas/authority-directory-entry.schema.json`

- Policy release discipline:
  - `schemas/rulebook-manifest.schema.json`
  - `rulebook-test-vectors/` (fixtures for validators and implementers)

- Corrections and recompute:
  - `schemas/registry-correction-request.schema.json`
  - `schemas/registry-correction-response.schema.json`
  - `schemas/recompute-trigger.schema.json`

- Incidents, notifications, federation:
  - `schemas/incident.schema.json`
  - `schemas/notification-delivery.schema.json`
  - `schemas/federation-agreement.schema.json`
  - `schemas/tier0-log-entry.schema.json`

Conformance guidance:
- `conformance/mdk-tier-profile.md` (Tier-driven “what is required when”)

### Meta-governance pack (governing the governors)
Second-order controls so governance does not silently fail:

- `schemas/governance-authority-delegation.schema.json` (mandates, scope, limits, lifecycle, oversight)
- `schemas/oversight-review.schema.json` (audit-of-auditor / independence / peer review)
- `schemas/governance-trigger.schema.json` (machine-readable triggers for governance adaptation)
- `artifacts/governance-risk-register.md`
- `artifacts/governance-transparency-scorecard.md`
- `docs/guides/meta-governance-operationalising.md`

### Supply-chain / vendor attestations
- `schemas/vendor-capability-attestation.schema.json`
- `schemas/supply-chain-control.schema.json`
- `rulebook-test-vectors/vendor-attestation/` (known-good/known-bad fixtures)

### Shared schema primitives
To reduce drift and make schemas composable:

- `schemas/common-defs.schema.json`
- `schemas/lawful-basis.schema.json`
- `schemas/reason-codes.vocab.json`

Migration note:
- `docs/migrations/v0.5-to-v0.6.md` (lawful basis rules + common defs consolidation)

### Operational playbooks
Scenario playbooks for recurring governance failure modes:

- `playbooks/model-drift.md`
- `playbooks/widespread-misclassification.md`
- `playbooks/security-compromise.md`

---

## TRACE alignment and conformance

This repository ships **TRACE-aligned operational artifacts**.

- Alignment contract: `docs/trace-alignment.md`
- TRACE version: `TRACE_VERSION`
- Conformance evidence bundle: `conformance/evidence-bundle.md`

---

## Quickstart (recommended adoption path)

1. **Start with Tiering**  
   Apply `artifacts/dpi-ai-risk-scoring-matrix.md` to classify a system (Tier 0–3).

2. **Make decisions auditable by default**  
   Require `schemas/decision-receipt.schema.json` for consequential decisions.  
   Tier 2/3 + *person* decisions: follow the lawful basis requirements in `docs/migrations/v0.5-to-v0.6.md`.

3. **Make redress real (not ceremonial)**  
   Implement `schemas/appeal-filing.schema.json` and `schemas/appeal-decision.schema.json`, and capture oversight using `schemas/audit-finding.schema.json`.

4. **Make governance itself observable**  
   Adopt the meta-governance pack: delegation ledger + oversight review + governance triggers.

5. **Prove it with evidence**  
   Use `conformance/evidence-bundle.md` to operationalize assurance claims in a TRACE evaluation.

---

## Validation (schemas + examples)

This repository ships **examples** and **test vectors** that validate against the schemas.

Run locally:

```bash
python -m pip install jsonschema
python tools/validate_schemas.py
```

---

## Repository structure

| Path | What it contains |
|---|---|
| `artifacts/` | Published governance artifacts (risk registers, scorecards, tiering) |
| `schemas/` | Machine-readable contracts for governance interfaces |
| `templates/` | Example instances and implementation templates |
| `rulebook-test-vectors/` | Known-good/known-bad fixtures for validators |
| `conformance/` | Conformance profiles and evidence bundles |
| `playbooks/` | Practitioner playbooks for common failure modes |
| `docs/` | Guides, traceability, alignment, and migration notes |
| `tools/` | Validation and helper tooling |

---

## Acknowledgements

This repo translates ideas into implementable artifacts and is **not affiliated with** or endorsed by the authors below.

- “The Minimum Digital Kernel of an Effective State” (Digital Statecraft / Substack)  
  https://open.substack.com/pub/digitalstatecraft/p/the-minimum-digital-kernel-of-an

- “Meta-governance of AI systems” (Shru14stack / Substack)  
  https://open.substack.com/pub/shru14stack/p/meta-governance-of-ai-systems

---

## Citation and attribution

If you reuse or adapt this work, please attribute:

Sankarshan Mukhopadhyay (2026). *DPI–AI Governance Artifacts*. Licensed under **CC BY-SA 4.0**.

Contact: sankarshan@qbfconsulting.digital

## License

All materials in this repository are licensed under **CC BY-SA 4.0** unless noted otherwise. See `LICENSE.md`.
