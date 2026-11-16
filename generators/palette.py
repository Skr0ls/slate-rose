"""Load the approved palette schema without modifying its source."""

import json
import re
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType


class PaletteValidationError(ValueError):
    """A palette could not be read or does not match the supported schema."""


@dataclass(frozen=True)
class Palette:
    name: str
    version: str
    colors: Mapping[str, str]


_TOKENS = frozenset(
    {
        "bg",
        "surface",
        "surface2",
        "fg",
        "muted",
        "type",
        "primitive",
        "func",
        "property",
        "keyword",
        "control",
        "string",
        "number",
        "namespace",
        "parameter",
        "variable",
        "constant",
        "interface",
        "attribute",
        "operator",
        "error",
        "warning",
        "selection",
        "accent",
    }
)
_HEX = re.compile(r"#[0-9a-fA-F]{6}")


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise PaletteValidationError(f"Duplicate JSON key: {key!r}")
        result[key] = value
    return result


def load_palette(path: Path) -> Palette:
    """Read and validate a palette, preserving all supplied values unchanged."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise PaletteValidationError(f"Cannot read palette {path}: {exc}") from exc
    try:
        data = json.loads(text, object_pairs_hook=_unique_object)
    except json.JSONDecodeError as exc:
        raise PaletteValidationError(
            f"Invalid JSON in {path} at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc
    if not isinstance(data, dict):
        raise PaletteValidationError("Palette root must be an object")
    required = {"name", "version", "colors"}
    missing = required - data.keys()
    unknown = data.keys() - required
    if missing:
        raise PaletteValidationError(
            f"Missing palette fields: {', '.join(sorted(missing))}"
        )
    if unknown:
        raise PaletteValidationError(
            f"Unknown palette fields: {', '.join(sorted(unknown))}"
        )
    for field in ("name", "version"):
        if not isinstance(data[field], str) or not data[field].strip():
            raise PaletteValidationError(f"Palette {field} must be a nonempty string")
    colors = data["colors"]
    if not isinstance(colors, dict):
        raise PaletteValidationError("Palette colors must be an object")
    missing_tokens = _TOKENS - colors.keys()
    unknown_tokens = colors.keys() - _TOKENS
    if missing_tokens:
        raise PaletteValidationError(
            f"Missing color tokens: {', '.join(sorted(missing_tokens))}"
        )
    if unknown_tokens:
        raise PaletteValidationError(
            f"Unknown color tokens: {', '.join(sorted(unknown_tokens))}"
        )
    validated: dict[str, str] = {}
    for token, value in colors.items():
        if not isinstance(value, str) or _HEX.fullmatch(value) is None:
            raise PaletteValidationError(
                f"Color token {token!r} must be a six-digit #RRGGBB hex string"
            )
        validated[token] = value
    return Palette(data["name"], data["version"], MappingProxyType(validated))
