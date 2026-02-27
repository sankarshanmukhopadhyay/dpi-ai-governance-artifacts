# Escalation, Override, and Kill-Switch Runbook (Template)

This is a starter runbook for production systems where agents can act on behalf of an authority.

## 1) Activation conditions (examples)

- Credible incident report affecting multiple users
- Evidence of unauthorized delegation or privilege escalation
- Repeated high-severity complaints tied to a single workflow
- Model drift that materially changes outcomes for protected groups
- Security compromise / data integrity failure

## 2) Roles and decision rights

- Incident commander:
- Override authority:
- Communications owner:
- Audit evidence owner:

## 3) Actions

### A) Pause / rate-limit agent actions
- Mechanism:
- Scope:
- Expected impact:

### B) Switch to human-in-the-loop
- Workflow:
- SLA:
- Evidence produced:

### C) Full kill-switch (disable)
- Preconditions:
- Approval path:
- Audit log requirements:

## 4) Evidence outputs (minimum)

- Incident record (`schemas/incident.schema.json`)
- Decision receipts for overrides (`schemas/decision-receipt.schema.json`)
- Notification delivery logs (`schemas/notification-delivery.schema.json`)
- Oversight review (`schemas/oversight-review.schema.json`)
