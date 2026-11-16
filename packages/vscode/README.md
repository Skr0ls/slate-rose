# Slate Rose

Slate Rose is a prototype dark editor and workbench theme. Install the local VSIX using
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
for observations and limitations. Owner acceptance remains pending.

C# semantic keyword tokens can override the lexical primitive and flow colors;
the theme retains semantic highlighting without a generic keyword override,
which cannot distinguish those roles. Workbench mappings are provisional; a representative
[native workbench review](https://github.com/Skr0ls/slate-rose/blob/dev/previews/vscode/workbench/README.md)
records tested states, contrast observations and remaining coverage. Owner acceptance
remains pending. This package is not published to the Marketplace.

Licensed under the MIT License; see the included LICENSE notice.
