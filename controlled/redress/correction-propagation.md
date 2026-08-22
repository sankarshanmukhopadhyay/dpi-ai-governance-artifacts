---
layout: default
title: Correction propagation
parent: Remediation catalog
nav_order: 5
---

# Correction propagation

A successful correction is not complete when a source registry accepts a change. If downstream decisions or effects relied on the superseded fact or decision, the correction must propagate through the dependency chain and produce evidence of what changed and what remains unresolved.

## Lifecycle

```mermaid
flowchart LR
    A[Accepted source correction] --> B[Correction order]
    B --> C[Discover dependent targets]
    C --> D[Invalidate / recompute / replace / compensate]
    D --> E{All required targets complete?}
    E -->|Yes| F[Execution receipt: complete]
    E -->|No| G[Execution receipt: partial]
    G --> H[Retry / escalation / compensating action]
```

The existing registry correction request/response schemas remain the source-correction interface. This capability begins after a correction is authorized and turns it into downstream execution.

## Evidence chain

```mermaid
sequenceDiagram
    participant A as Correction authority
    participant R as Source registry
    participant O as Correction orchestrator
    participant D as Dependent decision service
    participant E as Effect service

    A->>O: issue correction order
    O->>R: resolve corrected source
    O->>D: invalidate/recompute dependent decision
    D-->>O: new decision + supersedes reference
    O->>E: compensate/replace affected effect
    E-->>O: target acknowledgement
    O-->>A: correction execution receipt
```

## Completion rule

An execution receipt must not claim `complete` while a mandatory target is failed, pending or omitted. Partial execution is evidence, not success; unresolved targets must remain visible and route to retry, escalation or compensating action.

## Provenance

This capability was evidence-derived from corpus `digital-statecraft-dpi-2026-wave1`, reviews DS-TRACE-002, DS-TRACE-005 and DS-TRACE-006, recurring gap class `non_executable_correction_propagation`.

## Authority

The artifacts represent an authorized correction and its execution. They do not decide whether the underlying correction is legally warranted. That authority remains with the adopting registry, appellate, judicial or other competent institution.
