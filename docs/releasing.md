# Prepare a Slate Rose release

The Quality workflow assembles three installable files as
`slate-rose-release-assets` after the host package jobs pass.

| Asset | Use |
| --- | --- |
| `slate-rose.vsix` | [VS Code extension](../packages/vscode/README.md) |
| `slate-rose-jetbrains.jar` | [JetBrains plugin](../packages/jetbrains/README.md) |
| `slate-rose-zed.zip` | [Zed development extension](../packages/zed/README.md) |

## Release versioning

Git tags track the Slate Rose release across editors. Each editor package has
its own manifest version.

For each preview or release candidate, promote `dev` to `main` through a
pull request. Tag the commit after its Quality push run passes and publish
the three verified packages as a GitHub pre-release.

1. Use `v0.1.0-preview.1` for the initial preview. Begin release candidates
   once all three packages can be installed using the release instructions
   and there are no known release blockers.
2. Tag the first candidate `v0.1.0-rc.1`. Promote any blocking fixes through
   the same flow and tag the next candidate `v0.1.0-rc.2`, incrementing the
   suffix as needed.
3. Once a candidate passes acceptance, tag its exact commit `v0.1.0` and
   publish the stable release with the files attached to the accepted
   candidate.
4. At stable release, create `release/0.1` from `v0.1.0`. Keep one branch
   per released series for patches such as `v0.1.1` while development of
   the next series continues on `dev`.

The current draft workflow accepts Quality bundles from pushes to `main`.
Before shipping patches from a maintenance branch, extend the workflow to
verify and select bundles built on that branch.

## Platform coverage

All three packages are available in CI for a preview release. The package
guides record the tested editor versions and context.

| Platform | Verified scope | Open acceptance |
| --- | --- | --- |
| VS Code | Local VSIX, editor, and accepted workbench slice | Native terminal acceptance and broader workbench states |
| JetBrains | Resource plugin and scheme with bounded Rider and IntelliJ evidence | Compatibility across additional IDEs and builds |
| Zed | Development extension installed on Zed 1.28.1, TypeScript editor smoke | Completion, search, tabs, and panel review |

## Draft workflow

The **Draft release** workflow becomes available when its file lands on
`main`, the default branch. Run it on `main` with the existing release
tag and leave **dry_run** enabled for the first pass. The summary identifies
the tagged commit, the selected successful Quality run and the verified
assets. If there is no matching run, check the Quality workflow for the
tagged commit. Disable **dry_run** only when ready to create the draft.
Keep the release tag fixed during preparation. The workflow rechecks the tag's
commit immediately before draft creation.

Review the draft in GitHub Releases before publishing. Select **This is a
pre-release** for previews and release candidates. If an upload fails
after creating the draft, attach the missing files from the verified bundle
in the Releases UI. An existing draft blocks another automated creation.

## Manual fallback

1. Bring the release commit onto `main` using the
   [release promotion flow](../CONTRIBUTING.md#git-workflow). Use an approved
   tag already pushed to GitHub and pointing to that commit.
2. Open a successful [Quality run](https://github.com/Skr0ls/slate-rose/actions/workflows/quality.yml)
   triggered by a push to `main` whose head SHA matches the tag's commit. Download its
   `slate-rose-release-assets` artifact and extract the three files.
3. Create a draft release for the existing tag and attach the three files.
   From the extracted directory, set `tag` to the approved tag, then run
   the following command. Add `--prerelease` for previews and release candidates.

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
