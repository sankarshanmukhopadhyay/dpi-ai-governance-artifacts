#!/usr/bin/env python3
import json
import sys
from pathlib import Path

def err(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)

def load_yaml(path: Path):
    try:
        import yaml  # type: ignore
    except Exception as e:
        err("PyYAML not available. Install with: pip install pyyaml")
        raise
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def main(repo_root: Path) -> int:
    packs_dir = repo_root / "packs"
    if not packs_dir.exists():
        err("packs/ directory not found")
        return 2

    manifests = sorted(list(packs_dir.rglob("manifest.yaml")) + list(packs_dir.rglob("manifest.yml")))
    if not manifests:
        err("No pack manifests found under packs/**/manifest.y*ml")
        return 2

    rc = 0
    for m in manifests:
        data = load_yaml(m)
        if not isinstance(data, dict):
            err(f"{m}: manifest is not a mapping")
            rc = 2
            continue

        pack_id = data.get("pack_id")
        title = data.get("title")
        version = data.get("version")
        artifacts = data.get("artifacts")

        if not pack_id or not title or not version:
            err(f"{m}: missing one of required fields: pack_id, title, version")
            rc = 2

        if not isinstance(artifacts, list) or not artifacts:
            err(f"{m}: artifacts must be a non-empty list")
            rc = 2
            continue

        seen = set()
        for i, item in enumerate(artifacts):
            if not isinstance(item, dict) or "path" not in item:
                err(f"{m}: artifacts[{i}] must be a mapping with 'path'")
                rc = 2
                continue

            rel = item["path"]
            if not isinstance(rel, str) or not rel.strip():
                err(f"{m}: artifacts[{i}].path must be a non-empty string")
                rc = 2
                continue

            if rel in seen:
                err(f"{m}: duplicate artifact path: {rel}")
                rc = 2
            seen.add(rel)

            target = repo_root / rel
            if not target.exists():
                err(f"{m}: referenced artifact missing: {rel}")
                rc = 2

    # Basic JSON sanity for machine-readable registries
    json_files = [
        repo_root / "controls" / "registry.json",
        repo_root / "TRACE_COMPATIBILITY.json",
    ]
    for jf in json_files:
        if jf.exists():
            try:
                json.loads(jf.read_text(encoding="utf-8"))
            except Exception as e:
                err(f"{jf}: invalid JSON ({e})")
                rc = 2

    # Hygiene: no OS cruft
    cruft = list(repo_root.rglob(".DS_Store"))
    if cruft:
        for c in cruft:
            err(f"OS cruft present: {c.relative_to(repo_root)}")
        rc = 2

    return rc

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    sys.exit(main(root))
