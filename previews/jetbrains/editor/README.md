# Initial JetBrains editor review

This is a bounded import/editor review, not acceptance of a complete JetBrains UI theme or language matrix. Rider is the primary review host; IntelliJ provides one Java smoke check. Broader IDE testing follows the UI plugin.

| Host on macOS arm64 | Context | Evidence |
| --- | --- | --- |
| Rider 2026.2.4, build 262.11879.110 | C# linked SDK project; .NET 8.0.419, net8.0 | [Overview](rider-overview.png) |
| IntelliJ IDEA 2026.3 RC, build 263.7307.112 | Java source root; project SDK/language level 25 | [Overview](idea-overview.png) |

## Reproduce

1. Follow the [fixture setup](../../../fixtures/jetbrains/README.md). Compilation succeeded for both disposable copies; neither fixture was executed.
2. Create `idea.properties` and `rider.properties` under `/tmp/sr-jb-review`. For each host, set `idea.config.path`, `idea.system.path`, `idea.plugins.path` and `idea.log.path` to its own `/tmp/sr-jb-review/<host>/{config,system,plugins,log}` directories. The review logs confirmed those config/system paths. These isolate storage locations, not necessarily every inherited IDE preference.
3. Launch the installed IDE with its [properties environment variable](https://www.jetbrains.com/help/idea/tuning-the-ide.html):

   ```sh
   IDEA_PROPERTIES=/tmp/sr-jb-review/idea.properties "/Applications/IntelliJ IDEA.app/Contents/MacOS/idea"
   RIDER_PROPERTIES=/tmp/sr-jb-review/rider.properties /Applications/Rider.app/Contents/MacOS/rider
   ```

4. Open the disposable projects. The owner approved trust for only these two test folders; no parent-directory trust was selected.
5. In Settings → Appearance, use Editor color scheme → Show Scheme Actions → Import Scheme and choose the generated `packages/jetbrains/colors/Slate Rose.icls`. IntelliJ additionally offers the `.icls` import format. Both hosts reported successful import and selected Slate Rose; save/apply the settings.
6. Open the fixture, select `result` after `return`, and inspect syntax, selection, current line and caret. UI remains Islands Dark. IntelliJ's window was fitted to the display for capture; product layout/font settings were not changed by the scheme.

## Observations

These are visual observations, not pixel measurements or proof of every effective language key.

| Example | Observed |
| --- | --- |
| Named types | C# `Task`/`ArgumentOutOfRangeException` and Java `String` appear sand. Unused class declarations are dimmed by inspections. |
| Functions | C# `Yield` appears blue. Unused method declarations are dimmed; Java exception constructor calls appear blue. |
| Fields/constants | `prefix`, `MaxLabels` and `MAX_LABELS` appear rose; unused properties can be dimmed. |
| Literals | Strings appear green and numbers amber. |
| Keywords/control | Declarations, `if`, `return` and `throw` remain lilac in these fixtures. Coral control distinctions are not mapped yet. |
| Primitive aliases | C# `string`/`int` and Java `int` remain lilac. `float` is not covered by these fixtures. |
| Namespace/punctuation | C# namespace is foreground; Java package name is sand. Some punctuation, inspection marks and occurrence backgrounds retain inherited colors. |
| Editor states | Current line and six-character selection are distinguishable; the caret is at the selection end. Selection text remains readable. |

Both saved native schemes retain all six explicit color keys and 22 attribute entries, with hex values equal to the generated source ignoring case. Native serialization lowercases attribute hex values. [Verification hashes](verification.json) identify the source, fixtures, imported files and captures; this comparison does not resolve language-plugin overrides.

## C# builtin-type follow-up

Selecting `string` and invoking **Jump to Colors and Fonts** led to **C# → Keywords → Builtin Type Keywords (int, short, bool, etc)**, inheriting the corresponding Language Defaults category. The [category capture](csharp-builtin-category.png) records that separate control; no setting was edited.

Installed Rider registration strings in `Contents/lib/intellij.rider.languages.jar`, `CSharpTextAttributeKeys.class`, identify `ReSharper.CSHARP_BUILTIN_TYPE_KEYWORD`; `RiderLanguageTextAttributeKeys.class` identifies the inherited `ReSharper.BUILTIN_TYPE_KEYWORD`. A focused follow-up can map C# aliases to the approved `primitive` color and verify them natively without recoloring other keywords. Registration evidence alone is not verification of that future override.

## Limits and next step

The next priority is an Islands-based UI plugin on Rider, including outer framing and gaps. This scheme does not theme the surrounding IDE. Other JetBrains products, OSes, versions, languages, completion/search/diagnostic states and terminal colors are unreviewed. Inherited inspections, unused-code dimming, folding and occurrence highlighting were retained. No palette, generator or generated output changed in this review.
