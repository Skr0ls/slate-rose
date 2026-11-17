# Design

## Context

See proposal.md. The deterministic Python adapter emits language-default class, function, property and keyword attributes, inheriting host-specific categories. The existing isolated IDEA project has Java SDK 25 and a manually imported Slate Rose editor scheme. Kotlin plugin 263.7307.112-IJ and offline Kotlin 2.4.10 libraries/compiler are installed with IDEA.

## Goals / Non-Goals

Review one Kotlin/JVM fixture in one installed IDEA build. Preserve palette, generators, generated editor/UI artifacts, highlighting preferences and historical fixtures. No Swift, Zed, Kotlin multiplatform, broad keyword recoloring or new plugin installation in this change.

## Decisions

- Add `fixtures/jetbrains/TypeRoles.kt`: original, self-contained package `preview`, covering Int/String/Boolean/Float declarations and uses, nullable/generic types, Unit type/value, typealias declaration/use, class/fun/val/var, if/when/return/throw, contextual get/field. Use named standard types rather than treating them as Java/C# primitive aliases. Avoid a main function or executing fixture code.
- Reuse the already trusted `/tmp/sr-jb-review/projects/idea` and isolated IDEA profile. Attach only installed Kotlin stdlib when required, with disposable project/library instructions; verify SDK/source root, Kotlin mode/plugin/language context, class resolution, indexing and selected editor scheme before evidence capture. Optional offline compilation does not execute the fixture. Record unavailable context explicitly instead of claiming semantic verification.
- Audit pinned official Kotlin keyword/type references plus bounded installed highlighter/annotator registrations. Inspect representative types, aliases, Unit contexts and keyword controls with Jump to Colors and Fonts. Keep source/lexical findings separate from native project-aware results; not every repeated occurrence needs a separate inspector visit. Report visual-only occurrences honestly.
- Deliver `previews/jetbrains/kotlin-types/README.md`, compact verification JSON with fixture/scheme/relevant JAR/capture hashes, and at most two unmodified captures. Record host/plugin/tool versions, category/key/fallback, appearance, status and reproduction instructions. Exact file values are distinct from visual runtime appearance. Keep source links and metadata proportional to the findings.
- Update only the Kotlin backlog entry, retaining unreviewed hosts/contexts. Completion means every selected construct is accounted for, including a documented limitation if applicable. A verified narrow mapping candidate is follow-up work, not automatic behavior change in this review.

## Risks / Trade-offs

- Unresolved stdlib types resemble classification failures -> attach installed stdlib and verify project-aware resolution first.
- Kotlin keyword and annotator layers can overlap -> inspect native categories and installed registrations; do not infer keys from text or color alone.
- Java review is integrated -> keep the Kotlin review independently scoped and preserve the Java evidence.
- Review evidence can become oversized -> group equivalent occurrences in one table and cap captures at two.
