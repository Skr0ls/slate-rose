# Prepare a Slate Rose release

The Quality workflow assembles three installable files as
`slate-rose-release-assets` after the host package jobs pass.

| Asset | Use |
| --- | --- |
| `slate-rose.vsix` | [VS Code extension](../packages/vscode/README.md) |
| `slate-rose-jetbrains.jar` | [JetBrains plugin](../packages/jetbrains/README.md) |
| `slate-rose-zed.zip` | [Zed development extension](../packages/zed/README.md) |

## GitHub Releases

1. Bring the release commit onto `main` using the
   [release branch flow](../CONTRIBUTING.md#git-workflow). Use an approved
   tag already pushed to GitHub and pointing to that commit.
2. Open a successful [Quality run](https://github.com/Skr0ls/slate-rose/actions/workflows/quality.yml)
   whose head SHA matches the tag's commit. Download its
   `slate-rose-release-assets` artifact and extract the three files.
3. Create a draft release for the existing tag and attach the three files.
   From the extracted directory, set `tag` to the approved tag, then run

   ```sh
   gh release create "$tag" --repo Skr0ls/slate-rose --verify-tag --draft \
     --generate-notes slate-rose.vsix slate-rose-jetbrains.jar slate-rose-zed.zip
   ```
4. Review the notes, versions, and installation links before publishing.
   See the [GitHub release guide](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
   and [CLI options](https://cli.github.com/manual/gh_release_create).

## Editor marketplaces

- **VS Code Marketplace**. Confirm ownership of the manifest's publisher ID
  and prepare listing metadata before publishing the VSIX. Set up publishing
  credentials when the publisher is ready. [Publishing guide](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)
- **JetBrains Marketplace**. Set up the vendor profile and verify the plugin
  and its compatibility against the intended IDE builds. Prepare listing
  metadata and submit the approved build. [Plugin upload guide](https://plugins.jetbrains.com/docs/marketplace/uploading-a-new-plugin.html)
- **Zed Extensions**. Submit the approved repository commit to
  `zed-industries/extensions` with `path = "packages/zed"` and the version
  from `extension.toml`. Zed packages the extension from that repository
  entry. [Registry publishing guide](https://zed.dev/docs/extensions/publishing/publishing-guide)
