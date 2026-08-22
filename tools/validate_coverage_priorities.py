#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "remediation" / "remediation-registry.yaml"
PRIORITIES = ROOT / "remediation" / "coverage-priorities.yaml"


def main() -> int:
    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    priorities = yaml.safe_load(PRIORITIES.read_text(encoding="utf-8")) or {}

    known = {item.get("capability_id"): item for item in registry.get("capabilities", [])}
    errors: list[str] = []
    seen_ranks: set[int] = set()
    seen_caps: set[str] = set()

    for item in priorities.get("priorities", []):
        rank = item.get("rank")
        cap = item.get("capability_id")
        if not isinstance(rank, int) or rank < 1:
            errors.append(f"invalid priority rank for {cap}: {rank}")
        elif rank in seen_ranks:
            errors.append(f"duplicate priority rank: {rank}")
        else:
            seen_ranks.add(rank)

        if cap in seen_caps:
            errors.append(f"duplicate capability priority: {cap}")
        seen_caps.add(cap)

        if cap not in known:
            errors.append(f"priority references unknown capability: {cap}")
            continue

        if item.get("current_coverage") != known[cap].get("coverage"):
            errors.append(
                f"coverage mismatch for {cap}: priorities={item.get('current_coverage')} registry={known[cap].get('coverage')}"
            )

        recurrence = item.get("recurrence") or {}
        with_gap = recurrence.get("reviews_with_gap")
        total = recurrence.get("reviews_total")
        if not isinstance(with_gap, int) or not isinstance(total, int) or total < 1 or with_gap < 0 or with_gap > total:
            errors.append(f"invalid recurrence for {cap}: {recurrence}")

        gates = item.get("next_evidence_gate") or []
        if not gates:
            errors.append(f"missing next evidence gate for {cap}")

    ranks = sorted(seen_ranks)
    if ranks and ranks != list(range(1, len(ranks) + 1)):
        errors.append(f"priority ranks must be contiguous from 1: {ranks}")

    if errors:
        print("Coverage priority validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 2

    print(f"Coverage priority validation OK: {len(seen_caps)} capabilities")
    return 0


if __name__ == "__main__":
    sys.exit(main())
