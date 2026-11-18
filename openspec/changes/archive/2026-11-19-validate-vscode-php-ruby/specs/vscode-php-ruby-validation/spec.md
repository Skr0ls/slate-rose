# Spec Delta

## Purpose

Provide reproducible evidence for built-in PHP and Ruby highlighting in VS Code while making provider and runtime validation limits explicit.

## ADDED Requirements

### Requirement: Representative fixtures
The project SHALL provide small PHP and Ruby fixtures exposing applicable approved syntax roles without requiring application frameworks.

#### Scenario: Fixture inspection
- **WHEN** either fixture is opened in its documented language mode
- **THEN** it exposes types, functions, fields, variables, constants, declarations, control flow and literals where the language supports those distinctions

### Requirement: Installed lexical review
The review SHALL verify installed theme JSON identity and record native lexical observations, actual editor and built-in provider versions, language modes, screenshots and relevant scope inspections for both fixtures.

#### Scenario: Review evidence
- **WHEN** a fixture is reviewed in an isolated profile
- **THEN** the report identifies the fixture, artifact, context, observed colors and unsupported distinctions without claiming unreviewed provider coverage

### Requirement: Explicit semantic availability
The review SHALL query semantic-token availability separately for PHP and Ruby and distinguish reviewed, unavailable, limited and blocked semantic outcomes.

#### Scenario: No semantic provider
- **WHEN** the selected built-in profile returns no semantic provider or tokens
- **THEN** the report records the actual query result and does not claim semantic review passed

#### Scenario: Semantic provider available
- **WHEN** a provider supplies semantic tokens
- **THEN** actual token classifications and their native displayed colors are inspected and recorded separately from lexical results

### Requirement: Narrow verified corrections
Any mapping correction SHALL preserve palette bytes, remain limited to evidenced PHP/Ruby scopes, and include regression checks and updated native evidence from the rebuilt and reinstalled final theme.

#### Scenario: Corrected artifact
- **WHEN** an observed discrepancy leads to a mapping correction
- **THEN** generated, packaged and installed theme JSON match, affected inspections are repeated, and the report describes the final artifact

### Requirement: Honest validation boundaries
The report SHALL distinguish syntax checks, automated artifact checks and manual visual evidence, including unavailable tools and third-party providers.

#### Scenario: Runtime absent
- **WHEN** a language runtime is unavailable
- **THEN** its syntax check is recorded as unavailable rather than passed, and visual highlighting is not presented as proof of program validity
