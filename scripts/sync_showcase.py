#!/usr/bin/env python3
"""Copy a verified University Lab build into the public Pages directory."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DESTINATION = REPO_ROOT / "site" / "vortex-university-lab"
HTML_FILES = ("index.html", "uczestnik.html", "prowadzacy.html")
SCHEMA_FILES = ("vortexrun.schema.json", "vortexrun-v1.schema.json", "vortexrun-v2.schema.json")
COLOR_SCHEME_META = '  <meta name="color-scheme" content="light">'
ROBOTS_META = '  <meta name="robots" content="noindex,nofollow">'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update the public University Lab showcase")
    parser.add_argument("build_directory", type=Path, help="Generated and verified showcase directory")
    return parser.parse_args()


def require_file(path: Path) -> None:
    if not path.is_file():
        raise SystemExit(f"Missing required build file: {path}")


def copy_html(source: Path, destination: Path) -> None:
    document = source.read_text(encoding="utf-8")
    if ROBOTS_META not in document:
        if COLOR_SCHEME_META not in document:
            raise SystemExit(f"Cannot add robots metadata to: {source}")
        document = document.replace(COLOR_SCHEME_META, f"{COLOR_SCHEME_META}\n{ROBOTS_META}", 1)
    destination.write_text(document, encoding="utf-8")


def main() -> None:
    args = parse_args()
    build_directory = args.build_directory.expanduser().resolve()
    for name in HTML_FILES:
        require_file(build_directory / name)
    for name in SCHEMA_FILES:
        require_file(build_directory / "schemas" / name)

    (DESTINATION / "schemas").mkdir(parents=True, exist_ok=True)
    for name in HTML_FILES:
        copy_html(build_directory / name, DESTINATION / name)
    for name in SCHEMA_FILES:
        shutil.copy2(build_directory / "schemas" / name, DESTINATION / "schemas" / name)

    print(f"Updated public showcase in {DESTINATION}")


if __name__ == "__main__":
    main()
