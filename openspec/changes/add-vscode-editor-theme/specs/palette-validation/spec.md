# Spec Delta

## Purpose

Ensure the canonical Slate Rose palette can be safely consumed by every editor adapter without silently accepting invalid input.

## ADDED Requirements

### Requirement: Validate palette structure and tokens
The validator SHALL require the palette metadata and all 24 approved token names, reject unknown or duplicate token names, and accept color values only in six-digit #RRGGBB hexadecimal format.

#### Scenario: Approved palette
- **WHEN** the validator reads the current palette/colors.json
- **THEN** validation succeeds without rewriting the file

#### Scenario: Invalid input
- **WHEN** the input is malformed JSON, has invalid metadata, missing, unknown or duplicate tokens, or invalid hex values
- **THEN** validation exits nonzero with an actionable error identifying the problem

### Requirement: Preserve the approved source
Validation and generation SHALL leave the canonical palette byte-for-byte unchanged and SHALL NOT automatically adjust approved colors.

#### Scenario: Generation completes
- **WHEN** any build or validation command finishes
- **THEN** palette/colors.json retains its original bytes
