# Slate Rose for Zed

Slate Rose is a dark editor theme generated from the shared
[palette](../../palette/colors.json). The package contains a theme manifest,
one generated theme, and the MIT notice.

## Local installation

1. From the repository root, run `python -m generators check zed`.
2. In Zed, run **zed: install dev extension** from the command palette and
   select this `packages/zed` directory.
3. Run **theme selector: toggle** and choose **Slate Rose**.

After a palette mapping change, run `python -m generators build zed` from the
repository root and reload the development extension if needed. The
[Zed extension development guide](https://zed.dev/docs/extensions/developing-extensions#developing-an-extension-locally)
describes local installation.

## Scope and verification

The theme sets editor surfaces, text, line numbers, and documented
[Tree-sitter captures](https://zed.dev/docs/extensions/languages#syntax-highlighting).
The surrounding workbench and terminal use Zed defaults. The
[official theme schema](https://zed.dev/schema/themes/v0.2.0.json) validated the
generated JSON.

The package installed as a development extension in Zed 1.28.1 on macOS.
In an isolated profile, Slate Rose appeared in the selector and rendered the
[TypeScript fixture](../../fixtures/showcase.ts) with sand types, blue functions,
rose property access, and green strings. The sampled declaration and control
words were lilac through the common keyword style. Coverage depends on each
language grammar. A broader workbench review is tracked in the
[Zed backlog](../../openspec/README.md#4-zed--add-zed-theme).
