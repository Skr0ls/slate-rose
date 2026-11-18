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
        self.assertEqual(manifest["icon"], "icon.png")
        self.assertIn("icon.png", manifest["files"])
        for key in ("main", "browser", "activationEvents", "dependencies"):
            self.assertNotIn(key, manifest)
        theme = manifest["contributes"]["themes"]
        self.assertEqual(len(theme), 1)
        self.assertEqual(theme[0]["uiTheme"], "vs-dark")
        self.assertTrue((PACKAGE / theme[0]["path"]).is_file())
        self.assertEqual(
            (PACKAGE / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes()
        )

    def make_archive(self, path: Path, *, fault: str | None = None) -> None:
        manifest = json.loads((PACKAGE / "package.json").read_text())
        theme = manifest["contributes"]["themes"][0]["path"].removeprefix("./")
        if fault == "wrong_manifest_icon":
            manifest["icon"] = "other.png"
        icon_path = (
            "extension/other.png"
            if fault == "wrong_icon_path"
            else "extension/icon.png"
        )
        icon_asset = ""
        if fault != "missing_icon_asset":
            icon_asset = f'<Asset Type="Microsoft.VisualStudio.Services.Icons.Default" Path="{icon_path}" />'
        vsix_icon = (
            "extension/other.png"
            if fault == "wrong_vsix_icon"
            else "extension/icon.png"
        )
        assets = (
            f"<PackageManifest><Metadata><Icon>{vsix_icon}</Icon></Metadata><Assets>"
            '<Asset Type="Microsoft.VisualStudio.Services.Content.License" Path="extension/LICENSE.txt" />'
            '<Asset Type="Microsoft.VisualStudio.Services.Content.Details" Path="extension/README.md" />'
            + icon_asset
            + "</Assets></PackageManifest>"
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
                b"wrong" if fault == "wrong_theme" else (PACKAGE / theme).read_bytes(),
            )
            if fault != "missing_license":
                archive.writestr(
                    "extension/LICENSE.txt", (ROOT / "LICENSE").read_bytes()
                )
            if fault != "missing_icon":
                archive.writestr(
                    "extension/icon.png",
                    b"wrong"
                    if fault == "wrong_icon"
                    else (PACKAGE / "icon.png").read_bytes(),
                )
            if fault == "extra":
                archive.writestr("extension/index.js", "runtime")

    def test_valid_and_invalid_archives(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.vsix"
            self.make_archive(path)
            check_vsix(path)
            cases = {
                "missing_license": "unexpected or missing archive files",
                "wrong_theme": "archived theme differs",
                "extra": "unexpected or missing archive files",
                "missing_icon": "unexpected or missing archive files",
                "wrong_icon": "archived icon differs",
                "missing_icon_asset": "cannot validate VSIX",
                "wrong_icon_path": "VSIX manifest has incorrect icon path",
                "wrong_manifest_icon": "embedded package.json has incorrect icon",
                "wrong_vsix_icon": "VSIX manifest has incorrect icon",
            }
            for fault, message in cases.items():
                with self.subTest(fault=fault):
                    self.make_archive(path, fault=fault)
                    with self.assertRaisesRegex(VsixError, message):
                        check_vsix(path)


if __name__ == "__main__":
    unittest.main()
