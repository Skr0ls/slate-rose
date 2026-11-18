"""Checks for the Zed theme and extension package."""

import json
import subprocess
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

from generators.palette import load_palette
from generators.zed import EDITOR, SYNTAX, render_theme

ROOT = Path(__file__).resolve().parent.parent


class ZedThemeTests(unittest.TestCase):
    def test_theme_shape_mappings_and_determinism(self) -> None:
        palette = load_palette(ROOT / "palette/colors.json")
        rendered = render_theme(palette)
        self.assertEqual(rendered, render_theme(palette))
        self.assertEqual(
            rendered, (ROOT / "packages/zed/themes/slate-rose.json").read_text()
        )
        theme = json.loads(rendered)
        self.assertEqual(theme["$schema"], "https://zed.dev/schema/themes/v0.2.0.json")
        self.assertEqual((theme["name"], theme["author"]), (palette.name, "Skr0ls"))
        self.assertEqual(len(theme["themes"]), 1)
        variant = theme["themes"][0]
        self.assertEqual(
            (variant["name"], variant["appearance"]), (palette.name, "dark")
        )
        style = variant["style"]
        self.assertEqual(style["editor.background"], palette.colors["bg"])
        self.assertEqual(
            style["syntax"]["type.builtin"], {"color": palette.colors["primitive"]}
        )
        self.assertEqual(
            style["syntax"]["keyword"], {"color": palette.colors["keyword"]}
        )
        self.assertTrue(
            all(key.startswith("editor.") for key in style if key != "syntax")
        )
        self.assertEqual(
            style,
            {
                **{key: palette.colors[token] for key, token in EDITOR.items()},
                "syntax": {
                    key: {"color": palette.colors[token]}
                    for key, token in SYNTAX.items()
                },
            },
        )

    def test_package_metadata_and_license(self) -> None:
        package = ROOT / "packages/zed"
        manifest = tomllib.loads((package / "extension.toml").read_text())
        self.assertEqual(manifest["id"], "slate-rose-theme")
        self.assertEqual(manifest["version"], "0.1.0")
        self.assertEqual(manifest["schema_version"], 1)
        self.assertEqual(manifest["authors"], ["Skr0ls"])
        self.assertEqual(manifest["repository"], "https://github.com/Skr0ls/slate-rose")
        self.assertEqual(
            (package / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes()
        )

    def test_cli_build_check_missing_and_stale(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "theme.json"

            def run(command: str) -> subprocess.CompletedProcess[str]:
                return subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "generators",
                        command,
                        "zed",
                        "--output",
                        str(output),
                    ],
                    cwd=ROOT,
                    capture_output=True,
                    text=True,
                    check=False,
                )

            self.assertNotEqual(run("check").returncode, 0)
            self.assertEqual(run("build").returncode, 0)
            self.assertEqual(run("check").returncode, 0)
            output.write_text("stale")
            result = run("check")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("stale", result.stderr)


if __name__ == "__main__":
    unittest.main()
