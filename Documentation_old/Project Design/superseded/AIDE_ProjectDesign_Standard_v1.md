# AIDE Project Design — Standard

> **Identity:** `AIDE_ProjectDesign@v1`
> **Common name:** Project Design
> **Version 1** (2026-08-30). Initial behavioural contract for defining substantial project work and handing defined execution to Build.
>
> **Default weight:** Expectation

---

## Purpose

Define substantial work coherently before execution: establish intent and requirements, determine the current model/approach, review proportionately, and hand execution to Build through a complete WorkPackage where needed.

## Apply proportionately

Use the amount of structure justified by consequence, reach, reversibility and uncertainty. Small clear tasks do not require ceremony merely to imitate a large project.

## Establish the work

For work that needs design, establish enough of the following to remove material ambiguity:

- objective/need and intended outcome;
- authorised scope and non-goals;
- requirements and constraints;
- material assumptions/uncertainties;
- decisions and credible alternatives where consequential;
- the current design/model/approach; and
- defined deliverables or acceptance signals.

Do not allow detailed implementation to become the place where unresolved design is silently decided.

## Use a layered checkpoint for substantial design

Before descending into extensive mechanics, maintain a compact view of:

1. **Intent/system:** purpose, premises, ownership/boundaries, inputs/outputs and surrounding relationships.
2. **Model:** principal concepts, responsibilities, relationships, lifecycle/flow and major rules.

If this view is difficult to make clear, reassess the model before adding mechanisms.

## Record authoritative state

Design records the current confirmed position. Decisions record material reasoning and rejected alternatives. Downstream outcomes consume the confirmed Design/defined outcome, not Decisions history.

Confirmed material must be written according to the governing Documentation Methodology rather than left only in conversation.

## Review

Use `AIDE_Review` when required by the governing workflow/Standard/WorkPackage or when an independent reasoning path is expected to add material value. The Lead retains design ownership and Finding disposition.

## Handoff to Build

When execution is required, provide a WorkPackage conforming to `AIDE_WorkPackage@v1`.

The package must make the required result, authority, work-specific inputs and acceptance clear. Do not embed generic execution-platform knowledge that is already supplied by the Build environment.

## Handle Build return

On Build Outcome:

- close/record completion when acceptance is satisfied;
- resolve returned design questions before authorising changed execution; or
- record an authorised residual difference/risk.

Build may resolve implementation detail within authority; it does not silently change objectives, major scope, acceptance or architecture.

## Keep the model simple

When implementation begins accumulating exceptions or compensating machinery, test whether a simpler model, boundary or requirement removes the complexity before adding another mechanism.

---
Dependencies: !AIDE_DocumentationMethodology@v18, ProjectDesign_Design_v1, AIDE_Review@v1
References: AIDE_WorkPackage@v1
