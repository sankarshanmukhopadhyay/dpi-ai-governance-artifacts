# DPI–AI Governance Artifacts

## Documentation

- Overview: `docs/overview.md`
- Pack catalog: `packs/README.md`
- Freshness + audit guardrails: `docs/documentation-freshness.md`

![License](https://img.shields.io/badge/license-CC--BY--SA--4.0-blue)
![Release](https://img.shields.io/badge/release-v1.1.0-green)
![Focus](https://img.shields.io/badge/focus-DPI%20%2B%20AI%20governance-orange)
![Pages](https://img.shields.io/badge/docs-GitHub%20Pages-blue)

**Operational packs** for DPI + AI systems: portable schemas, templates, playbooks, test vectors, and conformance materials that turn governance propositions into **interfaces you can procure, implement, test, audit, revoke, correct, and evidence**.

This repository is the remediation side of the DPI AI Governance Lab improvement loop:

```text
TRACE evaluation
  -> governance gap
  -> required capability
  -> remediation registry
  -> implementation artifacts
  -> adversarial tests
  -> closure evidence
  -> TRACE re-evaluation
```

For an implementer or operator, start with:

- `remediation/remediation-registry.yaml` — machine-readable capability-to-artifact resolver
- `docs/remediation-resolution.md` — gap-to-implementation and closure workflow
- `docs/operator-playbook.md` — practical operator path
- `tools/validate_remediation_registry.py` — CI-safe validation that mapped artifacts exist

## New in v1.1.0

The Digital Statecraft DPI first-wave programme supplied evidence for three recurring capability gaps that are now standardized as reusable, publication-independent remediation contracts:

- **Consequential inference traceability** — `CAP-INFERENCE-TRACEABILITY`
  - immutable model/algorithm identity and version
  - decision-time input/threshold/output binding
  - rule-vs-inference separation
  - decision-receipt correlation
- **Correction propagation and recomputation** — `CAP-CORRECTION-PROPAGATION`
  - correction orders
  - downstream dependency targets
  - invalidation/recompute/replace/compensate actions
  - execution receipts and partial-failure semantics
- **Inter-institutional admissibility** — `CAP-INTERINSTITUTIONAL-ADMISSIBILITY`
  - relying-party admissibility profiles
  - purpose/jurisdiction/validity/assurance conditions
  - revocation and expiry
  - authentic-but-inadmissible negative tests

The same programme also standardized bounded delegation and proved a six-capability worked fixture in the companion Lab. The historical corpus baseline remains unchanged; v1.1.0 records the current reusable remediation state.

> **Authority boundary:** these artifacts encode and test adopted governance rules. They do not create legal authority, jurisdictional admissibility, certification, or deployment approval by themselves.

## Governance surface

The repository ships:

- Decision and accountability contracts: decision receipts, appeals, audit findings
- Authority and delegation controls: bounded delegation and runtime authorization records
- Trust/reliance controls: inter-institutional admissibility and relying-party decisions
- AI decision evidence: inference traces with immutable model/version/input/threshold bindings
- Correction/redress controls: source correction, downstream propagation, recomputation, supersession, and remedy
- Policy-as-code release discipline: schemas and test vectors
- Assurance and evidence bundles: TRACE-aligned conformance artifacts
- Operational playbooks for recurring failure modes

The remediation registry deliberately distinguishes **partial** from **standardized** coverage. A partial entry must expose where further design work is still required rather than overstating repository maturity.

## Adoption & integration guidance

- `docs/guides/how-to-use-this-repo.md`
- `docs/guides/adoption-pathways.md`
- `docs/guides/maturity-model-alignment.md`
- `docs/faq.md`

> TRACE means **Trust, Risk, Architecture & Conformance Evaluation**.

## Governance spine

Start here:

- `governance/primary.md` — purpose, scope, authority, normativity, revisions
- `governance/schedule-of-controlled-docs.md` — authoritative controlled-document index
- `governance/normative-language.md` — MUST/SHOULD/MAY conventions

Controlled documents live under `controlled/`:

- `controlled/risk/`
- `controlled/assurance/`
- `controlled/redress/`
- `controlled/governance/`
- reserved domains under `controlled/technical/`, `controlled/info-trust/`, `controlled/inclusion-accessibility/`, and `controlled/legal/`

Key entry points:

- `controlled/governance/bounded-delegation.md`
- `controlled/governance/inference-traceability.md`
- `controlled/trust/interinstitutional-admissibility.md`
- `controlled/redress/correction-propagation.md`
- `controlled/assurance/evidence-bundles.md`
- `controlled/risk/risk-register.md`

## Where this fits

This repository is the **operational remediation layer** for the DPI–AI Governance Lab methodology.

- Evaluation, findings, gap normalization, verification, and re-evaluation: `dpi-ai-governance-lab`
- Reusable schemas, controls, test vectors, guidance, and evidence requirements: this repository

See:

- `docs/methodology-alignment.md`
- `docs/traceability.md`
- `docs/traceability.json`

## ToIP acknowledgment

This repository borrows structural discipline from the Trust Over IP Governance Metamodel. It does **not** claim ToIP Governance Framework compliance.

See:

- `annex/toip-governance-metamodel-mapping.md`
- `REFERENCES.md`

## Repository map

- `schemas/` — machine-testable JSON Schemas
- `templates/` — fillable governed-artifact structures
- `test-vectors/` and `rulebook-test-vectors/` — deterministic positive/negative examples
- `playbooks/` — operational runbooks
- `remediation/` — capability-to-artifact resolution registry and coverage evidence
- `controlled/` — governed operator guidance
- `evidence-bundles/` — assurance evidence structures
- `docs/` — guides, methodology alignment, migrations, traceability, and Pages content

## Methodology

Operational templates align to the TRACE↔TSAM spine; see `docs/reference/TRACE-TSAM.md`.

## Documentation index

See `docs/INDEX.md` and the GitHub Pages site for the rendered operator documentation.
