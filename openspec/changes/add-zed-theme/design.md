# Design

Generate a single dark theme family from the shared palette using the official Zed theme schema v0.2.0. Declare only editor backgrounds, text and line numbers plus documented Tree-sitter syntax captures. Where a query uses generic `keyword` for both declaration and flow, use the approved keyword color. Keep the shell and terminal on Zed defaults.

Keep the extension manifest beside the generated theme. The package contains only theme data and the MIT notice. Add `zed` to the existing build and check commands and validate output deterministically in the Quality workflow. Schema validation and one native install smoke test cover the first package. A broader Zed UI review and release packaging remain separate backlog items.
