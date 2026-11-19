# Codex instructions — Slate Rose

Read `README.md` and `palette/colors.json` before editing.

## Source of truth
- The user explicitly approved **Slate Rose v0.2 Contrast**. Treat every value in `palette/colors.json` as immutable unless the user asks to change it.
- Do not claim this is an existing Neovim theme or that the original colors were recovered from source.
- Describe design provenance neutrally; do not claim visual originality or uniqueness.
- Preserve the semantic distinction: types sand, functions blue, fields rose, declarations lilac, flow-control coral, strings green.
- No unrequested palette variants or automatic contrast-adjustment of approved colors.

## Engineering
- Keep theme generators deterministic and generated artifacts reproducible.
- Prefer simple, documented data structures over a large framework.
- Validate token names and hex values; fail loudly on invalid input.
- Keep host-specific mappings separate; never assume VS Code, Zed, JetBrains and Visual Studio share the same schema.
- Consult current official host schemas/docs before generating native theme files; do not invent unsupported keys.
- Add small fixture snippets in C++, C#, TypeScript and Python.
- Avoid vendoring or copying third-party theme assets.
- Document unavoidable semantic-highlight limitations and provisional UI token choices.

## Working process
- Implement in small reviewable steps. Begin with one functioning editor theme rather than building all platforms at once.
- Before changing palette or making a significant design choice, explain the tradeoff and request approval.
- At the end of each step report tests, installation steps, and unresolved TODOs.

## Release publishing
- A human maintainer initiates public releases by default. An agent may initiate a public release only after a human maintainer separately and explicitly asks the agent to publish that specific release.
- Agents may build and verify packages, prepare unpublished drafts, and run dry runs. For preparation requests, hand off the verified draft or workflow inputs to the maintainer.
- Treat general requests to implement a plan, prepare a release, or verify a workflow as preparation. The separate request applies to publishing drafts, uploading to a public marketplace, running or rerunning a workflow in publish mode, and pushing or merging changes that trigger publication. It covers public previews and updates as well as stable releases.

## Suggested first task
Implement a palette validator and a VS Code editor-only theme generator, with fixtures and instructions. Keep JetBrains, Zed and Visual Studio as subsequent adapters.

## Collaboration and Git
- Follow [CONTRIBUTING.md](CONTRIBUTING.md) for branch flow, task delegation, independent review, and local checks.
- Keep OpenSpec's active checklist as the source of truth; archive completed changes with durable specs retained.
- Only the initial bootstrap may go directly to `main`; subsequent changes use small feature pull requests into `dev`.
