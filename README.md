# DPI–AI Governance Artifacts

![License](https://img.shields.io/badge/license-CC--BY--SA--4.0-blue)
![Release](https://img.shields.io/badge/release-v0.6.0-green)
![Focus](https://img.shields.io/badge/focus-DPI%20%2B%20AI%20governance-orange)

**Operational packs** for DPI + AI systems: portable schemas, templates, playbooks, and conformance materials that turn “governance” from a slide deck into **interfaces you can procure, implement, test, and audit**.

This repo ships a **full governance surface area**:
- Decision and accountability contracts (decision receipts, appeals, audit findings)
- Policy-as-code release discipline (schemas, test vectors)
- Assurance and evidence bundles (TRACE-aligned conformance artifacts)
- Operational playbooks for recurring failure modes

---

## Adoption & integration guidance

Lower the cognitive barrier to adoption by starting with the practical guides below:

- **Companion evaluation engine (Lab):** `dpi-ai-governance-lab` — TRACE (TRACE (Trust, Risk, Architecture & Conformance Evaluation)) method + reproducible paper reviews (see `methodology/` in the Lab repo)
- **How to use this repo (implementation guide):** `docs/guides/how-to-use-this-repo.md`
- **Suggested adoption pathways (startup, enterprise, state):** `docs/guides/adoption-pathways.md`
- **Maturity model alignment:** `docs/guides/maturity-model-alignment.md`
- **Practitioner FAQ:** `docs/faq.md`

## Governance spine (how this repo is organized)

This repository now has an explicit **governance spine** to clarify:
- what is normative vs informative,
- how controlled documents are structured,
- how changes and versions are managed.

Start here:
- `governance/primary.md` (purpose, scope, objectives, principles, normativity, revisions)
- `governance/schedule-of-controlled-docs.md` (authoritative index)
- `governance/normative-language.md` (MUST/SHOULD/MAY conventions)

---

## Controlled documents (modular governance)

Controlled documents live under `controlled/`:

- Risk: `controlled/risk/`
- Assurance: `controlled/assurance/`
- Redress: `controlled/redress/`
- Technical (reserved): `controlled/technical/`
- Information trust (reserved): `controlled/info-trust/`
- Inclusion & accessibility (reserved): `controlled/inclusion-accessibility/`
- Legal (reserved): `controlled/legal/`

Key entry points:
- Evidence bundles: `controlled/assurance/evidence-bundles.md`
- Tier profiles: `controlled/assurance/tier-profiles/`
- Risk register: `controlled/risk/risk-register.md`
- Redress + remediation: `controlled/redress/redress-and-remediation.md`

---

## Where this fits (portfolio view)

This repository is the **operational layer** for the DPI–AI Governance Lab methodology.

- Normative methodology + evaluation workflow: `dpi-ai-governance-lab`
- Operational artifacts you can embed into programs and systems: this repo

See:
- Methodology alignment: `docs/methodology-alignment.md`
- Traceability map: `docs/traceability.md` and `docs/traceability.json`

---

## ToIP acknowledgment (inspiration, not compliance)

This repository borrows structural discipline from the Trust Over IP (ToIP) Governance Metamodel (primary + controlled documents, and normative drafting conventions). It does **not** claim ToIP Governance Framework compliance.

See the mapping:
- `annex/toip-governance-metamodel-mapping.md`

And the ToIP references:
- `REFERENCES.md`

---

## Repository map

- `schemas/` — JSON Schemas (machine-testable)
- `templates/` — fillable structures for governed artifacts
- `rulebook-test-vectors/` — examples to validate implementations
- `playbooks/` — operational runbooks for recurring failure modes
- `docs/` — guides, methodology alignment, migrations, traceability
