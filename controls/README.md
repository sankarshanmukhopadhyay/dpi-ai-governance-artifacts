# Control Library

This repository includes a lightweight **control library** with stable **control IDs** to make governance requirements:

- **traceable** (controls ↔ artifacts ↔ evidence)
- **machine-operable** (registry in YAML/JSON)
- **crosswalkable** to external frameworks (NIST AI RMF, OECD AI Principles, ISO/IEC 42001) where applicable

## Control IDs

**Format:** `DPI-AI-CTRL-XXX` (zero-padded)

Controls are grouped into the following categories:

- Governance
- Risk
- Assurance
- Redress
- Transparency

## Registry files

- `controls/registry.yaml`
- `controls/registry.json`

These registries are intended to be consumed by tools and pipelines (e.g., validation, evidence checklists, conformance tooling).

## Crosswalks

The registry includes **indicative** mapping fields:

- NIST AI RMF (function-level: GOV / MAP / MEASURE / MANAGE)
- OECD AI Principles (principle name-level)
- ISO/IEC 42001 (topic-level)

> These mappings are starting points for alignment work. They are **not** authoritative compliance determinations.

## How packs use controls

Operational Packs SHOULD list:

- which control IDs they operationalize
- the artifact(s) that satisfy evidence expectations
- tier-conditional requirements (where relevant)


## Categories

The control registry categorizes controls into: Governance, Risk, Assurance, Redress, Transparency, and Identity Assurance.
