"""Package a downloaded Zed artifact as a reproducible ZIP."""

import argparse
import io
import sys
import zipfile
from pathlib import Path

MEMBERS = ("LICENSE", "README.md", "extension.toml", "themes/slate-rose.json")


def package(source: Path, output: Path) -> None:
    entries = [(name, (source / name).read_bytes()) for name in MEMBERS]
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, data in entries:
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(buffer.getvalue())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        package(args.source, args.output)
    except OSError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
