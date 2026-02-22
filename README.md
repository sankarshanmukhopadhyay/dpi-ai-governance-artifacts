# DPI–AI Governance Artifacts

![License](https://img.shields.io/badge/license-CC--BY--SA--4.0-blue)
![Version](https://img.shields.io/badge/version-v0.4.0-green)
![Type](https://img.shields.io/badge/type-governance--artifacts-orange)

A lightweight, evolving repository of governance-ready artifacts for DPI + AI systems.

This release adds an **operational pack** that translates the "Minimum Digital Kernel" idea into **portable interface contracts**: schemas, templates, and conformance profiles that teams can adopt in procurement, implementation, and audit workflows.



## TRACE alignment

This repository provides **TRACE-aligned operational artifacts**.

- TRACE definition and controls live in the Lab repo (`docs/trace/`).
- Alignment contract: `docs/trace-alignment.md`
- Traceability map: `docs/traceability.md` and `docs/traceability.json`
- TRACE version: `TRACE_VERSION`

## Acknowledgements

This operational pack is inspired by the essay **“The Minimum Digital Kernel of an Effective State”** (Digital Statecraft / Substack).

- Source essay: https://open.substack.com/pub/digitalstatecraft/p/the-minimum-digital-kernel-of-an

This repository also includes a **meta-governance** layer inspired by the essay **“Meta-governance of AI systems”** (Shru14stack / Substack).

- Source essay: https://open.substack.com/pub/shru14stack/p/meta-governance-of-ai-systems

This repository is **not** affiliated with or endorsed by the author/publisher of the essay. It aims to translate the essay’s concepts into implementable, auditable interface contracts (schemas, templates, and conformance profiles).

## Version

Current release: **v0.4.0** (Minimum Digital Kernel + Meta-Governance Operational Pack)

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

### Meta-governance operational pack
- `schemas/governance-authority-delegation.schema.json`
  Delegation ledger: who has mandate, scope, limits, oversight, and lifecycle.
- `schemas/oversight-review.schema.json`
  Second-order oversight: audit-of-the-auditor independence and peer review record.
- `schemas/governance-trigger.schema.json`
  Trigger model: machine-readable conditions for when governance must adapt.
- `artifacts/governance-risk-register.md`
  Second-order risk register for governance system failure modes.
- `artifacts/governance-transparency-scorecard.md`
  Transparency scorecard to keep governance observable (not just compliant).
- `templates/governance-constitutional-constraints.template.md`
  Constitutional guardrails template: non-derogable constraints and emergency power limits.
- `docs/guides/meta-governance-operationalising.md`
  Practitioner guide for adopting the meta-governance layer.

## How to use

1. Start with the Tier model in `artifacts/dpi-ai-risk-scoring-matrix.md`.
2. Adopt `schemas/decision-receipt.schema.json` as a procurement and implementation requirement for consequential decisions.
3. Use `conformance/mdk-tier-profile.md` to map risk tiers to mandatory kernel primitives.
4. Plug in the templates under `templates/` to standardize audits, registry corrections, and appeals.


## Validation (schemas + examples)

This repository ships with **examples** and **test vectors** that are validated in CI.

Run locally:

```bash
python -m pip install jsonschema
python tools/validate_schemas.py
```

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
