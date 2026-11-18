# Tasks

## 1. Baseline and fixtures

Implementation base and PR 7 merge: `8399f2cfd33328173906ee2a00145b15762d86bf`, on `feature/php-ruby-validation` from `origin/dev`.

- [x] 1.1 Verify PR 7 is merged and the implementation branch starts from updated `origin/dev`; record the base commit without carrying pre-rebase commits.
- [x] 1.2 Add PHP and Ruby fixtures and role/context guidance; verify applicable constructs are present, run Ruby syntax checking, and explicitly record unavailable PHP lint rather than claiming it passed.

## 2. Installed editor review

- [x] 2.1 Build and install the local VSIX in an isolated profile; verify generated, packaged and installed theme JSON match byte-for-byte and record hashes and host version.
- [x] 2.2 Review lexical colors in exact `php` and `ruby` modes with built-in provider versions; save native screenshots and questionable-token inspections with captions matching the pictured tokens.
- [x] 2.3 Query semantic legend/token availability for each fixture after language activation; record actual outcomes and inspect displayed semantic colors if tokens exist, otherwise explicitly report semantic unavailability in this profile.

## 3. Corrections and integration

- [x] 3.1 Correct only observed PHP/Ruby mapping discrepancies with narrow selectors and regression checks, or verify generation is unchanged; document limits, preserve palette bytes, and repeat affected native review after rebuilding and reinstalling any correction.
- [x] 3.2 Run documented validator, generator build/check, unit tests, hooks, strict OpenSpec validation and VSIX checks; verify repeated fixed-metadata packaging is byte-identical and document results.
- [x] 3.3 Obtain independent read-only review, resolve findings and re-review meaningful changes; verify evidence and checklist accurately reflect completed work and remaining provider coverage.

## Workflow follow-up

- Archive after owner review and merge, retaining the durable capability spec.
- Keep third-party PHP/Ruby language-server validation queued if unavailable in this built-in review.
