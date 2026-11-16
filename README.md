# Slate Rose

Slate Rose is a dark color theme for VS Code, JetBrains IDEs, and Zed.

**Status:** The v0.2 Contrast design baseline is approved and palette validation
and VS Code theme generation and local VSIX packaging are available. Workbench
mappings and a representative native workbench review are available; owner acceptance is pending.
Modern UI shell gutters and frame colors are included; native window controls and layout settings are preserved.

## Design

Slate Rose pairs cool graphite surfaces with muted, legible syntax colors:

- Sand for types and blue for functions.
- Rose for fields, lilac for declarations, and coral for flow control.
- Green for strings, with ordinary variables and punctuation kept quiet.

The approved [palette](palette/colors.json) is the source of truth. The
[design baseline](docs/design-baseline.md) records language examples, editor
targets, architecture, and outstanding UI design work.

## Editor support

The project plans separate adapters for VS Code, JetBrains IDEs, and Zed, with
Visual Studio investigated separately. VS Code is the first editor and workbench
implementation. Host-specific limitations and mappings will be documented as
each adapter is built.

## Development

With Python 3.11 or newer, validate the palette, build or check the generated VS Code theme, and run the tests:

```sh
python -m generators validate
python -m generators build vscode
python -m generators check vscode
python -m unittest discover -s tests -v
```

Pass a path after `validate` to check another palette. The schema requires only
`name`, `version`, and `colors` at the root, with all 24 supported color tokens.
Validation reads the input without modifying it. Build and check accept optional
`--palette PATH` and `--output PATH`; defaults resolve relative to this project
even from another working directory. Check is read-only and reports missing or
stale output. See [VS Code mappings](docs/vscode-mappings.md) for limitations.

## Local VS Code installation

Use Node.js 22 or newer and Python 3.11 or newer. No publisher credentials are
needed to package locally:

```sh
python -m generators check vscode
mkdir -p dist
(cd packages/vscode && SOURCE_DATE_EPOCH=1794787200 TZ=UTC npx --yes @vscode/vsce@4.1.1 package --no-dependencies --out ../../dist/slate-rose.vsix)
python scripts/check_vsix.py dist/slate-rose.vsix
```

In VS Code, run **Extensions: Install from VSIX...**, choose the generated file,
then select **Slate Rose** using **Preferences: Color Theme**. The manifest
supports VS Code 1.143 and newer. The initial four fixtures were reviewed in
VS Code 1.143.1; JavaScript, JSX, and TSX were reviewed in 1.146.0. See the
[initial review](previews/vscode/README.md), [web review](previews/vscode/web/README.md),
[workbench review](previews/vscode/workbench/README.md), and [VS Code mappings](docs/vscode-mappings.md) for observations and provider
limitations. These reviews do not cover every intermediate version or host.
Owner acceptance remains pending.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the workflow and local checks.
[OpenSpec](openspec/README.md) contains the backlog and specifications; the
first implementation checklist is
[add-vscode-editor-theme](openspec/changes/add-vscode-editor-theme/tasks.md).

## License

Slate Rose is licensed under the [MIT License](LICENSE).
