# Delegated Agent Governance — Artifact Checklist

## Required (MUST)
- Agent authorization boundaries
- Action logs / receipts for governed actions
- Override/kill-switch runbook + tests
- Approval logs for high-impact agent actions

## Optional (MAY)
- Public transparency extracts (aggregated)
- Agent performance evaluation reports


### Agentic additions (post-2023)

- [ ] Agent registry entry created (`schemas/agent/agent-registry-entry.schema.json`)
- [ ] Capability manifest created (`schemas/agent/agent-capability-manifest.schema.json`)
- [ ] Policy constraints issued (`schemas/agent/agent-policy-constraints.schema.json`)
- [ ] Delegation chain recording enabled (`schemas/agent/delegation-chain-entry.schema.json`)
- [ ] Stop-rights and shutdown path tested (see `override-kill-switch.runbook.template.md`)
