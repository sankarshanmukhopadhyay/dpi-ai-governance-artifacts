# Changelog

## [1.0.0] - 2026-03-16

### Summary

Infrastructure release. This version establishes the repository's CI baseline, documentation freshness discipline, and public documentation site. It does not introduce new governance artifacts or schema changes — those are preserved from v0.9.0.

### Fixed

- `CITATION.cff`: repaired malformed YAML (`authors:` key was missing, causing the file to be invalid).

### Added

- `.github/workflows/lint-markdown.yml`: Markdown linting CI using `avto-dev/markdown-lint`. Pre-existing style violations are suppressed via `.markdownlint.json` rather than fixed wholesale.
- `.markdownlint.json`: lint configuration with suppressions for MD013 (line length), MD033 (inline HTML), MD041 (first heading), MD024 (duplicate headings).
- `.github/workflows/pages.yml`: GitHub Actions workflow deploying the repository to GitHub Pages on every push to `main`.
- `_config.yml`: Jekyll/primer theme configuration for GitHub Pages.
- `index.md`: curated landing page for the GitHub Pages site.

### Changed

- `.github/workflows/repo-integrity.yml`: extended hygiene check to detect `.pyc` files and `__pycache__` directories in addition to `.DS_Store`.
- `docs/documentation-freshness.md`, `docs/overview.md`, `docs/INDEX.md`, `README.md`: updated `last_reviewed` dates to 2026-03-16 as part of scheduled Tier 0 freshness sweep.
- `TRACE_COMPATIBILITY.json`: added `{ "lab": "0.7.0", "artifacts": "1.0.0", "status": "supported" }` compatibility entry.
- `CITATION.cff`: updated `version` to `1.0.0` and `date-released` to `2026-03-16`.
- `VERSION`: bumped to `1.0.0`.

### Notes

- GitHub Pages requires manual activation in repository settings: Settings → Pages → Source → **GitHub Actions**.
- No governance artifacts, schemas, or controlled documents were modified in this release. See v0.9.0 for the latest substantive changes.

## [Unreleased]

## [0.9.0] - 2026-03-14

### Added
- Canonical governance control catalog in machine-readable JSON plus narrative documentation (`controls/dpi-ai-governance-controls.json`, `controls/dpi-ai-governance-controls.md`).
- Portable risk register JSON Schema and example instance (`schemas/risk-register.schema.json`, `templates/risk-register.example.json`).
- Reference assurance evidence bundle layout and deployment profiles for representative DPI-AI systems (`evidence-bundles/`, `profiles/`).
- Standards crosswalk connecting TRACE-oriented controls to NIST AI RMF, ISO/IEC 42001, OECD AI Principles, and the EU AI Act (`crosswalks/`).

### Changed
- Updated compatibility metadata and documentation navigation for the new Lab v0.6.0 / Artifacts v0.9.0 release pair.
- Refreshed README positioning so the repo presents as an operational toolkit rather than a pile of earnest PDFs in a trench coat.

### Fixed
- Removed metadata drift across `VERSION`, `TRACE_COMPATIBILITY.json`, and release-facing docs.


## [0.8.0] - 2026-03-05

### Added
- Baseline CI pipelines for link checking and repository integrity validation (schema + manifest consistency).
- Pack integrity validator to ensure referenced artifacts exist and pack manifests remain internally consistent.

### Changed
- Documentation refreshed to align with the documentation freshness checklist: improved navigation, ownership cues, and version clarity.
- Version synchronization: repository `VERSION` now reflects the current release series and is kept consistent across docs and release notes.

## [0.6.1]

### Added
- Control library with stable control IDs (`DPI-AI-CTRL-XXX`) and machine-readable registries (`controls/registry.yaml`, `controls/registry.json`).
- Pack-level implementation guides, artifact checklists, control mappings, and additional templates across MDK, Meta-Governance, Redress, Procurement, and Delegated Agent Governance.

### Changed
- Updated pack manifests to reference pack artifacts and declare control coverage.
- Updated README and roadmap to reflect operational pack expansion and control library availability.


## [0.6.0] - 2026-02-22

### Added
- Lawful basis support and conditional enforcement in decision receipts (`schemas/lawful-basis.schema.json`, updates to `schemas/decision-receipt.schema.json`).
- Consolidated shared primitives in `schemas/common-defs.schema.json` to reduce schema drift.
- Vendor capability attestation vectors under `rulebook-test-vectors/vendor-capability-attestation/`.
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

## [0.4.0] - 2026-02-22

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

## [0.3.0] - 2026-02-22

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

## [0.2.1] - 2026-02-22

### Added
- Added explicit acknowledgement and reference link to the Digital Statecraft essay that motivated the Minimum Digital Kernel operational pack.
- Added `REFERENCES.md`.

## [0.2.0] - 2026-02-22

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

## [0.1.0] - 2026-02-21

### Added
- Initial DPI–AI Risk Scoring Matrix artifact
- CC BY-SA 4.0 LICENSE
- CITATION.cff metadata
- VERSION file
- Baseline repository structure
