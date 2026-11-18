# Design

Add a packaging job to the existing Quality workflow. Check for stale
generated output, validate against the official Zed v0.2.0 schema with a
pinned validator, and upload the theme package using the existing
`upload-artifact` action. GitHub's artifact archive holds the manifest,
license, guide and theme at the relative paths Zed expects. A contributor
extracts it to a stable directory and selects that directory in Zed.
Registry submission remains a release task.
