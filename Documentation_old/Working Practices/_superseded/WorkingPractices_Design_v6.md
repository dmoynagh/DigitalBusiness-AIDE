# Working Practices — Design

> **Version 6** (2026-09-01). Clarifies the Documentation Methodology/Working Practices
> ownership seam and adds a live continuity holder for Project Handoffs whose reconciliation is
> deferred.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

## §1 — Purpose

Working Practices defines the practical cross-cutting conventions used when an AI and user work
together.

It answers:

> How should work be approached, communicated, organised, preserved, completed and handed over in
> practice?

It applies across chat, documents/design, code/repository work, Work-style artifact environments,
Build execution, research, administration and non-development AI use where a practice remains
relevant.

Working Practices is part of AIDE but can also be deployed independently.

## §2 — Boundary with Principles

```text
Principles
  → durable reasoning and judgement premises

Working Practices
  → concrete collaboration and operational conventions
```

A Working Practice may implement a Principle but should not duplicate its rationale unnecessarily.

## §3 — Boundary with specialised owners

Working Practices tells the AI **how to work with the user and handle work operationally**. It does
not take semantic ownership from specialised components.

Examples:

```text
Documentation Methodology
  → WIP / Working / OpenItems / WorkRegister document semantics and lifecycle.

Working Practices
  → when active state should be persisted, checkpointed, transferred or verified in practice.

Core / Index
  → generic Index / Item / Item Type semantics.

Working Practices
  → use current authoritative sources and preserve owner state during updates.

AI Deployment
  → deployment reconciliation / verification.

Working Practices
  → distinguish generated intent from confirmed applied/deployed state.
```

A physical folder never defines a Documentation Methodology lifecycle state. Resolve semantic state
under its owner first; apply the current Working Practices handling convention second.

## §4 — Containers and top-level topics

A chat project, master folder or workspace is a **context/storage container**. It may host one or
several top-level topics because those topics benefit from access to a shared information pool.

Documentation Methodology defines the semantic top-level-topic anchor and the scope/delegation
rules for its standing document-state mechanisms. Working Practices consumes that model
operationally: before persisting, transferring or resuming active state, resolve which owning
top-level topic the current Documentation Methodology assigns it to rather than inferring ownership
from UI or filesystem co-location.

This section does not define OpenItems, WorkRegister or other document-state semantics; it defines
how their owner-defined scope is respected in practical handling.

## §5 — Base guidance and Guidance Profiles

`AIDE_WorkingPractices@v1` remains the portable base.

Optional organisation/group/team/user Guidance Profiles may provide deltas:

```text
Add
Refine
Override
```

Profiles contain only differences from the base. A narrower applicable profile changes only the
practices it explicitly addresses. Unmentioned base guidance remains effective. Equal-specificity
conflict fails visibly unless explicit ordering exists. Host/platform instruction priority remains
outside AIDE.

The shared profile concept is not promoted into a separate generic component yet.

## §6 — Confirmed Working Practices

### WP1 — Change Delivery Package

For a material multi-file change, cross-project change set, corpus reconciliation or other output where
application steps are non-obvious, deliver one package containing:

- all files created/changed by the change set; and
- one concise application-instructions document.

The instructions identify, as applicable:

- add/replace action and destination;
- semantic lifecycle action plus the applicable physical handling convention;
- rename/move/ownership change;
- Binder/Bundle regeneration/replacement;
- project-context additions/removals/replacements;
- cross-project, source or deployment consequences;
- transfer-only artefacts;
- intentionally unchanged related items where omission could be mistaken for oversight;
- actions still requiring another process/authority; and
- unconfirmed state changes.

Do not force a package for a trivial one-file output whose application is obvious.

Creating the package does not mean its contents were applied.

Under the current AIDE repository convention, stage active Change Delivery ZIPs in
`Documentation/_changeDeliveryPackages/`; after application/review is complete, move them to
`Documentation/_changeDeliveryPackages/_completed/`.


### WP2 — Use the owning top-level topic's current baseline for cross-project master changes

Before issuing authoritative changes for another owning top-level topic/container, use that owner's current Binder
or current master sources when reasonably available.

Do not reconcile another project from a stale snapshot when a current coherent source is available.

If current state cannot be obtained, state the limitation rather than claiming current
reconciliation.

Never edit a generated Binder directly; edit masters and regenerate.

### WP3 — Gloss coded references

On first use, briefly explain opaque section/decision/question IDs or document/capability references
when their meaning is not already clear from immediate context.

### WP4 — Verify inspectable current/external facts

Where a statement depends on current records, files, installed state, environment state or another
inspectable authority, check the available source/tool first when reasonably possible.

If it cannot be verified, state the uncertainty. Do not compose a plausible value.

### WP5 — Distinguish generated intent from applied state

Do not silently conflate states such as:

```text
created → proposed → handed off → applied → installed/deployed → verified
```

Claim only the state that the available authority/tool/environment actually establishes.

### WP6 — Surface architecture-shaping choices

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

### WP7 — Work in layers before detail

For complex work, establish compact intent/premises and the working model before deep elaboration.
Keep the active set human-comprehensible and expose partial conclusions early enough for steering.

### WP8 — Preserve durable handoff

When substantial confirmed work moves to another project/session/environment/owner, preserve the
authoritative sources/pointers, confirmed model/decisions and material reasoning, remaining work,
important deferred/non-goals, and application/integration instructions needed to continue safely.

Treat handoff summaries as transfer material unless explicitly adopted as authoritative masters.
Remove stale handoff summaries from ongoing context once their job is complete.

### Project Handoff

**Project Handoff** is the named cross-project form of durable handoff. **Handoff** may be used as
conversational shorthand when the destination/context is obvious.

> A Project Handoff is a concise transfer of material knowledge, reasoning, decisions, implications
> and authoritative source pointers from one AIDE project to another project that owns or should act
> on that information.

Use or suggest one when knowledge developed in the current project would materially help another
owning project **make, understand or implement its next decision**. Do not create one for routine
chatter or information already fully represented in authoritative sources. Proactively suggest a
Project Handoff when material work clearly creates a consequence owned by another project; produce
one when requested or when the agreed work calls for it.

Proportionately include:

- why the Handoff is being made and what destination action is expected;
- material reasoning/context and destination-relevant confirmed decisions;
- important alternatives, constraints, trade-offs, implications and consequences;
- unresolved/deferred items and important non-goals/boundaries;
- authoritative source artefacts/pointers; and
- what is proposed versus already confirmed.

Keep it concise transfer context, not a transcript or duplicate corpus.

The destination's **current Binder/masters are the baseline**. Reconcile the Handoff against them,
surface genuine conflict, incorporate useful content into the destination's own authoritative
Design/Decisions/outcomes, and normally remove the Handoff from active context once incorporated.
An older Handoff does not override newer destination state.

On destination receipt, preserve continuity until that reconciliation is complete:

- if the Handoff is reconciled/incorporated in the same pass or active context, no additional live
  register entry is required;
- if reconciliation is deferred beyond the current pass/context, create one concise destination
  OpenItem under the current Documentation Methodology, for example
  `Reconcile Project Handoff <identity/source>`;
- remove that OpenItem when reconciliation/incorporation is complete; and
- remove the transfer material from active context once its purpose is complete.

This is operational use of the existing OpenItems mechanism, not a Project Handoff DocType,
register or separate lifecycle.

Discovering another project's consequence does not itself authorise remote master editing. The
normal flow is:

```text
originating project → Project Handoff → owning project → authoritative update
```

If cross-project master changes are separately authorised, WP2 applies before issuing them.

A **Project Handoff** transfers knowledge, reasoning, decisions and implications. A **Change
Delivery Package** transfers concrete created/changed files plus application instructions. They may
accompany each other, but neither substitutes for the other, and a knowledge-only Project Handoff
does not by itself require a Change Delivery Package.

### WP9 — Management-folder and historical-storage convention

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

### WP10 — Version and place generated Binders for easy current-context use

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



#### Live work state is loaded separately

Binder composition and live-state lifecycle semantics belong to the current Documentation
Methodology. Operationally, when active work needs live state that is not in the normal Binder,
load the owner-defined current live material separately and verify its actual currency where the
platform permits. Do not infer that generating or transferring a new live-state checkpoint has
updated the Binder or loaded project context.

### WP11 — Batch file/document output at meaningful checkpoints

Do not output changed masters, Binders or Change Delivery Packages after every individual change by
default.

Accumulate confirmed changes during active work and issue one consolidated output pass at the end
of a significant work unit, work session or meaningful completion/integration checkpoint, or when
the user explicitly asks to run/output the pass.

Before autonomously producing a material file set or Change Delivery Package, ask whether the user
wants the accumulated changes output now or whether other pending work should be included. An
explicit request to output/update/build the files or package already counts as confirmation.

Where another project/chat response is reasonably expected, especially during Project Handoff
exchange, normally queue resulting changes until the exchange reaches a useful checkpoint rather
than regenerating files/packages on every round.

Never batch at material risk of losing confirmed information, creating significant ambiguity, or
materially affecting downstream work. Preserve at-risk state promptly using the least-churn
appropriate durable mechanism, then consolidate normal deliverable output later.

### WP12 — Persist active work before context loss would be costly

Do not allow valuable current thinking to depend solely on a volatile chat/session/platform context
once losing that context would materially impair continuation.

Use the current Documentation Methodology to select the correct semantic state holder. Working
Practices governs the preservation decision and timing, not the document-role definitions. For
volatile continuation, this will often mean issuing a lightweight WIP checkpoint; where the state
has already crossed into another owner-defined role, use that role instead rather than duplicating
its semantics here.

Useful WIP checkpoint triggers include:

- ending a material work session;
- switching chats, project containers or platforms;
- moving to unrelated work likely to displace the active context;
- completing a substantial reasoning block not yet represented durably;
- before a context/cache reset or where context eviction appears likely; or
- explicit request for a physical current-work checkpoint.

Do not checkpoint every message merely because WIP exists. Where the AI judges persistence is
materially useful, it should advise/create the checkpoint according to current authority rather
than waiting for the human to discover context loss.

The preservation rule is stronger than batching: **do not lose thinking**. If the choice is between
an extra lightweight checkpoint and material loss/reconstruction risk, preserve first and
consolidate normal deliverable output later.

### WP13 — Use visible WIP version currency when moving context

When a WIP checkpoint is intended to be added/replaced in an AI project/context or exchanged across
platforms, use the current versioned filename and identify the version being transferred.

The practical question is:

> Is the WIP file I have loaded the current issued checkpoint?

Do not infer successful replacement/sync merely because a new file was generated. Verify the
loaded/available version where the platform permits.

The version is a currency/transport signal as well as an issued checkpoint. This is especially
useful where project-file UIs provide weak feedback about which file revision is actually loaded.

### Binder/live-state handling

Follow the current Documentation Methodology for Binder composition, live-state inclusion/exclusion,
series discovery and lifecycle semantics. Working Practices adds only the operational requirement:
make the current owner-defined live state available separately when needed for continuation, and
verify currency rather than assuming a generated/transferred checkpoint is the one actually
loaded.

## §7 — Standalone use

A general AI environment may deploy only:

```text
AIDE_Principles
AIDE_WorkingPractices
```

through an appropriate Bootstrap Profile.

A full AIDE environment may deploy the same base guidance alongside Core, Domain, Project Design,
Build, Documentation Methodology and other capabilities.

## §8 — Intended output

Produce:

```text
AIDE_WorkingPractices@v1
```

This pass remains within the first distributable v1 capability identity because no consumer
release has yet established a migration obligation. The Standard document issue increments to
version 4.

---
Dependencies: !AIDE_DocumentationMethodology@v21
References: WorkingPractices_Decisions_v6, Principles_Design_v3, Core_Bootstrap_Design_v2
