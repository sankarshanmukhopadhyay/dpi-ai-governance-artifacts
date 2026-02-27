# Minimum Digital Kernel — Operational Pack

This pack turns the **Minimum Digital Kernel** framing into an adoptable bundle: a small set of artifacts that make
**legitimate action** possible in DPI+AI systems (procure → implement → test → audit).

## Scope

In-scope:
- Decision accountability contracts (decision receipts, reason codes)
- Authority and responsibility mapping (authority directory)
- Rulebook interface (rulebook manifest + change-control)
- Tier profile binding (how “assurance tiers” affect expectations)

Out-of-scope:
- Full risk libraries and sector-specific controls (use the broader repo for that)

## Adoption path (practical)

1. **Adopt the Tier Profile**
   - Use the tier profile to decide what is mandatory for your program.
2. **Stand up Decision Receipts**
   - Emit decision receipts for high-impact decisions first, then expand coverage.
3. **Publish Authority Directory**
   - Maintain a machine-readable directory of responsible governance actors.
4. **Publish Rulebook Manifest + Change Control**
   - Treat your governance rules like an API: versioned, testable, and reviewable.
5. **Evidence + Conformance**
   - Assemble the evidence bundle and use checklists to validate completeness.

## Primary outputs

- Decision Receipt(s)
- Authority Directory Entry / Directory
- Rulebook Manifest (+ change-control)
- Tier binding evidence (tier profile + declared tier)

## Key references

- Guide: `docs/guides/minimum-digital-kernel-operationalising.md`
- Conformance tier profile: `conformance/mdk-tier-profile.md`
- Evidence bundling: `conformance/evidence-bundle.md`

## Included artifacts

See [`manifest.yaml`](./manifest.yaml) for the exact inventory.


---

## What’s in this pack (quick links)

- Implementation guide: `implementation-guide.md`
- Artifact checklist: `artifact-checklist.md`
- Control mapping: `controls-mapping.md`
- Templates: `decision-receipt.template.md`, `authority-directory.template.md`

This pack uses the shared schemas and examples referenced in `manifest.yaml` and maps to stable control IDs in `controls/registry.yaml`.
