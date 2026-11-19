## ADDED Requirements

### Requirement: JetBrains Marketplace package handoff

The JetBrains theme package SHALL include the Slate Rose plugin logo and
the metadata needed for its first Marketplace submission.

#### Scenario: Package the plugin logo

- **WHEN** the JetBrains theme package is built for Marketplace
- **THEN** the resource-only JAR contains a 40 by 40 SVG at `META-INF/pluginIcon.svg`
- **AND** the package retains its plugin ID, theme provider, and MIT notice

#### Scenario: Verify the submission candidate

- **WHEN** the first submission is prepared
- **THEN** the candidate passes package checks and Plugin Verifier on the listed IDE builds
- **AND** the maintainer receives the verified package, listing text, representative screenshots, and license and source links
