# Rider C# builtin type review

This bounded review used Rider 2026.2.4, build 262.11879.110, in an isolated
profile with .NET SDK 8.0.418. The successfully loaded project was
`/tmp/sr-jb-review/projects/rider/builtins/jetbrains/Builtins.csproj`, linking
`fixtures/jetbrains/BuiltinTypes.cs`. Dependencies and Roslyn were present.
The fixture build succeeded with no errors and three unassigned-field warnings;
the fixture was never executed.

The [before capture](before.png) used the imported Slate Rose scheme with the
previous JAR (`db5ad7238a57cdb84dead9c56af24ecfa1d8768020db1969e17bf956addf37ca`).
The [after capture](after.png) used the packaged scheme from the installed JAR
(`1d704d9ee610146779dd071a4d2a0c6bd6960098d4c3a1268e2c531582233e12`).
The screenshots are unmodified; their geometry differs and the before capture
has white padding. Hashes are recorded in [verification.json](verification.json).

Before, the four aliases were lilac and `Task` and `String` were sand. After,
`int`, `string`, `float` and `bool` appeared in the primitive color, while
`var`, `public`, `private`, `class`, `if` and `return` remained lilac and
`Task`, `String` and `List` remained sand. Unused-code inspections and occurrence
highlights remained present. Jump to Colors and Fonts identified the `string`
declaration before and after, and the `int` cast after, as C# > Keywords >
Builtin Type Keywords (int, short, bool, etc.); `var` was C# > Keywords > Keyword.

The packaged scheme sets `ReSharper.CSHARP_BUILTIN_TYPE_KEYWORD` to `D8B981`.
This is an exact source and package value; the screenshots establish visual
appearance, not a measured pixel-color comparison. No native `.icls` export was
obtained. These observations do not establish Java, Kotlin, VS Code or other
host parity.

An older imported scheme initially shadowed the bundled scheme. The old copy was
preserved under `Slate Rose (imported baseline)`. Although the UI showed Slate
Rose, the persisted global scheme still named the baseline. With Rider closed,
the isolated profile's scheme options were backed up and its global scheme name
set to `Slate Rose`; after restart the packaged colors appeared, and a final exit
persisted that name. When upgrading, select the packaged scheme if an imported
copy shadows it; preserve any old copy and avoid automatic preference changes.

The user approved installation. The UI installer was unreliable in this isolated
profile, so the JAR was copied to its plugin directory and Rider restarted, per
[JetBrains command-line installation guidance](https://www.jetbrains.com/help/rider/Install_plugins_from_the_command_line.html).
