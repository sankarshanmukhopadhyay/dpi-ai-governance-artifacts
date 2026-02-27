# Evidence Request Template — DPI+AI Governance (Procurement Annex)

Use this annex in an RFP/RFQ to request **specific, auditable governance artifacts**.

## Instructions to bidders

Provide:
1. The requested artifact (or a URL to it)
2. The artifact version/date
3. Ownership (who maintains it)
4. A short note explaining how it is used operationally

## Evidence Requests (baseline)

### A) Accountability & Decisioning
- Decision Receipt sample(s) and emission logic overview  
  Reference: `schemas/decision-receipt.schema.json`, examples in `templates/decision-receipt.*.json`
- Reason codes vocabulary (if applicable)  
  Reference: `schemas/reason-codes.vocab.json`

### B) Authority & Delegation
- Authority directory entry / directory excerpt  
  Reference: `schemas/authority-directory-entry.schema.json`
- Governance authority delegation record(s)  
  Reference: `schemas/governance-authority-delegation.schema.json`

### C) Governance Controls & Change Management
- Rulebook manifest + change-control procedure  
  Reference: `schemas/rulebook-manifest.schema.json`, `templates/rulebook-change-control.template.md`
- Governance triggers and recompute triggers (if used)  
  Reference: `schemas/governance-trigger.schema.json`, `schemas/recompute-trigger.schema.json`

### D) Redress, Remediation, and Incident Handling
- Redress workflow description and SLA measurement approach  
  Reference: `controlled/redress/redress-and-remediation.md`, `templates/correction-sla-metrics.md`
- Appeal filing and decision processes (with samples)  
  Reference: `schemas/appeal-filing.schema.json`, `schemas/appeal-decision.schema.json`
- Incident reporting and audit finding handling (with samples)  
  Reference: `schemas/incident.schema.json`, `schemas/audit-finding.schema.json`

### E) Supply Chain & Vendor Capability
- Vendor capability attestation payload  
  Reference: `schemas/vendor-capability-attestation.schema.json`
- Supply-chain control declarations and dependency inventory approach  
  Reference: `schemas/supply-chain-control.schema.json`

## Optional: Validation

Where possible, bidders SHOULD validate JSON artifacts against the referenced schemas and provide validation output.
