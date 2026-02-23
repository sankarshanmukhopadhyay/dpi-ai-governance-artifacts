# Annex: Mapping to ToIP Governance Metamodel (compatibility, not compliance)

This repository borrows **structural discipline** from the Trust Over IP (ToIP) Governance Metamodel:
- modular governance documents (primary + controlled documents),
- normative language conventions,
- separation between human-auditable policies and machine-testable rules.

This is a **compatibility mapping**. It does **not** assert that this repository is a ToIP Governance Framework.

## Source references (ToIP)

- ToIP Governance Metamodel Specification v1.0 (21 Dec 2021)
  https://trustoverip.org/wp-content/uploads/ToIP-Governance-Metamodel-Specification-V1.0-2021-12-21.pdf

- ToIP Governance Metamodel Specification Companion Guide v1.0 (21 Dec 2021)
  https://trustoverip.org/wp-content/uploads/ToIP-Governance-Metamodel-Specification-Companion-Guide-V1.0-2021-12-21.pdf

## Section mapping

| ToIP concept | ToIP section | DPI–AI Governance Artifacts location |
|---|---|---|
| Primary document (“home page”) | Primary Document | `governance/primary.md` |
| Terminology + notation | Terminology and Notation | `governance/normative-language.md` + `docs/governance-model/artifact-kinds.md` |
| Purpose / Scope / Objectives / Principles | Primary Document | `governance/primary.md` |
| Revisions | Revisions | `governance/primary.md` + `CHANGELOG.md` + `docs/migrations/` |
| Schedule of controlled documents | Schedule of Controlled Documents | `governance/schedule-of-controlled-docs.md` |
| Risk Assessment | Controlled Documents | `controlled/risk/` |
| Trust Assurance and Certification | Controlled Documents | `controlled/assurance/` |
| Technical Requirements | Controlled Documents | `controlled/technical/` (reserved) |
| Information Trust Requirements | Controlled Documents | `controlled/info-trust/` (reserved) |
| Inclusion, Equitability, Accessibility | Controlled Documents | `controlled/inclusion-accessibility/` (reserved) |
| Legal Agreements | Controlled Documents | `controlled/legal/` (reserved) |
| Dispute resolution / enforcement | Governance Requirements + Legal | `controlled/redress/` (expanded beyond ToIP baseline) |

## Known divergences

- This repository prioritizes **artifact-first operationalization** (schemas/templates/test vectors) over governance website publication mechanics.
- DID/DID-URL addressability is not mandated here; versioning is repo-native (`VERSION`, `TRACE_VERSION`) with migration guides.
