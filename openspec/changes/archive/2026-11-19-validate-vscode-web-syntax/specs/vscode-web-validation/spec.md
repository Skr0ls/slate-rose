# Spec Delta

## Purpose

Provide verifiable VS Code highlighting evidence for representative JavaScript, JSX, and TSX syntax.

## ADDED Requirements

### Requirement: Representative web syntax fixtures
The project SHALL provide one small fixture each for JavaScript, JSX, and TSX that exercises applicable approved syntax roles.

#### Scenario: Fixture coverage
- **WHEN** each fixture is inspected
- **THEN** it exposes functions, variables, properties, declarations, flow control, strings, numbers, member access, and constant bindings where applicable; TSX also exposes types, and JSX and TSX separately expose component and intrinsic tags, attributes, props, and embedded expressions

### Requirement: Review of installed artifact
The web syntax review SHALL use an isolated VS Code profile and an installed package whose theme JSON file is verified byte-identical to the source-generated theme JSON.

#### Scenario: Artifact identity
- **WHEN** the fixtures are reviewed
- **THEN** the evidence records the artifact identity and comparison result, VS Code version, exact language modes, provider and provider version, and project context

### Requirement: Separate lexical and semantic evidence
The project SHALL record a separate lexical and semantic outcome for each fixture and SHALL distinguish passed, limited, blocked, and unreviewed outcomes.

#### Scenario: Provider available
- **WHEN** the applicable built-in language service supplies semantic tokens
- **THEN** the review examines lexical and semantic results separately and records observations and screenshots for that file

#### Scenario: Provider unavailable or uncertain
- **WHEN** semantic token availability or provider resolution cannot be established
- **THEN** the report records the limitation or block and does not claim semantic review passed

### Requirement: Approved roles and constrained corrections
The review SHALL compare applicable tokens with approved palette roles, document unsupported distinctions, and restrict any mapping correction to an evidenced issue in the three reviewed syntaxes.

#### Scenario: Highlighting discrepancy
- **WHEN** a problematic token is observed
- **THEN** its scope or semantic token and displayed result are recorded, and any correction preserves the approved palette and avoids generic semantic keyword overrides and globally disabling semantic highlighting

#### Scenario: Corrected artifact
- **WHEN** a mapping correction changes the theme artifact
- **THEN** the corrected package is rebuilt and reinstalled, its installed theme JSON identity is verified, and affected lexical and semantic inspections and screenshots are refreshed so the reported outcomes describe the final artifact

### Requirement: Review evidence is honest
The report SHALL identify screenshots as manual evidence and SHALL avoid claiming coverage for unreviewed languages or unavailable provider behavior.

#### Scenario: Incomplete review
- **WHEN** any fixture or highlighting layer remains limited, blocked, or unreviewed
- **THEN** the report states that status and its reason rather than presenting it as passed or claiming completion of the broader web-language batch
