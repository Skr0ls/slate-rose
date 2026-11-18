## ADDED Requirements

### Requirement: Publish the verified VSIX on demand

The VS Code publication workflow SHALL publish the VSIX from an existing
GitHub Release after matching it to the successful Quality bundle for the tag.

#### Scenario: Verify a Marketplace publication

- **WHEN** a maintainer dispatches verification from main for a published release
- **THEN** the workflow verifies the package identity, version, and bytes
- **AND** dry-run ends after reporting the verified version and SHA-256

#### Scenario: Publish a verified package

- **WHEN** a maintainer requests publication and verification succeeds
- **THEN** the workflow publishes the verified VSIX to the regular Marketplace channel using Trusted Publishing

#### Scenario: Refuse unverifiable packages

- **WHEN** the tag or published release cannot be verified, or the VSIX is missing or differs from the Quality bundle
- **THEN** the workflow fails before the publication job runs
