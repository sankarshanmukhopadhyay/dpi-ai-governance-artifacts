---
layout: default
title: Operator playbook
nav_order: 2
---

# Operator playbook

Use this workflow when a governance evaluation has identified a missing capability and you need to turn repository assets into an operational control.

If you are starting from **what you intend to build** rather than from a known `CAP-*`, use [Implementation recipes](implementation-recipes.md) first.

## 1. Resolve the capability

Find the `CAP-*` identifier in `remediation/remediation-registry.yaml`.

- `standardized` means this repository has a reusable remediation set with test/evidence expectations.
- `partial` means useful assets exist but material parts of the capability remain uncovered.
- a capability absent from the registry remains an artifact-development gap rather than implied coverage.

## 2. Check implementation requirements

The registry entry states what the deployment must actually establish. Treat templates as scaffolding, not evidence that the requirement has been met.

For a system-level composition, use the [build-intent recipes](implementation-recipes.md) to identify adjacent capabilities that become necessary because of your architecture—for example admissibility when relying on another institution's evidence, or inference traceability when a model contributes to a consequential decision.

## 3. Name the authority and enforcement point

Before filling a schema, identify:

- the accountable authority;
- any delegate or automated actor;
- the action/resource/purpose being governed;
- the runtime point at which the rule is enforced;
- the revocation or invalidation source;
- the downstream effect that must correlate to the decision.

A control that exists only as a static document but cannot affect runtime behavior is not operational remediation.

## 4. Instantiate the assets

Bind the artifact to deployment reality: authorities, actors, resources, actions, evidence types, policy versions, lifecycle, escalation, revocation, redress, correction and evidence production as applicable.

## 5. Exercise failure paths

A remediation is incomplete if only the happy path works. Select negative vectors appropriate to the capability, including:

- exceeded authority;
- revoked or expired delegation;
- authentic but inadmissible evidence;
- stale facts or policy versions;
- inference version/threshold mismatch;
- unavailable redress;
- partial correction propagation;
- missing effect/authorization correlation;
- failed evidence integrity.

Record expected behavior **and** the evidence showing that enforcement occurred.

## 6. Produce closure evidence

The remediation registry lists the evidence the Lab should expect. Preserve provenance and integrity so an independent verifier can reproduce the assurance result.

A minimum closure package normally includes:

- system/profile version;
- authority and delegation records;
- versioned policy/rule references;
- runtime decision records;
- capability-specific evidence;
- positive/negative test results;
- evidence manifest/hashes;
- residual limitations and unresolved risks.

## 7. Check readiness for TRACE verification

Before returning evidence to the Lab, confirm that:

- all required capability artifacts are instantiated;
- runtime enforcement points are identified;
- expected negative paths actually fail or escalate as designed;
- effects can be correlated to governing decisions;
- redress/correction evidence exists where applicable;
- evidence is inspectable without relying on undocumented operator knowledge.

See [Implementation recipes — Prepare for TRACE verification](implementation-recipes.md#recipe-6--prepare-for-trace-verification).

## 8. Return to TRACE

Send the implementation evidence back through the Lab's gap lifecycle. The Lab can move the gap from implementation or verification pending to closed only when its acceptance criteria pass.

{: .evidence }
A completed template or schema-valid record is an input to verification, not proof of closure by itself.
