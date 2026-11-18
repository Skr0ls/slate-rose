# Design

## Context

The current VS Code adapter has explicit lexical/semantic mappings, deterministic packaging and prior native review evidence. Installed built-in PHP grammar/features and Ruby grammar manifests are version 10.0.0. Ruby 2.6.10 is available for syntax checks; PHP CLI is absent. See proposal.md for motivation.

## Goals / Non-Goals

**Goals:** Reproduce the built-in PHP/Ruby experience and distinguish observed colors from unavailable semantic classifications.

**Non-Goals:** Installing runtimes, gems or third-party language servers; claiming coverage of all providers; changing other hosts, palette values or unrelated language mappings.

## Decisions

1. Use one self-contained `showcase.php` and `showcase.rb`, with no application framework. Cover classes, methods, fields, parameters, local variables, constants, declarations, control flow, strings, numbers and interpolation where meaningful. Ruby syntax must parse with the available Ruby version. PHP uses ordinary typed class syntax; lack of PHP runtime validation is recorded rather than hidden.
2. Use an isolated profile containing the theme and built-in language extensions. Exact modes are `php` and `ruby`; record grammar/feature IDs, versions and actual host version. This baseline avoids making provider installation part of a theme change. Query the documented semantic-token commands after language activation; persist results and errors. An absent provider is an unavailable outcome, not a semantic pass. Full PHP/Ruby language-server review stays queued separately.
3. Compare generated, packaged and installed theme JSON bytes. Review fixture copies only when byte-identical to their sources; record actual workspace and trust context. Inspect questionable tokens in the native editor and save state and screenshot together so captions identify the token actually pictured.
4. Make only corrections supported by native scope evidence and the installed official grammar. Use narrow language-context selectors, preserve existing generic keyword/variable behavior and add small emitted-theme contract regressions. Avoid a simulated TextMate engine or blanket semantic overrides. Unsupported distinctions remain explicit limitations.
5. If mappings change, regenerate, rebuild and reinstall the package, verify identity and repeat affected native inspections/screenshots. Report final artifact hashes and distinguish historical observations. Use existing hooks, validator, generator checks, unit tests and archive checker; repeat packaging with fixed metadata to verify reproducibility.

## Risks / Trade-offs

- Built-in providers may supply no semantic tokens → report unavailability and keep third-party server coverage separate.
- Grammar categories can combine roles such as declarations and flow → avoid broad recoloring and document inseparable cases.
- Ruby syntax validation cannot validate PHP → record PHP lint as unavailable and do not infer success from highlighting.
- A fixture review is bounded evidence → retain per-language/per-layer outcomes rather than general language-support claims.

## Migration Plan

Ship through a small feature PR into `dev`. No runtime migration is needed; a mapping correction can be reverted and regenerated.
