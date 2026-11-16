"""Checks for the declarative VS Code package and its archive."""

import json
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

from scripts.check_vsix import PACKAGE, ROOT, VsixError, check_vsix


class VsixTests(unittest.TestCase):
    def test_manifest_is_declarative_and_license_is_synced(self) -> None:
        manifest = json.loads((PACKAGE / "package.json").read_text())
        self.assertEqual(manifest["license"], "MIT")
        for key in ("main", "browser", "activationEvents", "dependencies"):
            self.assertNotIn(key, manifest)
        theme = manifest["contributes"]["themes"]
        self.assertEqual(len(theme), 1)
        self.assertEqual(theme[0]["uiTheme"], "vs-dark")
        self.assertTrue((PACKAGE / theme[0]["path"]).is_file())
        self.assertEqual(
            (PACKAGE / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes()
        )

    def make_archive(
        self,
        path: Path,
        *,
        missing_license: bool = False,
        wrong_theme: bool = False,
        extra: bool = False,
    ) -> None:
        manifest = json.loads((PACKAGE / "package.json").read_text())
        theme = manifest["contributes"]["themes"][0]["path"].removeprefix("./")
        assets = (
            "<PackageManifest><Assets>"
            '<Asset Type="Microsoft.VisualStudio.Services.Content.License" Path="extension/LICENSE.txt" />'
            '<Asset Type="Microsoft.VisualStudio.Services.Content.Details" Path="extension/README.md" />'
            "</Assets></PackageManifest>"
        )
        with ZipFile(path, "w") as archive:
            archive.writestr("[Content_Types].xml", "<Types />")
            archive.writestr("extension.vsixmanifest", assets)
            archive.writestr("extension/package.json", json.dumps(manifest))
            archive.writestr(
                "extension/README.md", (PACKAGE / "README.md").read_bytes()
            )
            archive.writestr(
                "extension/" + theme,
                b"wrong" if wrong_theme else (PACKAGE / theme).read_bytes(),
            )
            if not missing_license:
                archive.writestr(
                    "extension/LICENSE.txt", (ROOT / "LICENSE").read_bytes()
                )
            if extra:
                archive.writestr("extension/index.js", "runtime")

    def test_valid_and_invalid_archives(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.vsix"
            self.make_archive(path)
            check_vsix(path)
            for option in ("missing_license", "wrong_theme", "extra"):
                with self.subTest(option=option):
                    self.make_archive(path, **{option: True})
                    with self.assertRaises(VsixError):
                        check_vsix(path)


if __name__ == "__main__":
    unittest.main()
