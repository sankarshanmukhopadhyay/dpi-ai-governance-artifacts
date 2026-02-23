# Artifact kinds

This repository uses multiple artifact kinds. Treat them differently:

- **Policy**: human-auditable requirements (processes/practices).
- **Rule**: machine-testable requirements (rules engine / checks).
- **Schema**: machine-readable structural constraints (JSON Schema, etc.).
- **Template**: a fillable structure for producing governed artifacts (decision receipts, findings, etc.).
- **Profile**: a scoped bundle of requirements for a given tier/context.
- **Evidence bundle**: an explicit list of required/optional evidence artifacts for assurance.
- **Test vector**: a concrete input/output example for validating implementations.
- **Playbook**: operational steps for recurring failure modes.

Controlled documents (`controlled/`) are where we state conformance expectations and how these kinds interlock.
