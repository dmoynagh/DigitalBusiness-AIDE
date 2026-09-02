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
