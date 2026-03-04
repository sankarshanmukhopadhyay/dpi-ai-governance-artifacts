# Delegated Agent Governance — Implementation Notes

This note provides practical guidance for governing agentic systems using artifacts already present in this repository.

## 1) Delegation is a contract, not a vibe

Use `schemas/governance-authority-delegation.schema.json` and the agent schemas under `schemas/agent/` (registry, capability manifest, delegation chain, policy constraints) to represent:
- Delegator (authority)
- Delegatee (agent/operator/system)
- Scope and constraints (what actions are allowed, bounded contexts)
- Expiry/revocation conditions
- Oversight and escalation points

## 2) Agent actions must be reconstructable

For any action that can materially impact rights, benefits, access, or outcomes:

- Emit a **Decision Receipt** (or a decision receipt-equivalent)
  - Reference: `schemas/decision-receipt.schema.json`
- Maintain a minimal action log entry
  - Reference: `schemas/tier0-log-entry.schema.json`

## 3) Override and kill-switch are governance controls

Operationally define:
- Who can override the agent
- Under what conditions (triggered by incidents, drift, complaints)
- How override decisions are recorded (decision receipts + oversight review)

## 4) Trigger-driven governance (don’t wait for a scandal)

Declare governance triggers for:
- Repeated user complaints
- Suspicious action patterns
- Model drift signals
- Security compromise indicators

Reference: `schemas/governance-trigger.schema.json` (and optionally `schemas/recompute-trigger.schema.json`)

## 5) Oversight is a recurring operational activity

Run oversight reviews periodically and record findings.
Reference: `schemas/oversight-review.schema.json`


## 5) Agent-specific risk levers (what changed post-2023)

Agentic systems break pre-2023 assumptions because they can:
- Use tools autonomously (write operations, external side-effects)
- Spawn sub-agents / orchestrate multiple agents
- Preserve state across sessions (memory)
- Create feedback loops across systems
- Resist shutdown (intentionally or emergently)

Treat these as *structural properties* that must be governed with explicit controls:
- **Registration**: every operational agent MUST have an entry in an Agent Registry.
- **Mandate**: every agent MUST operate under an explicit mandate with scope, constraints, and expiry.
- **Containment**: agents with tool access SHOULD run in constrained environments with stop-rights and rapid shutdown.
- **Monitoring**: agent behavior MUST be continuously observable post-deployment (not just pre-release evaluation).
- **Delegation provenance**: delegation chains MUST be reconstructable end-to-end.
