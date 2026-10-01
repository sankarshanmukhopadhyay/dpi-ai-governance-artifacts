---
layout: default
title: Capability conformance
nav_order: 7
---

# Capability conformance

The remediation registry answers **what reusable assets exist for a capability**. A capability conformance profile answers a different question: **what must an implementation demonstrate before a technical conformance claim can be made for that capability**.

The contract is intentionally small:

```text
CAP-* capability
  -> versioned conformance profile
  -> mandatory requirements
  -> required evidence
  -> negative cases
  -> implementation assessment
```

A profile is a reusable technical assurance contract. It does not create legal admissibility, deployment approval, institutional authority, certification, or permission to act.

## Initial profiles

This tranche publishes profiles only for:

- `CAP-AUTHORITY-BOUNDED-DELEGATION`
- `CAP-CORRECTION-PROPAGATION`

They were selected because both are already standardized and have strong failure-path semantics. Additional profiles should be added only when implementation evidence demonstrates reuse value.

## Evidence rule

Missing required evidence is missing evidence. A consumer must not infer PASS from absence of a known failure. Positive conformance requires the mandatory propositions to be affirmatively established.

## Continuing reliance after change

A successful assessment establishes conformance for a particular implementation, profile baseline, evidence set, and evaluation time. It does not remain implicitly current forever.

Each published profile can therefore declare `continuity.rules`. A rule maps an observed change class to one of three technical effects:

- `preserves`: the declared change does not, by itself, require a new assessment;
- `reassessment_required`: the previous result remains historical evidence, but present reliance requires a fresh assessment;
- `invalidates`: the change contradicts or revokes a basis on which present reliance depended.

The Artifacts repository declares the reusable effect of a **classified** change. It does not observe production systems and does not decide whether such a change actually occurred. Change observation and evidence belong to the evaluating or operating environment.

The current bounded-delegation, correction-propagation, and evidence-closure profiles include continuity triggers for authority/revocation, scope or policy change, implementation change, contradictory evidence, and conformance-contract change where applicable.

## Machine-verifiable surfaces

- `schemas/conformance/capability-conformance.schema.json`
- `conformance/profiles/`
- `tools/validate_capability_conformance.py`

The validator checks schema validity, unique requirement identifiers, registry/profile consistency, and a deliberately invalid falsification fixture.

## Authority boundary

The repository owns these reusable technical contracts. Adopting organizations retain legal, institutional, policy, deployment, delegation, revocation, correction, and approval authority.
