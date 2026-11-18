# Language validation backlog

This is a queue for future OpenSpec changes, not approval to implement them or a
claim of language support. Review each host separately; results do not imply
parity across hosts. The JetBrains UI plugin is integrated; start each selected
language change from fresh `dev` after its predecessor integrates.
Continue focused language reviews alongside the Zed adapter as concrete
mapping gaps arise.
The batches below are practical groupings, not a popularity ranking. Split a
batch further if it cannot fit in a small, reviewable PR.

## Review and completion criteria

For each language or format in a selected batch, record an evidence row with
the status, fixture path, editor and version, language ID, provider and version,
and any runtime or project context. Use **unreviewed**, **lexical reviewed**,
**semantic reviewed**, **limited**, or **blocked**; explain limitations and
link evidence. Rendering alone does not establish support.

Done for a batch means every selected item has:

1. A small, original, non-secret fixture covering applicable roles and
   constructs. Use a minimal valid project only when a provider needs it;
   offline compilation is optional. Never execute script fixtures or include
   credentials.
2. A lexical baseline review, then a separate semantic review when available;
   document an unavailable provider or semantic result instead of assuming it.
   Capture screenshots and token inspections for deviations, with enough
   context to reproduce them.
3. Findings and a status in the evidence row. Inspect applicable primitives,
   flow control, fields, constants, decorators, interpolation, macros and
   lifetimes, traits and generics. Also inspect shell pipes, variables and here
   documents; PowerShell verb-noun commands, cmdlets and parameters; XML
   attributes; SQL quoted identifiers; and INI/environment substitution where
   relevant. Apply semantic roles only where meaningful; do not force field or
   function roles onto every configuration format.

For each selected language, compare built-in keyword types, named standard types
and contextual keywords where applicable. Base findings on the host category,
not spelling alone; fix only observed narrow keys or document inseparable
limitations.

Fix native mappings only for observed issues, with a small regression test that
fails before and passes after the fix. Keep the approved palette unchanged;
significant design choices require owner approval. Do not blanket-disable
semantic highlighting. For mapping changes run the existing validator,
generator check, tests and relevant hooks. Screenshots and token inspections
are review evidence, not automated tests.

For JetBrains, use a minimal valid loaded project and fix missing SDK setup
before inspecting; record the host, version and provider. Its optional
**Semantic highlighting** setting colors variables and parameters; it is not
the same as a VS Code semantic-token provider. Inspect lexical and annotator
keys using Jump to Colors and Fonts or UI Inspector as described in the
[JetBrains highlighting documentation](https://plugins.jetbrains.com/docs/intellij/syntax-highlighting-and-error-highlighting.html).
Do not disable semantic highlighting globally or recolor broad keyword groups.

Use VS Code's [language overview](https://code.visualstudio.com/docs/languages/overview)
and [semantic highlighting guide](https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide)
to distinguish grammar tokenization from provider semantics.

## Semantic role adaptations

Select small language batches incrementally. For each language, host, provider
and version, inspect actual lexical and semantic categories before choosing a
mapping. Prefer supported, narrow overrides for meaningful roles: types sand,
declarations lilac and flow control coral. Do not recolor broad keyword groups,
disable semantic highlighting by default, or modify language parsers/runtime behavior.
If a category mixes inseparable roles, document the limitation and seek an
owner decision. For an actual fix, use relevant fixtures, before/after evidence,
regression checks and native verification under the [criteria above](#review-and-completion-criteria).
The [JetBrains native editor review](../previews/jetbrains/editor/README.md)
records the initial evidence. Use the remaining batches to track concrete
mapping gaps in small PRs. A review may identify limitations without requiring
a code fix.

- [x] **Rider C# builtin aliases:** The
  [focused change](changes/archive/2026-11-19-fix-rider-csharp-builtins/tasks.md) and
  [bounded native review](../previews/jetbrains/csharp-builtins/README.md) cover `int`, `string`, `float` and
  `bool` using the registered `ReSharper.CSHARP_BUILTIN_TYPE_KEYWORD` category
  and the existing `primitive` color, keeping ordinary keywords unchanged.
  Reviewed declaration and usage locations and mixed `var` or contextual
  identifier cases where applicable; do not automatically treat `var` as a
  primitive. Retain the prior owner decision to leave and document VS Code C#;
  investigate it only if its provider exposes a narrow category.
- [ ] **Java primitive keywords:** **Limited** in the focused
  [IntelliJ review](../previews/jetbrains/java-primitives/README.md): inspected
  primitive keywords share Java Keyword with ordinary keywords; no narrow
  selector was established. Named types, `var`, `void` and a contextual
  identifier were compared. Current theme output is retained; other providers
  and contexts remain unverified.

- [x] **Kotlin types and contextual words:** **Limited** in IntelliJ IDEA
  263.7307.112 with Kotlin plugin 263.7307.112-IJ, Kotlin/JVM and project JDK
  25; the focused [fixture and evidence](../previews/jetbrains/kotlin-types/README.md)
  record semantic review of built-in class types, aliases and `Unit`. The
  selected declaration and flow-control words share a keyword category, and
  the backing-field reference has a quiet foreground. A narrow backing-field
  candidate needs separate review; no mapping was changed. Other hosts and
  contexts remain unreviewed. See the [keyword reference](https://kotlinlang.org/docs/keyword-reference.html)
  and [`Int` API](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/).

- [x] **Swift types and contextual words:** Reviewed `Int`, `String`, `Bool` and
  `Float` as named standard-library types, not reserved primitive keyword
  aliases. Inspect optional, generic and `typealias` declarations and uses;
  distinguish type identifiers from initializer calls. Compare `typealias`,
  `struct`, `func`, `let` and `var` with `if`, `return` and `throw`; inspect
  contextual `any` and `some` in type positions without blanket coloring them
  as types. The [limited VS Code review](../previews/vscode/swift/README.md)
  found built-in types sand, flow-control `if`/`throw`/`return` lilac, and a
  generic declaration foreground. The [Swift flow control fix](changes/archive/2026-11-19-fix-vscode-swift-flow-colors/tasks.md)
  covers the observed control scopes. The generic declaration remains a
  separate candidate, and other hosts and contexts
  remain unreviewed. See Swift's [types](https://docs.swift.org/latest/documentation/the-swift-programming-language/types/)
  and [lexical structure](https://docs.swift.org/latest/documentation/the-swift-programming-language/lexicalstructure/).

After these focused reviews, review the baseline regressions batch below.

## Batches

Every checkbox is a candidate future PR/OpenSpec change. Done means the review
and completion criteria above are met for each named item; lexical and semantic
results are recorded separately.

- [ ] **Baseline regressions:** C++, C#, TypeScript and Python, using the
  existing fixtures and checking their established role distinctions.
  C++ has a bounded [lexical and native provider review](../previews/vscode/cpp-baseline/README.md)
  for the sampled context. The [C++ flow control fix](changes/fix-vscode-cpp-flow-colors/tasks.md)
  covers the observed `if` and `for` scopes. TypeScript has a bounded
  [provider review](../previews/vscode/typescript-baseline/README.md) and a
  [native flow control fix](../previews/vscode/typescript-baseline/README.md#native-flow-control-verification)
  for `if`, `for` and `throw`. The [C# flow control fix](../previews/vscode/csharp-flow/README.md)
  covers the sampled Microsoft C# semantic control keywords. Python has a
  bounded [MagicPython and Pylance review](../previews/vscode/python-baseline/README.md)
  with a documented dataclass field limitation. The wider native TypeScript
  and C# baselines remain pending.
- [ ] **Systems:** C, Go, Rust and Zig; cover declarations, control flow,
  types, functions and fields, plus language-specific constructs.
  C has a bounded [lexical and IntelliSense review](../previews/vscode/c-baseline/README.md)
  with a shared flow-control scope limitation. The [Go review](../previews/vscode/go-baseline/README.md)
  covers lexical primitive and flow-color corrections and the semantic
  keyword limitation with gopls. The [Rust review](../previews/vscode/rust-baseline/README.md)
  covers primitive types, semantic flow control, and the shared lexical scope
  limitation. Zig remains pending.
- [ ] **JVM:** Java, Kotlin, Scala and Groovy; cover types, methods, fields,
  annotations and generics where applicable.
- [ ] **Apple:** Swift and Objective-C; cover declarations, types, methods,
  properties and language-specific syntax.
- [ ] **Web:** JavaScript, JSX, TSX, PHP and Ruby; cover functions, properties,
  interpolation and embedded markup where applicable.
  JavaScript, JSX and TSX have a bounded [review record](../previews/vscode/web/README.md);
  PHP and Ruby have a bounded [built-in review](../previews/vscode/php-ruby/README.md);
  third-party PHP and Ruby semantic-provider reviews remain queued, so this batch
  is still open.
- [ ] **Scripting:** Lua, PowerShell, POSIX shell and Bash; distinguish shell
  dialects and inspect their applicable command and variable constructs.
- [ ] **Lisps:** Clojure, Common Lisp and Scheme; cover definitions, calls,
  symbols and language-specific forms.
- [ ] **Additional languages:** Dart and R; cover declarations, calls, types
  where applicable, and representative language-specific forms.
- [ ] **SQL baseline:** generic SQL first, covering keywords, identifiers,
  quoted identifiers, literals and applicable calls. PostgreSQL, MySQL and
  T-SQL are separate later dialect reviews, each with its own provider and
  context; the generic review does not establish their coverage.
- [ ] **Markup and configuration:** HTML, CSS/SCSS, JSON, JSONC, YAML, TOML,
  XML, INI, `.env` and Markdown; cover format-specific keys, values, nesting,
  attributes, interpolation or embedded syntax where applicable.
- [ ] **`.conf` samples:** nginx, Apache, Git configuration and generic INI.
  `.conf` is a filename extension, not a language: choose and record the actual
  format, language ID and provider for each sample. No universal `.conf`
  coverage follows from these reviews.

Later candidates, not commitments: zsh and fish as separate shell dialects;
Emacs Lisp; Elixir, Erlang, Haskell, OCaml, F# and Julia; Dockerfile,
Makefile, HCL and Nix. Select and scope each separately before work begins.
