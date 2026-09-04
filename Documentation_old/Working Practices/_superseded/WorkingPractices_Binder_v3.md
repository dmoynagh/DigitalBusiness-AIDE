# Working Practices Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.
> **Binder Version 3** (2026-09-01). Review B R1 remediation: restores the Documentation Methodology/Working Practices ownership boundary and adds deferred Project Handoff continuity handling.

## Binder manifest

- `WorkingPractices_Index_v6.md` — sha256 `100e6035b89d`
- `WorkingPractices_Brief_v5.md` — sha256 `b62ce0e2fa05`
- `WorkingPractices_Design_v6.md` — sha256 `4dc102cc1b80`
- `WorkingPractices_Decisions_v6.md` — sha256 `88296a641505`
- `AIDE_WorkingPractices_Standard_v5.md` — sha256 `b82a2fc455e9`

---

<!-- BEGIN SOURCE: WorkingPractices_Index_v6.md -->
# Working Practices — Index

> **Version 6** (2026-09-01). Registers the Review B R1 ownership-boundary and Project Handoff
> continuity remediation.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

`{scope: "AIDE/Working Practices", type: DocumentationTopic}`

## Contents

- **Working Practices** — portable cross-surface collaboration and operating conventions.  
  `{standard: AIDE_WorkingPractices@v1}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Working Practices | None | `WorkingPractices` | independent | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `WorkingPractices_Index` | v6 | Index | Current |
| `WorkingPractices_Brief` | v5 | Brief | Current |
| `WorkingPractices_Design` | v6 | Design | Current |
| `WorkingPractices_Decisions` | v6 | Decisions | Current |
| `AIDE_WorkingPractices_Standard` | v5 | Standard | Current; identity `AIDE_WorkingPractices@v1` |

### Generated consumption artifact

Regenerate the current Working Practices Binder after these masters are applied. Binder/live-state
composition follows the current Documentation Methodology; Working Practices governs the practical
loading, currency verification and handling of that owner-defined state.

### Local configuration

None.

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Index@v1
References: WorkingPractices_Design_v6, AIDE_WorkingPractices@v1
<!-- END SOURCE: WorkingPractices_Index_v6.md -->

---

<!-- BEGIN SOURCE: WorkingPractices_Brief_v5.md -->
# Working Practices — Brief

> **Version 5** (2026-09-01). Clarifies semantic/operational ownership and records deferred
> Project Handoff continuity handling.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

## Purpose

Working Practices defines **how an AI and user practically work together** across chat, documents,
code, repositories, Work-style environments and other AI-assisted surfaces.

## Required model

Working Practices must be:

- cross-cutting and independently deployable;
- complementary to Principles;
- portable across software and non-software work;
- explicit about generated/proposed versus applied/verified state;
- protective of valuable thinking across context/session/platform boundaries; and
- clear that practical containers are not automatically semantic top-level topics.

## Demonstrated practices

- material multi-file output uses a Change Delivery Package;
- cross-project ownership changes use Project Handoff and the destination's current baseline;
- a received Handoff that cannot be reconciled in the same pass is held by one concise destination
  OpenItem until reconciliation completes;
- generated Binders are independently versioned read-only consumption artefacts;
- confirmed output is batched at meaningful checkpoints rather than after every edit;
- **valuable active thinking is checkpointed to WIP when loss of current context would materially
  impair continuation**;
- WIP versioning is used as a visible currency signal when context files are swapped/synced across
  chats/platforms;
- routine low-risk choices are handled autonomously while architecture decisions are surfaced;
- externally held/current facts are checked rather than plausibly invented; and
- material state-changing actions are not silently assumed complete.

## Outcome

```text
AIDE_WorkingPractices@v1
```

---
Dependencies: !AIDE_DocumentationMethodology@v21
References: WorkingPractices_Design_v6, Principles_Design_v3
<!-- END SOURCE: WorkingPractices_Brief_v5.md -->

---

<!-- BEGIN SOURCE: WorkingPractices_Design_v6.md -->
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
<!-- END SOURCE: WorkingPractices_Design_v6.md -->

---

<!-- BEGIN SOURCE: WorkingPractices_Decisions_v6.md -->
# Working Practices — Decisions

> **Version 6** (2026-09-01). Preserves the complete prior decision history and records Review B
> R1 ownership-boundary remediation plus deferred Project Handoff continuity handling.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

## D1 — Working Practices is a top-level AIDE topic

**Decision.** Working Practices is a sibling of Principles, Core, Project Design, Build,
Capabilities and other principal AIDE concerns.

**Reason.** It governs practical AI/user collaboration across work types and output forms.

## D2 — Working Practices is independently deployable

**Decision.** `AIDE_WorkingPractices@v1` is usable without full AIDE.

**Reason.** General AI sessions can benefit from working conventions without development-specific
context.

## D3 — Working Practices is base guidance

**Decision.** The canonical Standard supplies portable defaults rather than one user/team's final
customised behaviour.

## D4 — Guidance Profiles provide deltas

**Decision.** Organisation/group/team/user Profiles may Add, Refine or explicitly Override named
Working Practices without copying/forking the base Standard.

## D5 — Specialised owners retain semantics

**Decision.** Working Practices may require the AI to communicate/hand off specialised state but
does not redefine lifecycle, deployment, dependency, migration, Domain or other owned semantics.

## D6 — Material multi-file handoff uses a Change Delivery Package

**Trigger / problem.** Multi-file and cross-project outputs leave the user reconstructing file
placement, supersession, Binder/context and follow-up actions from conversation.

**Decision.** Deliver one package containing the created/changed deliverables plus concise
application instructions.

**Alternative considered.** Provide files individually and explain them conversationally. Rejected
for material change sets because the conversation is not a durable application manifest and steps
are easily missed.

## D7 — Package creation does not imply application

**Decision.** A Change Delivery Package is a transfer artefact; generation does not mean its
changes were applied.

## D8 — Trivial one-file output does not require package ceremony

**Decision.** Apply Change Delivery proportionately based on complexity/risk.

## D9 — Preserve operational seed behaviours from Principles

**Decision.** Coded-reference glossing, verification before assertion and no-silent-state-change
behaviour remain as Working Practices rather than being lost during Principles separation.

## D10 — Architecture decisions are surfaced selectively

**Decision.** Routine/reversible choices are handled autonomously; genuinely architecture-shaping
choices expose recommendation, rationale, alternative and consequence.

## D11 — Layered work is a Working Practice backed by Principles

**Decision.** Complex work establishes compact intent/model layers before deep elaboration.

## D12 — Durable handoff is required when substantial work moves

**Decision.** Cross-project/session/environment handoffs preserve authoritative inputs, confirmed
decisions, remaining work and integration instructions.

**Consequence.** Handoff summaries are normally transfer-only and should not become stale competing
sources beside adopted masters.

## D13 — Cross-project master changes use the owner's current baseline

**Trigger / problem.** A cross-project change package was prepared from an earlier Core/DocMeth
state while parallel work subsequently advanced Domain integration and Documentation Methodology.

**Alternatives considered.**

- Trust the earlier handoff snapshot and let the destination reconcile conflicts later. Rejected
  because it creates avoidable stale-version collisions.
- Always require every master file individually before doing cross-project work. Rejected because a
  current generated Binder is specifically intended to provide a coherent read-only corpus source.

**Decision.** Before issuing cross-project master changes, use the owning project's current Binder
or current masters when reasonably available.

**Consequence.** The destination's current state is the baseline; generated Binders are never edited
directly, and the changed masters are used to regenerate them afterward.

## D14 — Project Handoff is the named cross-project form of durable handoff

**Trigger / problem.** WP8 already requires durable transfer when substantial work moves between
projects, sessions, environments or owners, but cross-project work lacked a concise shared name and
an explicit lifecycle. As a result, useful reasoning could either remain trapped in the originating
conversation or persist as stale context beside the destination's authoritative sources.

**Alternatives considered.**

- Create Project Handoff as a wholly separate Working Practice. Rejected because the underlying
  behaviour is already the cross-project case of WP8 and a second mechanism would duplicate the
  same preservation/lifecycle rules.
- Treat every cross-project conversation or transfer as a Project Handoff. Rejected because routine
  chatter and already-authoritative information do not justify transfer artefacts.

**Decision.** **Project Handoff** is the named cross-project form of WP8. It transfers material
knowledge, reasoning, decisions, implications and authoritative source pointers from an originating
project to the project that owns or should act on them. Use it where the transferred knowledge would
materially help the owning project make or understand its next decision.

**Consequences.** The destination reconciles the Handoff against its current Binder/masters before
changing authoritative state, incorporates useful content into its own authoritative records, and
normally removes the Handoff from active context once that transfer is complete. The AI should
proactively suggest or produce a Project Handoff when material work clearly creates a consequence
owned by another project.

## D15 — Project Handoff and Change Delivery Package remain distinct

**Trigger / problem.** Existing Change Delivery language used the generic word “handoff”, while the
newly named Project Handoff solves a different problem. Without an explicit distinction, a
knowledge-only Project Handoff could incorrectly trigger file-packaging ceremony, or a file package
could be mistaken for preservation of design reasoning.

**Decision.** Keep the two mechanisms separate:

```text
Project Handoff
  → transfers knowledge/reasoning/decisions/implications/source pointers

Change Delivery Package
  → transfers concrete created/changed files plus application instructions
```

They may be used together. A Project Handoff may contain no changed files; a Change Delivery
Package may carry or point to a Project Handoff when both are needed.

**Consequence.** WP1 language uses “cross-project change set” rather than “cross-project handoff” so
Project Handoff does not accidentally become a packaging trigger.

## D16 — Project Handoff clarification remains within AIDE_WorkingPractices@v1

**Decision.** Keep the formal capability identity `AIDE_WorkingPractices@v1` and reissue the
canonical Standard as document version 2 rather than creating a new capability release.

**Reason.** This pass names and sharpens an already-established v1 durable-handoff behaviour and
removes an ambiguity with Change Delivery; it does not require consumer-state migration or introduce
a new independent mechanism. Document issue version and capability release identity remain distinct.

**Consequence.** `AIDE_WorkingPractices_Standard_v1.md` becomes superseded by
`AIDE_WorkingPractices_Standard_v2.md`, while the published capability identity remains
`AIDE_WorkingPractices@v1`.

## D17 — Project Handoff has a material-knowledge trigger and compact transfer contract

**Trigger / problem.** The initial named form established in D14 identifies when cross-project
knowledge matters, but the operational contract must also make Handoffs recognisable from natural
work and useful without becoming conversation transcripts or copied mini-corpora.

**Decision.** Use or suggest a Project Handoff when knowledge developed in one project would
materially help the owning project make, understand or implement its next decision. A Handoff
proportionately carries the reason for transfer, material reasoning/context, destination-relevant
confirmed decisions, important alternatives/constraints/trade-offs, implications, unresolved or
deferred items, authoritative source pointers, proposed-versus-confirmed state, expected destination
action, and important non-goals/boundaries.

Conversational **Handoff** is acceptable shorthand where the cross-project destination/context is
obvious. Routine chatter and information already fully represented by authoritative sources do not
justify a Project Handoff.

**Consequence.** The AI can recognise cross-project ownership consequences during ordinary work,
proactively suggest a Project Handoff, and produce one when requested without needing a separate
mechanism or document type.

## D18 — Cross-project ownership defaults to Handoff, not remote master editing

**Trigger / problem.** WP2 permits safe cross-project master changes when such changes are actually
authorised, but discovery of a consequence in one project does not itself confer authority to
modify another project's authoritative corpus. Without the distinction, Project Handoff could be
undermined by direct editing based on originating-project assumptions.

**Decision.** The normal ownership-preserving flow is:

```text
originating project
→ Project Handoff
→ owning project
→ authoritative update
```

A Project Handoff never overrides the destination's current authoritative state. The destination
reconciles against its current Binder/masters, surfaces genuine conflict, incorporates useful
content into its own authoritative records, and normally removes the Handoff from active context
once its purpose is complete.

Where a separate task or authority explicitly requires cross-project master changes, D13/WP2 still
applies and current owner state must be obtained before those changes are issued.

**Consequence.** Ownership is preserved without weakening the existing current-baseline safeguard.

## D19 — Fuller Project Handoff wording is another document issue, not a capability release

**Decision.** Preserve formal capability identity `AIDE_WorkingPractices@v1` and reissue the
canonical Standard as document version 3.

**Reason.** This pass completes the operational expression of the already-confirmed WP8/D14 model.
It introduces no new independent capability mechanism and requires no consumer-state migration.
The earlier document-v2 delivery was issued but superseded before adoption into the project's
Current masters.

**Consequence.** The intended Current Standard after this delivery is
`AIDE_WorkingPractices_Standard_v3.md`; capability identity remains `AIDE_WorkingPractices@v1`.


## D20 — Documentation lifecycle meaning and physical workflow are separate concerns

**Trigger / problem.** Documentation Methodology historically described both lifecycle states and
some physical storage conventions, making the document methodology unnecessarily filesystem-aware.

**Decision.** Documentation Methodology retains document lifecycle/version semantics. Working
Practices owns practical file/repository handling conventions used to implement those states.

**Reason.** “Why this artefact is Superseded/Archived” is a documentation-governance question;
“where we put it in this repository” is an operating-practice question.

**Consequence.** A folder name never creates lifecycle state. The semantic owner determines state
first; Working Practices then applies the current physical handling convention.

## D21 — Management folders use a leading underscore convention

**Decision.** Where useful in filesystem/repository work, structural/workflow-management folders
use a leading `_` to distinguish them visually from substantive content and ordinary working
folders.

**Current examples.** `_superseded/`, `_archived/`, `_changeDeliveryPackages/`, `_completed/`.

**Reason.** The distinction reduces navigation/file-handling friction without requiring extra
metadata or complex structure.

**Constraint.** The convention does not require creating management folders that the workflow does
not need and does not define semantic lifecycle state.

## D22 — Superseded and archived storage names are Working Practices conventions

**Decision.** Under the current repository convention, Superseded material is handled through
`_superseded/` and Archived material through `_archived/` where physical folders are used.

**Reason.** The names make management structure immediately recognisable while preserving the
semantic/storage separation established in D20.

**Portability.** Non-filesystem environments may use an equivalent representation.

## D23 — Change Delivery Packages have a staging/completion workflow

**Decision.** Under the current AIDE repository workflow, stage active Change Delivery ZIPs in
`Documentation/_changeDeliveryPackages/` and move completed/applied ZIPs to
`Documentation/_changeDeliveryPackages/_completed/`.

**Reason.** This creates one predictable place to review/apply deliveries and separates active from
completed transfer material without making either a corpus master.

## D24 — Historical management material may leave the active repository

**Decision.** Historical contents of `_superseded/`, `_archived/` and
`_changeDeliveryPackages/_completed/` may periodically be transferred to longer-term external
storage to control active-repository size.

**Constraint.** Required history, traceability and authoritative lifecycle meaning must be
preserved. Repository-size reduction is not permission to discard governed history.

## D25 — Binders are independently versioned current consumption artefacts

**Trigger / problem.** An unversioned Binder makes it unnecessarily difficult to tell at a glance
which assembled corpus version is loaded in an AI project/context.

**Decision.** Issue Binders as `<Project>_Binder_vN.md`, with an independent Binder version counting
issued Binder assemblies.

**Decision.** Keep the current Binder in the active/master project folder alongside Current masters
for easy project-context selection. It remains generated/read-only and non-authoritative.

**Decision.** When a newly issued Binder replaces the active one, the prior Binder becomes
Superseded and may be retained under `_superseded/` according to the current repository convention.

**Alternative considered.** Keep current Binders in a separate generated folder. Rejected because
it adds navigation/selection overhead while the generated/read-only marker and manifest already
make the Binder's non-authoritative role clear.

## D26 — The consolidated pre-distribution issue remains AIDE_WorkingPractices@v1

**Trigger / problem.** The management-folder and Binder conventions add substantive operating
guidance after the Project Handoff work, but no Working Practices capability release has yet been
distributed to consumers.

**Decision.** Incorporate the confirmed conventions into the first distributable
`AIDE_WorkingPractices@v1` capability rather than manufacturing an `@v2` transition before any
consumer state exists.

**Consequence.** The canonical Standard remains document version 3 with formal identity
`AIDE_WorkingPractices@v1`. No Working Practices migration transition is introduced by this
pre-distribution reconciliation. Future post-distribution semantic changes may require a later
capability release in the normal way.


## D27 — File/document output is batched at meaningful checkpoints

**Trigger / problem.** Producing masters, Binders and Change Delivery Packages after each individual
confirmed change creates disproportionate file/version churn and user handling overhead. The effect
is particularly severe during cross-project Handoff exchanges where several rounds of useful
“chat tennis” may occur before the owning projects settle the resulting changes.

**Alternatives considered.**

- Output immediately after every confirmed change. Rejected because it optimises against knowledge
  loss at the cost of excessive file churn, repeated Binder regeneration and repeated Change
  Delivery handling.
- Delay all output until explicitly requested. Rejected because confirmed state can sometimes be at
  material risk of loss or can have significant downstream impact before the user asks for files.

**Decision.** Queue confirmed file/document changes during active work and issue them in a
consolidated pass at the end of a significant work unit, work session or meaningful completion/
integration checkpoint, or when the user explicitly asks to run/output the pass.

Before autonomously issuing a material file set or Change Delivery Package, prompt the user so
other pending work can be included. An explicit user request for output/package generation counts as
that confirmation.

**Loss-risk override.** If delaying durable output would materially risk losing confirmed
information, create ambiguity, or materially affect downstream work, preserve the state promptly
using the least-churn appropriate durable mechanism. Reduction in file churn never takes precedence
over preservation of significant confirmed state.

**Cross-project consequence.** When a Project Handoff has been sent and a destination response or
further consequence is reasonably expected, normally queue resulting document changes until the
exchange reaches a useful checkpoint rather than reissuing documents/packages after every round.

## D28 — Active thinking needs a low-friction persisted checkpoint

**Trigger / problem.** AI conversations can accumulate substantial current reasoning before it has
a durable destination. Switching chats, projects or platforms can clear/replace context caches, and
reconstruction is slower and less reliable than carrying a current physical checkpoint.

**Alternatives considered.** Rely on chat history/memory; write every thought immediately to
OpenItems/Design/Decisions; broaden Working to carry both short current context and long-form
exploration.

**Decision.** Working Practices shall actively use the Documentation Methodology `WIP` DocType when
loss of current conversational/context state would materially impair continuation.

**Consequence.** The AI may advise/produce WIP at session/platform/context transition points and
after material reasoning blocks, without checkpointing every conversational turn.

## D29 — “Do not lose thinking” overrides output-churn minimisation

**Decision.** WP11 batching remains the default for normal masters/packages, but preservation of
valuable active thinking takes precedence when current context is materially at risk.

**Reason.** A cheap WIP checkpoint is less costly than either premature authoritative publication or
later reconstruction from incomplete context.

## D30 — Visible WIP filename version is a currency/sync signal

**Trigger / problem.** AI project/context UIs do not always make replacement/sync success obvious.
When moving between Claude/GPT/other contexts, the user needs a simple visible way to tell which
working state was loaded.

**Decision.** Use issued WIP `_vN` filename version as a practical currency/transport signal.
Increment when a new persisted WIP checkpoint is issued for reuse/sync/resumption; verify the loaded
version where the platform permits.

**Consequence.** WIP versioning is purposeful despite high churn: it helps detect stale context
rather than serving historical ceremony.

## D31 — Containers do not define workflow-state scope

**Decision.** Practical workflow handling recognises that a chat project/master folder may contain
several top-level topics. Standing document-state semantics follow Documentation Methodology's
top-level-topic anchor rather than assuming the container is one semantic project.

## D32 — First distributable capability identity remains v1

**Decision.** Keep `AIDE_WorkingPractices@v1` for the first deployment while issuing Standard
document version 4.

**Reason.** The capability has not yet been deployed to consumers. The new WIP preservation
behaviour should be part of the first distributable base rather than manufacturing a migration
between undistributed releases.


## D33 — Documentation Methodology owns live-state semantics; Working Practices owns operational handling

**Trigger / problem.** Review B R1 found that the intended ownership split was already declared,
but some Working Practices wording repeated Binder/live-state and standing-register rules as
normative Working Practices semantics. That creates two apparent owners for the same model.

**Decision.** Preserve the split:

```text
Documentation Methodology
  → WIP / Working / OpenItems / WorkRegister semantics, lifecycle, authority and Binder/live-state
    semantic treatment

Working Practices
  → when/how active state is persisted, checkpointed, transferred, synchronised, verified and
    handled operationally
```

Working Practices may reference or briefly summarise owner-defined semantics only to make an
operational instruction intelligible; the summary is not an independent normative definition.
Practical checkpoint triggers, preservation-first behaviour, currency/transfer verification,
physical/repository handling and handoff workflow remain Working Practices concerns.

**Alternatives considered.** Keep duplicate text for convenience. Rejected because copied semantic
rules can drift and make later ownership/refactoring ambiguous. Move all WIP/Binder operational
behaviour into Documentation Methodology. Rejected because that would make the methodology own
cross-surface operating behaviour rather than document semantics.

**Consequence.** D31 remains historical context but is read through this clarification: Working
Practices recognises and obeys the Documentation Methodology top-level-topic/state model; it does
not define that model.

## D34 — A deferred received Project Handoff uses one existing OpenItem as its continuity holder

**Trigger / problem.** A Project Handoff is transfer material and should disappear after
reconciliation, but if the destination defers incorporation beyond the current pass/context there
is otherwise no durable live reminder that the transfer still needs action.

**Decision.** On destination receipt:

- same-pass/context reconciliation requires no additional live entry;
- deferred reconciliation creates one concise OpenItem such as
  `Reconcile Project Handoff <identity/source>`;
- completing reconciliation removes that OpenItem; and
- completed transfer material is removed from active context.

This uses the existing Documentation Methodology OpenItems semantics. It does not create a Project
Handoff DocType, Handoff register/archive, obligations ledger or separate lifecycle system.

**Consequence.** Project Handoff remains non-authoritative transfer material while still surviving
context change long enough to be reconciled safely.

## D35 — Review B R1 remediation remains within AIDE_WorkingPractices@v1

**Decision.** Preserve formal capability identity `AIDE_WorkingPractices@v1` and issue the
canonical Standard as document version 5.

**Reason.** The pass removes duplicated ownership, tightens existing operational behaviour and uses
an existing OpenItems mechanism for deferred Handoff continuity. It introduces no new independent
capability mechanism or persisted consumer-state migration.

---
Dependencies: !AIDE_DocumentationMethodology@v21, WorkingPractices_Design_v6
References: DocumentationMethodology_Decisions_v19, Principles_Decisions_v3
<!-- END SOURCE: WorkingPractices_Decisions_v6.md -->

---

<!-- BEGIN SOURCE: AIDE_WorkingPractices_Standard_v5.md -->
# AIDE Working Practices — Standard

> **Identity:** `AIDE_WorkingPractices@v1`
> **Common name:** Working Practices
> **Version 5** (2026-09-01). Clarifies Documentation Methodology semantic ownership and adds
> deferred Project Handoff continuity handling while preserving `AIDE_WorkingPractices@v1`.
>
> **Default weight:** Expectation

## Purpose

Provide portable base conventions for how an AI and user practically approach, communicate,
organise, complete and hand over work.

This Standard may be used as part of full AIDE or independently.

## WP1 — Change Delivery Package

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


## WP2 — Use the owning project's current baseline for cross-project master changes

Before issuing authoritative changes for another owning top-level topic/container, use that owner's current Binder
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

On destination receipt:

- if reconciliation/incorporation completes in the same pass or active context, no additional live
  entry is required;
- if it is deferred beyond the current pass/context, create one concise destination OpenItem under
  the current Documentation Methodology, for example `Reconcile Project Handoff <identity/source>`;
- remove that OpenItem when reconciliation is complete; and
- remove the transfer material from active context once its purpose is complete.

This is operational use of the existing OpenItems mechanism, not a new Project Handoff DocType,
register or lifecycle.

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

Binder composition and live-state lifecycle semantics belong to the current Documentation
Methodology. Operationally, when active work needs owner-defined live state that is not in the
normal Binder, load that current material separately and verify its actual currency where the
platform permits. Do not infer that generating or transferring a new live-state checkpoint has
updated the Binder or loaded project context.

When a newly issued Binder replaces the active Binder, the prior Binder becomes Superseded and may
be retained under `_superseded/` according to the current repository convention. Replace the loaded
project-context Binder with the new current Binder.


## WP11 — Batch file/document output at meaningful checkpoints

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

## WP12 — Persist active work before context loss would be costly

Do not allow valuable current thinking to depend solely on a volatile chat/session/platform context
once losing that context would materially impair continuation.

Use the current Documentation Methodology to select the correct semantic state holder. Working
Practices governs the preservation decision and timing, not those document-role definitions. For
volatile continuation, this will often mean issuing a lightweight WIP checkpoint; where the state
has already crossed into another owner-defined role, use that role instead.

Useful WIP checkpoint triggers include ending a material work session, switching chats/projects/
platforms, moving to unrelated work likely to displace active context, completing a substantial
reasoning block not represented durably, impending context/cache reset, or explicit request for a
physical continuation checkpoint.

Do not checkpoint every message merely because WIP exists. Where the AI judges persistence is
materially useful, advise/create the checkpoint according to current authority rather than waiting
for the human to discover context loss.

## WP13 — Use visible WIP version currency when moving context

When a WIP checkpoint is intended for project/context replacement or inter-platform transfer, use
the current versioned filename and identify the version being transferred.

The practical question is:

> Is the WIP file I have loaded the current issued checkpoint?

Do not infer successful replacement/sync merely because a new file was generated. Verify the
loaded/available version where the platform permits.

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

Documentation Methodology owns document lifecycle meaning, WIP/Working/OpenItems/WorkRegister
semantics and Binder/live-state semantic treatment. Working Practices owns the operational
checkpoint, transfer, synchronisation, verification and physical-handling behaviour that uses those
semantics; any brief role summary here is non-normative. Use the specialised owner for Domain,
Dependencies, Migration, Review, Build or Deployment semantics.

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
Dependencies: !AIDE_DocumentationMethodology@v21
References: WorkingPractices_Design_v6, AIDE_Principles@v1
<!-- END SOURCE: AIDE_WorkingPractices_Standard_v5.md -->

---
