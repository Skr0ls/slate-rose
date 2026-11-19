## Tasks

- [x] Verify the existing release JAR with the current package checker and Plugin Verifier on the installed Rider and IntelliJ IDEA builds.
- [x] Add the approved rose as a JetBrains SVG logo, include it in the JAR, and verify reproducible packaging for the new candidate.
- [x] Prepare English listing copy, change notes, MIT and source links, and representative screenshots. Confirm the intended Vendor profile and listing channel with the maintainer.
- [ ] Verify the candidate against the intended IDE builds. Check installation and selection of the full plugin in IntelliJ IDEA.
- [ ] Hand the verified JAR and listing assets to the maintainer for upload. Record Marketplace approval and installation once available.

## Baseline verification

The [preview.2 release](https://github.com/Skr0ls/slate-rose/releases/tag/v0.1.0-preview.2)
JAR passed the repository package check. Its SHA-256 is
`1d704d9ee610146779dd071a4d2a0c6bd6960098d4c3a1268e2c531582233e12`.

JetBrains Plugin Verifier 1.411 reported plugin
`com.github.skr0ls.slaterose:0.1.0` compatible with Rider
`RD-262.11879.110` and IntelliJ IDEA `IU-263.7307.112`. The verifier warned
about missing layout entries in the local IDE installations and reported
no plugin incompatibilities for these builds. The candidate with the logo
will be checked separately.

## Marketplace candidate

The `0.1.1` JAR contains the 40 by 40 SVG logo and passed reproducible
packaging and Plugin Verifier 1.411 on Rider `RD-262.11879.110` and IntelliJ
IDEA `IU-263.7307.112`. Both results were `Compatible`. SHA-256
`b6dfd2a08d6885ce23880a49241b889a81f26b1d49688e2a824156ba76252af8`.
Both the editor scheme and UI theme resources match the baseline JAR byte for
byte. IntelliJ IDEA loaded `0.1.1` in a disposable profile and listed Slate
Rose in its theme selector.

The maintainer chose `Skr0ls` and the Stable channel. Vendor creation is
pending. The [listing handoff](../../../packages/jetbrains/marketplace.md)
contains the copy, license and source links, and the verified Rider screenshot.
