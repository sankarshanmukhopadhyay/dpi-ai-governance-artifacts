# Public repository baseline

This record captures controls reviewed under issue #17. It is repository assurance evidence, not external certification or regulatory approval.

| Control | State | Evidence | Residual risk |
|---|---|---|---|
| Purpose, maturity and artifact role | PASS | `README.md`, `PROJECT-STATUS.yaml`, `index.md`, remediation/catalog documentation | Artifact availability does not itself prove deployment governance closure. |
| Licensing / provenance | PASS | `LICENSE.md`, `CITATION.cff`, `VERSION`, `TRACE_VERSION`, `CHANGELOG.md` | Publication remains maintainer judgment. |
| Security reporting and evidence invalidation | PASS | `SECURITY.md` | Hosted private-reporting enablement remains platform evidence. |
| Contribution / community / support | PASS | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SUPPORT.md`, PR template | None identified. |
| Dependency update management | PASS | `.github/dependabot.yml` | Hosted Dependabot enablement remains platform evidence. |
| Default-branch protection | PARTIAL | active `protect-main` observed 2026-09-05: PRs, resolved conversations, linear history, deletion/non-fast-forward protection, no bypass actors | No required validation status check is present; tracked separately. |
| Validation / trace evidence | PASS / bounded | existing workflows, schemas, trace compatibility and remediation validation surfaces | Workflow green is evidence of repository consistency, not external assurance. |
| Release/version provenance | PASS | version/trace-version, changelog, citation and release surfaces | Downstream consumers must bind to explicit artifact versions. |
| Authority boundary | PASS | README, references, remediation catalog | Repository owns reusable governance artifacts and traces; regulatory, institutional, specification and deployment authorities remain external. |
| Experimental / historical distinction | PASS | baseline/remediation/versioned evidence structure | Historical mappings must not be mistaken for current closure evidence. |

## Completion boundary

Repository-owned public baseline gaps are closed by the associated remediation PR. Required-status enforcement remains a GitHub-hosted residual and must not be represented as PASS until independently observed.
