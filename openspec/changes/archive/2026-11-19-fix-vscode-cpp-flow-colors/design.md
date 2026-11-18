# Design

## Context

The baseline inspector identified two C++ scopes whose foreground falls back to the generic keyword rule.

## Goals / Non-Goals

Assign the existing control color to those two scopes. Preserve the approved palette and existing classifications.

## Decisions

Add both fully qualified scopes to the shared generator's control rule. Verify them using the shipped TextMate engine with the existing fixture and use declaration, primitive, and control tokens as comparisons.

## Risks / Trade-offs

Other providers may assign a semantic foreground or different scopes. The requirement applies when either observed TextMate scope supplies the foreground.
