#!/usr/bin/env python3
"""Validate repository JSON artifacts against JSON Schemas.

Validates:
- templates/*.example*.json against matching schema in schemas/
- rulebook-test-vectors/**.json against schema inferred from top-level folder name

Conventions:
- Vectors under a path containing `/invalid/` are expected to FAIL validation.
- All other vectors/examples are expected to PASS validation.

Exit code:
- 0 if everything behaves as expected
- 1 otherwise
"""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = REPO_ROOT / "schemas"
TEMPLATES_DIR = REPO_ROOT / "templates"
VECTORS_DIR = REPO_ROOT / "rulebook-test-vectors"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validator_for(schema_path: Path) -> Draft202012Validator:
    schema = load_json(schema_path)
    return Draft202012Validator(schema)


def iter_template_examples():
    for p in sorted(TEMPLATES_DIR.glob("*.json")):
        if ".example" in p.name:
            yield p


def schema_for_template(example_path: Path) -> Path | None:
    # appeal-filing.example.json -> appeal-filing.schema.json
    stem = example_path.name.split(".example")[0]

    candidate = SCHEMAS_DIR / f"{stem}.schema.json"
    if candidate.exists():
        return candidate

    # vocabulary convention (reason-codes.vocab.example.json -> reason-codes.vocab.json)
    candidate = SCHEMAS_DIR / f"{stem}.vocab.json"
    if candidate.exists():
        return candidate

    candidate = SCHEMAS_DIR / f"{stem}.json"
    if candidate.exists():
        return candidate

    return None


def iter_vectors():
    if not VECTORS_DIR.exists():
        return
    for p in sorted(VECTORS_DIR.rglob("*.json")):
        yield p


def schema_for_vector(vector_path: Path) -> Path | None:
    # vectors live under rulebook-test-vectors/<schema-stem>/
    rel = vector_path.relative_to(VECTORS_DIR)
    if not rel.parts:
        return None
    schema_stem = rel.parts[0]
    candidate = SCHEMAS_DIR / f"{schema_stem}.schema.json"
    return candidate if candidate.exists() else None


def validate_one(schema_path: Path, instance_path: Path) -> list[str]:
    v = validator_for(schema_path)
    instance = load_json(instance_path)
    errors = sorted(v.iter_errors(instance), key=lambda e: list(e.path))
    msgs = []
    for e in errors:
        loc = "$" + "".join([f"[{p}]" if isinstance(p, int) else f".{p}" for p in e.path])
        msgs.append(f"{instance_path}: {loc}: {e.message}")
    return msgs


def main() -> int:
    failures: list[str] = []

    # templates
    for ex in iter_template_examples():
        schema_path = schema_for_template(ex)
        if schema_path is None:
            failures.append(f"{ex}: No matching schema found in schemas/")
            continue
        failures.extend(validate_one(schema_path, ex))

    # vectors
    for vec in iter_vectors() or []:
        schema_path = schema_for_vector(vec)
        if schema_path is None:
            failures.append(f"{vec}: No matching schema found for vector directory")
            continue

        expected_invalid = "invalid" in vec.parts
        errs = validate_one(schema_path, vec)

        if expected_invalid:
            if not errs:
                failures.append(f"{vec}: Expected INVALID, but validation PASSED")
        else:
            failures.extend(errs)

    if failures:
        print("Schema validation FAILED:\n")
        for msg in failures:
            print(" - " + msg)
        return 1

    print("Schema validation OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
