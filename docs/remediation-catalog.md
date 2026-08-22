---
layout: default
title: Remediation catalog
nav_order: 3
---

# Remediation catalog

The canonical machine-readable source is `remediation/remediation-registry.yaml`. This page presents the operator view.

| Capability | Coverage | What the operator gets |
| --- | --- | --- |
| `CAP-REDRESS-APPEAL` | Standardized | appeal workflow template, schema, redress/remediation guidance, closure evidence contract |
| `CAP-AUTHORITY-BOUNDED-DELEGATION` | Partial | decision-rights and RACI templates; runtime delegation/revocation evidence remains incomplete |
| `CAP-EVIDENCE-CLOSURE` | Standardized | evidence-bundle guidance, audit-trail schema, conformance declaration, verification evidence contract |

## How to read coverage

**Standardized** does not mean universally sufficient or legally authoritative. It means the repository has a reusable remediation package that can be instantiated and tested.

**Partial** identifies a real product backlog. The first real-review TRACE baseline found bounded authority/delegation gaps in all three rebaselined publications, making this the highest-priority capability to strengthen.

## Closure

A remediation mapping is successful only when deployment-specific evidence satisfies the originating gap's acceptance criteria and the result survives TRACE re-evaluation.
