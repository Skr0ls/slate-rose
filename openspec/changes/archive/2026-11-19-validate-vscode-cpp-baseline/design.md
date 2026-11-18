# Design

## Context

The initial C++ fixture review used VS Code 1.143.1 and Microsoft C/C++ 1.35.6 with IntelliSense ready.

## Goals / Non-Goals

Refresh the evidence for the same fixture in the isolated VS Code profile. Keep mappings, palette and fixture unchanged.

## Decisions

- Tokenize the fixture with the installed TextMate grammar and compare its scopes with the generated theme. Verify syntax without running the fixture.
- Inspect the native editor with Microsoft C/C++ in the isolated profile. Record versions, fixture and theme hashes, effective categories and colors where available, and any limitations. Keep evidence to one raw capture.
- Update the C++ baseline entry and keep any mapping changes in separate work.

## Risks / Trade-offs

Classifications vary with provider and project context. Record the actual context and keep lexical evidence distinct from native observations.
