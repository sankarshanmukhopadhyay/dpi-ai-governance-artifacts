# Operationalising the Minimum Digital Kernel

This repository provides a practical path from "Minimum Digital Kernel" concepts to implementable and auditable interfaces.

## The thin waist

Start by standardizing a small set of portable contracts:

1. Decision receipts
2. Authority directory entries
3. Versioned rulebooks and manifests
4. Registry correction and recompute workflows
5. Appeals and audit interfaces

## Suggested adoption sequence

1. Adopt decision receipts as a required output for consequential decisions.
2. Stand up an authority directory that can verify keys, roles, and status.
3. Implement rulebook release discipline and publish manifests.
4. Add correction and recompute interfaces for the registries that drive the largest denial volume.
5. Add appeals and audit interfaces for Tier 3 workflows.

## Practical guardrails

- Keep receipts minimal. Use hashes and references, not raw personal data.
- Use reason codes that point to remedies.
- Treat correction and recompute as first-class workflows, not customer support exceptions.
- Ensure that appeals and audit authorities can issue enforceable orders.
