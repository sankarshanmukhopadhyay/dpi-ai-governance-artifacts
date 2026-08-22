# Remediation Resolution for TRACE Governance Gaps

## Purpose

This repository is the operational remediation side of the TRACE improvement loop.

A TRACE governance gap should not terminate in a narrative recommendation. It should resolve, where possible, to reusable artifacts that tell an implementer:

- what capability is required;
- what controls are relevant;
- what must be instantiated or changed;
- which schemas or templates apply;
- what tests or evidence are expected; and
- what an assessor will need to verify closure.

## Canonical registry

`remediation/remediation-registry.yaml` is the machine-readable capability-to-artifact resolver.

Each registry entry contains:

- `capability_id` — the normalized capability expected from the Lab gap contract;
- `gap_classes` — recurring deficiency classes addressed by the capability;
- `coverage` — `partial` or `standardized`;
- `controls` — relevant TRACE control identifiers;
- `implementation_requirements` — operator-facing requirements;
- `artifacts` — repository paths to templates, schemas, guidance, test vectors, or evidence definitions; and
- `closure_evidence` — evidence expected when the operator claims the gap has been addressed.

## Coverage semantics

### Partial

The repository contains useful remediation assets, but an implementer still requires additional design or governance work before the capability can be considered standardized.

### Standardized

The repository contains a coherent reusable remediation path with at least one concrete artifact and declared closure evidence.

`standardized` is a repository maturity statement. It is not a legal compliance, certification, or deployment approval claim.

## Authority boundary

The remediation registry is explicitly non-normative by default.

It recommends reusable implementation assets derived from TRACE evaluation experience. Deployment owners, competent authorities, procurement authorities, legal authorities, and other accountable institutions retain their own decision authority.

A consumer may choose to incorporate an artifact normatively through its own governance process. That external adoption does not cause this repository to acquire the adopter's authority.

## Operator workflow

```text
TRACE gap
  -> required capability
  -> remediation registry lookup
  -> selected artifacts
  -> local instantiation
  -> implementation tests
  -> closure evidence
  -> TRACE re-evaluation
```

For example, a `CAP-REDRESS-APPEAL` gap resolves to the redress workflow template, redress workflow schema, and controlled redress guidance. An operator is still responsible for naming the real accountable authority, configuring timelines, integrating the workflow, and producing evidence that the deployed process works.

## Validation

Run:

```bash
python tools/validate_remediation_registry.py
```

The validator fails when:

- capability identifiers are invalid or duplicated;
- standardized coverage has no artifact;
- implementation requirements or closure evidence are missing; or
- a referenced repository artifact does not exist.

This makes dead remediation mappings a CI failure rather than documentation debt.

## Development rule

New artifacts should preferentially be introduced in response to one of the following:

1. a recurring gap observed across independent TRACE evaluations;
2. a material gap with no existing remediation coverage;
3. operator feedback showing that an existing remediation path is insufficient; or
4. closure testing showing that an artifact cannot produce adequate evidence.

This keeps the repository evidence-derived while preserving room for forward-looking reference architectures and research artifacts where their purpose is clearly labelled.
