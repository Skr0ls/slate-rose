# Proposal

## Why

The next language-backlog item is Swift type and keyword classification. Java and Kotlin findings do not establish Swift grammar or SourceKit-LSP behavior in VS Code.

## What Changes

- Add one original Swift fixture and minimal disposable SwiftPM library instructions.
- Review lexical scopes and available semantic categories in one isolated VS Code profile, recording context and limitations.
- Update the Swift backlog entry with bounded evidence and any narrow mapping candidates.
- Record Xcode as a future adapter candidate, as requested during this review.

## Capabilities

### New Capabilities

None. This fixture/evidence change sets `skip_specs: true`.

### Modified Capabilities

None. Theme output remains unchanged; a demonstrated mapping defect is separate follow-up work.

## Impact

Swift fixture, disposable setup, concise evidence/metadata, at most two raw captures and OpenSpec tracking. Reuse installed Apple Swift 6.4 and install the official Swift extension only in a disposable VS Code profile. Start from updated dev after Kotlin PR #18 integrates.
