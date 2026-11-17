# Kotlin type-role review

The fixture is [TypeRoles.kt](../../../fixtures/jetbrains/TypeRoles.kt);
setup and optional offline compilation are documented in the [fixture instructions](../../../fixtures/jetbrains/README.md).
The local compiler was Kotlin 2.4.10-release-377 from IntelliJ IDEA; compilation
succeeded without running the output.

## Native review

**Status: limited.** In the isolated IntelliJ IDEA 263.7307.112 project,
Kotlin plugin 263.7307.112-IJ inspected `TypeRoles.kt` as Kotlin/JVM with
project JDK 25 and the bundled stdlib attached. The project source root is
`projects/idea`, with the fixture in package `preview`; standard classes
resolved and no unresolved-type errors were visible. Indexing had finished
before inspection (exit dumb mode at 01:57:53.272 on 2026-11-18). The IDE
language version was not explicitly verified. The Slate Rose scheme was
selected in all 19 Jump to Colors and Fonts probes; no highlighting preference
was changed.

| Selected construct | Native category and appearance |
| --- | --- |
| `Int`, `String`, `Boolean`, `Float` property types | Class → Classes → Class name (Language Defaults); sand |
| `Label` alias declaration and use | Type alias → Classes and Interfaces → Class (Kotlin); sand |
| `Unit` return type | Chooser offered Java Errors and Warnings → Unused code and Object; redundant type appeared dimmed |
| `Unit` value | Object → Class (Kotlin); sand |
| `typealias`, `class`, `fun`, `if`, `when`, `return`, `throw` | Keyword → Keyword (Java); lilac |
| `val`, `var` | Separate Kotlin `'val'` and `'var'` categories → Keyword (Kotlin); lilac |
| accessor `get` | Chooser offered Java Errors and Warnings → Weak Warning and Kotlin Keyword |
| backing reference `field` | Backing field variable plus Var (mutable variable) overlay; quiet foreground and underline |

Other `Int`, `String`, `Boolean` and `Float` parameter and local type
occurrences, nullable `String?`, and `List<Int>` appeared sand but were not
individually inspected. The local `Unit` annotation appeared dimmed and was
not individually inspected. The
`IllegalArgumentException` constructor appeared blue; its category was not
inspected. The shared keyword category prevents separating the selected
declaration and control-flow words by that key. A separate follow-up may
review a narrow backing-field foreground override, preserving the mutable
overlay; no mapping change is made here.

For reproduction, follow the [fixture setup](../../../fixtures/jetbrains/README.md),
wait for indexing and verify resolution and scheme. Place the caret on a
selected token, use **Help → Find Action**, and choose **Jump to Colors and
Fonts**; select a category when the chooser offers multiple entries. The raw
[overview](overview.png) and [field category chooser](field-categories.png)
captures retain their original padding. Their hashes and the scheme hash are
recorded in [verification.json](verification.json).

## Provider evidence

The installed Kotlin plugin is 263.7307.112-IJ, in IntelliJ IDEA build
263.7307.112. Inspection of the installed highlighter and semantic analyzer
bytecode indicates that resolved named built-in classes use `KOTLIN_CLASS`,
`Unit` uses `KOTLIN_OBJECT`, and type alias names use `KOTLIN_TYPE_ALIAS`.
The type analyzer skips constructor references. The lexical highlighter uses
`KOTLIN_KEYWORD` for `class`, `fun`, `typealias` and flow-control keywords;
`val` and `var` have separate keys. The pre-resolve visitor marks contextual
`get` and `field` soft-keyword tokens with `KOTLIN_KEYWORD`.
A resolved backing-field reference receives `KOTLIN_BACKING_FIELD_VARIABLE`,
with a mutable-variable overlay for a `var`. These are provider findings, not
observations of the current project or its displayed colors.

Pinned upstream sources provide context, but their commit has not been established
as the installed build's source revision: [highlighting colors](https://github.com/JetBrains/intellij-community/blob/3d935d69c9009c360243f09cc834ecea2ae783c6/plugins/kotlin/highlighting/highlighting-minimal/src/org/jetbrains/kotlin/idea/highlighter/KotlinHighlightingColors.java),
[lexical highlighter](https://github.com/JetBrains/intellij-community/blob/3d935d69c9009c360243f09cc834ecea2ae783c6/plugins/kotlin/highlighting/highlighting-minimal/src/org/jetbrains/kotlin/idea/highlighter/KotlinHighlighter.java),
[pre-resolve visitor](https://github.com/JetBrains/intellij-community/blob/3d935d69c9009c360243f09cc834ecea2ae783c6/plugins/kotlin/highlighting/highlighting-minimal/src/org/jetbrains/kotlin/idea/highlighter/BeforeResolveHighlightingVisitor.kt),
[alias declaration visitor](https://github.com/JetBrains/intellij-community/blob/3d935d69c9009c360243f09cc834ecea2ae783c6/plugins/kotlin/highlighting/highlighting-k2/src/org/jetbrains/kotlin/idea/highlighting/beforeResolve/DeclarationHighlightingVisitor.kt),
[type analyzer](https://github.com/JetBrains/intellij-community/blob/3d935d69c9009c360243f09cc834ecea2ae783c6/plugins/kotlin/highlighting/highlighting-k2/src/org/jetbrains/kotlin/idea/highlighting/analyzers/KotlinTypeSemanticAnalyzer.kt),
and [variable analyzer](https://github.com/JetBrains/intellij-community/blob/3d935d69c9009c360243f09cc834ecea2ae783c6/plugins/kotlin/highlighting/highlighting-k2/src/org/jetbrains/kotlin/idea/highlighting/analyzers/KotlinVariableReferenceSemanticAnalyzer.kt).

Artifact hashes, bytecode targets and the inspection command are recorded in
[verification.json](verification.json).

The installed `KOTLIN_CLASS` falls back to Language Defaults class name;
`KOTLIN_OBJECT` and `KOTLIN_TYPE_ALIAS` fall back to `KOTLIN_CLASS`.
`KOTLIN_BACKING_FIELD_VARIABLE` and `KOTLIN_MUTABLE_VARIABLE` have no
fallback key. The imported scheme inherits Darcula and has no explicit entries
for these Kotlin keys. Its `DEFAULT_INSTANCE_FIELD` foreground is `#E28DA4`,
but the backing-field key does not fall back to it. The installed Darcula
Kotlin defaults give the backing-field key bold and the mutable-variable key
an effect, neither an explicit foreground; overlay precedence is not inferred.
