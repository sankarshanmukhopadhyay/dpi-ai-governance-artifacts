---
layout: default
title: Start here
nav_order: 1
---

# Start here

This repository supplies reusable remediation assets for governance gaps identified by TRACE or an equivalent evidence-backed evaluation.

## Choose your task

### I have a TRACE governance gap

1. Read the gap's `required_capability.id`.
2. Resolve that capability in `remediation/remediation-registry.yaml`.
3. Check whether coverage is `standardized`, `partial`, or `none`.
4. Instantiate the listed artifacts against the real deployment.
5. Produce the listed closure evidence.
6. Return the evidence to the Lab for verification and re-evaluation.

### I am implementing or operating a system

Use the [Operator playbook](operator-playbook.md). It explains how to move from a reusable artifact to a deployment-specific control with testable evidence.

### I want to see remediation maturity

Use the [Remediation catalog](remediation-catalog.md) and the [first evidence-derived coverage baseline](../remediation/baselines/2026-08-22-coverage.md).

### I maintain this repository

Use the evidence-derived backlog. Repeated `partial` or `none` coverage in real evaluations should normally outrank speculative catalogue expansion.

{: .warning }
Artifacts are reusable implementation aids. They do not acquire the legal, institutional, programme, procurement, or deployment authority of an adopting organization.
