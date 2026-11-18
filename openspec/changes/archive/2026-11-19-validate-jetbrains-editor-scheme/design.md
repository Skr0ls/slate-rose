# Design

## Context

The generated `.icls` covers Language Defaults; language plugins can supply overrides. Installed hosts are Rider 2026.2.4 and IntelliJ IDEA 2026.3 RC. Their native rendering is not established by XML tests.

## Goals / Non-Goals

Verify import, representative syntax, caret/current line and selection in each host. Keep mapping changes in a separate evidence-driven PR.

## Decisions

- Reuse `fixtures/showcase.cs` in a minimal SDK project and add one small Java analogue. Work in disposable copies under `/tmp`, not application code or the user's projects.
- Prefer separate config/system/plugin/log directories through documented platform properties. Do not copy accounts or credentials into test profiles; activation blockers remain explicit.
- Import the exact generated file through Settings, then inspect representative type, function, field, keyword, primitive/control and literal examples. Record observed colors separately from intended roles. UI selection of a category can support a classification claim; a screenshot alone does not prove an exact effective key/RGB.
- Retain one overview PNG per host and a concise evidence table with scheme/fixture hashes, versions, import steps and provider limitations. Extra captures are limited to evidence needed for a specific finding. No helper plugin or screenshot matrix.

## Risks / Trade-offs

- Fresh profiles can encounter licensing/onboarding/trust gates -> report the actual blocker and leave affected checks open; do not substitute another host for required native evidence.
- Language defaults can lose role distinctions -> record concrete examples for the next mapping fix; do not claim semantic parity.
- User profile settings can affect rendering -> record the actual review context and any temporary display changes.
