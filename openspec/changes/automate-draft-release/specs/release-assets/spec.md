## ADDED Requirements

### Requirement: Verify and draft a release on demand

The release workflow SHALL verify a tag on main and select a successful Quality bundle from the same commit.

#### Scenario: Preview a release

- **WHEN** a maintainer dispatches the workflow in dry-run mode
- **THEN** the workflow reports the selected commit and verifies the three assets with read permissions

#### Scenario: Create a draft

- **WHEN** the maintainer explicitly disables dry-run and verification succeeds
- **THEN** the workflow creates an unpublished draft for the existing tag and attaches the verified assets
- **AND** an existing release remains intact
