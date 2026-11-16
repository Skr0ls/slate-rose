# JetBrains editor scheme

Generate the scheme with `python -m generators build jetbrains`. In a JetBrains
IDE, open **Settings | Editor | Color Scheme**, use the scheme menu to import
`colors/Slate Rose.icls`, then select Slate Rose. See the [official import
instructions](https://www.jetbrains.com/help/idea/settings-colors-and-fonts.html).

This initial scheme has automated XML checks and a bounded [native C#/Java review](../../previews/jetbrains/editor/README.md)
in Rider and IntelliJ IDEA. Language plugins may override shared defaults. Flow
control, primitives and namespaces have no separate override mapped here;
unmapped styles and states inherit Darcula. Font settings, IDE UI and terminal
colors are outside this scheme. The next priority is an Islands-based UI plugin;
broader IDE validation, language mapping fixes and terminal support remain follow-ups.

The scheme follows the [official format example](https://blog.jetbrains.com/platform/2017/12/export-intellij-editor-themes-as-plugins/),
[scheme version](https://github.com/JetBrains/intellij-community/blob/master/platform/editor-ui-ex/src/com/intellij/openapi/editor/colors/impl/AbstractColorsScheme.java),
[text attribute](https://github.com/JetBrains/intellij-community/blob/master/platform/core-api/src/com/intellij/openapi/editor/HighlighterColors.java),
[language defaults](https://github.com/JetBrains/intellij-community/blob/master/platform/core-api/src/com/intellij/openapi/editor/DefaultLanguageHighlighterColors.java),
and [editor color keys](https://github.com/JetBrains/intellij-community/blob/master/platform/editor-ui-api/src/com/intellij/openapi/editor/colors/EditorColors.java).
