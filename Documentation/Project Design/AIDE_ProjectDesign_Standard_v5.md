# AIDE Project Design — Standard

> **Identity:** `AIDE_ProjectDesign@v5`
> **Common name:** Project Design
> **Version 5** (2026-09-02). Adds flexible Design contributions, section hosting and direct cross-Topic reconciliation.
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

Design/Definition/Standards/Tools hold the applicable current confirmed position. Decisions retains material evolutionary reasoning and rejected alternatives. Downstream outcomes consume current authoritative inputs, not Decisions history.

Confirmed material must be written according to the governing Documentation Methodology rather than left only in conversation.

## Track undelivered Design consequences

**Weight: Requirement**

Documentation Methodology owns the general WorkRegister type/admission semantics. Project Design
owns the following mandatory producer guarantee.

Whenever the confirmed Design changes, identify the downstream outcomes that must change for
delivered reality to remain aligned.

For each material consequence:

```text
fully delivered in the same pass → no Design-generated standing obligation remains
not fully delivered               → record/update it in the owning top-level topic's WorkRegister
```

The WorkRegister entry must state the source Design change and required downstream code/build/
document/production changes in enough detail that later delivery can be reconciled.

This producer rule does **not** define WorkRegister as exclusively Design-generated work. Confirmed
non-Design work may also belong there under the governing WorkRegister/type contract. WorkRegister
is still not a generic backlog: unresolved ideas, possible work and unconfirmed attention remain
outside it.

## Review

Use `AIDE_Review` when required by the governing workflow/Standard/WorkPackage or when an independent reasoning path is expected to add material value. The Lead retains design ownership and Finding disposition.

## Handoff to Build

When execution is required, provide a WorkPackage conforming to `AIDE_WorkPackage@v3`.

A WorkPackage may be created directly from defined work or select manageable portions of one or
more WorkRegister obligations. Where it is sourced from WorkRegister, identify the source item IDs
and the portion of each obligation covered.

The package must make the required result, authority, work-specific inputs and acceptance clear.
WorkRegister references are traceability, not a substitute for a self-contained execution contract.
Do not embed generic execution-platform knowledge already supplied by the Build environment.

## Handle Build return

**Weight: Requirement**

On Build Outcome:

- reconcile returned evidence against each mapped WorkRegister obligation where applicable;
- remove a WorkRegister item only when its full confirmed obligation is actually delivered;
- retain partial/blocked items with returned result and remaining work;
- close/record completion when acceptance and the committed outcome are satisfied;
- resolve returned design questions before authorising changed execution; or
- record an authorised residual difference/risk.

If a mapped Outcome is received and reconciliation cannot be completed in the same uninterrupted
step, before leaving the context preserve a compact `Returned — reconciliation pending` state on
the owning mapped item(s) and point to the Outcome. Detailed evidence remains in Outcome rather
than being duplicated into WorkRegister.

Project Design/the directing owner reconciles and closes the obligation. Build reports evidence;
it does not silently close the owning WorkRegister.

Build may resolve implementation detail within authority; it does not silently change objectives,
major scope, acceptance or architecture.

## Keep the model simple

When implementation begins accumulating exceptions or compensating machinery, test whether a simpler model, boundary or requirement removes the complexity before adding another mechanism.

```yaml
MigrationSummary:
  CurrentVersion: v5
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None

Transition:
  Version: v4
  Posture: None
```


## Design contributions and hosts

Design is confirmed knowledge, not a required one-document-per-output chain. Use zero, one or many
Design documents/sections proportionately. Directly author the proper authoritative outcome when an
intermediate Design would only duplicate it.

One contribution may affect several outputs; one output may aggregate several contributions. If
current contributions conflict materially, reconcile them before Build. Build must not choose.

Brief/Purpose, Requirements and Considerations are semantic sections. A domain Standard may permit
compact hosting in a domain control document while retaining one authoritative instance per scope.
Externalise only when size, lifecycle, retrieval, reuse or complexity warrants it.

## Cross-Topic work

Topic ownership determines authoritative baseline and destination, not physical work location. A
sufficiently sourced and authorised Working Context may reconcile several Topics. Use Project
Handoff only where Working Practices identifies a real transfer boundary.

```yaml
Transition:
  Version: v5
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v27, ProjectDesign_Design_v5, AIDE_Review@v3
References: AIDE_WorkPackage@v3
