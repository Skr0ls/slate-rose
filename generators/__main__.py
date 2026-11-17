"""Command-line entry point for shared palette and theme tools."""

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from .jetbrains import render_scheme
from .jetbrains.ui import render_ui
from .palette import PaletteValidationError, load_palette, load_terminal_palette
from .vscode import render_theme

_ROOT = Path(__file__).resolve().parent.parent
_PALETTE = _ROOT / "palette/colors.json"
_TERMINAL_PALETTE = _ROOT / "palette/terminal.json"
_OUTPUT = _ROOT / "packages/vscode/themes/slate-rose-color-theme.json"
_JETBRAINS_OUTPUT = _ROOT / "packages/jetbrains/colors/Slate Rose.icls"
_JETBRAINS_UI_OUTPUT = _ROOT / "packages/jetbrains/resources/Slate Rose.theme.json"


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
    validate.add_argument("--terminal-palette", type=Path, default=_TERMINAL_PALETTE)
    for command in ("build", "check"):
        sub = commands.add_parser(command, help=f"{command} a generated theme")
        sub.add_argument("host", choices=("vscode", "jetbrains", "jetbrains-ui"))
        sub.add_argument("--palette", type=Path, default=_PALETTE)
        sub.add_argument("--terminal-palette", type=Path, default=_TERMINAL_PALETTE)
        sub.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        palette_path = args.path if args.command == "validate" else args.palette
        palette = load_palette(palette_path)
        terminal_palette = load_terminal_palette(args.terminal_palette)
        jetbrains_scheme = (
            render_scheme(palette)
            if args.command != "validate" and args.host in ("jetbrains", "jetbrains-ui")
            else None
        )
        print(
            f"Valid palette: {palette.name} (version {palette.version}, {len(palette.colors)} tokens) [{palette_path}]"
        )
        print(
            f"Valid palette: {terminal_palette.name} (version {terminal_palette.version}, {len(terminal_palette.colors)} tokens) [{args.terminal_palette}]"
        )
        if args.command == "validate":
            return 0
        if args.output is None:
            args.output = {
                "vscode": _OUTPUT,
                "jetbrains": _JETBRAINS_OUTPUT,
                "jetbrains-ui": _JETBRAINS_UI_OUTPUT,
            }[args.host]
        if any(
            _same_file(args.output, path)
            for path in (
                args.palette,
                _PALETTE,
                args.terminal_palette,
                _TERMINAL_PALETTE,
            )
        ):
            print(f"Output {args.output} conflicts with a palette", file=sys.stderr)
            return 1
        expected = (
            render_theme(palette, terminal_palette)
            if args.host == "vscode"
            else render_ui(palette)
            if args.host == "jetbrains-ui"
            else jetbrains_scheme
        ).encode("utf-8")
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
