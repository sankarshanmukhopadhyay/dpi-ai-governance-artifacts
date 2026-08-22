---
layout: default
title: Start here
nav_order: 1
---

# Start here

This repository supplies reusable governance-remediation assets that teams can **instantiate, enforce, test and evidence** in real DPI/AI systems.

You do not need to know a `CAP-*` identifier before you begin.

## Choose your task

| I need to… | Start here |
| --- | --- |
| Build a consequential service, agent, evidence-reliance flow, model-assisted decision, or redress path | [Implementation recipes](implementation-recipes.md) |
| Close a known governance gap from TRACE | Remediation registry + [Operator playbook](operator-playbook.md) |
| Understand what reusable capability packages exist | [Remediation catalog](remediation-catalog.md) |
| Prepare an implementation for TRACE verification | [Implementation recipes — Prepare for TRACE verification](implementation-recipes.md#recipe-6--prepare-for-trace-verification) |
| Understand historical vs current remediation maturity | [Evidence-derived coverage baseline](../remediation/baselines/2026-08-22-coverage.md) |

## If you are building something

Start with [Implementation recipes](implementation-recipes.md). Choose by the thing you intend to build rather than by repository taxonomy.

The recipes cover:

- consequential eligibility/entitlement/approval services;
- delegated agents and automated actors;
- cross-institution evidence reliance;
- model-assisted consequential decisions;
- appeal, correction and remedy;
- evidence packaging for TRACE verification.

Each recipe identifies the exact schemas/guidance/test vectors to instantiate, the required authority inputs, negative tests and closure evidence.

## If you already have a TRACE governance gap

1. Read the gap's `required_capability.id`.
2. Resolve that capability in `remediation/remediation-registry.yaml`.
3. Check whether coverage is `standardized`, `partial`, or absent from the registry.
4. Instantiate the listed artifacts against the deployment or fixture.
5. Exercise positive and negative paths.
6. Produce the listed closure evidence.
7. Return the evidence to the Lab for verification and re-evaluation.

## What this repository does not do

This repository can encode and test an adopted governance rule. It cannot create the authority behind that rule.

{: .warning }
Artifacts do not acquire the legal, institutional, programme, procurement, jurisdictional or deployment authority of an adopting organization. A schema-valid object is not proof that the underlying decision is lawful, legitimate or approved.
