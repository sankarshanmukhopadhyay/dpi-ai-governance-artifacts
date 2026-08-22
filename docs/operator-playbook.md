---
layout: default
title: Operator playbook
nav_order: 2
---

# Operator playbook

Use this workflow when a governance evaluation has identified a missing capability and you need to turn repository assets into an operational control.

## 1. Resolve the capability

Find the `CAP-*` identifier in `remediation/remediation-registry.yaml`.

- `standardized` means this repository has a reusable remediation set.
- `partial` means useful assets exist but material parts of the capability remain uncovered.
- `none` means the evaluation has exposed an artifact-development gap.

## 2. Check implementation requirements

The registry entry states what the deployment must actually establish. Treat templates as scaffolding, not evidence that the requirement has been met.

## 3. Instantiate the assets

Bind the artifact to deployment reality: accountable authority, actors, resources, actions, policy versions, lifecycle, escalation, revocation, redress, and evidence production as applicable.

## 4. Exercise failure paths

A remediation is incomplete if only the happy path works. Test the relevant negative conditions, including exceeded authority, revoked delegation, stale or missing evidence, unavailable redress, and failed evidence integrity.

## 5. Produce closure evidence

The registry lists the evidence the Lab should expect. Preserve provenance and integrity so an independent verifier can reproduce the assurance result.

## 6. Return to TRACE

Send the implementation evidence back through the Lab's gap lifecycle. The Lab can move the gap from implementation or verification pending to closed only when its acceptance criteria pass.

{: .evidence }
A completed template is an input to verification, not proof of closure by itself.
