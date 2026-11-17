# IntelliJ IDEA Java primitive review

Status: **limited**. In the inspected IntelliJ IDEA project, primitive
keywords and ordinary keywords shared the Java Keyword category. No narrow
primitive selector was established; this result does not establish that none
exists in other providers or contexts. Current theme output is retained.

The [fixture](../../../fixtures/jetbrains/PrimitiveTypes.java) was reviewed in
IntelliJ IDEA 2026.3 RC, build `263.7307.112`, with the bundled Java plugin `com.intellij.java` version `263.7307.112`.
The project source root was `idea` (package `preview`); project SDK `25` used
`/opt/homebrew/opt/java/libexec/openjdk.jdk/Contents/Home` (25.0.1) and
language level `JDK_25`. Startup scanning finished and the project exited indexing mode; class resolution was available. Optional offline
compilation used the separate IntelliJ bundled JDK `javac 25.0.4.1`; the fixture
was not executed. [Fixture instructions](../../../fixtures/jetbrains/README.md)
describe the disposable project. The active editor scheme was confirmed as
`Slate Rose` in Jump to Colors and Fonts; no highlighting preference changed.

| Fixture target | Native project-aware observation | Evidence / status |
| --- | --- | --- |
| `int` field, return, cast; `boolean` field and parameter; `float` field and local | Java > Keyword (`JAVA_KEYWORD`), inheriting Keyword (Language Defaults); lilac | Jump to Colors and Fonts; semantic reviewed |
| Other primitive parameters, returns, locals and array element type | Lilac appearance | [Overview](overview.png); limited (appearance only) |
| `String`, `Integer`, `Boolean` fields | Java > Classes and Interfaces > Class, inheriting Classes > Class name (Language Defaults); sand | Jump to Colors and Fonts; semantic reviewed |
| `List` and generic `Integer` | Sand appearance | [Overview](overview.png); limited (appearance only) |
| Inference `var`, `void` return, `class`, `if` | Java > Keyword (`JAVA_KEYWORD`), inheriting Keyword (Language Defaults); lilac | Jump to Colors and Fonts; semantic reviewed |
| `record` local identifier | Chooser offered Warning and Local variable; identifier foreground, with inspection overlay | Jump to Colors and Fonts; limited |
| `public`, `private`, `return`, `throw` | Lilac appearance | [Overview](overview.png); limited (appearance only) |
| `IllegalStateException` constructor call | Blue appearance (constructor-call context) | [Overview](overview.png); limited (appearance only) |

`void` is not a primitive type, and `var` inference is not a primitive alias.
The [keyword capture](keyword.png) shows the selected scheme and inherited
category. The dialog displayed `CAA1DE`; captures show appearance and are not
a native export proving exact runtime hex values. See [verification.json](verification.json)
for hashes and context. The source audit below is lexical evidence; the table
records separate loaded-project observations.

## Pinned upstream source audit

The following official IntelliJ Community sources are pinned to revision
`40b68d9360d885b27d5b41631b6a88ad34f83efb`:

- [SyntaxElementTypes.kt, lines 16–49](https://github.com/JetBrains/intellij-community/blob/40b68d9360d885b27d5b41631b6a88ad34f83efb/java/java-syntax/src/com/intellij/java/syntax/element/SyntaxElementTypes.kt#L16-L49)
  lists keyword token types, including the selected primitives and ordinary keywords.
- [JavaFileHighlighter.java, lines 17–50](https://github.com/JetBrains/intellij-community/blob/40b68d9360d885b27d5b41631b6a88ad34f83efb/java/java-frontback-impl/src/com/intellij/ide/highlighter/JavaFileHighlighter.java#L17-L50)
  supplies the Java lexer and syntax highlighting implementation.
- [AbstractBasicJavaFileHighlighter.java, lines 29–33](https://github.com/JetBrains/intellij-community/blob/40b68d9360d885b27d5b41631b6a88ad34f83efb/java/java-frontback-impl/src/com/intellij/ide/highlighter/AbstractBasicJavaFileHighlighter.java#L29-L33)
  maps Java keywords to the shared `KEYWORD` attribute.
- [JavaHighlightingColors.java, lines 14–48](https://github.com/JetBrains/intellij-community/blob/40b68d9360d885b27d5b41631b6a88ad34f83efb/java/java-frontback-psi-impl/src/com/intellij/ide/highlighter/JavaHighlightingColors.java#L14-L48)
  defines `JAVA_KEYWORD`.
- [JavaNamesHighlightVisitor.java, lines 215–294](https://github.com/JetBrains/intellij-community/blob/40b68d9360d885b27d5b41631b6a88ad34f83efb/java/java-analysis-impl/src/com/intellij/codeInsight/daemon/impl/analysis/JavaNamesHighlightVisitor.java#L215-L294)
  visits soft keywords; the inspected path does not establish a primitive-specific
  override.
- [HighlightNamesUtil.java, lines 421–426](https://github.com/JetBrains/intellij-community/blob/40b68d9360d885b27d5b41631b6a88ad34f83efb/java/java-analysis-impl/src/com/intellij/codeInsight/daemon/impl/analysis/HighlightNamesUtil.java#L421-L426)
  highlights the relevant soft-keyword helper with `KEYWORD`.

This source revision is upstream evidence, not confirmation of the registration
or behavior of the installed IntelliJ IDEA build `263.7307.112`. These paths do not establish what every highlighting provider can do; no
selector change is proposed from this audit alone.

The installed Java plugin descriptor identifies `com.intellij.java` version
`263.7307.112`. Inspection of its bundled bytecode found `JAVA_KEYWORD` falling
back to the language-default keyword, the keyword token set mapped to that
attribute, the soft-keyword visitor/helper path, and the named-class path using
`CLASS_NAME`. This corroborates the inspected paths for this installation; it
does not establish that the installed binaries are identical to the pinned
upstream revision or exhaust every provider and layer.

To reproduce the installed keyword-map inspection:

```sh
rtk proxy '/opt/homebrew/opt/java/libexec/openjdk.jdk/Contents/Home/bin/javap' -p -c -classpath '/Applications/IntelliJ IDEA.app/Contents/plugins/java/lib/intellij.java.frontback.impl.jar' com.intellij.ide.highlighter.AbstractBasicJavaFileHighlighter | rtk proxy sed -n '/protected static void fillStandardMaps/,/getstatic.*LITERAL_BIT_SET/p'
```

The other class targets can be inspected with `javap` and their corresponding
JAR classpaths listed in [verification.json](verification.json); the plugin
descriptor is an entry in `java-impl.jar`.
