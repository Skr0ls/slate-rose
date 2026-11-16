# Tasks

## 1. Validated palette and generation

- [x] 1.1 Add the exact approved terminal source and shared strict loader entrypoint; verify canonical loading is immutable and malformed metadata, token sets, hex, JSON and duplicate keys fail through focused tests while the original palette bytes remain unchanged.
- [x] 1.2 Integrate both inputs into validation/build/check and protect selected/canonical source aliases; verify invalid terminal input fails before output changes or directory creation and collision/stale-check tests preserve bytes, with documented CLI flags.
- [x] 1.3 Generate the sixteen ANSI and ten terminal UI mappings using supported keys; verify emitted values, existing syntax/UI preservation and deterministic build/check, and document exact mappings, approval and host contrast/bold limitations.

## 2. Native terminal review

- [x] 2.1 Build the final fixed-metadata VSIX twice and install in an isolated profile; record source hashes, identical package bytes, generated/packaged/installed theme identity and native color export matches.
- [x] 2.2 Review controlled foreground/background, normal/bright, bold/reverse/default text, cursor, active/inactive selection and search in the native integrated terminal; retain reproducible display-only helper, screenshots, effective settings and an honest coverage/contrast matrix without executing shell fixtures or changing product settings.

## 3. Integration

- [x] 3.1 Run complete validator, generator build/check, tests, hooks, strict OpenSpec and VSIX checks; confirm accepted palettes, prior UI/syntax and generated output remain consistent.
- [x] 3.2 Obtain independent read-only review of implementation, native evidence and final package, resolve findings and re-review meaningful corrections; verify checklist completion reflects final results.

## Workflow follow-up

- Review this terminal commit against workbench base b4bd009; rebase/retarget to dev after the workbench branch lands, without carrying pre-rebase history forward.
- Do not auto-merge or publish; archive after owner review and integration.
- Continue with the Zed adapter after the VS Code terminal slice.
