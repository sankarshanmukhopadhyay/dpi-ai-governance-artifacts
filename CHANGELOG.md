# Changelog

## [Unreleased]

## [1.1.0] - 2026-08-22

### Summary

Evidence-derived governance-capability release. This version closes the three reusable remediation gaps identified across the Digital Statecraft DPI first-wave TRACE corpus while preserving the repository's authority boundary and historical baselines.

### Added

- `CAP-INFERENCE-TRACEABILITY`
  - `schemas/governance/inference-trace.schema.json`
  - deterministic positive/negative inference-trace vectors
  - CI validator for version, digest, threshold, input-snapshot, decision-correlation, and rule-vs-inference semantics
  - controlled operator guidance with diagrams
- `CAP-CORRECTION-PROPAGATION`
  - machine-readable correction-order and correction-execution-receipt contracts
  - downstream invalidation, recomputation, replacement, and compensation semantics
  - partial-failure and false-completion prevention tests
  - controlled lifecycle/sequence guidance
- `CAP-INTERINSTITUTIONAL-ADMISSIBILITY`
  - admissibility-profile and reliance-decision schemas
  - purpose, jurisdiction, validity, assurance-condition, expiry, revocation, and recourse semantics
  - authentic-but-inadmissible negative tests
  - controlled trust/reliance guidance
- Evidence provenance in the remediation registry linking each new capability to the Digital Statecraft corpus, contributing TRACE reviews, recurring gap class, and previous coverage state.
- Operator-first Just-the-Docs information architecture, Pages manifests, front-matter enforcement, and diagrams for the new capability surfaces.

### Changed

- Remediation registry advanced from `0.2.0` historical baseline state to `0.5.0` current state while keeping historical evidence immutable.
- First-wave Digital Statecraft gap mapping improves from 10/19 standardized mappings (52.63%) to 19/19 current mappings (100%).
- `TRACE_COMPATIBILITY.json` records the supported Lab `0.8.0` / Artifacts `1.1.0` release pair.
- README now foregrounds the gap → capability → artifact → test → closure workflow and the new reusable capability families.

### Assurance boundary

- Repository artifacts remain non-normative unless adopted by an external authority.
- Inter-institutional admissibility artifacts represent an adopting institution's reliance policy; they do not create legal admissibility.
- Inference traces record model contribution; they do not certify model lawfulness, fairness, or accuracy.
- Correction propagation executes authorized correction semantics; it does not determine whether a correction is legally warranted.

## [1.0.0] - 2026-03-16

### Summary

Infrastructure release. This version establishes the repository's CI baseline, documentation freshness discipline, and public documentation site. It does not introduce new governance artifacts or schema changes — those are preserved from v0.9.0.

### Fixed

- `CITATION.cff`: repaired malformed YAML (`authors:` key was missing, causing the file to be invalid).

### Added

- `.github/workflows/lint-markdown.yml`: Markdown linting CI using `avto-dev/markdown-lint`.
- `.markdownlint.json`: lint configuration.
- `.github/workflows/pages.yml`: GitHub Actions workflow deploying the repository to GitHub Pages.
- `_config.yml`: Jekyll/primer theme configuration.
- `index.md`: curated landing page for the GitHub Pages site.

### Changed

- `.github/workflows/repo-integrity.yml`: extended hygiene checks.
- Documentation freshness metadata updated.
- `TRACE_COMPATIBILITY.json`: added the Lab `0.7.0` / Artifacts `1.0.0` supported pair.
- `CITATION.cff` and `VERSION` synchronized to `1.0.0`.

## [0.9.0] - 2026-03-14

### Added

- Canonical governance control catalog in machine-readable JSON plus narrative documentation.
- Portable risk register JSON Schema and example instance.
- Reference assurance evidence bundle layout and representative deployment profiles.
- Standards crosswalk connecting TRACE-oriented controls to NIST AI RMF, ISO/IEC 42001, OECD AI Principles, and the EU AI Act.

### Changed

- Updated compatibility metadata and documentation navigation for the Lab v0.6.0 / Artifacts v0.9.0 release pair.
- Refreshed README positioning toward an operational toolkit.

### Fixed

- Removed metadata drift across `VERSION`, `TRACE_COMPATIBILITY.json`, and release-facing docs.

## [0.8.0] - 2026-03-05

### Added

- Baseline CI pipelines for link checking and repository integrity validation.
- Pack integrity validator ensuring referenced artifacts exist and pack manifests remain internally consistent.

### Changed

- Documentation refreshed for navigation, ownership cues, and version clarity.
- Version synchronization across release surfaces.

## [0.6.1]

### Added

- Control library with stable control IDs and machine-readable registries.
- Pack-level implementation guides, artifact checklists, control mappings, and additional templates.

### Changed

- Pack manifests reference pack artifacts and declare control coverage.
- README and roadmap updated for operational pack expansion.

## [0.6.0] - 2026-02-22

### Added

- Lawful-basis support and conditional enforcement in decision receipts.
- Consolidated shared schema primitives.
- Vendor capability attestation vectors.
- Conformance evidence bundle for TRACE evaluations.
- Migration guide for implementers.

### Changed

- Expanded repository validation conventions and fixtures.

## [0.4.1] - 2026-02-22

### Added

- TRACE alignment contract and traceability map.
- `TRACE_VERSION` declaration.

### Changed

- Repository version bumped to 0.4.1.

## [0.4.0] - 2026-02-22

### Added

- New incident, notification delivery, federation agreement, and Tier 0 log schemas.
- Examples for schema types and substantive decision-receipt test vectors.
- Schema validation tooling and CI.

### Changed

- Decision receipt tier-conditioned enforcement and structured rulebook manifest references.
- Recompute trigger scope support.

### Fixed

- Registry correction denial reason-code requirements.
- Appeal denial/dismissal rationale requirements.
- Governance delegation endpoint typing.
- Tier 0 risk/profile clarification.

## [0.3.0] - 2026-02-22

### Added

- Meta-governance operational pack covering delegation ledger, oversight review, adaptive triggers, second-order risks, transparency, and constitutional constraints.

### Changed

- README updated for meta-governance pack and acknowledgements.

## [0.2.1] - 2026-02-22

### Added

- Explicit acknowledgement and reference link to the Digital Statecraft essay that motivated the Minimum Digital Kernel operational pack.
- `REFERENCES.md`.

## [0.2.0] - 2026-02-22

### Added

- Minimum Digital Kernel operational pack including decision receipts, authority directory entries, rulebook manifests, registry correction/recompute workflows, appeals, audit findings, and conformance profiles.

### Changed

- README updated for clearer onboarding and operational usage.

## [0.1.0] - 2026-02-21

### Added

- Initial DPI–AI Risk Scoring Matrix artifact.
- CC BY-SA 4.0 license.
- Citation metadata.
- Baseline repository structure.

All notable changes to this repository are documented here. The format is based on Keep a Changelog and the project follows Semantic Versioning.
