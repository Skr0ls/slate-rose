"""Render the Zed editor theme from the validated palette."""

import json

from ..palette import Palette

EDITOR = {
    "editor.background": "bg",
    "editor.foreground": "fg",
    "editor.gutter.background": "bg",
    "editor.line_number": "muted",
    "editor.active_line_number": "fg",
    "editor.active_line.background": "surface",
}
SYNTAX = {
    "attribute": "attribute",
    "comment": "muted",
    "comment.doc": "muted",
    "constant": "constant",
    "constructor": "func",
    "function": "func",
    "keyword": "keyword",
    "number": "number",
    "operator": "operator",
    "property": "property",
    "punctuation": "fg",
    "string": "string",
    "type": "type",
    "type.builtin": "primitive",
    "variable": "variable",
    "variable.parameter": "parameter",
}


def render_theme(palette: Palette) -> str:
    """Render deterministic JSON without touching the filesystem."""
    colors = palette.colors
    theme = {
        "$schema": "https://zed.dev/schema/themes/v0.2.0.json",
        "name": palette.name,
        "author": "Skr0ls",
        "themes": [
            {
                "name": palette.name,
                "appearance": "dark",
                "style": {
                    **{key: colors[token] for key, token in EDITOR.items()},
                    "syntax": {
                        key: {"color": colors[token]} for key, token in SYNTAX.items()
                    },
                },
            }
        ],
    }
    return json.dumps(theme, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
