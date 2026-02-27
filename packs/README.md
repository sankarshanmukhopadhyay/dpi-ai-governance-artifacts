# Operational Packs

Operational Packs are **implementation-ready bundles** of schemas, templates, playbooks, and controlled documentation.

They are designed to be adopted as **units of work**: something a program team can pick up, integrate, and evidence
within a defined delivery cycle.

## Packs in this repository

| Pack | What it is for | Primary outputs |
|---|---|---|
| [Minimum Digital Kernel](./minimum-digital-kernel/README.md) | Establish the minimum governance surface area needed for legitimate action in DPI+AI systems | Decision receipts, authority directory, rulebook manifest, tier profile |
| [Meta-Governance](./meta-governance/README.md) | Put governance itself under change-control and oversight | Delegation contracts, governance triggers, oversight reviews, rulebook change-control |
| [AI Redress & Accountability](./ai-redress-accountability/README.md) | Make redress, remediation, and auditability operational | Appeals, incidents, audit findings, correction workflows, SLAs |
| [Public Sector AI Procurement](./public-sector-ai-procurement/README.md) | Translate governance requirements into procurement language and vendor evidence | Vendor capability attestation, control evidence requests, evaluation scorecard |
| [Delegated Agent Governance](./delegated-agent-governance/README.md) | Govern agent delegation boundaries, accountability handoffs, and override semantics | Delegation register, agent action logging expectations, escalation/kill-switch patterns |

## Pack contract (common structure)

Each pack provides:

- **README**: scope, adoption path, and evidence outputs
- **Manifest**: a machine-readable inventory of included artifacts (paths and roles)
- **Starter bundle**: optional examples you can copy and adapt

## How to use packs

1. Pick a pack aligned to your program objective.
2. Start with the pack README “Adoption Path”.
3. Use the manifest to pull artifacts into your own repo, program workspace, or procurement pack.
4. Produce the pack’s “Primary outputs” and validate them with schemas / checklists.

> Note: Packs **reference** canonical artifacts elsewhere in this repo (e.g., `schemas/`, `templates/`, `controlled/`) rather than duplicating them.
