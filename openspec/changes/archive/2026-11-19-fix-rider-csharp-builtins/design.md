# Design

## Context

See proposal.md. The editor renderer currently emits only shared `DEFAULT_*` attributes. The [native review](../../../../previews/jetbrains/editor/README.md#c-builtin-type-follow-up) records Rider's C# category and registration evidence; that is not yet verification of an effective override. Implement after the Islands package PR is integrated, on a fresh branch from updated `dev`.

## Goals / Non-Goals

Add one C#-specific mapping without a language framework. Java/Kotlin review, flow-control splits, namespace fixes, VS Code limitations and UI work remain separate changes.

## Decisions

- Add a small explicit external-key mapping alongside shared defaults. Emit `ReSharper.CSHARP_BUILTIN_TYPE_KEYWORD` exactly, without the `DEFAULT_` prefix, with foreground from `primitive` (`#D8B981`). Do not change the inherited `ReSharper.BUILTIN_TYPE_KEYWORD`: the C# key avoids affecting other Rider languages. Preserve the existing shared map and deterministic ordering.
- Keep `var`, escaped/contextual identifiers, ordinary declaration/flow keywords and named reference types as negative controls. Do not map source spelling with regex or disable highlighting. This preserves host classification; an inseparable category is a documented limitation requiring a separate owner decision.
- Add a separate small C# fixture under `fixtures/jetbrains/` and document a disposable project using the existing SDK project pattern. Keep historical `showcase.cs` and previous acceptance captures intact. Cover all four aliases in fields/parameters/returns/locals where applicable, casts/generic/nullable type usages, `System.String`/`String`, `Task`, ordinary keywords and `var`/an escaped identifier. Never execute it.
- Regression verification checks the exact external key and literal approved color, shared keyword/class values and unchanged other attributes. Avoid deriving the test's expected map from the implementation map. Rebuild the generated scheme and deterministic JAR; compare both palette files, UI JSON and VS Code output against the integration baseline.
- Native review uses Jump to Colors and Fonts for declaration/use/negative controls, records the effective category and exported override, and compares before/after under unchanged preferences. [JetBrains SDK guidance](https://plugins.jetbrains.com/docs/intellij/syntax-highlighting-and-error-highlighting.html) distinguishes layered text keys; JetBrains' optional variable/parameter semantic coloring is not equivalent to VS Code's semantic-token provider.

  The completed review could not obtain a native export: equivalent bounded verification combines the exact installed-package value, registered-key bytecode, native categories and visual before/after evidence; it does not claim an exported runtime value or measured pixel equality.

## Risks / Trade-offs

- A registered key may be shadowed by a layered style -> prove effective behavior in Rider before marking complete; do not infer acceptance from XML alone.
- Missing pinned SDK can put the file in Miscellaneous Files -> select an installed SDK in the disposable project and verify successful native loading before capture.
- Local package updates can require restart/confirmation -> prepare and review the concrete package first, then install only in the approved isolated profile under applicable action-time confirmation rules.
- Existing exact-attribute tests will need one new entry -> retain assertions for all old attributes so a broad recoloring cannot pass unnoticed.
