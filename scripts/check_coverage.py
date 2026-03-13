#!/usr/bin/env python3
"""Report HTML files that lack an assigned docs section."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parent.parent

CATEGORIES: Dict[str, str] = {
    "news": "docs/system.md",
    "intro": "docs/system.md",
    "config": "docs/system.md",
    "imm": "docs/system.md",
    "announce": "docs/system.md",
    "newhand": "docs/newbie.md",
    "skill": "docs/skills.md",
    "realm": "docs/realm.md",
    "map": "docs/maps.md",
    "download": "docs/download.md",
    "link": "docs/links.md",
    "links": "docs/links.md",
    "phorum": "docs/links.md",
    "body": "docs/index.md",
    "system": "docs/system.md",
    "topmenu": "docs/index.md",
}

SPECIAL = {
    "announce.html": "docs/system.md",
    "announce-m.html": "docs/system.md",
    "download.html": "docs/download.md",
    "download-m.html": "docs/download.md",
    "newhand.html": "docs/newbie.md",
    "newhand-m.html": "docs/newbie.md",
    "links.html": "docs/links.md",
    "links-m.html": "docs/links.md",
    "phorum.html": "docs/links.md",
    "phorum-m.html": "docs/links.md",
    "realm.html": "docs/realm.md",
    "realm-m.html": "docs/realm.md",
    "system.html": "docs/system.md",
    "system-m.html": "docs/system.md",
    "body.html": "docs/index.md",
    "body-l.html": "docs/index.md",
    "body-r.html": "docs/index.md",
    "toplogo.html": "docs/index.md",
    "topmenu.html": "docs/index.md",
    "index.html": "docs/index.md",
}


def classify(path: Path) -> str:
    if path.name in SPECIAL:
        return SPECIAL[path.name]
    parts = path.parts
    if len(parts) > 1:
        prefix = parts[0]
        return CATEGORIES.get(prefix, "")
    return ""


def main() -> None:
    parser = argparse.ArgumentParser(description="Check docs coverage for HTML files")
    parser.add_argument("--root", default=ROOT, type=Path)
    args = parser.parse_args()

    missing: List[str] = []
    for html_file in sorted(args.root.rglob("*.html")):
        rel = html_file.relative_to(args.root).as_posix()
        if rel.startswith("docs/"):
            continue
        if classify(Path(rel)):
            continue
        missing.append(rel)
    if missing:
        print("Unassigned HTML files (needs manual review):")
        for item in missing:
            print(f" - {item}")
    else:
        print("All HTML files mapped to a docs section.")


if __name__ == "__main__":
    main()
