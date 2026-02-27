# Meta-Governance — Implementation Guide

This pack operationalizes **governance of governance**: putting the rules, delegations, and oversight mechanisms under explicit change control.

## What you implement

1. **Authority delegation** records (who can delegate what, to whom, and under which constraints)
2. **Governance triggers** (events that require governance action)
3. **Oversight reviews** (periodic and trigger-driven)
4. **Rulebook change control** (shared with MDK)

## Practical rollout

- Start with a trigger registry for: incidents, policy changes, model updates, vendor changes.
- Define oversight review cadence and minimum evidence required.
- Use delegation artifacts to bind responsibility when authority is delegated.
