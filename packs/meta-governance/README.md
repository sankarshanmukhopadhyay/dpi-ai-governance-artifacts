# Meta-Governance — Implementation Pack

This pack operationalizes **meta-governance**: governance about governance.
It makes authority, delegation, triggers, and oversight **explicit, versioned, and reviewable**.

## Scope

In-scope:
- Governance authority delegation (who can do what, with what constraints)
- Governance triggers (what events force review, recomputation, rollback)
- Oversight reviews (how governance decisions get audited)
- Rulebook change-control (how rules evolve without chaos)

## Adoption path

1. **Define delegation boundaries**
   - Capture authority delegation as a contract.
2. **Instrument triggers**
   - Declare trigger conditions that force review and recomputation.
3. **Operationalize oversight**
   - Run periodic oversight reviews and record outcomes.
4. **Change-control the rulebook**
   - Treat governance changes like controlled releases.

## Primary outputs

- Governance Authority Delegation record(s)
- Governance Trigger definitions
- Oversight Review records
- Rulebook change-control record(s)

## Key references

- Guide: `docs/guides/meta-governance-operationalising.md`

## Included artifacts

See [`manifest.yaml`](./manifest.yaml) for the exact inventory.
