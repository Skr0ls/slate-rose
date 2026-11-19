## Tasks

- [x] Verify the existing release JAR with the current package checker and Plugin Verifier on the installed Rider and IntelliJ IDEA builds.
- [ ] Add the approved rose as a JetBrains SVG logo, include it in the JAR, and verify reproducible packaging for the new candidate.
- [ ] Prepare English listing copy, change notes, MIT and source links, and representative screenshots. Confirm the intended Vendor profile and listing channel with the maintainer.
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
