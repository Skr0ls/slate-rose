# Proposal

## Why

People trying the Zed theme need an installable download from CI.

## What Changes

Publish the existing theme directory as a GitHub Actions artifact after
checking the generated JSON against Zed's official schema.

## Capabilities

### Modified Capabilities

- `zed-theme` provides a validated, downloadable development extension.

## Impact

The Quality workflow and Zed installation guide.
