from __future__ import annotations

from datetime import datetime
from pathlib import Path
import sys
import yaml


def parse(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def decide(delegation: dict, request: dict) -> tuple[str, str]:
    status = delegation.get("status")
    if status == "revoked":
        return "deny", "delegation_revoked"
    if status == "suspended":
        return "deny", "delegation_suspended"
    at = parse(request["at"])
    if at < parse(delegation["not_before"]):
        return "deny", "delegation_not_yet_valid"
    if at > parse(delegation["not_after"]):
        return "deny", "delegation_expired"
    if request["actor"] != delegation["actor"]:
        return "deny", "delegate_mismatch"
    if request["action"] not in delegation["actions"]:
        return "deny", "action_out_of_scope"
    if request["resource"] not in delegation["resources"]:
        return "deny", "resource_out_of_scope"
    if request["purpose"] not in delegation["purposes"]:
        return "deny", "purpose_out_of_scope"
    return "allow", "delegation_valid"


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "test-vectors/governance/bounded-delegation.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    failures: list[str] = []
    for case in data.get("cases", []):
        actual = decide(case["delegation"], case["request"])
        expected = (case["expected"]["decision"], case["expected"]["reason"])
        if actual != expected:
            failures.append(f"{case['id']}: expected {expected}, got {actual}")
        else:
            print(f"PASS {case['id']}: {actual[0]} ({actual[1]})")
    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 2
    print(f"Bounded delegation vectors OK: {len(data.get('cases', []))} cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
