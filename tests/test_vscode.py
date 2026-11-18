"""VS Code generation and CLI behavior."""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from generators.palette import load_palette, load_terminal_palette
from generators.vscode import render_theme

ROOT = Path(__file__).resolve().parent.parent
PALETTE = ROOT / "palette/colors.json"
TERMINAL = ROOT / "palette/terminal.json"
ARTIFACT = ROOT / "packages/vscode/themes/slate-rose-color-theme.json"


class ThemeTests(unittest.TestCase):
    def test_rust_primitive_and_semantic_control_scopes(self) -> None:
        palette = load_palette(PALETTE)
        theme = json.loads(render_theme(palette, load_terminal_palette(TERMINAL)))
        scopes = {
            scope: rule["settings"]["foreground"]
            for rule in theme["tokenColors"]
            for scope in rule["scope"]
        }
        for scope in (
            "entity.name.type.primitive.rust",
            "entity.name.type.numeric.rust",
        ):
            self.assertEqual(scopes[scope], palette.colors["primitive"])
        self.assertNotIn("keyword.control.rust", scopes)
        self.assertEqual(scopes["keyword"], palette.colors["keyword"])
        semantic = theme["semanticTokenColors"]
        self.assertEqual(
            semantic["keyword.controlFlow:rust"], palette.colors["control"]
        )
        self.assertEqual(semantic["builtinType:rust"], palette.colors["primitive"])
        self.assertEqual(semantic["type"], palette.colors["type"])
        self.assertNotIn("keyword:rust", semantic)
        self.assertNotIn("keyword", semantic)

    def test_go_lexical_primitive_and_control_scopes(self) -> None:
        palette = load_palette(PALETTE)
        theme = json.loads(render_theme(palette, load_terminal_palette(TERMINAL)))
        scopes = {
            scope: rule["settings"]["foreground"]
            for rule in theme["tokenColors"]
            for scope in rule["scope"]
        }
        for scope in (
            "storage.type.numeric.go",
            "storage.type.string.go",
            "storage.type.boolean.go",
        ):
            self.assertEqual(scopes[scope], palette.colors["primitive"])
        self.assertEqual(scopes["keyword.control.go"], palette.colors["control"])
        self.assertEqual(scopes["keyword"], palette.colors["keyword"])
        self.assertNotIn("keyword.control", scopes)
        self.assertNotIn("keyword.control.import.go", scopes)
        self.assertNotIn("keyword", theme["semanticTokenColors"])

    def test_csharp_semantic_flow_control(self) -> None:
        palette = load_palette(PALETTE)
        theme = json.loads(render_theme(palette, load_terminal_palette(TERMINAL)))
        semantic = theme["semanticTokenColors"]
        self.assertEqual(semantic["controlKeyword:csharp"], palette.colors["control"])
        self.assertNotIn("controlKeyword", semantic)
        self.assertNotIn("keyword", semantic)

    def test_ruby_instance_field_scope(self) -> None:
        palette = load_palette(PALETTE)
        scopes = {
            scope: rule["settings"]["foreground"]
            for rule in json.loads(
                render_theme(palette, load_terminal_palette(TERMINAL))
            )["tokenColors"]
            for scope in rule["scope"]
        }
        self.assertEqual(
            scopes["source.ruby variable.other.readwrite.instance"],
            palette.colors["property"],
        )
        self.assertEqual(scopes["variable.other.readwrite"], palette.colors["fg"])
        self.assertNotIn("variable.other.readwrite.instance", scopes)
        self.assertNotIn("source.ruby variable.other.readwrite.class", scopes)

    def test_cpp_if_and_for_control_scopes(self) -> None:
        palette = load_palette(PALETTE)
        scopes = {
            scope: rule["settings"]["foreground"]
            for rule in json.loads(
                render_theme(palette, load_terminal_palette(TERMINAL))
            )["tokenColors"]
            for scope in rule["scope"]
        }
        for scope in ("keyword.control.if.cpp", "keyword.control.for.cpp"):
            self.assertEqual(scopes[scope], palette.colors["control"])
        self.assertEqual(scopes["keyword"], palette.colors["keyword"])
        self.assertEqual(scopes["storage"], palette.colors["keyword"])
        self.assertNotIn("keyword.control", scopes)

    def test_swift_flow_control_scopes(self) -> None:
        palette = load_palette(PALETTE)
        scopes = {
            scope: rule["settings"]["foreground"]
            for rule in json.loads(
                render_theme(palette, load_terminal_palette(TERMINAL))
            )["tokenColors"]
            for scope in rule["scope"]
        }
        for scope in (
            "keyword.control.branch.swift",
            "keyword.control.exception.swift",
            "keyword.control.transfer.swift",
        ):
            self.assertEqual(scopes[scope], palette.colors["control"])
        for scope in (
            "keyword.other.generic-constraint-introducer.swift",
            "storage.type.enum.case.swift",
            "storage.modifier.exception.swift",
            "keyword.other.operator.type.existential.swift",
            "keyword.other.operator.type.opaque.swift",
        ):
            self.assertNotIn(scope, scopes)

    def test_typescript_flow_control_scopes(self) -> None:
        palette = load_palette(PALETTE)
        theme = json.loads(render_theme(palette, load_terminal_palette(TERMINAL)))
        scopes = {
            scope: rule["settings"]["foreground"]
            for rule in theme["tokenColors"]
            for scope in rule["scope"]
        }
        for scope in (
            "keyword.control.conditional.ts",
            "keyword.control.loop.ts",
            "keyword.control.trycatch.ts",
        ):
            self.assertEqual(scopes[scope], palette.colors["control"])
        self.assertEqual(scopes["keyword"], palette.colors["keyword"])
        self.assertEqual(scopes["storage"], palette.colors["keyword"])
        self.assertNotIn("keyword.control", scopes)
        self.assertNotIn("keyword", theme["semanticTokenColors"])

    def test_web_trycatch_control_scope(self) -> None:
        palette = load_palette(PALETTE)
        scopes = {
            scope: rule["settings"]["foreground"]
            for rule in json.loads(
                render_theme(palette, load_terminal_palette(TERMINAL))
            )["tokenColors"]
            for scope in rule["scope"]
        }
        for scope in (
            "source.js keyword.control.trycatch",
            "source.tsx keyword.control.trycatch",
        ):
            self.assertEqual(scopes[scope], palette.colors["control"])
        self.assertEqual(scopes["keyword"], palette.colors["keyword"])
        self.assertEqual(scopes["storage"], palette.colors["keyword"])
        for scope in (
            "keyword.control.trycatch",
            "source.ts keyword.control.trycatch",
            "source.cs keyword.control.trycatch",
        ):
            self.assertNotIn(scope, scopes)

    def test_workbench_states_and_overlays(self) -> None:
        palette = load_palette(PALETTE)
        colors = json.loads(render_theme(palette, load_terminal_palette(TERMINAL)))[
            "colors"
        ]
        for key, role in {
            "tab.activeBackground": "bg",
            "tab.inactiveBackground": "surface",
            "tab.activeBorderTop": "accent",
            "list.focusOutline": "accent",
            "list.inactiveFocusOutline": "accent",
            "list.hoverBackground": "surface2",
            "disabledForeground": "muted",
            "editorInfo.foreground": "accent",
            "editorHint.foreground": "muted",
            "gitDecoration.modifiedResourceForeground": "func",
            "editorGutter.addedBackground": "string",
            "editorGutter.deletedBackground": "error",
        }.items():
            self.assertEqual(colors[key], palette.colors[role], key)
        overlays = {
            "editor.inactiveSelectionBackground": ("selection", "80"),
            "editor.findMatchBackground": ("accent", "33"),
            "editor.findMatchHighlightBackground": ("accent", "1A"),
            "editor.wordHighlightBackground": ("accent", "1A"),
            "editor.wordHighlightStrongBackground": ("accent", "1A"),
            "terminal.inactiveSelectionBackground": ("selection", "80"),
            "terminal.findMatchBackground": ("accent", "33"),
            "terminal.findMatchHighlightBackground": ("accent", "1A"),
            "scrollbarSlider.background": ("muted", "33"),
            "scrollbarSlider.hoverBackground": ("muted", "55"),
            "scrollbarSlider.activeBackground": ("muted", "77"),
            "diffEditor.insertedTextBackground": ("string", "33"),
            "diffEditor.removedTextBackground": ("error", "33"),
            "diffEditor.insertedLineBackground": ("string", "1A"),
            "diffEditor.removedLineBackground": ("error", "1A"),
        }
        self.assertEqual({k for k, v in colors.items() if len(v) != 7}, set(overlays))
        for key, (role, alpha) in overlays.items():
            self.assertEqual(colors[key], palette.colors[role] + alpha, key)
        self.assertEqual(colors["editor.findMatchBorder"], palette.colors["accent"])
        self.assertNotEqual(
            colors["tab.activeBackground"], colors["tab.inactiveBackground"]
        )
        self.assertNotEqual(
            colors["editor.selectionBackground"],
            colors["editor.inactiveSelectionBackground"],
        )
        self.assertNotEqual(
            colors["scrollbarSlider.background"],
            colors["scrollbarSlider.hoverBackground"],
        )
        self.assertNotEqual(
            colors["scrollbarSlider.hoverBackground"],
            colors["scrollbarSlider.activeBackground"],
        )

    def test_modern_shell_and_title_bar_colors(self) -> None:
        palette = load_palette(PALETTE)
        colors = json.loads(render_theme(palette, load_terminal_palette(TERMINAL)))[
            "colors"
        ]
        for key, role in {
            "modernUI.shellBackground": "bg",
            "modernUI.inactiveShellBackground": "bg",
            "titleBar.activeBackground": "bg",
            "titleBar.inactiveBackground": "bg",
            "titleBar.border": "bg",
            "titleBar.activeForeground": "fg",
            "titleBar.inactiveForeground": "muted",
            "surface.background": "surface",
            "surface.foreground": "fg",
            "surface.border": "surface2",
            "editor.border": "surface2",
            "modernPanel.border": "surface2",
            "modernActivityBar.border": "surface2",
        }.items():
            self.assertEqual(colors[key], palette.colors[role], key)

    def test_roles_and_shape(self) -> None:
        palette = load_palette(PALETTE)
        theme = json.loads(render_theme(palette, load_terminal_palette(TERMINAL)))
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
            [value for value in theme["colors"].values() if len(value) == 7]
            + list(semantic.values())
            + list(scopes.values())
        )
        self.assertTrue(
            set(values)
            <= set(palette.colors.values())
            | set(load_terminal_palette(TERMINAL).colors.values())
        )
        self.assertEqual(
            render_theme(palette, load_terminal_palette(TERMINAL)),
            render_theme(palette, load_terminal_palette(TERMINAL)),
        )
        self.assertEqual(
            ARTIFACT.read_bytes(),
            render_theme(palette, load_terminal_palette(TERMINAL)).encode(),
        )


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
