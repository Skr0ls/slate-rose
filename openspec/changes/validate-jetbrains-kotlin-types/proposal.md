# Proposal

## Why

The language backlog calls for checking Kotlin type and keyword roles before extending editor coverage. Java and C# findings cannot establish how the Kotlin provider classifies built-in classes or contextual words.

## What Changes

- Add one original Kotlin fixture and disposable project setup instructions.
- Review its lexical and project-aware categories in the existing isolated IntelliJ profile, documenting evidence and limitations.
- Update only the Kotlin backlog entry with the bounded result.

## Capabilities

### New Capabilities

None. This fixture and evidence change declares `skip_specs: true`.

### Modified Capabilities

None; palette, mappings and generated output remain unchanged. An observed mapping defect requires a separate implementation change.

## Impact

Kotlin fixture, review notes, at most two raw captures, verification metadata and OpenSpec tracking. Reuse installed Kotlin/JDK resources without adding project dependencies to the repository. This Kotlin review is independent of the integrated Java review and preserves its evidence.
