# Model Drift Playbook

This playbook operationalizes repeatable response to **post-deployment performance drift** (accuracy, bias, latency, stability) for an AI system that impacts DPI workflows.

## Trigger conditions

One or more of:

- Monitoring detects statistically significant degradation against agreed KPIs (e.g., quality, latency, error rate).
- Drift indicators cross threshold (data drift, concept drift, label drift) for N consecutive windows.
- Material stakeholder complaints correlate with a specific model/version.
- Audit sampling shows increasing non-conformance to policy constraints.

## Roles

- **On-call Operator**: first responder; executes containment, captures evidence.
- **Model Owner**: approves rollback / retrain decisions; accountable for remediation plan.
- **Risk & Compliance Lead**: confirms regulatory / policy obligations; oversees documentation.
- **Communications Lead**: handles external comms when required.
- **Oversight / Governance Body**: escalation point for high-impact systems.

## Severity and SLAs

- **SEV1 (High-impact / safety / rights risk)**: contain within **1 hour**, notify oversight within **4 hours**.
- **SEV2 (Material degradation, limited blast radius)**: contain within **4 hours**, notify oversight within **1 business day**.
- **SEV3 (Minor degradation)**: track within **5 business days**, remediate in next release window.

## Containment checklist

1. **Freeze** deployment pipeline for the affected model (no further rollout).
2. **Identify blast radius**:
   - model version(s), tenant(s), decision stream(s), time window(s)
3. **Choose a containment action** (prefer reversible):
   - rollback to last known-good version
   - switch to safe-mode rules / human review gating
   - disable affected features / endpoints
4. **Record an incident** using the incident schema:
   - Template: `templates/incident.example.json`
   - Schema: `schemas/incident.schema.json` (if present in this repo)

## Diagnosis and evidence

- Capture:
  - monitoring charts / metric snapshots
  - sampled inputs/outputs (redacted)
  - model + data version identifiers
  - policy constraints that were violated (if any)
- Run validation:
  - rerun test vectors (including `/invalid/` conventions where applicable)
  - re-score recent sample set and compare against baseline

## Remediation options

Choose one (or combine) with explicit acceptance criteria:

- **Rollback + harden**: ship a patch that prevents recurrence (guardrails, thresholds, feature flags).
- **Recompute + backfill**: if incorrect decisions were produced, trigger recomputation:
  - Template: `templates/recompute-trigger.example.json`
- **Retrain + re-validate**: perform retrain with updated data, then:
  - run conformance suite
  - regenerate evidence bundle and update control mappings

## Communications

- Internal notification (SEV1/SEV2) MUST include:
  - affected scope, containment action, next update time, owner
- External notification (only when required) SHOULD include:
  - what happened (plain language), what users should do, timelines, contact

## Post-incident review

Within **5 business days** for SEV1/SEV2:

- Root cause analysis (RCA)
- Control gaps and corrective actions
- Update:
  - monitoring thresholds
  - test vectors
  - documentation / playbook improvements
