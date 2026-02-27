# Delegated Agent Governance — Operational Pack

This pack focuses on **delegated action**: when an agent (human or machine) performs actions on behalf of an authority.

The core objective: make delegation boundaries, accountability handoffs, and override semantics **auditable and enforceable**.

## Scope

In-scope:
- Delegation contracts and constraints
- Agent action logging expectations (evidence of action + rationale)
- Escalation, override, and kill-switch patterns (governance-grade operational controls)
- Governance triggers for agent behaviour and drift

Out-of-scope:
- Model-specific safety research (this pack is about operational governance interfaces)

## Adoption path

1. **Define delegation boundaries**
2. **Declare action logging and decision receipt requirements**
3. **Implement escalation and override paths**
4. **Wire governance triggers for agent behaviour**
5. **Run oversight reviews and retain evidence**

## Primary outputs

- Delegation register (delegation contracts + constraints)
- Agent action logging spec + sample logs
- Decision receipt emission policy for agentic actions
- Escalation/override/kill-switch runbook

## Included artifacts

See [`manifest.yaml`](./manifest.yaml) for the exact inventory.
