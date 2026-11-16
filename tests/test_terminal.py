"""Terminal palette validation, mappings, and input protection."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from generators.palette import (
    PaletteValidationError,
    load_palette,
    load_terminal_palette,
)
from generators.vscode import render_theme

ROOT = Path(__file__).resolve().parent.parent
CORE = ROOT / "palette/colors.json"
TERMINAL = ROOT / "palette/terminal.json"


class TerminalTests(unittest.TestCase):
    def test_canonical_and_mappings(self) -> None:
        before = (CORE.read_bytes(), TERMINAL.read_bytes())
        core = load_palette(CORE)
        terminal = load_terminal_palette(TERMINAL)
        self.assertEqual(
            (terminal.name, terminal.version, len(terminal.colors)),
            ("Slate Rose Terminal", "0.1", 16),
        )
        with self.assertRaises(TypeError):
            terminal.colors["red"] = "#FFFFFF"  # type: ignore[index]
        theme = json.loads(render_theme(core, terminal))
        colors = theme["colors"]
        expected = {
            "Black": "#2B323E",
            "Red": "#E47691",
            "Green": "#A9CE91",
            "Yellow": "#D8B981",
            "Blue": "#8CC6F1",
            "Magenta": "#CAA1DE",
            "Cyan": "#8FCBC5",
            "White": "#D1D4DC",
            "BrightBlack": "#8992A1",
            "BrightRed": "#F19DB0",
            "BrightGreen": "#C1DFA9",
            "BrightYellow": "#E0C38C",
            "BrightBlue": "#ACD7F5",
            "BrightMagenta": "#DEB9EC",
            "BrightCyan": "#A9E0D9",
            "BrightWhite": "#EFF1F5",
        }
        expected = {"terminal.ansi" + key: value for key, value in expected.items()}
        expected.update(
            {
                "terminal.background": "#191D25",
                "terminal.foreground": "#D1D4DC",
                "terminalCursor.foreground": "#99C4E6",
                "terminalCursor.background": "#191D25",
                "terminal.border": "#2B323E",
                "terminal.selectionBackground": "#364455",
                "terminal.inactiveSelectionBackground": "#36445580",
                "terminal.findMatchBackground": "#99C4E633",
                "terminal.findMatchBorder": "#99C4E6",
                "terminal.findMatchHighlightBackground": "#99C4E61A",
            }
        )
        self.assertEqual(
            {
                k: v
                for k, v in colors.items()
                if k.startswith(("terminal.", "terminalCursor."))
            },
            expected,
        )
        self.assertEqual(before, (CORE.read_bytes(), TERMINAL.read_bytes()))

    def test_invalid_sources(self) -> None:
        data = json.loads(TERMINAL.read_text())
        cases = ["{", '{"name": 1, "name": 2}', '{"colors": {"red": 1, "red": 2}}']
        for field, value in (("name", " "), ("version", None), ("extra", 1)):
            modified = dict(data, **{field: value})
            cases.append(json.dumps(modified))
        for colors in (
            {k: v for k, v in data["colors"].items() if k != "red"},
            dict(data["colors"], extra="#123456"),
            dict(data["colors"], red="#bad"),
        ):
            cases.append(json.dumps(dict(data, colors=colors)))
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "invalid.json"
            for content in cases:
                with self.subTest(content=content):
                    path.write_text(content)
                    with self.assertRaises(PaletteValidationError):
                        load_terminal_palette(path)
                    self.assertEqual(path.read_text(), content)
            with self.assertRaises(PaletteValidationError):
                load_terminal_palette(path / "missing")

    def test_cli_failure_and_aliases(self) -> None:
        def cli(*args: str) -> subprocess.CompletedProcess[str]:
            return subprocess.run(
                [sys.executable, "-m", "generators", *args],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            core = root / "core.json"
            terminal = root / "terminal.json"
            core.write_bytes(CORE.read_bytes())
            terminal.write_bytes(TERMINAL.read_bytes())
            invalid = root / "invalid.json"
            invalid.write_text("{}")
            output = root / "missing" / "theme.json"
            for command in ("validate", "build", "check"):
                args = [command] + (
                    [] if command == "validate" else ["vscode", "--output", str(output)]
                )
                result = cli(*args, "--terminal-palette", str(invalid))
                self.assertEqual(result.returncode, 1)
                self.assertFalse(output.parent.exists())
            output.parent.mkdir()
            output.write_bytes(b"stale")
            result = cli("check", "vscode", "--output", str(output))
            self.assertEqual(result.returncode, 1)
            self.assertEqual(output.read_bytes(), b"stale")
            result = cli(
                "build",
                "vscode",
                "--output",
                str(output),
                "--terminal-palette",
                str(invalid),
            )
            self.assertEqual(result.returncode, 1)
            self.assertEqual(output.read_bytes(), b"stale")
            for source in (core, terminal, CORE, TERMINAL):
                for kind in ("direct", "symlink", "hardlink"):
                    alias = root / ("alias-" + kind)
                    if alias.exists():
                        alias.unlink()
                    if kind == "symlink":
                        alias.symlink_to(source)
                    elif kind == "hardlink":
                        alias.hardlink_to(source)
                    else:
                        alias = source
                    before = source.read_bytes()
                    for command in ("build", "check"):
                        result = cli(
                            command,
                            "vscode",
                            "--palette",
                            str(core),
                            "--terminal-palette",
                            str(terminal),
                            "--output",
                            str(alias),
                        )
                        self.assertEqual(result.returncode, 1, result.stderr)
                        self.assertIn("conflicts", result.stderr)
                        self.assertEqual(source.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
