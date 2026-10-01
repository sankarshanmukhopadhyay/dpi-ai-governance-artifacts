#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "conformance" / "capability-conformance.schema.json"
PROFILES = ROOT / "conformance" / "profiles"
INVALID_FIXTURE = ROOT / "conformance" / "fixtures" / "invalid-missing-requirements.yaml"
INVALID_CONTINUITY_FIXTURE = ROOT / "conformance" / "fixtures" / "invalid-continuity-effect.yaml"
REGISTRY = ROOT / "remediation" / "remediation-registry.yaml"


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors: list[str] = []
    profiles: dict[str, dict] = {}

    for path in sorted(PROFILES.glob("*.yaml")):
        data = load_yaml(path)
        validation = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        if validation:
            for error in validation:
                errors.append(f"{path}: {error.message}")
            continue

        profile_id = data["profile_id"]
        capability_id = data["capability_id"]
        if profile_id in profiles:
            errors.append(f"duplicate profile_id: {profile_id}")
        requirement_ids = [item["id"] for item in data["requirements"]]
        if len(requirement_ids) != len(set(requirement_ids)):
            errors.append(f"{profile_id}: duplicate requirement id")
        continuity = data.get("continuity") or {}
        rules = continuity.get("rules") or []
        if not rules:
            errors.append(f"{profile_id}: continuity.rules must not be empty")
        event_types = [item.get("event_type") for item in rules]
        if len(event_types) != len(set(event_types)):
            errors.append(f"{profile_id}: duplicate continuity event_type")
        profiles[profile_id] = data

    invalid = load_yaml(INVALID_FIXTURE)
    if not list(validator.iter_errors(invalid)):
        errors.append("falsification fixture unexpectedly validated")

    invalid_continuity = load_yaml(INVALID_CONTINUITY_FIXTURE)
    if not list(validator.iter_errors(invalid_continuity)):
        errors.append("invalid continuity effect fixture unexpectedly validated")

    registry = load_yaml(REGISTRY)
    for capability in registry.get("capabilities", []):
        profile_ref = capability.get("conformance_profile")
        if not profile_ref:
            continue
        profile_path = ROOT / profile_ref
        if not profile_path.exists():
            errors.append(f"{capability['capability_id']}: missing conformance profile {profile_ref}")
            continue
        data = load_yaml(profile_path)
        if data.get("capability_id") != capability.get("capability_id"):
            errors.append(f"{capability['capability_id']}: conformance profile capability mismatch")

    if errors:
        print("FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Capability conformance profiles OK: {len(profiles)}")
    print("Falsification fixtures correctly rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
