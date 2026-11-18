"""Approved Islands shell colors; all other UI values are inherited."""

import json

from ..palette import Palette


def render_ui(palette: Palette) -> str:
    colors = palette.colors
    ui = {
        **dict.fromkeys(
            (
                "MainWindow.background",
                "MainToolbar.background",
                "ToolWindow.Stripe.background",
                "StatusBar.background",
            ),
            colors["surface2"],
        ),
        **dict.fromkeys(
            (
                "ToolWindow.background",
                "ToolWindow.Header.background",
                "ToolWindow.Header.inactiveBackground",
                "Island.borderColor",
                "EditorTabs.background",
            ),
            colors["bg"],
        ),
        **dict.fromkeys(
            (
                "EditorTabs.underlinedTabBackground",
                "EditorTabs.inactiveUnderlinedTabBackground",
            ),
            colors["surface"],
        ),
        "EditorTabs.underlinedBorderColor": colors["accent"],
        "EditorTabs.inactiveUnderlinedTabBorderColor": colors["surface2"],
        **dict.fromkeys(
            (
                "StatusBar.borderColor",
                "ToolWindow.Stripe.borderColor",
                "MainToolbar.borderColor",
            ),
            colors["bg"] + "00",
        ),
    }
    return (
        json.dumps(
            {
                "name": palette.name,
                "author": "Skr0ls",
                "dark": True,
                "parentTheme": "Islands Dark",
                "editorScheme": "/colors/SlateRose.xml",
                "ui": ui,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n"
    )
