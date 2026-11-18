"""Tests for the reproducible Zed release archive."""

import os
import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.package_zed import package


class PackageZedTests(unittest.TestCase):
    def test_archive_contents_and_reproducibility(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            names = ["LICENSE", "README.md", "extension.toml", "themes/slate-rose.json"]
            for name in names:
                path = source / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(name.encode())
            (source / "extra.txt").write_bytes(b"outside the package")
            output = root / "release" / "zed.zip"
            package(source, output)
            original = output.read_bytes()
            with self.assertRaisesRegex(ValueError, "refers to a Zed package input"):
                package(source, source / "extension.toml")
            self.assertEqual(
                (source / "extension.toml").read_bytes(), b"extension.toml"
            )
            with zipfile.ZipFile(output) as archive:
                self.assertEqual(archive.namelist(), names)
                for name in names:
                    self.assertEqual(archive.read(name), name.encode())
                    self.assertEqual(
                        archive.getinfo(name).compress_type, zipfile.ZIP_STORED
                    )
                    os.utime(source / name, (1_700_000_000, 1_700_000_000))
            package(source, output)
            self.assertEqual(output.read_bytes(), original)

    def test_missing_member_preserves_existing_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "zed.zip"
            output.write_bytes(b"existing")
            with self.assertRaises(FileNotFoundError):
                package(root / "missing", output)
            self.assertEqual(output.read_bytes(), b"existing")


if __name__ == "__main__":
    unittest.main()
