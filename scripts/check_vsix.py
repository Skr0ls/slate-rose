"""Check a locally packaged VS Code extension against its source files."""

from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import BadZipFile, ZipFile

ROOT = Path(__file__).resolve().parent.parent
PACKAGE = ROOT / "packages" / "vscode"


class VsixError(ValueError):
    """An extension archive is missing or contains unexpected content."""


def check_vsix(path: Path) -> None:
    """Raise VsixError when the archive does not match this package."""
    try:
        source = json.loads((PACKAGE / "package.json").read_text(encoding="utf-8"))
        icon = source.get("icon")
        if icon != "icon.png":
            raise VsixError("package.json has incorrect icon")
        expected_icon_path = f"extension/{icon}"
        license_bytes = (ROOT / "LICENSE").read_bytes()
        if (PACKAGE / "LICENSE").read_bytes() != license_bytes:
            raise VsixError("package LICENSE differs from root LICENSE")
        with ZipFile(path) as archive:
            names = {name for name in archive.namelist() if not name.endswith("/")}
            if len(names) != len(
                [n for n in archive.namelist() if not n.endswith("/")]
            ):
                raise VsixError("archive contains duplicate entries")
            manifest = ET.fromstring(archive.read("extension.vsixmanifest"))
            icons = [
                element.text
                for element in manifest.iter()
                if element.tag.rsplit("}", 1)[-1] == "Icon"
            ]
            if icons != [expected_icon_path]:
                raise VsixError("VSIX manifest has incorrect icon")
            assets = {
                element.attrib["Type"]: element.attrib["Path"]
                for element in manifest.iter()
                if element.tag.rsplit("}", 1)[-1] == "Asset"
                and "Type" in element.attrib
                and "Path" in element.attrib
            }
            license_path = assets["Microsoft.VisualStudio.Services.Content.License"]
            readme_path = assets["Microsoft.VisualStudio.Services.Content.Details"]
            icon_path = assets["Microsoft.VisualStudio.Services.Icons.Default"]
            if icon_path != expected_icon_path:
                raise VsixError("VSIX manifest has incorrect icon path")
            embedded = json.loads(archive.read("extension/package.json"))
            for key in (
                "name",
                "publisher",
                "version",
                "license",
                "icon",
                "engines",
                "contributes",
            ):
                if embedded.get(key) != source.get(key):
                    raise VsixError(f"embedded package.json has incorrect {key}")
            theme_path = "extension/" + source["contributes"]["themes"][0][
                "path"
            ].removeprefix("./")
            expected = {
                "[Content_Types].xml",
                "extension.vsixmanifest",
                "extension/package.json",
                theme_path,
                license_path,
                readme_path,
                icon_path,
            }
            if names != expected:
                raise VsixError(
                    f"unexpected or missing archive files: {sorted(names ^ expected)}"
                )
            if archive.read(license_path) != license_bytes:
                raise VsixError("archived license differs from root LICENSE")
            if archive.read(readme_path) != (PACKAGE / "README.md").read_bytes():
                raise VsixError("archived README differs from package README")
            if archive.read(icon_path) != (PACKAGE / icon).read_bytes():
                raise VsixError("archived icon differs from package icon")
            if (
                archive.read(theme_path)
                != (PACKAGE / theme_path.removeprefix("extension/")).read_bytes()
            ):
                raise VsixError("archived theme differs from generated theme")
    except VsixError:
        raise
    except (OSError, BadZipFile, KeyError, ValueError, ET.ParseError, TypeError) as exc:
        raise VsixError(f"cannot validate VSIX {path}: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="VSIX archive to inspect")
    args = parser.parse_args()
    try:
        check_vsix(args.path)
    except VsixError as exc:
        print(f"VSIX check failed: {exc}", file=sys.stderr)
        return 1
    print(f"VSIX check passed: {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
