# Working Practices Binder

> **Generated Binder — do not edit directly.**
> **Binder Version 1** (2026-08-31). First independently versioned Working Practices Binder,
> finalised before distribution with Project Handoff, repository/Binder and checkpoint-based
> output-batching conventions.
> Edit the individual Current master documents and regenerate/issue the Binder.

## Binder status

This is a generated, read-only consumption artefact kept in the active/master project folder for
easy project-context selection. It is not an authoritative master. Binder version counts issued
Binder assemblies independently of the contained document/capability versions.

## Binder manifest

- `WorkingPractices_Index_v4.md` — sha256 `d852f400856f`
- `WorkingPractices_Brief_v3.md` — sha256 `a77119a30a4e`
- `WorkingPractices_Design_v4.md` — sha256 `b289d6e97861`
- `WorkingPractices_Decisions_v4.md` — sha256 `9c087bb7f500`
- `AIDE_WorkingPractices_Standard_v3.md` — sha256 `5b9ad37515f6`

---

<!-- BEGIN SOURCE: WorkingPractices_Index_v4.md -->
# Working Practices — Index

> **Version 4** (2026-08-31). Registers the consolidated Project Handoff, Documentation
> Methodology v20 ownership boundary, repository/Binder conventions and checkpoint-based output
> batching for the first distributable Working Practices capability.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## Project identity

**Topic:** Working Practices  
**Master folder / GPT Project:** `AIDE/Working Practices/`  
**Published capability identity:** `AIDE_WorkingPractices@v1`

Working Practices is a top-level cross-cutting AIDE concern and can also be deployed independently.

## Topic declarations

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Working Practices | None | `WorkingPractices` | independent | expanded |

## Local configuration

None.

## Document register

| Document | Version | Type | Management | Status |
|---|---:|---|---|---|
| `WorkingPractices_Index` | v4 | Index | established | Current |
| `WorkingPractices_Brief` | v3 | Brief | established | Current |
| `WorkingPractices_Design` | v4 | Design | established | Current |
| `WorkingPractices_Decisions` | v4 | Decisions | established | Current |
| `AIDE_WorkingPractices_Standard` | v3 | Standard | established | Current canonical AI-facing outcome; identity `AIDE_WorkingPractices@v1` |


### Generated current consumption artefact

`WorkingPractices_Binder_v1.md` is the current generated/read-only project Binder. It is kept in
the active/master project folder for easy project-context selection, is not an authoritative
master, and is regenerated from the Current masters above.

### Withdrawn, renamed or rehomed

None.

## Output model

```text
WorkingPractices_Design
        ↓
AIDE_WorkingPractices_Standard
```

## Relationship to Principles

Principles owns durable reasoning/problem-solving premises.

Working Practices owns concrete cross-surface conventions for carrying out, communicating,
verifying and handing over work.

## Relationship to Documentation Methodology

Documentation Methodology owns document lifecycle meaning and document-governance semantics.

Working Practices owns the practical file/repository handling convention used to realise those
states in the current AIDE workflow, without making a physical folder the definition of a lifecycle
state.

## Assets register

None.

---
Dependencies: !AIDE_DocumentationMethodology@v20
References: WorkingPractices_Design_v4, AIDE_WorkingPractices@v1, Principles_Design_v3
<!-- END SOURCE: WorkingPractices_Index_v4.md -->

---

<!-- BEGIN SOURCE: WorkingPractices_Brief_v3.md -->
# Working Practices — Brief

> **Version 3** (2026-08-31). Consolidates Project Handoff, repository/Binder conventions and
> checkpoint-based batching of documentation/file output under the clarified Documentation
> Methodology ownership boundary.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## Purpose

Working Practices defines **how an AI and user practically work together** across chat, document,
code, Work, repository and other AI-assisted surfaces.

It covers cross-cutting conventions that are too operational to be Principles and too general to
belong to one work Domain or output methodology.

## Required model

Working Practices must be:

- a top-level AIDE concern;
- independently deployable;
- complementary to Principles;
- portable across software and non-software work;
- base guidance customisable through small Guidance Profile deltas;
- explicit about the distinction between generated intent and observed/applied state; and
- clear about the boundary between semantic ownership and practical workflow implementation.

## Demonstrated practices

- material multi-file output uses a Change Delivery Package;
- Change Delivery Packages use a defined staging/completion workflow where repository storage is
  available;
- cross-project master changes use the owning project's current Binder/current sources when
  available;
- material knowledge crossing AIDE project ownership boundaries uses a Project Handoff;
- structural/management folders are visually distinguished from substantive content using the
  current `_` prefix convention;
- generated project Binders are independently versioned, read-only consumption artefacts kept with
  the active masters for easy selection/context loading;
- confirmed file/document changes are normally queued and emitted in one consolidated pass at a
  significant work-unit, session or completion checkpoint rather than after every change;
- coded references are glossed on first use;
- externally held/current facts are checked rather than plausibly invented;
- material state-changing actions are not silently assumed complete;
- architecture-shaping choices are surfaced explicitly; and
- complex work proceeds in human-comprehensible layers.

## Outcome

```text
AIDE_WorkingPractices@v1
```

---
Dependencies: !AIDE_DocumentationMethodology@v20
References: WorkingPractices_Design_v4, Principles_Brief_v3
<!-- END SOURCE: WorkingPractices_Brief_v3.md -->

---

<!-- BEGIN SOURCE: WorkingPractices_Design_v4.md -->
# Working Practices — Design

> **Version 4** (2026-08-31). Consolidates Project Handoff, the Documentation Methodology v20
> lifecycle/workflow boundary, repository/Binder conventions and checkpoint-based batching of
> documentation/file output.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## §1 — Purpose

Working Practices defines the practical cross-cutting conventions used when an AI and user work
together.

It answers:

> How should work be approached, communicated, organised, completed and handed over in practice?

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

Working Practices tells the AI **how to work with the user and handle work operationally**.

It does not take semantic ownership from specialised components.

Examples:

```text
Documentation Methodology
  defines Current / Superseded / Archived meaning and document version/lifecycle rules.

Working Practices
  defines the practical file/repository handling convention used to realise those states.

AI Deployment
  defines deployment reconciliation/verification.

Working Practices
  requires deployment handoffs to distinguish generated intent from confirmed deployed state.

Core/Domain
  defines Domain resolution.

Working Practices
  may require checking the current owning-project Binder before cross-project edits.
```

A physical folder never defines a Documentation Methodology lifecycle state. Resolve semantic state
under its owning methodology first; apply the current Working Practices handling convention second.

## §4 — Base guidance and Guidance Profiles

`AIDE_WorkingPractices@v1` is the portable base.

Optional organisation/group/team/user Guidance Profiles may provide deltas:

```text
Add
Refine
Override
```

Profiles contain only differences from the base.

A narrower applicable profile changes only practices it explicitly addresses. Unmentioned base
guidance remains effective.

Equal-specificity conflict fails visibly unless explicit ordering exists.

Host/platform instruction priority remains outside AIDE.

The shared profile concept is not promoted into a separate generic component yet.

## §5 — Confirmed Working Practices

### WP1 — Material multi-file output uses a Change Delivery Package

When a session creates or materially changes multiple files, crosses project/master-folder
boundaries, or otherwise leaves non-obvious application steps, issue one **Change Delivery
Package**.

Normal portable representation where supported:

```text
<Project>_ChangeDelivery_<date>.zip
├── created/changed deliverable files
└── <Project>_ChangeDelivery_Instructions_<date>.md
```

The application instructions should identify, where applicable:

- file/action;
- destination master folder/project;
- whether new or replacing Current;
- prior issued versions becoming Superseded and their physical handling under the current Working Practices convention;
- archive/withdraw/remove action where relevant;
- rename/move/ownership changes;
- Binder/Bundle regeneration or replacement;
- GPT/Claude/project-context additions/removals/replacements;
- cross-project consequences;
- deployment/source consequences without claiming deployment occurred;
- transfer-only artefacts that must not become masters;
- actions requiring another project/process/authority;
- intentionally unchanged related items where omission could be mistaken for oversight; and
- unconfirmed actions still requiring user/environment execution.

Do not force this packaging ceremony for a trivial one-file output whose application is obvious.

Use it where complexity, lifecycle, destination, handoff or loss/misapplication risk makes the
instructions materially useful.

The ZIP/instructions are transfer artefacts. Generating them does not itself apply their contents.

Under the current AIDE repository workflow, stage active Change Delivery ZIPs in:

```text
Documentation/_changeDeliveryPackages/
```

After the package has been applied/reviewed and its required actions are complete, move the ZIP to:

```text
Documentation/_changeDeliveryPackages/_completed/
```

These locations implement workflow state; they are not authoritative corpus masters or document
lifecycle definitions.


### WP2 — Check the owning project's current baseline before cross-project master changes

Before creating or revising authoritative masters for another project/container, use that owning
project's current Binder or current master sources when reasonably available.

This is especially important where parallel activity may have changed versions, Standards,
Indexes or lifecycle rules since the originating discussion.

Do not modify another project from an old handoff snapshot merely because it was previously
authoritative.

If the current baseline cannot be obtained, state the limitation and avoid claiming reconciliation
against current state.

Generated Binders are read-only consumption sources: edit masters, then regenerate.

### WP3 — Gloss coded references

On first use in a response, give a short plain-language gloss for coded section/decision/question
IDs or opaque document/capability references when meaning is not already obvious in the immediate
context.

### WP4 — Check externally held/current facts before asserting them

When a statement depends on records, installed state, current files, environment configuration or
another inspectable authority, check the available source/tool first when reasonably possible.

If it cannot be verified, say what is unknown.

Do not manufacture a plausible value.

### WP5 — Do not silently assume material state changes

Generating, proposing or handing off a change is not the same as applying it.

Clearly distinguish states such as:

```text
created
proposed
handed off
applied
installed
deployed
verified
```

Use the appropriate authority/tool/environment observation before claiming completion.

### WP6 — Surface architecture-shaping choices

Handle routine, low-risk and reversible choices autonomously.

For genuinely architecture-shaping decisions or material trade-offs, present enough structure for
the user to decide without reconstructing the alternatives:

```text
Decision
Recommendation
Why
Credible alternative
Consequence
```

Do not inflate routine implementation details into decision ceremony.

### WP7 — Work in layers before detail

For complex design/problem-solving work, establish a compact intent/premise layer and model before
deep elaboration.

Prefer a small human-comprehensible working set and surface partial conclusions early enough for
the user to steer.

### WP8 — Preserve durable handoff when work moves

When substantial confirmed work moves to another project, session, environment or responsible
owner, provide a compact durable handoff containing, proportionately:

- authoritative source artefacts or pointers;
- confirmed model/decisions and material reasoning needed to understand them;
- what remains to be done;
- important deferred/non-goals; and
- application/integration instructions.

A handoff summary is transfer material unless the destination explicitly adopts it as a master.
Once integrated, stale handoff summaries should not remain in ongoing context beside authoritative
sources unless they still have an active purpose.

#### Project Handoff — named cross-project form

**Project Handoff** is the formal cross-project form of durable handoff. Conversational shorthand
may be **Handoff** where the destination and meaning are obvious.

> **Project Handoff** — a concise transfer of material knowledge, reasoning, decisions,
> implications and authoritative source pointers from one AIDE project to another project that owns
> or should act on that information.

Use or suggest a Project Handoff when work in one project develops knowledge that materially
affects another project's owned concern. A useful test is:

> Would this knowledge materially help the owning project make, understand or implement its next
> decision?

Do not create one for routine chatter or information already fully represented in authoritative
sources. The AI should proactively suggest a Project Handoff when material work clearly creates a
consequence owned by another project, and should produce one when requested or when the agreed
work/delivery calls for it.

A useful Project Handoff carries, proportionately:

- why the Handoff is being made;
- material reasoning/context not safely recoverable from final outputs alone;
- confirmed decisions relevant to the destination;
- important alternatives, constraints or trade-offs;
- destination-project implications/consequences;
- unresolved or deferred items;
- authoritative source artefacts/pointers;
- what is proposed versus already confirmed;
- action expected from the destination project; and
- important non-goals/boundaries that prevent needless re-derivation.

Keep it concise enough to function as transfer context rather than a transcript of the originating
conversation.

#### Project Handoff lifecycle and destination rule

Normal lifecycle:

```text
originating project
    develops relevant knowledge/reasoning
            ↓
Project Handoff
            ↓
destination owning project
    reconciles against CURRENT Binder/masters
            ↓
updates its own Design / Decisions / outcomes
            ↓
Handoff has served its purpose
```

A Project Handoff is normally transfer context, not an enduring master or second source of truth.
The destination's current authoritative corpus is the baseline. Before acting on the Handoff, use
the destination's current Binder or current master sources where reasonably available, surface any
genuine conflict, and do not let an older Handoff override newer destination state merely because
it was accurate when created.

Once useful content has been incorporated into the destination's authoritative corpus, normally
remove the Handoff from active project context unless it still serves an explicit purpose.

#### Ownership rule

Discovering a consequence owned by another project does not by itself authorise the originating
project to rewrite that project's masters. The normal ownership-preserving flow is:

```text
originating project
→ Project Handoff
→ owning project
→ authoritative update
```

If a separate task/authority explicitly requires cross-project master changes, WP2 still applies:
use the owning project's current Binder/masters as the baseline before issuing those changes.

#### Project Handoff versus Change Delivery Package

These are complementary but distinct transfer mechanisms:

```text
Project Handoff
  → knowledge, reasoning, decisions, implications and authoritative source pointers

Change Delivery Package
  → concrete created/changed files plus instructions for applying them
```

A Project Handoff may contain no changed files. A Change Delivery Package may include or accompany
a Project Handoff where another project needs reasoning/context as well as files. Do not merge the
two concepts or treat a knowledge-only Project Handoff as a packaging trigger.

### WP9 — Distinguish structural/management folders from substantive content

Where the work is realised in a filesystem/repository and the distinction is useful, prefix
structural or workflow-management folders with `_` so they are visibly distinct from substantive
content and ordinary working folders.

Current AIDE conventions include:

```text
_superseded/
_archived/
_changeDeliveryPackages/
_completed/
```

The prefix is an operational naming convention, not a semantic type system. Create management
folders only where the workflow actually needs them.

Under the current repository convention:

- material already determined to be **Superseded** may be physically held in `_superseded/`;
- material already determined to be **Archived** may be physically held in `_archived/`; and
- Change Delivery Packages use the staging/completion locations defined in WP1.

The semantic owner determines lifecycle state before Working Practices determines physical
handling.

To control active-repository size, historical contents of `_superseded/`, `_archived/` and
`_changeDeliveryPackages/_completed/` may periodically move to longer-term storage outside the
active repository, provided required history, traceability and authoritative lifecycle meaning are
preserved.

Where a platform does not use filesystem folders, use an equivalent management representation
rather than forcing these literal paths.

### WP10 — Keep the current versioned Binder with the active masters

Generated project Binders are read-only consumption artefacts that provide a coherent current
corpus for project context/retrieval. They are not authoritative masters.

Use an independently versioned filename:

```text
<Project>_Binder_vN.md
```

Binder version counts issued Binder assemblies, not project/capability/source-document versions.
Increment it when a newly issued Binder replaces the previously active Binder. Recreating the same
assembly without issuing a replacement need not create a new version.

Keep the current Binder in the active/master project folder alongside the Current masters so it is
easy to identify and select for project context. Its manifest should identify the exact source
versions and integrity/hash information used to assemble it.

When replaced:

1. the prior Binder becomes Superseded because it was replaced, not because of its folder;
2. under the current repository convention, move/retain it in `_superseded/` if historical Binder
   retention is useful; and
3. replace the loaded project-context Binder with the newly issued current Binder.

Never edit a Binder to change project state. Edit authoritative masters, then regenerate and issue
a replacement Binder.


### WP11 — Batch file/document output at meaningful checkpoints

Do not issue changed master files, generated Binders or Change Delivery Packages after every
individual confirmed change by default.

During an active unit of work, accumulate/queue confirmed changes and produce one consolidated
output pass when one of these conditions applies:

- a significant unit of work has completed;
- the work session is ending;
- a meaningful completion/integration checkpoint has been reached;
- the user explicitly asks to run/output the pass, for example `output updates`, `update docs`,
  `run the pass`, `build change file/package`, or equivalent; or
- delaying durable output would create material risk of losing confirmed information, creating
  ambiguity, or causing significant downstream impact.

Before autonomously producing a material file set or Change Delivery Package, ask whether the user
wants the accumulated changes output now or whether more pending work should be included. An
explicit user request to output/build the files or package is already that confirmation and should
not trigger another approval question.

The default working flow is therefore:

```text
work / discussion / Handoffs
        ↓
confirmed changes accumulate
        ↓
queue for next output pass
        ↓
significant unit / session / checkpoint
        ↓
confirm output if not already requested
        ↓
one consolidated file + Binder + Change Delivery pass
```

This batching posture is especially important where one chat/project has generated a Project
Handoff and a reply or further consequence is reasonably expected. Normally allow the exchange to
reach a useful checkpoint before reissuing documentation, rather than generating another document
set/package on each round.

Batching is subordinate to preservation. Never defer durable capture merely to reduce file churn
where confirmed state is at material risk of loss or where delay could materially mislead or block
downstream work. In that case, preserve the state using the least-churn appropriate durable
mechanism and consolidate normal deliverable output later.

## §6 — Standalone use

A general AI environment may deploy only:

```text
AIDE_Principles
AIDE_WorkingPractices
```

through an appropriate Bootstrap Profile.

A full AIDE environment may deploy the same base guidance alongside Core, Domain, Project Design,
Build, Documentation Methodology and other capabilities.

## §7 — Intended output

Produce:

```text
AIDE_WorkingPractices@v1
```

The Standard should be concise, operational and platform-neutral. Rich examples remain in Design
or future Guide material rather than bloating base guidance.

---
Dependencies: !AIDE_DocumentationMethodology@v20
References: WorkingPractices_Decisions_v4, Principles_Design_v3, Core_Bootstrap_Design_v2
<!-- END SOURCE: WorkingPractices_Design_v4.md -->

---

<!-- BEGIN SOURCE: WorkingPractices_Decisions_v4.md -->
# Working Practices — Decisions

> **Version 4** (2026-08-31). Preserves Project Handoff history and records the Documentation
> Methodology v20 workflow boundary, repository/Binder conventions and checkpoint-based batching
> of file/document output.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

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


---
Dependencies: !AIDE_DocumentationMethodology@v20, WorkingPractices_Design_v4
References: Principles_Decisions_v3
<!-- END SOURCE: WorkingPractices_Decisions_v4.md -->

---

<!-- BEGIN SOURCE: AIDE_WorkingPractices_Standard_v3.md -->
# AIDE Working Practices — Standard

> **Identity:** `AIDE_WorkingPractices@v1`
> **Common name:** Working Practices
> **Version 3** (2026-08-31). Consolidates Project Handoff, repository/Binder conventions and
> checkpoint-based batching of documentation/file output under the clarified Documentation
> Methodology v20 boundary. Formal capability identity remains `AIDE_WorkingPractices@v1`.
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
  CurrentVersion: v1
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v20
References: WorkingPractices_Design_v4, AIDE_Principles@v1
<!-- END SOURCE: AIDE_WorkingPractices_Standard_v3.md -->
