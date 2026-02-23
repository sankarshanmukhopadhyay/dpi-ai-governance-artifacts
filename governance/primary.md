# Governance Primary Document

This repository ships **operational governance artifacts** for DPI + AI systems: schemas, templates, playbooks, and conformance materials designed to be embedded into delivery workflows.

This document defines:
- the purpose and scope of this repository,
- what “normative” means here,
- how controlled documents are organized,
- how versions and changes are managed.

> Compatibility note: this structure borrows governance-document discipline from the Trust Over IP (ToIP) Governance Metamodel, but this repository does **not** claim ToIP Governance Framework compliance.

## 1. Purpose

Enable adopters to procure, implement, test, and audit DPI + AI governance by providing:
- **portable interface contracts** (schemas + templates),
- **assurance surfaces** (evidence bundles, tier profiles, checklists),
- **operational playbooks** for recurring failure modes,
- **traceability** back to methodology.

## 2. Scope

In scope:
- governance artifacts for DPI + AI systems across program design, procurement, implementation, and audit.
- conformance and evidence expectations (including tiering) for repeatable assurance.
- machine-readable schemas and test vectors where practical.

Out of scope (for now):
- jurisdiction-specific legal agreements packaged as ready-to-sign contracts (placeholders may exist under `controlled/legal/`).
- a single, universal risk taxonomy for all sectors and states.
- a full public-facing “governance framework website” implementation.

## 3. Objectives

- Reduce ambiguity in governance requirements by making them **addressable**, **testable**, and **audit-ready**.
- Reduce integration and procurement friction by shipping **stable interfaces** and **evidence bundles**.
- Enable incremental adoption through **tier profiles** and **migration discipline**.

## 4. Principles

Principles guide policies; they are not directly conformance-testable.

- **Operationality over rhetoric**: governance must be implementable as interfaces and workflows.
- **Risk-aligned tiering**: assurance expectations scale with material risk.
- **Separation of concerns**: policy vs rule vs schema vs template are different things—don’t blur them.
- **Traceability**: artifacts should map to evaluative questions and risks.

## 5. Normativity

This repository uses four labels:

- **Normative**: requirements that define conformance expectations.
- **Informative**: explanatory material, examples, and guidance.
- **Machine-testable**: requirements expressed as schemas, rules, or test vectors.
- **Human-auditable**: requirements expressed as policies and procedures.

Normative language rules live in `governance/normative-language.md`.

## 6. Controlled Documents

Controlled documents are the “modular governance surface” of this repository. They are listed in `governance/schedule-of-controlled-docs.md` and organized under `controlled/`.

## 7. Versioning and Compatibility

This repository maintains:
- `VERSION` for repo-wide release versioning.
- `TRACE_VERSION` for traceability model versioning.

Breaking changes include (non-exhaustive):
- schema changes that invalidate previously valid instances,
- changes to tier requirements that raise or lower mandatory evidence,
- renaming/moving normative artifacts without compatibility stubs.

Migration guides live under `docs/migrations/`.

## 8. Revisions

Changes MUST be recorded in `CHANGELOG.md`.

For governance-affecting changes, PRs/commits SHOULD:
- identify impacted controlled documents,
- describe backward-compatibility impact,
- update any relevant migration guides.
