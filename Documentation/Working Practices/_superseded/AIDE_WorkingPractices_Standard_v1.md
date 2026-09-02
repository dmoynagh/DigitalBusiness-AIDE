# AIDE Working Practices — Standard

> **Identity:** `AIDE_WorkingPractices@v1`
> **Common name:** Working Practices
> **Version 1** (2026-08-31). First canonical Working Practices contract produced from
> `WorkingPractices_Design_v2`.
>
> **Default weight:** Expectation

## Purpose

Provide portable base conventions for how an AI and user practically approach, communicate,
complete and hand over work.

This Standard may be used as part of full AIDE or independently.

## WP1 — Change Delivery Package

For a material multi-file change, cross-project handoff, corpus reconciliation or other output where
application steps are non-obvious, deliver one package containing:

- all files created/changed by the change set; and
- one concise application-instructions document.

The instructions identify, as applicable:

- add/replace action and destination;
- superseded/archive/withdraw/remove action;
- rename/move/ownership change;
- Binder/Bundle regeneration/replacement;
- project-context additions/removals/replacements;
- cross-project or deployment consequences;
- transfer-only artefacts;
- actions still requiring another process/authority; and
- unconfirmed state changes.

Do not force a package for a trivial one-file output whose application is obvious.

Creating the package does not mean its contents were applied.

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

## WP8 — Preserve durable handoff

When substantial confirmed work moves to another project/session/environment/owner, preserve:

- authoritative source artefacts;
- confirmed model/decisions;
- remaining work;
- important deferred/non-goals; and
- application/integration instructions.

Treat handoff summaries as transfer material unless explicitly adopted as authoritative masters.
Remove stale handoff summaries from ongoing context once their job is complete.

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

Working Practices governs collaboration/operating behaviour, not the semantics of specialised
mechanisms it mentions.

Use the specialised owner for document lifecycle, Domain, Dependencies, Migration, Review, Build or
Deployment semantics.

```yaml
MigrationSummary:
  CurrentVersion: v1
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v19
References: WorkingPractices_Design_v2, AIDE_Principles@v1
