# Delegated Agent Governance — Implementation Notes

This note provides practical guidance for governing agentic systems using artifacts already present in this repository.

## 1) Delegation is a contract, not a vibe

Use `schemas/governance-authority-delegation.schema.json` to represent:
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
