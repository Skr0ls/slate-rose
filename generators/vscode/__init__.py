"""Generate the VS Code editor theme from a validated palette."""

import json

from ..palette import Palette

# TextMate selectors are ordered broad to specific; VS Code resolves specificity.
LEXICAL: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("muted", ("comment",)),
    ("string", ("string",)),
    ("number", ("constant.numeric",)),
    ("keyword", ("keyword", "storage")),
    ("operator", ("keyword.operator",)),
    ("type", ("entity.name.type", "support.type")),
    ("func", ("entity.name.function", "support.function")),
    (
        "variable",
        ("variable.other.readwrite", "entity.name.variable", "variable.other.constant"),
    ),
    ("parameter", ("variable.parameter", "entity.name.variable.parameter")),
    ("fg", ("punctuation",)),
    (
        "constant",
        (
            "variable.other.constant.cs",
            "variable.other.enummember",
            "entity.name.variable.enum-member",
            "constant.other",
        ),
    ),
    (
        "property",
        (
            "entity.name.variable.field",
            "variable.other.property",
            "variable.object.property",
            "variable.other.object.property",
            "variable.other.constant.property",
            "variable.other.constant.object.property",
            "entity.name.variable.property",
        ),
    ),
    (
        "namespace",
        (
            "entity.name.namespace",
            "entity.name.type.namespace",
            "entity.name.type.module",
        ),
    ),
    (
        "attribute",
        (
            "entity.name.function.decorator",
            "entity.other.attribute-name",
            "support.other.attribute",
        ),
    ),
    (
        "primitive",
        (
            "storage.type.primitive",
            "storage.type.built-in.primitive",
            "storage.type.integral",
            "support.type.primitive",
            "source.cs keyword.type",
            "support.type.python",
        ),
    ),
    (
        "control",
        (
            "keyword.control.flow",
            "keyword.control.return",
            "keyword.control.throw",
            "keyword.control.break",
            "keyword.control.continue",
            "keyword.control.yield",
            "keyword.control.co_return",
            "keyword.control.co_await",
            "keyword.control.co_yield",
            "keyword.control.exception.throw",
            "source.js keyword.control.trycatch",
            "source.tsx keyword.control.trycatch",
            "keyword.operator.expression.await.cs",
        ),
    ),
)

SEMANTIC: dict[str, str] = {
    "type": "type",
    "class": "type",
    "enum": "type",
    "struct": "type",
    "typeParameter": "type",
    "interface": "interface",
    "function": "func",
    "method": "func",
    "property": "property",
    "event": "property",
    "namespace": "namespace",
    "parameter": "parameter",
    "variable": "variable",
    "enumMember": "constant",
    "decorator": "attribute",
    "comment": "muted",
    "string": "string",
    "regexp": "string",
    "number": "number",
    "operator": "operator",
}

EDITOR: dict[str, str] = {
    "editor.background": "bg",
    "editor.foreground": "fg",
    "editor.selectionBackground": "selection",
    "editorCursor.foreground": "accent",
    "editorLineNumber.foreground": "muted",
    "editorLineNumber.activeForeground": "fg",
    "editor.lineHighlightBackground": "surface",
    "editor.findMatchBorder": "accent",
    "editorError.foreground": "error",
    "editorWarning.foreground": "warning",
}


def render_theme(palette: Palette) -> str:
    """Render deterministic JSON without touching the filesystem."""
    colors = palette.colors
    theme = {
        "$schema": "vscode://schemas/color-theme",
        "name": palette.name,
        "colors": {key: colors[token] for key, token in EDITOR.items()},
        "tokenColors": [
            {
                "name": role,
                "scope": list(scopes),
                "settings": {"foreground": colors[role]},
            }
            for role, scopes in LEXICAL
        ],
        "semanticHighlighting": True,
        "semanticTokenColors": {key: colors[token] for key, token in SEMANTIC.items()},
    }
    return json.dumps(theme, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
