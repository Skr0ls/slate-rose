# Slate Rose for Zed

Slate Rose is a dark editor theme generated from the shared
[palette](https://github.com/Skr0ls/slate-rose/blob/dev/palette/colors.json). The package contains a theme manifest,
one generated theme, and the MIT notice.

## Local installation

Choose a package source:

- From a source checkout, run `python -m generators check zed` at the
  repository root and use its `packages/zed` directory.
- Download the `slate-rose-zed` artifact from a successful Quality workflow
  run on [GitHub Actions](https://github.com/Skr0ls/slate-rose/actions/workflows/quality.yml).
  GitHub requires sign-in to download artifacts; see its
  [artifact download documentation](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/download-workflow-artifacts).
  Extract the archive to a stable directory, since Zed's development extension
  installation references that directory.

In Zed, run **zed: install dev extension** from the command palette and select
the package directory. Run **theme selector: toggle** and choose **Slate Rose**.

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
[TypeScript fixture](https://github.com/Skr0ls/slate-rose/blob/dev/fixtures/showcase.ts) with sand types, blue functions,
rose property access, and green strings. The sampled declaration and control
words were lilac through the common keyword style. Coverage depends on each
language grammar. A broader workbench review is tracked in the
[Zed backlog](https://github.com/Skr0ls/slate-rose/blob/dev/openspec/README.md#4-zed--add-zed-theme).
