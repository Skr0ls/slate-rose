"""Command-line entry point for shared palette and theme tools."""

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from .palette import PaletteValidationError, load_palette
from .vscode import render_theme

_ROOT = Path(__file__).resolve().parent.parent
_PALETTE = _ROOT / "palette/colors.json"
_OUTPUT = _ROOT / "packages/vscode/themes/slate-rose-color-theme.json"


def _same_file(first: Path, second: Path) -> bool:
    if first.resolve() == second.resolve():
        return True
    try:
        return first.samefile(second)
    except FileNotFoundError:
        return False


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Slate Rose palette tools")
    commands = parser.add_subparsers(dest="command", required=True)
    validate = commands.add_parser(
        "validate", help="validate a palette without modifying it"
    )
    validate.add_argument("path", nargs="?", type=Path, default=_PALETTE)
    for command in ("build", "check"):
        sub = commands.add_parser(command, help=f"{command} a generated theme")
        sub.add_argument("host", choices=("vscode",))
        sub.add_argument("--palette", type=Path, default=_PALETTE)
        sub.add_argument("--output", type=Path, default=_OUTPUT)
    args = parser.parse_args(argv)
    try:
        palette = load_palette(
            args.path if args.command == "validate" else args.palette
        )
        if args.command == "validate":
            print(
                f"Valid palette: {palette.name} (version {palette.version}, {len(palette.colors)} tokens)"
            )
            return 0
        if _same_file(args.output, args.palette) or _same_file(args.output, _PALETTE):
            print(f"Output {args.output} conflicts with a palette", file=sys.stderr)
            return 1
        expected = render_theme(palette).encode("utf-8")
        if args.command == "check":
            if args.output.read_bytes() != expected:
                print(f"Generated theme is stale: {args.output}", file=sys.stderr)
                return 1
            print(f"Generated theme is current: {args.output}")
        else:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_bytes(expected)
            print(f"Generated theme: {args.output}")
    except (PaletteValidationError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
