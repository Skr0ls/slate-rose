## Design

Dispatch from main after publishing a GitHub Release. Resolve the exact tag
and select its successful Quality push run on main. Compare the release VSIX
to the Quality bundle and run the package checker from the tagged commit.

Dry-run stops after verification. On a publish dispatch, transfer the verified
file and recheck its digest in the publish job. Only that job requests an OIDC
token. The Marketplace policy binds the publisher to the workflow in the
`vscode-marketplace` environment.
