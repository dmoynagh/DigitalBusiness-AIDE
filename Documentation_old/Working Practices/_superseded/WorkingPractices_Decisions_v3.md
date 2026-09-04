# Working Practices — Decisions

> **Version 3** (2026-08-31). Records the clarified lifecycle/workflow ownership boundary,
> management-folder and Change Delivery storage conventions, independently versioned Binder
> handling, and the formal Project Handoff convention.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## D1 — Working Practices is a top-level AIDE topic

**Decision.** Working Practices is a sibling of Principles, Core, Project Design, Build,
Capabilities and other principal AIDE concerns.

**Reason.** It governs practical AI/user collaboration across work types and output forms.

## D2 — Working Practices is independently deployable

**Decision.** `AIDE_WorkingPractices` is usable without full AIDE.

**Reason.** General AI sessions can benefit from working conventions without development-specific
context.

## D3 — Working Practices is base guidance

**Decision.** The canonical Standard supplies portable defaults rather than one user/team's final
customised behaviour.

## D4 — Guidance Profiles provide deltas

**Decision.** Organisation/group/team/user Profiles may Add, Refine or explicitly Override named
Working Practices without copying/forking the base Standard.

## D5 — Specialised owners retain semantics

**Decision.** Working Practices may require the AI to communicate, organise or hand off specialised
state but does not redefine lifecycle, deployment, dependency, migration, Domain or other owned
semantics.

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
decisions, material reasoning/implications, remaining work and integration instructions.

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

## D14 — Documentation lifecycle meaning and physical workflow are separate concerns

**Trigger / problem.** Documentation Methodology historically described both lifecycle states and
some physical storage conventions, making the document methodology unnecessarily filesystem-aware.

**Decision.** Documentation Methodology retains document lifecycle/version semantics. Working
Practices owns practical file/repository handling conventions used to implement those states.

**Reason.** “Why this artefact is Superseded/Archived” is a documentation-governance question;
“where we put it in this repository” is an operating-practice question.

**Consequence.** A folder name never creates lifecycle state. The semantic owner determines state
first; Working Practices then applies the current physical handling convention.

## D15 — Management folders use a leading underscore convention

**Decision.** Where useful in filesystem/repository work, structural/workflow-management folders
use a leading `_` to distinguish them visually from substantive content and ordinary working
folders.

**Current examples.** `_superseded/`, `_archived/`, `_changeDeliveryPackages/`, `_completed/`.

**Reason.** The distinction reduces navigation/file-handling friction without requiring extra
metadata or complex structure.

**Constraint.** The convention does not require creating management folders that the workflow does
not need and does not define semantic lifecycle state.

## D16 — Superseded and archived storage names are Working Practices conventions

**Decision.** Under the current repository convention, Superseded material is handled through
`_superseded/` and Archived material through `_archived/` where physical folders are used.

**Reason.** The names make management structure immediately recognisable while preserving the
semantic/storage separation established in D14.

**Portability.** Non-filesystem environments may use an equivalent representation.

## D17 — Change Delivery Packages have a staging/completion workflow

**Decision.** Under the current AIDE repository workflow, stage active Change Delivery ZIPs in
`Documentation/_changeDeliveryPackages/` and move completed/applied ZIPs to
`Documentation/_changeDeliveryPackages/_completed/`.

**Reason.** This creates one predictable place to review/apply deliveries and separates active from
completed transfer material without making either a corpus master.

## D18 — Historical management material may leave the active repository

**Decision.** Historical contents of `_superseded/`, `_archived/` and
`_changeDeliveryPackages/_completed/` may periodically be transferred to longer-term external
storage to control active-repository size.

**Constraint.** Required history, traceability and authoritative lifecycle meaning must be
preserved. Repository-size reduction is not permission to discard governed history.

## D19 — Binders are independently versioned current consumption artefacts

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

## D20 — Project Handoff is the cross-project knowledge-transfer convention

**Trigger / problem.** Material reasoning developed in one AIDE project can affect another owning
project, but copying it into authoritative sources prematurely creates competing truth while leaving
it only in conversation risks losing useful reasoning.

**Decision.** Use **Project Handoff** for a concise transfer of material knowledge, reasoning,
decisions, implications and authoritative source pointers from one AIDE project to another project
that owns or should act on that information. “Handoff” is acceptable shorthand where the
destination is obvious.

**Trigger test.** Ask whether the knowledge would materially help the owning project make,
understand or implement its next decision. If yes, create or proactively suggest a Project Handoff.

**Constraint.** Do not create one for routine chatter or information already fully represented in
authoritative sources available to the destination.

**Consequence.** A Project Handoff is transfer material, not a duplicate authoritative source. The
destination reconciles it against its current baseline before changing masters.

---
Dependencies: !AIDE_DocumentationMethodology@v20, WorkingPractices_Design_v3
References: Principles_Decisions_v3
