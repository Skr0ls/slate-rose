# Proposal

## Why

Release preparation should select the validated packages for the release commit without downloading and attaching them by hand.

## What Changes

Add a manual draft-release workflow that checks an existing tag and validates the source CI run before attaching the three assets.

## Capabilities

### Modified Capabilities

- `release-assets` supports creating a draft GitHub Release from the validated bundle.

## Impact

GitHub Actions and the maintainer release guide.
