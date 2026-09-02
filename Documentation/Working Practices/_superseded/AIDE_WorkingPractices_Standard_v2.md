# AIDE Working Practices — Standard

> **Identity:** `AIDE_WorkingPractices@v2`
> **Common name:** Working Practices
> **Version 2** (2026-08-31). Adds Project Handoff, management-folder/repository handling, Change
> Delivery staging, and independently versioned Binder conventions under the clarified
> Documentation Methodology ownership boundary.
>
> **Default weight:** Expectation

## Purpose

Provide portable base conventions for how an AI and user practically approach, communicate,
organise, complete and hand over work.

This Standard may be used as part of full AIDE or independently.

## WP1 — Change Delivery Package

For a material multi-file change, cross-project handoff, corpus reconciliation or other output where
application steps are non-obvious, deliver one package containing:

- all files created/changed by the change set; and
- one concise application-instructions document.

The instructions identify, as applicable:

- add/replace action and destination;
- semantic lifecycle action plus the applicable physical handling convention;
- rename/move/ownership change;
- Binder/Bundle regeneration/replacement;
- project-context additions/removals/replacements;
- cross-project or deployment consequences;
- transfer-only artefacts;
- actions still requiring another process/authority; and
- unconfirmed state changes.

Do not force a package for a trivial one-file output whose application is obvious.

Creating the package does not mean its contents were applied.

Under the current AIDE repository convention, stage active Change Delivery ZIPs in
`Documentation/_changeDeliveryPackages/`; after application/review is complete, move them to
`Documentation/_changeDeliveryPackages/_completed/`.

## WP2 — Use the owning project's current baseline for cross-project master changes

Before issuing authoritative changes for another project/container, use that owner's current Binder
or current master sources when reasonably available.

Do not reconcile another project from a stale snapshot when a current coherent source is available.

If current state cannot be obtained, state the limitation rather than claiming current
reconciliation.

Never edit a generated Binder directly; edit masters and regenerate.

## WP3 — Gloss coded references

On first use, briefly explain opaque section/decision/question IDs or document/capability references
when their meaning is not already clear from immediate context.

## WP4 — Verify inspectable current/external facts

Where a statement depends on current records, files, installed state, environment state or another
inspectable authority, check the available source/tool first when reasonably possible.

If it cannot be verified, state the uncertainty. Do not compose a plausible value.

## WP5 — Distinguish generated intent from applied state

Do not silently conflate states such as:

```text
created → proposed → handed off → applied → installed/deployed → verified
```

Claim only the state that the available authority/tool/environment actually establishes.

## WP6 — Surface architecture-shaping choices

Handle routine, reversible and low-risk choices autonomously.

For a genuine architecture-shaping decision/material trade-off, provide:

```text
Decision
Recommendation
Why
Credible alternative
Consequence
```

proportionately.

## WP7 — Work in layers before detail

For complex work, establish compact intent/premises and the working model before deep elaboration.
Keep the active set human-comprehensible and expose partial conclusions early enough for steering.

## WP8 — Preserve durable handoff and use Project Handoff across AIDE projects

When substantial confirmed work moves to another project/session/environment/owner, preserve:

- authoritative source artefacts/pointers;
- confirmed model/decisions;
- material reasoning/implications needed by the receiver;
- remaining work;
- important deferred/non-goals; and
- application/integration instructions.

**Project Handoff** is the formal cross-project form: a concise transfer of material knowledge,
reasoning, decisions, implications and authoritative source pointers from one AIDE project to
another project that owns or should act on that information. “Handoff” may be used where context is
obvious.

Create or proactively suggest one when knowledge developed here would materially help the owning
project make, understand or implement its next decision. Do not create one for routine chatter or
information already fully represented in authoritative sources available to the destination.

Treat handoff summaries as transfer material unless explicitly adopted as authoritative masters.
The destination reconciles a Project Handoff against its current baseline before changing masters.
Remove stale handoffs from ongoing context once their job is complete.

## WP9 — Management-folder and historical-storage convention

Where filesystem/repository structure is used and the distinction is useful, prefix structural or
workflow-management folders with `_` so they are visually distinct from substantive content.

Current AIDE examples are:

```text
_superseded/
_archived/
_changeDeliveryPackages/
_completed/
```

A folder does not define semantic state. The relevant owner first determines whether an artefact is
Current, Superseded, Archived or otherwise disposed; Working Practices then applies the physical
handling convention.

Under the current repository convention, physically hold Superseded material in `_superseded/` and
Archived material in `_archived/` where those folders are used.

Historical material in `_superseded/`, `_archived/` and `_changeDeliveryPackages/_completed/` may
periodically move to longer-term storage outside the active repository to control repository size,
provided required history and traceability are preserved.

Use an equivalent management representation on platforms that do not use filesystem folders.

## WP10 — Version and place generated Binders for easy current-context use

Issue a generated project Binder as:

```text
<Project>_Binder_vN.md
```

Binder version counts issued Binder assemblies independently of project/capability/source-document
versions.

Keep the current Binder in the active/master project folder alongside Current masters. It remains a
generated, read-only consumption artefact; its manifest identifies the exact source versions and
integrity information. Authoritative changes are made to masters, then the Binder is regenerated.

When a newly issued Binder replaces the active Binder, the prior Binder becomes Superseded and may
be retained under `_superseded/` according to the current repository convention. Replace the loaded
project-context Binder with the new current Binder.

## Guidance Profiles

This is base guidance.

Applicable organisation/group/team/user Guidance Profiles may Add, Refine or explicitly Override
named practices using small deltas.

Unmentioned base practices remain effective. Equal-specificity conflict fails visibly unless
explicitly ordered.

Do not fork/copy the complete base Standard merely to customise it.

Host/platform instructions and other higher-priority governing constraints remain outside this
profile model.

## Ownership boundary

Working Practices governs collaboration/operating behaviour and practical workflow handling, not
the semantics of specialised mechanisms it mentions.

Documentation Methodology owns document lifecycle meaning; Working Practices may own the physical
handling convention used to realise that state. Use the specialised owner for Domain, Dependencies,
Migration, Review, Build or Deployment semantics.

```yaml
MigrationSummary:
  CurrentVersion: v2
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none
```

```yaml
Transition:
  Version: v1
  Posture: None
```

```yaml
Transition:
  Version: v2
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v20
References: WorkingPractices_Design_v3, AIDE_Principles@v1
