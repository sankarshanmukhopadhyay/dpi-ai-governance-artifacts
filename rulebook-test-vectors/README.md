# Rulebook Test Vectors

This directory contains **validation test vectors** for the schemas in this repository.

## Current coverage

- `decision-receipt/valid/*` — known-good receipts (including tier-conditioned requirements)
- `decision-receipt/invalid/*` — negative tests intended to fail schema validation

## How to run

Use the repository validator:

```bash
python tools/validate_schemas.py
```

The validator checks:
- `templates/*.example.json` against `schemas/*.schema.json`
- `rulebook-test-vectors/**.json` against the relevant schema(s)

