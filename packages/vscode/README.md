# Slate Rose

Slate Rose is a prototype dark editor, workbench and terminal theme. Install the local VSIX using
**Extensions: Install from VSIX...**, then choose **Preferences: Color Theme**
and select **Slate Rose**. The package targets VS Code 1.143 and newer;
documented reviews cover 1.143.1 and 1.146.0, not every intermediate version
or host.

The intended syntax roles are sand types, blue functions, rose fields, lilac
declarations, coral flow control and green strings. Language providers can
classify tokens differently. Four standalone fixtures were reviewed in VS Code
1.143.1 with specific providers. JavaScript, JSX, and TSX were reviewed in
1.146.0; see the [initial review](https://github.com/Skr0ls/slate-rose/blob/dev/previews/vscode/README.md)
and [web review](https://github.com/Skr0ls/slate-rose/blob/dev/previews/vscode/web/README.md)
for observations and limitations.

C# semantic keyword tokens can override the lexical primitive and flow colors;
the theme retains semantic highlighting without a generic keyword override,
which cannot distinguish those roles. The owner accepted the workbench appearance and the separate ANSI design; a representative
[native workbench review](https://github.com/Skr0ls/slate-rose/blob/dev/previews/vscode/workbench/README.md)
records tested states, contrast observations and remaining coverage. Native terminal acceptance remains pending. Modern UI shell gutters, floating-card borders and supported custom
title bars use the theme palette without changing window settings or controls.
The separate approved ANSI palette colors the integrated terminal; the
[terminal review](https://github.com/Skr0ls/slate-rose/blob/dev/previews/vscode/terminal/README.md)
records native states and host contrast/bold behavior. This package is not published to the Marketplace.

## Build from source

Use Node.js 22 or newer and Python 3.11 or newer. Run these commands
from the repository root.

```sh
python -m generators check vscode
mkdir -p dist
(cd packages/vscode && SOURCE_DATE_EPOCH=1794787200 TZ=UTC npx --yes @vscode/vsce@4.1.1 package --no-dependencies --out ../../dist/slate-rose.vsix)
python scripts/check_vsix.py dist/slate-rose.vsix
```

Licensed under the MIT License; see the included LICENSE notice.
