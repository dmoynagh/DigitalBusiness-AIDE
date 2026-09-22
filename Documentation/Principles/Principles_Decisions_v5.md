> identity: Principles_Decisions@v5 | doctype: decisions | updated: 2026-09-15

# Principles — Decisions

> **Version 5** (2026-09-15). Authored fresh in the AIDE rebuild. Compacted
> from v3 where decisions still stand; new decisions added from the design pass.
>
> Created: 2026-08-27 | Last modified: 2026-09-15

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

## D10 — P3 strengthened: difficulty-as-evidence and apparatus-avoidance

Two strengthenings to the model-before-elaboration premise, both carried from the design-approach work (F12 pattern — sharpen existing premises, not new ones).

Difficulty-as-evidence adds the feedback signal P3 lacked. P3 previously said "state the model first" — sequential, one direction. The strengthening makes it bidirectional: when elaboration becomes difficult, that is evidence the model above needs review. The recurrence pattern (same accommodation appearing across several elements) is especially strong evidence. This is the portable root of the operational rule already placed in Project Design's commitment-and-return section (PD D25).

Apparatus-avoidance makes P3's failure mode explicit by naming the specific form. The previous failure mode described the symptom ("detailed mechanisms make an average premise look settled") without naming the specific form. The strengthening names it: stages, phases, procedural machinery built around a principle that is not yet well enough conceived.

Both pass the portability test — they hold outside AIDE. Difficulty-as-evidence is universal (hard implementation suggests wrong abstraction). Apparatus-avoidance is universal (procedure around a principle means the principle isn't clear enough).

## D11 — P4 strengthened: proportionality signal

P4 previously said "keep the working set small enough to hold" and "use layered progression" but carried no test for whether the layers were proportionate. The strengthening adds the signal: output markedly more elaborate than the intent above it is a warning that the solution is not yet well enough conceived.

Passes the portability test — across domains, output markedly more elaborate than the intent it serves is a useful signal to re-examine whether the problem and solution are sufficiently well conceived. It is a warning, not proof of a defective model.

Same F12 pattern as D10 — strengthen the existing premise, not a new one. The premise count stays at nine.

---

Version note: v5 — adds D10 (P3 strengthened: difficulty-as-evidence and apparatus-avoidance) and D11 (P4 strengthened: proportionality signal). Three candidate premise strengthenings from the design-approach work, all resolved as strengthenings per F12 pattern. Cross-review: F1 remediated (false-exclusive removed), F2 remediated (positive injunction → naming the form), F3 remediated (universal causation → warning signal). 2026-09-15.
