#!/usr/bin/env python3
"""Minimal P0 catalog validator for holubot-treasures."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_TOP = {"schema_version", "treasures"}
REQUIRED_ITEM = {
    "id",
    "name",
    "author",
    "owner",
    "category",
    "lane",
    "verified",
    "price",
    "description",
    "repo_path",
}
RECOMMENDED_ITEM = {"tags", "source_kind", "knowledge", "demo_ready"}
P0_REQUIRED_IDS = {
    "know-yourself",
    "deep-search",
    "super-office",
    "weekly-report",
    "ai-sentinel",
}


def _load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"[ERROR] catalog file not found: {path}")
    except yaml.YAMLError as exc:
        raise SystemExit(f"[ERROR] invalid YAML in {path}: {exc}")


def _non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate catalog.yaml for P0 staging.")
    parser.add_argument(
        "catalog_path",
        nargs="?",
        default="catalog.yaml",
        help="Path to catalog YAML (default: catalog.yaml).",
    )
    args = parser.parse_args()
    catalog_path = Path(args.catalog_path)
    data = _load_yaml(catalog_path)

    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(data, dict):
        errors.append("Top-level catalog must be a mapping.")
        data = {}

    missing_top = REQUIRED_TOP - set(data.keys())
    if missing_top:
        errors.append(f"Missing top-level fields: {sorted(missing_top)}")

    schema_version = data.get("schema_version")
    if not _non_empty_string(schema_version):
        errors.append("schema_version must be a non-empty string.")

    treasures = data.get("treasures")
    if not isinstance(treasures, list) or not treasures:
        errors.append("treasures must be a non-empty list.")
        treasures = []

    seen_ids: set[str] = set()
    indexed: dict[str, dict[str, Any]] = {}
    for i, item in enumerate(treasures, start=1):
        prefix = f"treasures[{i}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be a mapping.")
            continue

        missing_fields = REQUIRED_ITEM - set(item.keys())
        if missing_fields:
            errors.append(f"{prefix} missing required fields: {sorted(missing_fields)}")

        for field in RECOMMENDED_ITEM:
            if field not in item:
                warnings.append(f"{prefix} missing recommended field: {field}")

        treasure_id = item.get("id")
        if not _non_empty_string(treasure_id):
            errors.append(f"{prefix}.id must be a non-empty string.")
        else:
            if not ID_RE.fullmatch(treasure_id):
                errors.append(f"{prefix}.id must be hyphenated lowercase: {treasure_id!r}")
            if treasure_id in seen_ids:
                errors.append(f"Duplicate id found: {treasure_id!r}")
            seen_ids.add(treasure_id)
            indexed[treasure_id] = item

        repo_path = item.get("repo_path")
        if not _non_empty_string(repo_path):
            errors.append(f"{prefix}.repo_path must be a non-empty string.")
        else:
            if "/" not in repo_path:
                errors.append(f"{prefix}.repo_path must include owner path segment.")
            if _non_empty_string(treasure_id):
                tail = repo_path.split("/")[-1]
                if tail != treasure_id:
                    errors.append(
                        f"{prefix}.repo_path must end with id; got {repo_path!r} for id {treasure_id!r}"
                    )

    missing_required_ids = sorted(P0_REQUIRED_IDS - seen_ids)
    if missing_required_ids:
        errors.append(f"Missing required P0 treasures: {missing_required_ids}")

    ai_sentinel = indexed.get("ai-sentinel")
    if ai_sentinel:
        if ai_sentinel.get("demo_ready") is not False:
            errors.append("ai-sentinel.demo_ready must be false in current P0 scope.")
        knowledge = ai_sentinel.get("knowledge")
        if not isinstance(knowledge, dict):
            errors.append("ai-sentinel.knowledge must be a mapping with scope metadata.")
        elif knowledge.get("enabled") is not True:
            errors.append("ai-sentinel.knowledge.enabled must be true now that the packaged KB body ships in current P0 scope.")

    if warnings:
        print("[WARN] Catalog warnings:")
        for warning in warnings:
            print(f"  - {warning}")

    if errors:
        print("[ERROR] Catalog validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"[OK] Catalog validation passed: {catalog_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
