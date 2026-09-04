# Working Practices — Decisions

> **Version 2** (2026-08-31). Reissued against current Core/Documentation Methodology and records
> the first canonical Standard plus cross-project baseline checking.
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

---
Dependencies: !AIDE_DocumentationMethodology@v19, WorkingPractices_Design_v2
References: Principles_Decisions_v3
