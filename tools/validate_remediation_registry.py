#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "remediation" / "remediation-registry.yaml"


def main() -> int:
    if not REGISTRY.exists():
        print(f"Missing remediation registry: {REGISTRY}")
        return 2

    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    errors: list[str] = []

    if not isinstance(data, dict):
        errors.append("Registry root must be a mapping")
        data = {}

    if data.get("status") not in {"experimental", "candidate", "stable"}:
        errors.append("status must be experimental, candidate, or stable")

    authority = data.get("authority") or {}
    if authority.get("normative") is not False:
        errors.append("registry authority.normative must be false unless an explicit delegated authority model is introduced")

    capabilities = data.get("capabilities") or []
    if not capabilities:
        errors.append("Registry must contain at least one capability")

    seen: set[str] = set()
    for index, capability in enumerate(capabilities):
        cid = capability.get("capability_id")
        prefix = f"capabilities/{index}"
        if not cid or not str(cid).startswith("CAP-"):
            errors.append(f"{prefix}: capability_id must start with CAP-")
            continue
        if cid in seen:
            errors.append(f"{prefix}: duplicate capability_id {cid}")
        seen.add(cid)

        coverage = capability.get("coverage")
        if coverage not in {"partial", "standardized"}:
            errors.append(f"{cid}: coverage must be partial or standardized")

        requirements = capability.get("implementation_requirements") or []
        if not requirements:
            errors.append(f"{cid}: implementation_requirements must not be empty")

        evidence = capability.get("closure_evidence") or []
        if not evidence:
            errors.append(f"{cid}: closure_evidence must not be empty")

        artifacts = capability.get("artifacts") or []
        if coverage == "standardized" and not artifacts:
            errors.append(f"{cid}: standardized coverage requires at least one artifact")

        for artifact in artifacts:
            rel = artifact.get("path")
            if not rel:
                errors.append(f"{cid}: artifact path is required")
                continue
            path = ROOT / rel
            if not path.exists():
                errors.append(f"{cid}: referenced artifact does not exist: {rel}")

    if errors:
        print("FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK")
    print(f"Capabilities: {len(capabilities)}")
    standardized = sum(1 for item in capabilities if item.get("coverage") == "standardized")
    partial = sum(1 for item in capabilities if item.get("coverage") == "partial")
    print(f"Standardized: {standardized}")
    print(f"Partial: {partial}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
