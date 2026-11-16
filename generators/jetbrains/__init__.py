"""Render the shared JetBrains editor color scheme."""

from xml.etree import ElementTree as ET

from ..palette import Palette, PaletteValidationError

ATTRIBUTES = {
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
COLORS = {
    "CARET_COLOR": "accent",
    "CARET_ROW_COLOR": "surface",
    "LINE_NUMBERS_COLOR": "muted",
    "GUTTER_BACKGROUND": "bg",
    "EDITOR_GUTTER_BACKGROUND": "bg",
    "SELECTION_BACKGROUND": "selection",
}


def render_scheme(palette: Palette) -> str:
    """Render deterministic XML without touching the filesystem."""
    scheme = ET.Element(
        "scheme", name=palette.name, version="142", parent_scheme="Darcula"
    )
    colors = ET.SubElement(scheme, "colors")
    for key, token in COLORS.items():
        ET.SubElement(
            colors, "option", name=key, value=palette.colors[token][1:].upper()
        )
    attributes = ET.SubElement(scheme, "attributes")
    text = ET.SubElement(ET.SubElement(attributes, "option", name="TEXT"), "value")
    for key, token in (("FOREGROUND", "fg"), ("BACKGROUND", "bg")):
        ET.SubElement(text, "option", name=key, value=palette.colors[token][1:].upper())
    for key, token in ATTRIBUTES.items():
        value = ET.SubElement(
            ET.SubElement(attributes, "option", name=f"DEFAULT_{key}"), "value"
        )
        ET.SubElement(
            value, "option", name="FOREGROUND", value=palette.colors[token][1:].upper()
        )
    ET.indent(scheme, space="  ")
    xml = ET.tostring(scheme, encoding="unicode", short_empty_elements=True) + "\n"
    try:
        ET.fromstring(xml.encode("utf-8"))
    except (ET.ParseError, UnicodeEncodeError) as exc:
        raise PaletteValidationError("palette name is not valid XML text") from exc
    return xml
