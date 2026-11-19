## Context

The resource-only JetBrains JAR in preview.2 already installs from disk.
Plugin Verifier 1.411 reported it compatible with the installed IntelliJ
IDEA and Rider builds. The JAR has no Marketplace logo.

## Decisions

Adapt the approved Slate Rose mark to the JetBrains 40 by 40 SVG logo
format. Keep the resource-only JAR and add the logo to its explicit package
inputs. Bump the package to 0.1.1 when the logo changes the published 0.1.0
artifact.

Use Plugin Verifier on Rider build 262.11879.110 and IntelliJ IDEA build
263.7307.112. Check the full packaged theme in IntelliJ IDEA and use the
existing Rider screenshots where they faithfully represent the candidate.
Record the exact JAR and host builds for the maintainer.

Provide the approved candidate and listing assets for manual submission.
Marketplace approval and installation from its listing are follow-up checks.
