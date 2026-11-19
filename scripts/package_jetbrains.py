"""Build or check a reproducible, resource-only JetBrains theme JAR."""

import argparse
import io
import sys
import uuid
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

from generators.__main__ import _same_file
from generators.jetbrains import render_scheme
from generators.jetbrains.ui import render_ui
from generators.palette import (
    PaletteValidationError,
    load_palette,
    load_terminal_palette,
)

ROOT = Path(__file__).resolve().parents[1]


def build_archive(root: Path, output: Path) -> bytes:
    palette_path = root / "palette/colors.json"
    terminal_path = root / "palette/terminal.json"
    descriptor_path = root / "packages/jetbrains/META-INF/plugin.xml"
    icon_path = root / "packages/jetbrains/META-INF/pluginIcon.svg"
    theme_path = root / "packages/jetbrains/resources/Slate Rose.theme.json"
    scheme_path = root / "packages/jetbrains/colors/Slate Rose.icls"
    license_path = root / "LICENSE"
    inputs = (
        palette_path,
        terminal_path,
        descriptor_path,
        icon_path,
        theme_path,
        scheme_path,
        license_path,
    )
    if any(_same_file(output, path) for path in inputs):
        raise ValueError("output conflicts with an input")
    palette = load_palette(palette_path)
    load_terminal_palette(terminal_path)
    scheme = render_scheme(palette).encode("utf-8")
    theme = render_ui(palette).encode("utf-8")
    if scheme_path.read_bytes() != scheme or theme_path.read_bytes() != theme:
        raise ValueError("generated JetBrains resources are stale")
    descriptor = descriptor_path.read_bytes()
    try:
        xml = ET.fromstring(descriptor)
        provider = xml.find("./extensions/themeProvider")
        if (
            xml.tag != "idea-plugin"
            or [child.tag for child in xml]
            != [
                "id",
                "name",
                "version",
                "vendor",
                "description",
                "change-notes",
                "idea-version",
                "depends",
                "extensions",
            ]
            or xml.findtext("id") != "com.github.skr0ls.slaterose"
            or xml.findtext("name") != "Slate Rose"
            or xml.findtext("version") != "0.1.1"
            or xml.findtext("vendor") != "Skr0ls"
            or not (xml.findtext("description") or "").strip()
            or not (xml.findtext("change-notes") or "").strip()
            or xml.find("idea-version").attrib != {"since-build": "262"}
            or [e.text for e in xml.findall("depends")] != ["com.intellij.modules.lang"]
            or len(xml.findall("extensions")) != 1
            or xml.find("extensions").attrib != {"defaultExtensionNs": "com.intellij"}
            or len(xml.findall("./extensions/*")) != 1
            or provider is None
            or set(provider.attrib) != {"id", "path"}
            or provider.attrib["path"] != "/Slate Rose.theme.json"
            or uuid.UUID(provider.attrib["id"]).version != 4
        ):
            raise ValueError("invalid plugin descriptor")
    except (ET.ParseError, AttributeError, KeyError, ValueError) as exc:
        raise ValueError("invalid plugin descriptor") from exc
    icon = icon_path.read_bytes()
    try:
        svg = ET.fromstring(icon)
        if (
            svg.tag != "{http://www.w3.org/2000/svg}svg"
            or svg.get("width") != "40"
            or svg.get("height") != "40"
            or svg.get("viewBox") != "0 0 40 40"
        ):
            raise ValueError("invalid plugin icon")
    except ET.ParseError as exc:
        raise ValueError("invalid plugin icon") from exc
    entries = (
        ("META-INF/plugin.xml", descriptor),
        ("META-INF/pluginIcon.svg", icon),
        ("Slate Rose.theme.json", theme),
        ("colors/SlateRose.xml", scheme),
        ("META-INF/LICENSE", license_path.read_bytes()),
    )
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, data in entries:
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    return buffer.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "output", nargs="?", type=Path, default=ROOT / "dist/slate-rose-jetbrains.jar"
    )
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        expected = build_archive(ROOT, args.output)
        if args.check:
            if args.output.read_bytes() != expected:
                raise ValueError("package is stale or modified")
            print(f"Package is current: {args.output}")
        else:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_bytes(expected)
            print(f"Package built: {args.output}")
    except (OSError, ValueError, PaletteValidationError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
