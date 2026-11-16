"""Command-line entry point for shared palette tools."""

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from .palette import PaletteValidationError, load_palette


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Slate Rose palette tools")
    commands = parser.add_subparsers(dest="command", required=True)
    validate = commands.add_parser(
        "validate", help="validate a palette without modifying it"
    )
    validate.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "palette/colors.json",
    )
    args = parser.parse_args(argv)
    try:
        palette = load_palette(args.path)
    except PaletteValidationError as exc:
        print(f"Palette validation failed: {exc}", file=sys.stderr)
        return 1
    print(
        f"Valid palette: {palette.name} (version {palette.version}, {len(palette.colors)} tokens)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
