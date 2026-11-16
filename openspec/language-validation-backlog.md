# Language validation backlog

This is a queue for future OpenSpec changes, not approval to implement them or a
claim of language support. Start with VS Code and its existing C++, C#,
TypeScript and Python fixtures. Review other hosts separately after their
JetBrains and Zed adapters exist; results do not imply parity across hosts.
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

Fix native mappings only for observed issues, with a small regression test that
fails before and passes after the fix. Keep the approved palette unchanged;
significant design choices require owner approval. Do not blanket-disable
semantic highlighting. For mapping changes run the existing validator,
generator check, tests and relevant hooks. Screenshots and token inspections
are review evidence, not automated tests.

Use VS Code's [language overview](https://code.visualstudio.com/docs/languages/overview)
and [semantic highlighting guide](https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide)
to distinguish grammar tokenization from provider semantics.

## Batches

Every checkbox is a candidate future PR/OpenSpec change. Done means the review
and completion criteria above are met for each named item; lexical and semantic
results are recorded separately.

- [ ] **Baseline regressions:** C++, C#, TypeScript and Python, using the
  existing fixtures and checking their established role distinctions.
- [ ] **Systems:** C, Go, Rust and Zig; cover declarations, control flow,
  types, functions and fields, plus language-specific constructs.
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
