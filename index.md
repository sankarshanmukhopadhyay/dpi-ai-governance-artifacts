---
layout: default
title: DPI–AI Governance Artifacts
nav_order: 0
---

# DPI–AI Governance Artifacts

**Resolve a governance gap into something an operator can implement, test, and evidence.**

This repository is the remediation side of the TRACE improvement loop. It supplies reusable controls, schemas, templates, playbooks, test materials, and evidence contracts for DPI/AI governance weaknesses identified through structured evaluation.

{: .note }
The companion **DPI AI Governance Lab** owns evaluation, governance-gap normalization, and re-evaluation. This repository owns reusable remediation mappings and artifacts.

## Choose your path

### I have a governance gap

Start with [Start here](docs/start-here.md), resolve its `CAP-*` identifier in the remediation registry, and check whether the capability has standardized, partial, or no coverage.

### I need to implement the remediation

Use the [Operator playbook](docs/operator-playbook.md). Instantiate the mapped assets against your actual authorities, actors, lifecycle, controls, failure paths, and evidence production.

### I need to know what remediation exists

Use the [Remediation catalog](docs/remediation-catalog.md). It presents the machine-readable `remediation/remediation-registry.yaml` as an operator-oriented capability catalog.

### I want to know what we should build next

Use the [first remediation coverage baseline](remediation/baselines/2026-08-22-coverage.md) and `remediation/coverage-priorities.yaml`. The first real-review TRACE baseline makes bounded authority/delegation the highest-priority coverage gap because it recurs in 3/3 reviews and remains partial.

## Current evidence-derived signal

| Capability | Recurrence | Coverage | Next action |
| --- | ---: | --- | --- |
| Bounded authority and delegation | 3/3 | Partial | strengthen delegation, revocation, runtime authorization and negative-test artifacts |
| Operational appeal and remedy | 3/3 | Standardized | instantiate and test in a realistic deployment |
| Evidence-backed governance closure | 3/3 | Standardized | instantiate and verify an evidence bundle |

This is the distinction the programme now optimizes for: **artifact availability is not closure**. A deployment still has to instantiate, test, evidence, and survive re-evaluation.

## Broader operational packs

| Pack | Purpose |
| --- | --- |
| [Minimum Digital Kernel](packs/minimum-digital-kernel/README.md) | Decision receipts, authority directories, rulebook discipline |
| [Delegated Agent Governance](packs/delegated-agent-governance/README.md) | Agent registry, mandates, capability manifests, containment |
| [Meta-Governance](packs/meta-governance/README.md) | Oversight review, change control, triggers |
| [AI Redress & Accountability](packs/ai-redress-accountability/README.md) | Appeals, audit findings, remediation plans |
| [Public Sector AI Procurement](packs/public-sector-procurement/README.md) | Evaluation scorecards, supplier attestations, red flags |

## Reference surfaces

- [Control library](controls/README.md)
- [Governance spine](governance/primary.md)
- [Evidence bundles](controlled/assurance/evidence-bundles.md)
- [Standards crosswalk](crosswalks/README.md)
- [Documentation architecture](docs/information-architecture.md)

{: .warning }
Repository artifacts do not inherit the authority of an adopting organization. Legal, institutional, programme, procurement, and deployment authority remains external to this repository.
