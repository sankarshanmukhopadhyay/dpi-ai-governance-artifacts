---
last_reviewed: 2026-03-04
applies_to: main
owners:
  tier0: repo-maintainers
  tier1: repo-maintainers
---

# Documentation Freshness & Relevance

## Tiers and review SLAs

| Tier | Scope | Max age | Primary entrypoints |
|---|---|---:|---|
| Tier 0 | Onboarding and navigation | 30 days | `README.md`, `docs/overview.md`, `packs/README.md` |
| Tier 1 | Pack semantics + schemas + templates | 60 days | Pack READMEs, `controls/`, `annex/` |

## Guardrails

- Tier 0 docs declare `last_reviewed` and the branch they apply to.
- Internal Markdown links must resolve in-repo.
- External links should prefer canonical sources and stable permalinks.

## Run the docs audit locally

```bash
python scripts/docs_audit.py
```

## What changed in this review (2026-03-04)

- Fixed a broken internal link in `packs/README.md`.
- Added a documentation overview and freshness spine for consistent navigation.
