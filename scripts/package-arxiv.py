#!/usr/bin/env python3
"""Create and validate a deterministic, portable arXiv source archive."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import sys
import zipfile


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_ROOT_FILES = ("main.tex", "main.bbl", "references.bib")
APPENDIX_DIR = ROOT / "appendix"
DEFAULT_OUTPUT = ROOT / "output" / "arxiv" / "EDGD-arxiv-source.zip"
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Package the EDGD LaTeX sources for arXiv."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"archive path (default: {DEFAULT_OUTPUT.relative_to(ROOT)})",
    )
    return parser.parse_args()


def source_files() -> list[Path]:
    files = [ROOT / name for name in REQUIRED_ROOT_FILES]
    if not APPENDIX_DIR.is_dir():
        raise FileNotFoundError(f"missing appendix directory: {APPENDIX_DIR}")
    files.extend(sorted(path for path in APPENDIX_DIR.rglob("*") if path.is_file()))

    missing = [path for path in files if not path.is_file()]
    if missing:
        missing_text = "\n".join(f"  - {path}" for path in missing)
        raise FileNotFoundError(
            "required arXiv source files are missing:\n"
            f"{missing_text}\n"
            "Run latexmk before packaging so main.bbl is available."
        )
    return files


def archive_name(path: Path) -> str:
    name = path.relative_to(ROOT).as_posix()
    if "\\" in name or name.startswith("/") or ".." in Path(name).parts:
        raise ValueError(f"unsafe archive path: {name}")
    return name


def write_archive(output: Path, files: list[Path]) -> list[str]:
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    names: list[str] = []

    with zipfile.ZipFile(
        output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for path in files:
            name = archive_name(path)
            info = zipfile.ZipInfo(name, ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compresslevel=9)
            names.append(name)
    return names


def validate_archive(output: Path, expected_names: list[str]) -> str:
    with zipfile.ZipFile(output, "r") as archive:
        actual_names = archive.namelist()
        if actual_names != expected_names:
            raise ValueError(
                "archive manifest differs from the expected ordered source list"
            )
        if any("\\" in name for name in actual_names):
            raise ValueError("archive contains Windows path separators")
        if archive.testzip() is not None:
            raise ValueError("archive integrity check failed")

    return hashlib.sha256(output.read_bytes()).hexdigest().upper()


def main() -> int:
    args = parse_args()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    try:
        files = source_files()
        expected_names = [archive_name(path) for path in files]
        write_archive(output, files)
        digest = validate_archive(output, expected_names)
    except (FileNotFoundError, OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"Created: {output.resolve()}")
    print(f"Files: {len(expected_names)}")
    print(f"SHA-256: {digest}")
    for name in expected_names:
        print(f"  {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
