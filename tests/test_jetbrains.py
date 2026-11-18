import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from xml.etree import ElementTree as ET

from generators.jetbrains import render_scheme
from generators.palette import load_palette

ROOT = Path(__file__).resolve().parents[1]
PALETTE = ROOT / "palette/colors.json"
TERMINAL = ROOT / "palette/terminal.json"
OUTPUT = ROOT / "packages/jetbrains/colors/Slate Rose.icls"


class JetBrainsTests(unittest.TestCase):
    def test_scheme_roles_and_determinism(self) -> None:
        palette = load_palette(PALETTE)
        xml = render_scheme(palette)
        self.assertEqual(xml, render_scheme(palette))
        self.assertTrue(xml.endswith("\n"))
        root = ET.fromstring(xml)
        self.assertEqual(
            root.attrib,
            {"name": "Slate Rose", "version": "142", "parent_scheme": "Darcula"},
        )
        colors = {
            x.get("name"): x.get("value") for x in root.findall("./colors/option")
        }
        self.assertEqual(
            colors,
            {
                "CARET_COLOR": "99C4E6",
                "CARET_ROW_COLOR": "242A34",
                "LINE_NUMBERS_COLOR": "8992A1",
                "GUTTER_BACKGROUND": "191D25",
                "EDITOR_GUTTER_BACKGROUND": "191D25",
                "SELECTION_BACKGROUND": "364455",
            },
        )
        attrs = {
            x.get("name"): {
                v.get("name"): v.get("value") for v in x.findall("./value/option")
            }
            for x in root.findall("./attributes/option")
        }
        roles = {
            "CLASS_NAME": "type",
            "CLASS_REFERENCE": "type",
            "INTERFACE_NAME": "interface",
            "FUNCTION_DECLARATION": "func",
            "FUNCTION_CALL": "func",
            "INSTANCE_METHOD": "func",
            "STATIC_METHOD": "func",
            "INSTANCE_FIELD": "property",
            "STATIC_FIELD": "property",
            "IDENTIFIER": "variable",
            "LOCAL_VARIABLE": "variable",
            "PARAMETER": "parameter",
            "KEYWORD": "keyword",
            "STRING": "string",
            "NUMBER": "number",
            "CONSTANT": "constant",
            "METADATA": "attribute",
            "LINE_COMMENT": "muted",
            "BLOCK_COMMENT": "muted",
            "DOC_COMMENT": "muted",
            "OPERATION_SIGN": "operator",
        }
        expected = {
            f"DEFAULT_{key}": {"FOREGROUND": palette.colors[token][1:]}
            for key, token in roles.items()
        }
        expected["TEXT"] = {"FOREGROUND": "D1D4DC", "BACKGROUND": "191D25"}
        expected["ReSharper.CSHARP_BUILTIN_TYPE_KEYWORD"] = {"FOREGROUND": "D8B981"}
        self.assertEqual(attrs, expected)
        self.assertEqual(set(root.attrib), {"name", "version", "parent_scheme"})
        for value in list(colors.values()) + [
            v for values in attrs.values() for v in values.values()
        ]:
            self.assertRegex(value, r"^[0-9A-F]{6}$")
            self.assertIn("#" + value, palette.colors.values())
        self.assertEqual([child.tag for child in root], ["colors", "attributes"])

    def test_metadata_is_escaped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "palette.json"
            data = json.loads(PALETTE.read_text())
            data["name"] = 'Rose & <"test">'
            path.write_text(json.dumps(data))
            xml = render_scheme(load_palette(path))
            self.assertEqual(ET.fromstring(xml).get("name"), data["name"])
            self.assertIn("&amp;", xml)

    def run_cli(self, *args: str, cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "-m", "generators", *args],
            cwd=cwd,
            env={**os.environ, "PYTHONPATH": str(ROOT)},
            capture_output=True,
            text=True,
        )

    def test_cli_build_check_and_read_only_failures(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output = root / "nested" / "scheme.icls"
            self.assertEqual(
                self.run_cli("check", "jetbrains", "--output", str(output)).returncode,
                1,
            )
            self.assertFalse(output.parent.exists())
            for _ in range(2):
                self.assertEqual(
                    self.run_cli(
                        "build", "jetbrains", "--output", str(output), cwd=root
                    ).returncode,
                    0,
                )
                self.assertEqual(output.read_bytes(), OUTPUT.read_bytes())
            self.assertEqual(self.run_cli("check", "jetbrains", cwd=root).returncode, 0)
            output.write_text("stale")
            self.assertEqual(
                self.run_cli("check", "jetbrains", "--output", str(output)).returncode,
                1,
            )
            self.assertEqual(output.read_text(), "stale")
            invalid = root / "invalid.json"
            invalid.write_text("{}")
            for flag in ("--palette", "--terminal-palette"):
                missing = root / flag[2:] / "out"
                self.assertEqual(
                    self.run_cli(
                        "build",
                        "jetbrains",
                        flag,
                        str(invalid),
                        "--output",
                        str(missing),
                    ).returncode,
                    1,
                )
                self.assertFalse(missing.parent.exists())
                self.assertEqual(
                    self.run_cli(
                        "build",
                        "jetbrains",
                        flag,
                        str(invalid),
                        "--output",
                        str(output),
                    ).returncode,
                    1,
                )
                self.assertEqual(output.read_text(), "stale")

    def test_invalid_xml_names_fail_without_writing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            palette = root / "palette.json"
            existing = root / "existing.icls"
            existing.write_text("unchanged")
            missing = root / "missing" / "scheme.icls"
            data = json.loads(PALETTE.read_text())
            for name in ("Slate\x00Rose", "Slate\ud800Rose"):
                data["name"] = name
                palette.write_text(json.dumps(data))
                for output in (existing, missing):
                    result = self.run_cli(
                        "build",
                        "jetbrains",
                        "--palette",
                        str(palette),
                        "--output",
                        str(output),
                    )
                    self.assertEqual(result.returncode, 1)
                    self.assertIn("palette name is not valid XML text", result.stderr)
                    self.assertNotIn("Traceback", result.stderr)
                self.assertEqual(existing.read_text(), "unchanged")
                self.assertFalse(missing.parent.exists())

    def test_cli_rejects_palette_aliases(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for flag, canonical in (
                ("--palette", PALETTE),
                ("--terminal-palette", TERMINAL),
            ):
                selected = root / canonical.name
                selected.write_bytes(canonical.read_bytes())
                aliases = [selected, canonical]
                for name, link in (("symlink", os.symlink), ("hardlink", os.link)):
                    alias = root / (flag[2:] + name)
                    link(selected, alias)
                    aliases.append(alias)
                for output in aliases:
                    for command in ("build", "check"):
                        result = self.run_cli(
                            command,
                            "jetbrains",
                            flag,
                            str(selected),
                            "--output",
                            str(output),
                        )
                        self.assertEqual(
                            result.returncode, 1, result.stdout + result.stderr
                        )
                self.assertEqual(selected.read_bytes(), canonical.read_bytes())
