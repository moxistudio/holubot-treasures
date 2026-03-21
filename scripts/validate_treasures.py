#!/usr/bin/env python3
"""Directory and pack.yaml validation for treasures indexed by catalog.yaml."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml

PACK_REQUIRED_TOP = {"meta", "skill"}
PACK_REQUIRED_META = {"id", "name", "kind", "version", "description"}
PACK_REQUIRED_SKILL = {"entry"}
REQUIRED_FILES = ("pack.yaml", "SKILL.md", "README.md", "examples/smoke.md")


def _load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"[ERROR] missing YAML file: {path}")
    except yaml.YAMLError as exc:
        raise SystemExit(f"[ERROR] invalid YAML in {path}: {exc}")


def _non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _validate_pack(pack_path: Path, treasure_id: str) -> list[str]:
    errors: list[str] = []
    data = _load_yaml(pack_path)
    if not isinstance(data, dict):
        return [f"{pack_path}: pack.yaml must be a mapping."]

    missing_top = PACK_REQUIRED_TOP - set(data.keys())
    if missing_top:
        errors.append(f"{pack_path}: missing top-level fields: {sorted(missing_top)}")

    meta = data.get("meta")
    if not isinstance(meta, dict):
        errors.append(f"{pack_path}: meta must be a mapping.")
        meta = {}
    missing_meta = PACK_REQUIRED_META - set(meta.keys())
    if missing_meta:
        errors.append(f"{pack_path}: meta missing required fields: {sorted(missing_meta)}")
    for field in PACK_REQUIRED_META:
        if field in meta and not _non_empty_string(meta[field]):
            errors.append(f"{pack_path}: meta.{field} must be a non-empty string.")

    skill = data.get("skill")
    if not isinstance(skill, dict):
        errors.append(f"{pack_path}: skill must be a mapping.")
        skill = {}
    missing_skill = PACK_REQUIRED_SKILL - set(skill.keys())
    if missing_skill:
        errors.append(f"{pack_path}: skill missing required fields: {sorted(missing_skill)}")
    if "entry" in skill and not _non_empty_string(skill["entry"]):
        errors.append(f"{pack_path}: skill.entry must be a non-empty string.")

    pack_id = meta.get("id")
    if _non_empty_string(pack_id):
        normalized = pack_id.replace("_", "-")
        if normalized != treasure_id:
            errors.append(
                f"{pack_path}: meta.id {pack_id!r} does not match catalog id {treasure_id!r}."
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate treasure directories and pack.yaml.")
    parser.add_argument(
        "catalog_path",
        nargs="?",
        default="catalog.yaml",
        help="Path to catalog YAML (default: catalog.yaml).",
    )
    args = parser.parse_args()

    catalog_path = Path(args.catalog_path).resolve()
    repo_root = catalog_path.parent
    catalog = _load_yaml(catalog_path)

    errors: list[str] = []
    treasures = catalog.get("treasures") if isinstance(catalog, dict) else None
    if not isinstance(treasures, list):
        print("[ERROR] catalog does not contain a valid treasures list.")
        return 1

    for item in treasures:
        if not isinstance(item, dict):
            errors.append("catalog treasure entry is not a mapping.")
            continue
        treasure_id = item.get("id")
        repo_path = item.get("repo_path")
        if not _non_empty_string(treasure_id) or not _non_empty_string(repo_path):
            errors.append(f"Invalid catalog entry: id={treasure_id!r}, repo_path={repo_path!r}")
            continue

        treasure_dir = repo_root / repo_path
        if not treasure_dir.exists():
            errors.append(f"{treasure_id}: missing directory {treasure_dir}")
            continue
        if not treasure_dir.is_dir():
            errors.append(f"{treasure_id}: repo_path is not a directory: {treasure_dir}")
            continue

        for relative in REQUIRED_FILES:
            target = treasure_dir / relative
            if not target.exists():
                errors.append(f"{treasure_id}: missing required file {target}")

        pack_path = treasure_dir / "pack.yaml"
        if pack_path.exists() and pack_path.is_file():
            errors.extend(_validate_pack(pack_path, treasure_id))

    if errors:
        print("[ERROR] Treasure validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"[OK] Treasure directory validation passed for {len(treasures)} entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
