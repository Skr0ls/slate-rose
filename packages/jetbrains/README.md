# JetBrains theme

The Islands Dark shell slice covers framing, panels and tabs. Menus and controls
inherit the host; a [bounded Rider shell review](../../previews/jetbrains/islands/README.md)
is recorded. Generate and check it with
`python -m generators build jetbrains-ui` and `python -m generators check jetbrains-ui`.

Download `slate-rose-jetbrains.jar` from the release bundle. For a local
build, run `python -m scripts.package_jetbrains` and verify with
`python -m scripts.package_jetbrains --check`. In Rider, use
**Settings | Plugins | gear | Install Plugin from Disk**, select
`slate-rose-jetbrains.jar` (under `dist/` for a local build), restart if prompted, then select Slate Rose in
**Settings | Appearance & Behavior | Appearance**. The descriptor requires
platform build 262 or newer; compatibility with other IDEs has not been reviewed.
See [Rider plugin installation](https://www.jetbrains.com/help/rider/Managing_Plugins.html).

See the [Marketplace submission guide](marketplace.md) for listing details.

Generate the scheme with `python -m generators build jetbrains`. In a JetBrains
IDE, open **Settings | Editor | Color Scheme**, use the scheme menu to import
`colors/Slate Rose.icls`, then select Slate Rose. See the [official import
instructions](https://www.jetbrains.com/help/idea/settings-colors-and-fonts.html).

This initial scheme has automated XML checks and a bounded [native C#/Java review](../../previews/jetbrains/editor/README.md)
in Rider and IntelliJ IDEA. Language plugins may override shared defaults. Flow
control and namespaces have no separate override mapped here. The Rider C# key
`ReSharper.CSHARP_BUILTIN_TYPE_KEYWORD` maps builtin aliases to the approved
primitive color; a bounded [native Rider review](../../previews/jetbrains/csharp-builtins/README.md)
records its observed behavior. Other
languages' primitive mappings are unchanged;
unmapped styles and states inherit Darcula. Font settings, IDE UI and terminal
colors are outside this scheme. Broader IDE validation, language mapping fixes
and terminal support remain follow-ups.

The scheme follows the [official format example](https://blog.jetbrains.com/platform/2017/12/export-intellij-editor-themes-as-plugins/),
[scheme version](https://github.com/JetBrains/intellij-community/blob/master/platform/editor-ui-ex/src/com/intellij/openapi/editor/colors/impl/AbstractColorsScheme.java),
[text attribute](https://github.com/JetBrains/intellij-community/blob/master/platform/core-api/src/com/intellij/openapi/editor/HighlighterColors.java),
[language defaults](https://github.com/JetBrains/intellij-community/blob/master/platform/core-api/src/com/intellij/openapi/editor/DefaultLanguageHighlighterColors.java),
and [editor color keys](https://github.com/JetBrains/intellij-community/blob/master/platform/editor-ui-api/src/com/intellij/openapi/editor/colors/EditorColors.java).
