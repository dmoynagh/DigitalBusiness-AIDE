# Principles — Decisions

> **Version 4** (2026-09-08). Authored fresh in the AIDE rebuild. Compacted
> from v3 where decisions still stand; new decisions added from the design pass.
>
> Created: 2026-08-27 | Last modified: 2026-09-08

## D1 — Principles is a top-level topic, independently deployable

Principles is a cross-cutting concern applying to every project and scenario.
It is a top-level topic, not a subtopic of anything else. The standard works
both as part of AIDE and on its own, because base reasoning guidance is useful
in general AI sessions that are not doing full-AIDE work.

## D2 — Principles is base guidance, not a personalised configuration

The standard defines the portable default. Putting user or team preferences
directly into the base was rejected because the base would stop being portable
and every consumer would inherit one party's local choices.

## D3 — Principles and Working Practices are sibling concerns

Working Practices is not a child of Principles. Principles owns judgement
premises; Working Practices owns practical cross-surface collaboration and
operating conventions. Both can be independently useful.

## D4 — Guidance Profiles use a delta model, housed in Working Practices

Guidance Profiles may add, refine or explicitly override named base guidance
using small deltas. Unmentioned base guidance remains effective.
Equal-specificity contradictions fail visibly unless explicitly ordered.

No generic profile component is created yet — Principles and Working Practices
are the demonstrated consumers, and wider generalisation waits for evidence.

The profile mechanism and its review are housed in Working Practices. The open
question is whether the model earns its place for a solo developer — review
starts from these decisions (formerly D4 and D5).

## D5 — Portability is the defining test, meaning universality

A premise belongs in Principles only if it holds outside AIDE. Anything true
only inside AIDE drops to methodology or working practices. "Interaction"
premises qualify — a universal interaction premise is still a principle. The
real filter is "independent of platform or methodology."

Adopted during the rebuild design pass (2026-09-07) to make the existing
implicit test explicit.

## D6 — The information-holder boundary premise moved to Working Practices

The old P6 ("information holder decides the boundary") was about which
component, project or domain should answer a boundary question — AIDE-context
behaviour, not a universal premise. It fails the portability test and moves to
Working Practices.

## D7 — Authoritative evidence replaced declaration-over-inference wording

The original seed said "Domains are declared, not detected." The confirmed
model now permits implicit resolution from recognised authoritative structures.
Replaced with "authoritative evidence over incidental inference" — the deeper
intent (rejecting accidental presence or proximity inference) is preserved, the
rigid declaration-only rule is not.

The premise's AIDE-specific examples (declared relationships, folder proximity)
are demoted to illustration beneath the premise statement, so they do not read
as part of it.

## D8 — Operational seed behaviours moved without loss

Concrete behaviours from the original seed — coded-reference glossing,
verification before assertion, no-silent-state-change behaviour and others —
are represented in Working Practices. They remain valuable but are operational
conventions rather than root reasoning premises.

## D9 — Definition of done identified as a candidate premise

Definition of done has been promoted to a generic block type owned by Working
Practices, carrying a testable-or-assessable invariant. Whether it also earns a
place as a Principles premise is an open question — it reopens the Principles
element list once Working Practices completes its definition.
