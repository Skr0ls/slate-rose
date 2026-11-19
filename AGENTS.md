# Slate Rose agent rules

## Theme changes

- Before editing a theme, read [README.md](README.md) and the [approved palette](palette/colors.json). Preserve its values and semantic roles. Obtain maintainer approval before changing colors, adding variants, or making significant design choices.
- Keep generators deterministic and host mappings separate. Validate palette tokens and hex values, check current official host schemas, and document semantic highlighting limits and provisional UI choices.
- Describe provenance neutrally. Avoid copying third-party theme assets or claiming visual originality, Neovim provenance, or recovery from upstream source.

## Workflow

- Follow [CONTRIBUTING.md](CONTRIBUTING.md) for Git, OpenSpec, agent review, and local checks. Write code and repository documentation in English.
- Report verification results, installation steps where relevant, and any remaining limitations.

## Public releases

- A human maintainer publishes by default. An agent may publish a specific release only after a human maintainer separately and explicitly requests that public action.
- Treat general implementation, release preparation, and verification requests as permission to build packages, prepare unpublished drafts, and run dry runs. Hand off the verified draft or workflow inputs for publication.
- Require the same explicit request for previews, GitHub Releases, marketplace submissions, and any workflow run, push, or merge that triggers public publication.
