# Design

## Context

The original fixture was reviewed in VS Code 1.143.1 with bundled TypeScript 6.0.3 and no explicit project configuration.

## Goals / Non-Goals

Review the existing fixture in one installed VS Code build. Keep fixture, palette, and theme output unchanged.

## Decisions

- Inspect named and built-in types, functions, properties, declarations, flow control, constants, and strings. Compare TextMate scopes, language-service classifications, and representative native inspector readings when the isolated profile is accessible. Record any missing native evidence explicitly.
- Record the fixture and theme hashes, host and provider versions, context, and bounded findings. Capture at most one native screenshot if inspection succeeds.
- Update TypeScript progress in the baseline item; keep any genuine mapping changes in a separate PR.

## Risks / Trade-offs

Provider responses alone do not establish the final editor color. Identify the source of each observation.
