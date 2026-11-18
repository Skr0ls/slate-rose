# Design

## Context

See proposal.md. The [initial Java smoke check](../../../../previews/jetbrains/editor/README.md) used IntelliJ IDEA 2026.3 RC, build 263.7307.112, and Java 25. It observed lilac `int` and sand `String`, but did not inspect primitive-specific categories. The shared scheme maps keywords to lilac and named types to sand. C# has a host-specific follow-up in PR #16; its category does not establish Java support.

At upstream revision `40b68d9360d885b27d5b41631b6a88ad34f83efb`, the [lexical map](https://github.com/JetBrains/intellij-community/blob/40b68d9360d885b27d5b41631b6a88ad34f83efb/java/java-frontback-impl/src/com/intellij/ide/highlighter/AbstractBasicJavaFileHighlighter.java#L29-L33) uses the shared keyword attribute. The [semantic visitor](https://github.com/JetBrains/intellij-community/blob/40b68d9360d885b27d5b41631b6a88ad34f83efb/java/java-analysis-impl/src/com/intellij/codeInsight/daemon/impl/analysis/JavaNamesHighlightVisitor.java#L215-L294) does not establish a primitive-specific override; [keyword registration](https://github.com/JetBrains/intellij-community/blob/40b68d9360d885b27d5b41631b6a88ad34f83efb/java/java-frontback-psi-impl/src/com/intellij/ide/highlighter/JavaHighlightingColors.java#L14-L48) uses `JAVA_KEYWORD`. This is bounded upstream evidence, not native verification of the installed build or proof about every provider.

## Goals / Non-Goals

Deliver one reproducible classification review, including a supported-key candidate or a bounded limitation. Do not change theme output, install a new language/runtime plugin, disable highlighting, or expand to the whole JVM stack. Begin execution from updated `dev` after #16 integrates.

## Decisions

- Add `fixtures/jetbrains/PrimitiveTypes.java`, leaving historical fixtures unchanged. Keep it small and self-contained: `int`, `boolean`, `float` in fields, parameters, return types and locals; array/cast uses; `String` and boxed `Integer`/`Boolean` with a generic use; `public`/`class`/`if`/`return`/`throw` controls. Include local-inference `var`, a `void` method and a contextual-name control independently. `void` is not one of Java's eight primitives; `var` has context-dependent keyword behavior, not primitive-alias semantics. Use Java 25 syntax without preview features or external dependencies, following the [JLS type distinctions](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.2).
- Reuse `/tmp/sr-jb-review/projects/idea` and its isolated IDEA profile; record the actual IDE/Java plugin version, installed JDK, configured source root and language level. Verify project loading/indexing and the active editor scheme, not just the UI theme label. Use the already reviewed scheme baseline; do not add UI acceptance to this change. Optional offline compilation must not execute the fixture.
- Inspect primitive declarations and uses plus named/boxed types, `var`, `void` and keyword controls with Jump to Colors and Fonts. Record external keys and fallback/layering when UI Inspector or bundled registration evidence exposes them. Supplement native observations with the lexer and semantic visitor from a pinned official source revision; distinguish that revision from the installed binary. [JetBrains documents layered attributes and inspection](https://plugins.jetbrains.com/docs/intellij/syntax-highlighting-and-error-highlighting.html).
- Keep lexical and project-aware observations separate without toggling the IDE's optional variable/parameter coloring or disabling analysis. Source inspection provides lexical evidence; a loaded, indexed fixture provides the native project-aware review. Missing providers/SDKs or unavailable categories are recorded as unresolved, not as proof of absent support.
- Deliver `previews/jetbrains/java-primitives/README.md`, one compact verification JSON and at most two unmodified captures. The review table identifies each target, observed category/key, appearance, evidence and status (`lexical reviewed`, `semantic reviewed`, `limited` or `blocked`). Record scheme/JAR and fixture hashes, available context and reproduction steps. If no native export is obtained, distinguish exact packaged values from visual appearance; do not claim runtime hex equality.
- This review does not implement selectors. If primitives share an inseparable keyword key, retain current colors and document that bounded limitation. If a narrow registered selector is observed, record a concrete follow-up candidate with positive/negative cases for a separate mapping change. No regex by token spelling or parser changes.

## Risks / Trade-offs

- Lexer and semantic layers can disagree -> inspect both and label observations by layer/context.
- A manually imported scheme can shadow a package scheme -> verify and record the actual selected editor scheme before capture; preserve baseline copies.
- Upstream source can differ from the installed build -> retain the exact source revision and avoid universal impossibility claims.
- A review can conclude with a documented limitation -> completion means the selected cases are examined and reported, not that primitives were recolored or broader Java acceptance was achieved.
