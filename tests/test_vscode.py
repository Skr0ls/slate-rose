"""VS Code generation and CLI behavior."""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from generators.palette import load_palette
from generators.vscode import render_theme

ROOT = Path(__file__).resolve().parent.parent
PALETTE = ROOT / "palette/colors.json"
ARTIFACT = ROOT / "packages/vscode/themes/slate-rose-color-theme.json"


class ThemeTests(unittest.TestCase):
    def test_roles_and_shape(self) -> None:
        palette = load_palette(PALETTE)
        theme = json.loads(render_theme(palette))
        self.assertEqual(
            set(theme),
            {
                "$schema",
                "name",
                "colors",
                "tokenColors",
                "semanticHighlighting",
                "semanticTokenColors",
            },
        )
        self.assertTrue(theme["semanticHighlighting"])
        semantic = theme["semanticTokenColors"]
        for name, role in {
            "class": "type",
            "function": "func",
            "property": "property",
            "decorator": "attribute",
            "variable": "variable",
        }.items():
            self.assertEqual(semantic[name], palette.colors[role])
        self.assertNotIn("type.defaultLibrary", semantic)
        self.assertNotIn("property.readonly", semantic)
        self.assertNotIn("keyword", semantic)
        scopes = {
            scope: item["settings"]["foreground"]
            for item in theme["tokenColors"]
            for scope in item["scope"]
        }
        for scope, role in {
            "source.cs keyword.type": "primitive",
            "storage": "keyword",
            "keyword.control.flow": "control",
            "variable.other.constant.property": "property",
            "variable.other.constant.object.property": "property",
            "entity.name.function.decorator": "attribute",
            "entity.name.variable.field": "property",
            "entity.name.variable.parameter": "parameter",
            "entity.name.variable.enum-member": "constant",
            "entity.name.variable": "variable",
            "variable.other.constant": "variable",
            "variable.other.constant.cs": "constant",
        }.items():
            self.assertEqual(scopes[scope], palette.colors[role])
        # These assertions cover the relevant selectors, not VS Code rendering.
        self.assertNotIn("variable.other.constant.object", scopes)
        self.assertNotIn("storage.type", scopes)
        self.assertNotIn("keyword.control", scopes)
        values = (
            list(theme["colors"].values())
            + list(semantic.values())
            + list(scopes.values())
        )
        self.assertTrue(set(values) <= set(palette.colors.values()))
        self.assertEqual(render_theme(palette), render_theme(palette))
        self.assertEqual(ARTIFACT.read_bytes(), render_theme(palette).encode())


class CliTests(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "-m", "generators", *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_build_check_and_failures(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output = root / "nested/theme.json"
            args = ("--output", str(output))
            self.assertEqual(self.run_cli("build", "vscode", *args).returncode, 0)
            data = output.read_bytes()
            json.loads(data)
            self.assertEqual(self.run_cli("build", "vscode", *args).returncode, 0)
            self.assertEqual(data, output.read_bytes())
            stat = output.stat().st_mtime_ns
            self.assertEqual(self.run_cli("check", "vscode", *args).returncode, 0)
            self.assertEqual(
                (data, stat), (output.read_bytes(), output.stat().st_mtime_ns)
            )
            output.write_bytes(b"stale")
            stat = output.stat().st_mtime_ns
            result = self.run_cli("check", "vscode", *args)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(
                (b"stale", stat), (output.read_bytes(), output.stat().st_mtime_ns)
            )
            missing = root / "missing/theme.json"
            result = self.run_cli("check", "vscode", "--output", str(missing))
            self.assertEqual(result.returncode, 1)
            self.assertFalse(missing.parent.exists())
            invalid = root / "invalid.json"
            invalid.write_text("{}")
            for target in (output, missing):
                result = self.run_cli(
                    "build",
                    "vscode",
                    "--palette",
                    str(invalid),
                    "--output",
                    str(target),
                )
                self.assertEqual(result.returncode, 1)
                self.assertNotIn("Traceback", result.stderr)
            self.assertEqual(output.read_bytes(), b"stale")
            self.assertFalse(missing.parent.exists())

    def test_palette_collisions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            palette = root / "palette.json"
            palette.write_bytes(PALETTE.read_bytes())
            aliases = [palette, PALETTE]
            for name, link in (("symlink", os.symlink), ("hardlink", os.link)):
                alias = root / name
                try:
                    link(palette, alias)
                except OSError:
                    continue
                aliases.append(alias)
            for output in aliases:
                result = self.run_cli(
                    "build",
                    "vscode",
                    "--palette",
                    str(palette),
                    "--output",
                    str(output),
                )
                self.assertEqual(result.returncode, 1)
                self.assertNotIn("Traceback", result.stderr)
            self.assertEqual(palette.read_bytes(), PALETTE.read_bytes())


if __name__ == "__main__":
    unittest.main()
