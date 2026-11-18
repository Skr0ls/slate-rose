# Tasks

- [x] 1.1 Implement release asset assembly and deterministic Zed ZIP packaging.
- [x] 1.2 Update installation, release instructions and the follow-up backlog.
- [x] 1.3 Validate locally, obtain independent review and verify the CI bundle.

## Verification

The [first release asset run](https://github.com/Skr0ls/slate-rose/actions/runs/44401212238)
uploaded the three named files in `slate-rose-release-assets`. The downloaded
VSIX and JAR matched their original job artifacts byte for byte. The Zed
ZIP matched the local deterministic build and contained the four expected
extension files with their original contents.
