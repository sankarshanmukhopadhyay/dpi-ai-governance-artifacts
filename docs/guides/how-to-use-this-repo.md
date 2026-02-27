# How to use this repository

This repository is a **governance operations kit**: it provides *portable artifacts* (schemas, templates, controlled documents, and conformance guidance) you can lift into real procurement, implementation, audit, and incident workflows.

The fastest path is to:
1. **Pick a starting scenario** (startup, enterprise, state).
2. **Adopt a thin slice** (one workflow end-to-end: e.g., decision → receipt → redress).
3. **Bind to a maturity level / assurance tier** (so teams know what “good” looks like).
4. **Operationalize** through templates + controlled docs.
5. **Prove it** through conformance evidence bundles.

---

## Repository map

### `controlled/`
**Controlled documents** are the “operating system” text for governance: policies, commitments, and expectations that should not drift silently.

Use this when you need **stable, auditable language** (what your org commits to).

Examples:
- Risk management: `controlled/risk/*`
- Redress & remediation: `controlled/redress/*`
- Assurance / evidence bundles: `controlled/assurance/*`

### `schemas/`
JSON Schemas define **machine-checkable structures** for key artifacts.

Use this when you need:
- Standardized data capture
- Automated validation
- Tooling integration

### `templates/`
Templates are **human-friendly starting points** aligned to schemas and controlled docs.

Use this when you need:
- Adoption without building tooling first
- Repeatable governance workflows

### `conformance/`
Conformance guidance answers: **How do we prove we did what we said?**

Use this when you need:
- Evidence bundle expectations
- Repeatable audit posture
- Cross-team alignment on “done”

### `playbooks/`
Playbooks are **when-things-go-wrong** operational runbooks.

Use this when you need:
- Incident response patterns
- Model drift response
- Security compromise response

### `docs/`
Documentation and integration guidance.

---

## Adoption workflow (recommended)

### Step 1 — Choose a “front door” workflow
Pick one and implement end-to-end:
- **Decision transparency** (decision receipt + authority directory + traceability)
- **Redress & remediation** (appeal → investigation → remediation completion)
- **Risk management** (risk register + scoring matrix + governance triggers)

### Step 2 — Establish minimum governance commitments
Adopt the relevant **controlled document(s)** and tailor only what you must. Treat these as your baseline commitments.

### Step 3 — Wire in operational templates
Use templates to run the workflow in real teams (even via docs/spreadsheets to start). Then graduate to tool-based capture using schemas.

### Step 4 — Bind to a maturity level / tier
Use the maturity model alignment guide to decide what level you’re aiming at and what artifacts become mandatory.

### Step 5 — Produce evidence
Use `conformance/evidence-bundle.md` and `controlled/assurance/evidence-bundles.md` to assemble evidence for audits, procurement evaluation, or internal assurance.

---

## Integration patterns

### Lightweight adoption (no tooling)
- Use templates as living documents
- Validate structure manually against schema descriptions
- Store artifacts in a shared repo or document workspace

### Tool-assisted adoption
- Use schemas as validation contracts
- Generate artifacts from internal systems
- Export evidence bundles for audits

### Procurement adoption
- Use templates as vendor response requirements
- Treat evidence bundles as bid evaluation inputs
- Bind deliverables to maturity levels / tiers

---

## Change management and versioning

- **Controlled documents** should change via explicit review (treat as governed assets).
- **Schemas** should be versioned carefully; breaking changes should include migrations in `docs/migrations/`.
- Use `VERSION` and `CHANGELOG.md` to understand release boundaries.

---

## Next documents

- Suggested adoption pathways: `docs/guides/adoption-pathways.md`
- Maturity model alignment: `docs/guides/maturity-model-alignment.md`
- Practitioner FAQ: `docs/faq.md`
