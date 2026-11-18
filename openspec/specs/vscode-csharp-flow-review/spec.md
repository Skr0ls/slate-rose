# vscode-csharp-flow-review Specification

## Purpose

Define how VS Code colors C# semantic control keywords.

## Requirements

### Requirement: Color C# semantic control keywords

The VS Code theme SHALL assign the approved control foreground to the `controlKeyword` semantic type in C#.

#### Scenario: Compare control and declaration words

- **WHEN** the Microsoft C# provider assigns `controlKeyword` to a statement in the fixture
- **THEN** the theme renders it coral
- **AND** `public` retains its lilac foreground through the ordinary `keyword` category
- **AND** the lexical fallback and generic keyword mapping retain their existing behavior
