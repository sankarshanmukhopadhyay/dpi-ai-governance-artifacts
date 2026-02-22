# DPI–AI Governance Artifacts

![License](https://img.shields.io/badge/license-CC--BY--SA--4.0-blue)
![Version](https://img.shields.io/badge/version-v0.2.0-green)
![Type](https://img.shields.io/badge/type-governance--artifacts-orange)

A lightweight, evolving repository of governance-ready artifacts for DPI + AI systems.

This release adds an **operational pack** that translates the "Minimum Digital Kernel" idea into **portable interface contracts**: schemas, templates, and conformance profiles that teams can adopt in procurement, implementation, and audit workflows.

## Version

Current release: **v0.2.0** (Minimum Digital Kernel Operational Pack)

## What is inside

### Baseline artifacts
- `artifacts/dpi-ai-risk-scoring-matrix.md` 
  Risk scoring matrix and Tier 0–3 governance bindings.

### Minimum Digital Kernel operational pack
- `schemas/decision-receipt.schema.json` 
  A machine-readable contract for signed decision receipts.
- `schemas/authority-directory-entry.schema.json` 
  A minimal entry format for authority directories and trust directories.
- `schemas/rulebook-manifest.schema.json` 
  A release discipline format for versioned rulebooks (policy as code).
- `schemas/registry-correction-*.schema.json` and `schemas/recompute-trigger.schema.json` 
  Correction, recompute, and notification workflows.
- `schemas/appeal-*.schema.json` and `schemas/audit-finding.schema.json` 
  Contestability and oversight interfaces.
- `templates/` 
  Ready-to-use examples and governance templates (change control, validation checklists, SLAs).
- `conformance/mdk-tier-profile.md` 
  Tier-driven conformance expectations for Minimum Digital Kernel primitives.

## How to use

1. Start with the Tier model in `artifacts/dpi-ai-risk-scoring-matrix.md`.
2. Adopt `schemas/decision-receipt.schema.json` as a procurement and implementation requirement for consequential decisions.
3. Use `conformance/mdk-tier-profile.md` to map risk tiers to mandatory kernel primitives.
4. Plug in the templates under `templates/` to standardize audits, registry corrections, and appeals.

## Repository structure
- `/artifacts` 
  Published governance artifacts
- `/schemas` 
  Machine-readable schemas for operational governance
- `/templates` 
  Templates and examples for implementers
- `/conformance` 
  Conformance profiles and checklists
- `/docs` 
  Guides and notes

## Citation and attribution

If you reuse or adapt this work, please attribute as follows:

Sankarshan Mukhopadhyay (2026). *DPI–AI Governance Artifacts*. Licensed under **CC BY-SA 4.0**.

Contact: sankarshan@qbfconsulting.digital

## License

All materials in this repository are licensed under **CC BY-SA 4.0** unless noted otherwise. See `LICENSE.md`.
