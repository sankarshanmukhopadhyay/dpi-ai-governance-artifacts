# Widespread Misclassification Playbook

This playbook applies when the system produces **systemic incorrect decisions** (not isolated errors), especially for high-impact decision streams.

## Trigger conditions

- Spike in appeals, reversals, or complaint volume beyond threshold.
- Audit sampling finds consistent misclassification across a cohort (region, demographic, program).
- A policy update or model update correlates with incorrect outcomes.
- External watchdog / regulator flags systematic error.

## Roles

- **Decision Stream Owner**: accountable for service correctness.
- **On-call Operator**: containment + evidence capture.
- **Risk & Redress Lead**: ensures remediation and user redress workflows execute.
- **Oversight Body**: approves resumption for SEV1/high-impact.

## Severity and SLAs

- **SEV1 (High-impact rights risk)**: suspend within **1 hour**, notify oversight within **4 hours**
- **SEV2**: suspend within **8 hours**, notify within **1 business day**

## Containment

1. **Suspend the affected decision stream** or gate behind human review.
2. **Enable safe-mode** (rules-based baseline / conservative policy).
3. **Create an incident record**:
   - Template: `templates/incident.example.json`

## Diagnosis

- Identify:
  - affected cohort, decision types, time window, root cause hypothesis
- Validate:
  - run relevant test vectors
  - compare outputs to policy expectations / ground truth sample set

## Remediation and backfill

- If incorrect decisions were issued, create a recompute/backfill plan:
  - Template: `templates/recompute-trigger.example.json`
- Execute **redress**:
  - notify impacted users where required
  - provide appeal / correction pathway
  - track SLA metrics (see `templates/correction-sla-metrics.md`)

## Communications

- Provide clear service status updates:
  - what is paused, alternative path, expected next update
- For external comms, avoid technical jargon; focus on impacts and actions.

## Resumption criteria

Before resuming automated decisions:

- Validation passes for the corrected model/policy
- Monitoring thresholds updated
- Oversight sign-off recorded for SEV1

## Post-incident review

- Control improvements and new test vectors added.
- Pack documentation updated to reflect new guardrails.
