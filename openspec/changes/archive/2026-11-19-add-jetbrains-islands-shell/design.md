# Design

## Context

The Python CLI produces one file per host target. The existing `.icls` must remain byte-identical. See proposal.md for scope; the owner approved this UI allocation in the current session.

## Goals / Non-Goals

Deliver a resource-only plugin and one native Rider shell check. Do not add Gradle/Kotlin, a generic adapter framework, semantic fixes, menus/input states or marketplace jobs.

## Decisions

- Add `generators/jetbrains/ui.py` and a `jetbrains-ui` build/check target; default output is `packages/jetbrains/resources/Slate Rose.theme.json`. Keep existing outputs/validation/alias protection intact. Validate JetBrains metadata before printing it, as the editor adapter already does.
- Use the [official Islands keys](https://plugins.jetbrains.com/docs/intellij/supporting-islands-theme.html) and [platform metadata](https://github.com/JetBrains/intellij-community/blob/master/platform/platform-resources/src/themes/metadata/IntelliJPlatform.themeMetadata.json). Emit only these 16 keys: MainWindow.background, MainToolbar.background, ToolWindow.Stripe.background, StatusBar.background -> surface2; ToolWindow.background, ToolWindow.Header.background, ToolWindow.Header.inactiveBackground, Island.borderColor, EditorTabs.background -> bg; EditorTabs.underlinedTabBackground and EditorTabs.inactiveUnderlinedTabBackground -> surface; EditorTabs.underlinedBorderColor -> accent; EditorTabs.inactiveUnderlinedTabBorderColor -> surface2; StatusBar.borderColor, ToolWindow.Stripe.borderColor, MainToolbar.borderColor -> bg with alpha 00. Preserve inherited geometry/overlays and user project-color settings.
- JSON metadata: name Slate Rose, author Skr0ls, dark true, parentTheme Islands Dark, editorScheme `/colors/SlateRose.xml`. The canonical name matches `Slate Rose.theme.json`; no background/icon assets.
- Add `packages/jetbrains/META-INF/plugin.xml`: local ID `com.github.skr0ls.slaterose`, version 0.1.0, vendor Skr0ls, a required description, since-build 262, dependency `com.intellij.modules.lang`, and one newly generated stable themeProvider UUID referencing `/Slate Rose.theme.json`. Identity/version are local package metadata, not a release policy or publication commitment.
- A small standard-library `scripts/package_jetbrains.py` builds `dist/slate-rose-jetbrains.jar` (optional positional path) or verifies it with `--check`. Four entries only: META-INF/plugin.xml, Slate Rose.theme.json, colors/SlateRose.xml (existing `.icls` bytes), META-INF/LICENSE (root license). ZIP_STORED, fixed 1980 timestamp and file modes/order give reproducible bytes. A single JAR is supported by [Rider's disk installer](https://www.jetbrains.com/help/rider/Managing_Plugins.html).
- Validate canonical generated resources, descriptor identity/version/dependency/provider references and exact package content before writes. Protect every source input and both canonical palettes against output aliases. A check compares the archive to canonical bytes without rewriting it. CI checks UI output and builds/checks/uploads the JAR in the existing Python job; no SDK download is needed.

## Risks / Trade-offs

- Islands inheritance preserves unmapped native colors -> clearly describe this as a shell slice, with menus/controls next.
- User project colors and inactive-window overlays can affect visible colors -> record them rather than changing preferences automatically.
- Minimum build 262 is a declared compatibility boundary -> native acceptance covers the actual Rider version only, not every JetBrains product.
- A local plugin install may require confirmation/restart -> prepare and independently review the concrete artifact before that action; keep native task open until observed.
