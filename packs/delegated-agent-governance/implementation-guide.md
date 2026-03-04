# Delegated Agent Governance — Implementation Guide

This pack focuses on **delegated agents** acting on behalf of principals (people, org units, or state entities).

## What you implement
- Delegation model and authorization boundaries
- Action logging and decision receipts for agent actions
- Override and kill-switch runbooks (tested)
- Tier-conditional approvals for high-impact actions

## Practical rollout
1. Define agent scopes per function (read, propose, execute).
2. Bind every agent action to an accountable principal.
3. Require approvals for high-impact actions; log approvals.
4. Test overrides and record drill outcomes.


## Agent registry and capability manifests

To close the “agents running wild” gap, implement these *minimum* machine-readable artifacts:

- Agent Registry Entry: `schemas/agent/agent-registry-entry.schema.json`
- Agent Capability Manifest: `schemas/agent/agent-capability-manifest.schema.json`
- Delegation Chain Entry: `schemas/agent/delegation-chain-entry.schema.json`
- Agent Policy Constraints: `schemas/agent/agent-policy-constraints.schema.json`

These records SHOULD be signed and versioned. They MUST support revocation and expiry.
