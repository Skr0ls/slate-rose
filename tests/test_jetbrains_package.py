import io
import shutil
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

from scripts.package_jetbrains import build_archive

ROOT = Path(__file__).resolve().parents[1]
INPUTS = (
    "palette/colors.json",
    "palette/terminal.json",
    "packages/jetbrains/META-INF/plugin.xml",
    "packages/jetbrains/META-INF/pluginIcon.svg",
    "packages/jetbrains/resources/Slate Rose.theme.json",
    "packages/jetbrains/colors/Slate Rose.icls",
    "LICENSE",
)


class JetBrainsPackageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in INPUTS:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)
        self.output = self.root / "out" / "theme.jar"

    def test_archive_contents_and_metadata(self) -> None:
        data = build_archive(self.root, self.output)
        self.assertEqual(data, build_archive(self.root, self.output))
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            expected = {
                "META-INF/plugin.xml": INPUTS[2],
                "META-INF/pluginIcon.svg": INPUTS[3],
                "Slate Rose.theme.json": INPUTS[4],
                "colors/SlateRose.xml": INPUTS[5],
                "META-INF/LICENSE": "LICENSE",
            }
            self.assertEqual(archive.namelist(), list(expected))
            self.assertTrue(
                ET.fromstring(archive.read("META-INF/plugin.xml"))
                .findtext("description")
                .strip()
            )
            for info in archive.infolist():
                self.assertEqual(
                    archive.read(info),
                    (self.root / expected[info.filename]).read_bytes(),
                )
                self.assertEqual(
                    (info.compress_type, info.date_time, info.external_attr >> 16),
                    (zipfile.ZIP_STORED, (1980, 1, 1, 0, 0, 0), 0o100644),
                )

    def test_invalid_sources_and_aliases_fail_before_output(self) -> None:
        for name in INPUTS:
            source = self.root / name
            for alias in (source, self.root / "link", self.root / "hardlink"):
                if alias.name == "link":
                    alias.symlink_to(source)
                elif alias.name == "hardlink":
                    alias.hardlink_to(source)
                with self.assertRaises(ValueError):
                    build_archive(self.root, alias)
                if alias != source:
                    alias.unlink()
        self.assertFalse(self.output.parent.exists())
        for name, content in ((INPUTS[4], b"stale"), (INPUTS[2], b"<idea-plugin/>")):
            path = self.root / name
            original = path.read_bytes()
            path.write_bytes(content)
            with self.assertRaises(ValueError):
                build_archive(self.root, self.output)
            self.assertFalse(self.output.parent.exists())
            path.write_bytes(original)
        descriptor = self.root / INPUTS[2]
        original = descriptor.read_bytes()
        for tag in ("description", "change-notes"):
            with self.subTest(tag=tag):
                xml = ET.fromstring(original)
                xml.find(tag).text = "  "
                descriptor.write_bytes(ET.tostring(xml))
                with self.assertRaises(ValueError):
                    build_archive(self.root, self.output)
                self.assertFalse(self.output.parent.exists())

    def test_invalid_or_missing_icon_fails(self) -> None:
        icon = self.root / INPUTS[3]
        original = icon.read_bytes()
        for content in (
            b"<svg",
            b'<svg xmlns="http://www.w3.org/2000/svg" width="41" height="40" viewBox="0 0 40 40"/>',
            b'<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 20 20"/>',
            b'<other xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 40 40"/>',
        ):
            with self.subTest(content=content):
                icon.write_bytes(content)
                with self.assertRaisesRegex(ValueError, "invalid plugin icon"):
                    build_archive(self.root, self.output)
        icon.unlink()
        with self.assertRaises(FileNotFoundError):
            build_archive(self.root, self.output)
        self.assertFalse(self.output.parent.exists())
        icon.write_bytes(original)

    def test_cli_check_is_read_only(self) -> None:
        def run(*args: str) -> subprocess.CompletedProcess[bytes]:
            return subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "scripts.package_jetbrains",
                    str(self.output),
                    *args,
                ],
                cwd=ROOT,
                capture_output=True,
            )

        self.assertNotEqual(run("--check").returncode, 0)
        self.assertFalse(self.output.parent.exists())
        self.assertEqual(run().returncode, 0)
        data = self.output.read_bytes()
        self.assertEqual(run().returncode, 0)
        self.assertEqual(data, self.output.read_bytes())
        self.assertEqual(run("--check").returncode, 0)
        self.output.write_bytes(b"corrupt")
        self.assertNotEqual(run("--check").returncode, 0)
        self.assertEqual(self.output.read_bytes(), b"corrupt")
