# Security Compromise Playbook

This playbook covers suspected or confirmed **unauthorized access**, credential leakage, malicious modification of models/artifacts, or data exfiltration.

## Trigger conditions

- Access logs show anomalous activity (impossible travel, unusual volume, privilege escalation).
- Integrity checks fail (hash mismatch for artifacts, model, or release bundles).
- Secrets exposed (repo, CI logs, container image, runtime environment).
- Confirmed breach reported by internal team or external party.

## Roles

- **Security On-call / Incident Commander**: leads response, triage, and escalation.
- **Platform / Ops**: rotates keys, isolates hosts, restores services.
- **Repo Maintainers**: audit recent changes; revoke compromised credentials.
- **Legal / Compliance**: determines reporting obligations.
- **Communications Lead**: manages external comms.

## Severity and SLAs

- **SEV1**: contain within **30 minutes**, notify leadership within **1 hour**
- **SEV2**: contain within **4 hours**, notify within **1 business day**

## Immediate containment

1. **Isolate** affected systems (disable tokens, revoke sessions, quarantine runners).
2. **Rotate credentials**:
   - API keys, CI secrets, signing keys, service accounts
3. **Preserve evidence** (do not destroy logs):
   - access logs, CI logs, audit trails, recent deploy manifests
4. **Create an incident record**:
   - Template: `templates/incident.example.json`
   - Include suspected entry point and scope hypothesis

## Integrity verification

- Verify signed releases / artifact hashes.
- Review:
  - recent commits, release tags, and CI workflow changes
  - dependency lockfiles and build scripts

## Remediation

- Patch the vulnerability or misconfiguration.
- Rebuild and re-sign release bundles.
- If artifacts were modified, trigger a controlled re-validation pass:
  - `python tools/validate_schemas.py`

## Notification and disclosure

- Follow applicable legal / regulatory timelines.
- Publish a transparency note when required, including:
  - what was affected, what was not
  - mitigations taken
  - steps for downstream adopters (invalidate caches, rotate keys)

## Post-incident review

- Update threat model and controls mapping.
- Add regression tests for the compromise vector (where practical).
- Review and tighten:
  - least privilege
  - branch protections
  - CI hardening
