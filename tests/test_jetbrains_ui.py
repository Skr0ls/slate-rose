import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from generators.jetbrains.ui import render_ui
from generators.palette import load_palette

ROOT = Path(__file__).resolve().parents[1]


class JetBrainsUITests(unittest.TestCase):
    def test_roles_and_metadata(self) -> None:
        palette = load_palette(ROOT / "palette/colors.json")
        rendered = render_ui(palette)
        self.assertEqual(rendered, render_ui(palette))
        theme = json.loads(rendered)
        self.assertEqual(
            (
                theme["name"],
                theme["author"],
                theme["dark"],
                theme["parentTheme"],
                theme["editorScheme"],
            ),
            ("Slate Rose", "Skr0ls", True, "Islands Dark", "/colors/SlateRose.xml"),
        )
        roles = {
            "surface2": "MainWindow.background MainToolbar.background ToolWindow.Stripe.background StatusBar.background EditorTabs.inactiveUnderlinedTabBorderColor",
            "bg": "ToolWindow.background ToolWindow.Header.background ToolWindow.Header.inactiveBackground Island.borderColor EditorTabs.background",
            "surface": "EditorTabs.underlinedTabBackground EditorTabs.inactiveUnderlinedTabBackground",
            "accent": "EditorTabs.underlinedBorderColor",
        }
        expected = {
            key: palette.colors[role]
            for role, keys in roles.items()
            for key in keys.split()
        }
        expected.update(
            {
                key: palette.colors["bg"] + "00"
                for key in (
                    "StatusBar.borderColor",
                    "ToolWindow.Stripe.borderColor",
                    "MainToolbar.borderColor",
                )
            }
        )
        self.assertEqual(theme["ui"], expected)

    def test_cli_build_check_and_invalid_input(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "new" / "theme.json"

            def run(*args: str) -> subprocess.CompletedProcess[bytes]:
                return subprocess.run(
                    [sys.executable, "-m", "generators", *args],
                    cwd=ROOT,
                    capture_output=True,
                )

            self.assertNotEqual(
                run("check", "jetbrains-ui", "--output", str(output)).returncode, 0
            )
            self.assertFalse(output.parent.exists())
            self.assertEqual(
                run("build", "jetbrains-ui", "--output", str(output)).returncode, 0
            )
            first = output.read_bytes()
            self.assertEqual(
                run("build", "jetbrains-ui", "--output", str(output)).returncode, 0
            )
            self.assertEqual(first, output.read_bytes())
            self.assertEqual(
                run("check", "jetbrains-ui", "--output", str(output)).returncode, 0
            )
            output.write_text("stale")
            self.assertNotEqual(
                run("check", "jetbrains-ui", "--output", str(output)).returncode, 0
            )
            self.assertEqual(output.read_text(), "stale")
            palette = Path(tmp) / "palette.json"
            data = json.loads((ROOT / "palette/colors.json").read_text())
            data["name"] = "invalid\u0001"
            palette.write_text(json.dumps(data))
            result = run(
                "build",
                "jetbrains-ui",
                "--palette",
                str(palette),
                "--output",
                str(output),
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertNotIn(b"Valid palette", result.stdout)
            self.assertEqual(output.read_text(), "stale")
            data["name"] = "Slate Rose"
            palette.write_text(json.dumps(data))
            before = palette.read_bytes()
            self.assertNotEqual(
                run(
                    "build",
                    "jetbrains-ui",
                    "--palette",
                    str(palette),
                    "--output",
                    str(palette),
                ).returncode,
                0,
            )
            self.assertEqual(palette.read_bytes(), before)
