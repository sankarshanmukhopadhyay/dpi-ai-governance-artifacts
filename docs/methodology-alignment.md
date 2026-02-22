# Methodology alignment

This repository is the **operational layer** for the DPI AI Governance Lab methodology.

- **Normative methodology:** `dpi-ai-governance-lab` (the workbench, review workflow, schemas)
- **Operational artifacts:** this repository (packs, templates, rulebooks, schemas, test vectors)

The goal is to keep the two repos **loosely coupled** but **semantically locked** via explicit versioning + traceability.

---

## Declared compatibility

- **Aligned Lab version:** `dpi-ai-governance-lab` **v0.4.1**
- **Policy:**  
  - Minor edits in the Lab docs are tolerated without requiring artifact changes.  
  - Changes to *schemas*, *review output structure*, or *tier semantics* are considered breaking for operational packs and SHOULD trigger an update here.

---

## Traceability map (method outputs → operational artifacts)

The Lab produces deterministic review outputs (schemas + templates). This repository packages operational equivalents so teams can implement the same logic in real systems.

| Lab output / schema | Purpose | Operational artifact location | Notes |
|---|---|---|---|
| `schemas/reviews/paper-review-report.schema.json` | canonical review report | `artifacts/` and `templates/` | Use as the “source of truth” for report structure |
| `schemas/reviews/paper-review-scorecard.schema.json` | scoring model output | `templates/` + `playbooks/` | Operational packs SHOULD preserve scoring fields |
| `schemas/reviews/paper-analysis.schema.json` | extracted abstractions + claims | `playbooks/` | Bind to “what we believe the system is” |
| `schemas/reviews/semantic-validation.schema.json` | validation tier results | `tools/` + `rulebook-test-vectors/` | Enables deterministic QA for packs |

---

## Operational discipline

1. Every **operational pack** SHOULD declare which Lab version it targets.
2. Every **breaking change** in Lab schemas SHOULD be reflected here within the next repo increment.
3. When in doubt, prefer **explicit mapping** over “tribal knowledge”.

---

## References

- DPI AI Governance Lab: https://github.com/sankarshanmukhopadhyay/dpi-ai-governance-lab
