import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from generators.palette import PaletteValidationError, load_palette

ROOT = Path(__file__).resolve().parent.parent
CANONICAL = ROOT / "palette" / "colors.json"


class PaletteTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "palette.json"
        self.data = json.loads(CANONICAL.read_text(encoding="utf-8"))

    def write_data(self) -> None:
        self.path.write_text(json.dumps(self.data), encoding="utf-8")

    def assert_invalid(self, message: str) -> None:
        self.write_data()
        with self.assertRaisesRegex(PaletteValidationError, message):
            load_palette(self.path)

    def test_canonical_read_only_and_immutable(self) -> None:
        before = CANONICAL.read_bytes()
        palette = load_palette(CANONICAL)
        load_palette(CANONICAL)
        self.assertEqual(CANONICAL.read_bytes(), before)
        self.assertEqual(
            (palette.name, palette.version, len(palette.colors)),
            ("Slate Rose", "0.2", 24),
        )
        with self.assertRaises(TypeError):
            palette.colors["bg"] = "#FFFFFF"  # type: ignore[index]

    def test_hex_case_preserved(self) -> None:
        self.data["colors"]["bg"] = "#aBcDeF"
        self.write_data()
        self.assertEqual(load_palette(self.path).colors["bg"], "#aBcDeF")

    def test_tokens(self) -> None:
        del self.data["colors"]["bg"]
        self.assert_invalid("Missing color tokens: bg")
        self.data["colors"]["bg"] = "#abcdef"
        self.data["colors"]["unexpected"] = "#abcdef"
        self.assert_invalid("Unknown color tokens: unexpected")

    def test_duplicates_at_any_level(self) -> None:
        for raw, key in [
            (' {"name": 1, "name": 2}', "name"),
            ('{"colors": {"bg": 1, "bg": 2}}', "bg"),
        ]:
            with self.subTest(key=key):
                self.path.write_text(raw, encoding="utf-8")
                with self.assertRaisesRegex(
                    PaletteValidationError, f"Duplicate JSON key: '{key}'"
                ):
                    load_palette(self.path)

    def test_root_and_colors_types(self) -> None:
        self.data = []
        self.assert_invalid("root must be an object")
        self.data = json.loads(CANONICAL.read_text(encoding="utf-8"))
        self.data["colors"] = []
        self.assert_invalid("colors must be an object")

    def test_metadata_and_root_fields(self) -> None:
        for field in ("name", "version"):
            original = self.data[field]
            for value in ("", "  ", 5, None):
                with self.subTest(field=field, value=value):
                    self.data[field] = value
                    self.assert_invalid(f"{field} must be a nonempty string")
            del self.data[field]
            self.assert_invalid(f"Missing palette fields: {field}")
            self.data[field] = original
        self.data["extra"] = 1
        self.assert_invalid("Unknown palette fields: extra")

    def test_bad_hex(self) -> None:
        for value in (
            None,
            123,
            "#abc",
            "#abcdef00",
            "abcdef",
            "#abcdeg",
            "#abcdef\n",
            " #abcdef",
        ):
            with self.subTest(value=value):
                self.data["colors"]["bg"] = value
                self.assert_invalid("Color token 'bg'")

    def test_read_errors_and_malformed_json(self) -> None:
        for path in (self.path, Path(self.temp.name)):
            with (
                self.subTest(path=path),
                self.assertRaisesRegex(PaletteValidationError, "Cannot read palette"),
            ):
                load_palette(path)
        self.path.write_bytes(b"\xff")
        with self.assertRaisesRegex(PaletteValidationError, "Cannot read palette"):
            load_palette(self.path)
        self.path.write_text('{\n  "name": }', encoding="utf-8")
        with self.assertRaisesRegex(PaletteValidationError, "line 2, column"):
            load_palette(self.path)

    def cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        env = dict(os.environ, PYTHONPATH=str(ROOT))
        return subprocess.run(
            [sys.executable, "-m", "generators", *args],
            cwd=self.temp.name,
            env=env,
            text=True,
            capture_output=True,
        )

    def test_cli(self) -> None:
        for args in (("validate",), ("validate", str(CANONICAL))):
            with self.subTest(args=args):
                result = self.cli(*args)
                self.assertEqual(result.returncode, 0)
                self.assertIn("Slate Rose (version 0.2, 24 tokens)", result.stdout)
                self.assertEqual(result.stderr, "")
        result = self.cli("validate", str(self.path))
        self.assertEqual(result.returncode, 1)
        self.assertIn("Cannot read palette", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        result = self.cli("validate", "one", "two")
        self.assertEqual(result.returncode, 2)
        self.assertIn("usage:", result.stderr)

    def test_cli_invalid_content_is_read_only(self) -> None:
        invalid_hex = json.loads(CANONICAL.read_text(encoding="utf-8"))
        invalid_hex["colors"]["bg"] = "#bad"
        cases = (
            ('{"name": }', "Invalid JSON"),
            (json.dumps(invalid_hex), "Color token 'bg'"),
            ('{"name": "one", "name": "two"}', "Duplicate JSON key: 'name'"),
        )
        for content, expected in cases:
            with self.subTest(expected=expected):
                self.path.write_text(content, encoding="utf-8")
                before = self.path.read_bytes()
                result = self.cli("validate", str(self.path))
                self.assertEqual(result.returncode, 1)
                self.assertIn(expected, result.stderr)
                self.assertEqual(result.stdout, "")
                self.assertNotIn("Traceback", result.stderr)
                self.assertEqual(self.path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
