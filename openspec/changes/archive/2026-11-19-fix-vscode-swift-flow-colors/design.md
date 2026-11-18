# Design

## Context

The Swift fixture review reports three distinct TextMate scopes for branch, exception, and transfer statements.

## Goals / Non-Goals

Give the observed statements the existing control color. Preserve the colors of declaration keywords and contextual type words.

## Decisions

Check scope sharing in the installed Swift grammar before selecting each rule. Use fully qualified Swift selectors and verify their effects with the shipped TextMate engine. Compare the affected statements with declarations and the contextual `any` and `some` words.

## Risks / Trade-offs

TextMate selectors cover every token assigned the same scope and context by the grammar. Document that boundary and identify any provider-dependent limitations.
