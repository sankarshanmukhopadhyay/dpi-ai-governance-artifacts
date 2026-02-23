# Changelog

## [Unreleased]

### Added
- Governance spine (`governance/`) to clarify normativity, controlled documents, and revision discipline.
- Controlled document taxonomy under `controlled/` (risk, assurance, redress, plus reserved categories).
- ToIP compatibility mapping annex under `annex/` and ToIP references in `REFERENCES.md`.

### Changed
- Moved risk and assurance artifacts into `controlled/` (legacy pointers left in `artifacts/` and `conformance/`).

## [0.6.0] - 2026-02-22

### Added
- Lawful basis support and conditional enforcement in decision receipts (`schemas/lawful-basis.schema.json`, updates to `schemas/decision-receipt.schema.json`).
- Consolidated shared primitives in `schemas/common-defs.schema.json` to reduce schema drift.
- Vendor capability attestation vectors under `rulebook-test-vectors/vendor-attestation/`.
- Conformance evidence bundle for TRACE evaluations (`controlled/assurance/evidence-bundles.md`).
- Migration guide for implementers (`docs/migrations/v0.5-to-v0.6.md`).

### Changed
- Expanded repository validation conventions and fixtures to improve determinism for implementers and validators.

## [0.4.1] - 2026-02-22
### Added
- TRACE alignment contract (`docs/trace-alignment.md`) and traceability map (`docs/traceability.*`).
- `TRACE_VERSION` to declare the TRACE method version this repo aligns with.

### Changed
- Bumped repo version to 0.4.1.

All notable changes to this repository will be documented in this file.

The format is based on Keep a Changelog (https://keepachangelog.com/en/1.0.0/) and this project adheres to Semantic Versioning.

## [v0.4.0] - 2026-02-22

### Added
- New schemas to complete remediation and ecosystem interoperability surfaces:
  - `schemas/incident.schema.json` (incident record)
  - `schemas/notification-delivery.schema.json` (notification delivery record)
  - `schemas/federation-agreement.schema.json` (ecosystem federation mechanism)
  - `schemas/tier0-log-entry.schema.json` (portable Tier 0 log minimum)
- Examples for all schema types (plus new schemas) in `templates/`
- Substantive decision-receipt test vectors under `rulebook-test-vectors/decision-receipt/`
- Schema validation tooling and CI:
  - `tools/validate_schemas.py`
  - `.github/workflows/schema-validation.yml`

### Changed
- `schemas/decision-receipt.schema.json`
  - Tier-conditioned enforcement:
    - Tier 2/3 receipts require `subject`
    - Tier 1+ receipts require `appeal`
  - Introduced structured `rulebook.manifest` reference (machine-traversable); retained `manifest_ref` as deprecated
- `schemas/recompute-trigger.schema.json`
  - Added explicit `scope` and support for service-level/batch recompute targets

### Fixed
- `schemas/registry-correction-response.schema.json`
  - Denied responses must include `decision.reason_codes`
- `schemas/appeal-decision.schema.json`
  - Dismissed/denied decisions must include `rationale`
- `schemas/governance-authority-delegation.schema.json`
  - Typed `oversight_body.endpoints` (removed unbounded object)
- `controlled/risk/risk-scoring-matrix.md`
  - Clarified Tier 0 boundary and added conservative tiebreak rule at Priority = 12
- `controlled/assurance/tier-profiles/mdk-tier-profile.md`
  - Specified Tier 0 minimum portable logging format

### Notes
- Items related to lawful basis/consent, supply-chain control artifacts, and playbooks remain planned enhancements for a future release.

## [v0.3.0] - 2026-02-22

### Added
- Meta-governance operational pack (governance-of-governance primitives)
  - `schemas/governance-authority-delegation.schema.json` (delegation ledger)
  - `schemas/oversight-review.schema.json` (audit-of-the-auditor)
  - `schemas/governance-trigger.schema.json` (adaptive governance triggers)
  - `controlled/risk/risk-register.md` (second-order risk register)
  - `controlled/assurance/transparency-scorecard.md` (observable governance scorecard)
  - `templates/governance-constitutional-constraints.template.md` (constitutional guardrails)
  - `docs/guides/meta-governance-operationalising.md` (adoption guide)
- Added reference link to the Shru14stack essay that motivated the meta-governance layer.

### Changed
- README updated to document the meta-governance pack and acknowledgements.

## [v0.2.1] - 2026-02-22

### Added
- Added explicit acknowledgement and reference link to the Digital Statecraft essay that motivated the Minimum Digital Kernel operational pack.
- Added `REFERENCES.md`.

## [v0.2.0] - 2026-02-22

### Added
- Minimum Digital Kernel operational pack
  - Decision receipt schema and examples
  - Authority directory entry schema
  - Rulebook manifest schema, change control template, and test vector scaffold
  - Registry correction and recompute workflow schemas
  - Appeals and audit finding schemas
  - Tier-driven conformance profile for Minimum Digital Kernel primitives
  - Practitioner guides for operational adoption

### Changed
- README updated for clearer onboarding and operational usage

## [v0.1.0] - 2026-02-21

### Added
- Initial DPI–AI Risk Scoring Matrix artifact
- CC BY-SA 4.0 LICENSE
- CITATION.cff metadata
- VERSION file
- Baseline repository structure
