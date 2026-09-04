# Working Document — Interaction and Assurance Model

Status: working draft. Not a registered corpus document. No version register, index entry, or
corpus formatting conventions applied — placement to be decided once the remodelled AIDE
framework lands.

Date: 2026-09-03
Source: design conversation, Workflow project.

---

## 1. Purpose

To structure the working relationship so that Dave's time is concentrated on the decisions and
insights only he can supply, while work delegated to AI is chosen for suitability, executed to
defined intent and standards, and returned in a form that makes its correctness checkable rather
than merely plausible — with the undescribed parts of the intent surfaced rather than silently
filled.

Two shifts from the starting framing were made deliberately and are load-bearing:

**From reviewed to checkable.** Review is one instrument, not the centre. Review scales badly with
volume: as AI does more of the build, reviewing becomes a load on Dave or on a second model whose
agreement is only weakly informative. Where done has a testable meaning, correctness stops
depending on anyone reading carefully, and review is spent where it is strong — judgement and
approach, not conformance.

**Elicitation is in scope, not upstream of it.** The concept in Dave's head may not have been
described, resolved, or worked through. Drawing out and pinning down intent is part of what is
delegated, not a precondition to it. If this is not named in the purpose it will not be designed
for, and every convention built downstream will assume a well-formed input that often will not
exist.

Proportionality to risk is deliberately excluded here. It is a property of the mechanisms, not of
the objective.

---

## 2. The two parts

The work divides into two parts with different contexts, issues and challenges. They need
different conventions, not one convention applied twice.

**Part one — the why, what, who.** Building and defining clear outcomes.

Correctness here has no internal test. The artefact can be coherent, well-structured and
reviewable by any number of models and still be wrong, because nothing inside it says whether it
matches the concept in Dave's head or the actual business need. The only ground truth is Dave.
AI's role is almost entirely elicitation and challenge: drawing the thing out, finding where it is
underspecified, testing it against cases, reporting when the input is thin. The failure mode is
producing something plausible enough that the gap never surfaces.

**Part two — the how, when, where.** Designing, defining, planning, build, delivery, lifecycle.

Correctness here is checkable in principle. Given a settled why and what, the how can be validated
against it. This is where AI can own execution, where verification beats review, and where Dave's
involvement should concentrate at approach and acceptance rather than through the middle.

**The boundary is a gate.** Part two should not start on an input part one has not declared
settled. Part two discovering the why was wrong is a signal to go back, not to patch forward.

---

## 3. The evolving-scope problem

A percentage of the why, what and who will always be unknown, fluid or evolving. Projects change
as learning grows and understanding increases. This is a condition to be managed, not a defect to
be eliminated.

The consequence: the goal is not fuller scope up front. It is making the evolution **visible when
it happens** — noticing that an assumption made several steps back is no longer holding, and
surfacing it while it is still cheap to act on. That is a detection problem, not a completeness
problem.

Fire-and-forget structurally cannot do this. By the time the result arrives, the shift is baked in.

---

## 4. Layering — the response shape

Dave thinks in models and patterns and extrapolates readily from a single point. High volume at
headline resolution is fine and preferred. Unsolicited detail degrades capability, because it
substitutes for extrapolation Dave would do faster himself.

**Tier one — Overview.** Self-contained. The goal, the high-level approach, and the key defining
decisions together. A complete picture on its own. Someone could read only this and understand
what matters and why. Constrained to the small number of factors that make the structural
difference — not the mechanics of delivery.

**Tier two — Headline skeleton.** The next layer of decisions and points, rendered as headlines.
The key points stated briefly — as if the full detail were written and only the topic sentence of
each section kept. Scannable and listable. Every line an anchor to either nod at or pull on. Not
leftover material; the complete structure at headline resolution.

**Tier three — Detail.** Those same points flattened out with explanation, reasoning and
considerations. Supplied on request only.

**The discipline.** Sometimes tier one alone is the complete answer. In that case tier two is not
delivered; the existence of further material is simply named. The next layer is not produced
without request.

**Mechanics.** Tiering is a display choice, not a re-processing cost. The full thinking is done to
produce the response; expanding a point surfaces depth already held in context. Occasionally
expanding will surface a consideration that reshapes things — this is rare and is a feature.

---

## 5. Channel shapes

**Voice.** One concept per turn. No scrolling back, no re-reading; anything stacked in the middle
evaporates. Sized to hold and react to — not so small that the conversation becomes machine-gunned
or over-segmented. Voice is tier one by nature. Volume that would work as a text list becomes a
queue worked through conversationally.

Voice is a real working channel, used in time that would otherwise be unproductive.

**Text.** Can carry more items, because they can be scanned and returned to.

**Channel suitability by content type.** Assumptions, gap-fills and anomalies work well in voice —
short, judgement-shaped, benefit from immediate reaction. Definition of done and drift detection
want text, because they need precision and a record.

**Durability.** If voice carries anomalies and gap-fills, those exchanges must land somewhere
durable afterwards or the reasoning is lost when the session closes. Voice makes this more acute,
not less.

---

## 6. Lists, paging and acceptance

**The problem.** A list has no state. Reading through it, the first item needing a reaction gets
addressed, that branches into discussion, and on return it is easy to assume the remaining items
were covered when they were never reached. The loss is silent — the artefact still reads as
complete.

**Paging.** Present in manageable chunks. Work an item, branch as far as needed, return, mark it
closed, present the next.

**The return step is where it breaks**, so it is made mechanical rather than remembered: on
returning from a branch, restate position before continuing — what is closed, what is next, how
many remain. One line. Essential in voice, where there is no artefact to look back at.

**Branches generate new items.** If the register is only what was listed at the start, things
discovered during discussion disappear. The list must be able to grow, and additions during a
branch are surfaced on return rather than silently appended.

**Implicit acceptance by skip.** In a list of twenty, engaging item five accepts items one to four.
No confirmation sought; move on.

Exceptions, by risk-and-friction judgement: an item that is consequential, hard to reverse, or
marked at low confidence does not clear silently. Held back and confirmed in one line — not
re-presented. Anything rated Unbounded or Foundational (section 8) never clears on skip,
regardless of confidence, because the cost of being wrong is carried by Dave rather than by the
work.

Confidence markers pre-declare which items are eligible for silent acceptance, so the judgement is
visible before the skip rather than second-guessed after it.

**Asymmetry.** Skipping forward accepts. Returning to an earlier item later is always open —
acceptance by skip closes an item for now, not permanently.

---

## 7. Surfacing — what reaches Dave

The overview is not the deliverable. It is scaffolding that makes the deliverable usable. What
must reach Dave is the small set of things requiring his judgement, landing against a model rather
than arriving as free-floating items needing context reconstructed.

Three things must be true at once. Dave must be **exposed** to what matters (surfacing). The work
must **declare its own soft spots** (self-reporting). Some things must be **checked without either
party reading carefully** (verification). Surfacing without self-reporting shows only what was
already understood. Self-reporting without verification trusts the account of the work rather than
the work. Verification without surfacing catches the mechanical and misses everything else.

### Six elements

**1. Per-item confidence, not per-response.** Marked against the specific claim, decision or step —
not a global hedge. Uneven confidence within one piece of work is the normal case, and averaging
destroys the information. Turns reading from uniform attention into targeted attention. Highest
value of the six.

**2. Assumptions and gap-fills as a standing section.** Where the instruction ran out and a call
was made. Present even when short — an empty section is itself a claim that can be held to.
Addresses silent competence.

**3. Drift detection against the settled baseline.** Explicit checking of whether what is being
built still matches what part one declared. Reported when it fires, at the moment it fires, not at
delivery. This is what replaces fire-and-forget without replacing it with constant check-ins.

**4. The anomalies channel.** Things noticed that cannot be ranked and would not survive an impact
filter. No threshold, no justification required. Texture preserved rather than distilled.

Rationale: pattern recognition and implication-sensing run on specifics — the odd detail, the thing
that does not quite sit right. Compression strips exactly these, because they look like noise to
the compressor. A strict impact filter would suppress precisely the weak signals Dave's judgement
is best at reading. This channel exists to counteract that, and only works if things can be raised
without being defensible.

**5. Definition of done, written before the work, by Dave.** Acceptance stated in checkable terms
at the point work is commissioned. This is what lets verification substitute for review, and where
Dave's time converts most efficiently into assurance. For code in particular: the human-owned
artefact is the definition of done, not the code.

**6. Checkpoint density set at commission time, proportional to risk.** How often work surfaces,
agreed up front rather than negotiated mid-flight. Cheap and reversible work runs long;
consequential or hard-to-unwind work reports early and often.

### Two channels, not one

**What needs a decision** — ranked by consequence.
**What is worth an eye** — unranked, unjustified.

The tension between these is real rather than resolvable. Prioritisation by impact is correct for
decisions and wrong for weak signals.

### Caveat

Elements 1, 2 and 4 depend on accurate introspection about uncertainty, which is imperfect. They
shift the odds substantially; they do not close the gap. Elements 3 and 5 do not carry that
dependency, which is why they are weighted heavily despite being less interesting.

---

## 8. The rating scheme

Three fields. Two inputs and a derived triage output.

### Confidence

| Level | Meaning |
|---|---|
| **Certain** | Take it to the bank. Verified, or no constructible way of being wrong. |
| **Confident** | Would back myself. Would act without checking. |
| **Probable** | Confident but not absolute. My read, and I can see the shape of how it is wrong. |
| **Weak** | Low confidence but grounded. Reasoning from real information that is thin or partial. |
| **Guess** | No real basis. Filling a gap because something had to go there. |

Certain occurs legitimately and often where criteria are objective and checkable — works or does
not work, clear test. Certain as conviction on a judgement call is the degraded form and is worth
calling out when observed.

Guess earns the scale its keep: it turns silent gap-filling into a visible act.

### Impact

Rated on cost to correct if wrong.

| Level | Meaning |
|---|---|
| **Local** | Costs the work itself and nothing more. Notice, redo, move on. Cost bounded and roughly equal to what it took to produce. Nothing was built assuming it. Defining test: the fix is local — you can point at what needs changing and the list does not grow while you look. |
| **Bounded** | It propagated, but the reach is knowable. Affected items can be enumerated without hunting. The fix is mechanical once identified and can be priced before starting. Defining test: the extent is known at the moment the error is discovered. |
| **Unbounded** | It propagated and the reach is unknown. Cannot be bounded without going and looking, and the looking is the expensive part. Residual uncertainty survives the fix. Defining test: the cost cannot be estimated without investigation — and grows with every layer added before it is caught. |
| **Foundational** | Things were built on top and now depend on it. Not search-and-correct but rework of everything that assumed it. Architectural choices, schema decisions, the model something is organised around. Also covers durable error in another sense — published, sent, or externally acted on, so it cannot be quietly withdrawn. Defining test: correcting means undoing rather than amending, at cost disproportionate to the original decision. |

**Useful asymmetry.** Unbounded is expensive to find and cheap to fix once found. Foundational is
easy to find and expensive to fix. Unbounded is therefore the stronger candidate for early
escalation — Foundational tends to announce itself.

**Impact attaches to the action, not the location.** This is the correction most likely to revert
quietly, so it is stated explicitly. The rating measures the exposure created by what is being
done, not the importance of what it is being done to. A verified, tested fix to a foundational
document is Local — the blast radius is small because the error is identified and the fix is
checkable. An unverified assumption about that same document is Foundational. Same document,
different actions, different ratings.

Residual limitation: blast radius can be misjudged — a change thought contained may not be. The
definitions do not fix this. It is the same class as any other misjudgement and is what the
surfacing conventions and Dave's own eye exist to catch.

### Guardrail

Certain at Foundational is the most dangerous cell in the matrix — a wrong call passes with no
friction and gets built on. Where used, it carries the basis alongside it: one line stating what
makes it certain. If the test cannot be stated, it is not Certain, it is Confident, and it routes
accordingly.

### Triage output

Expressed as what is being asked of Dave — not what the work did.

| Value | Meaning |
|---|---|
| **Proceed** | No action needed. Stated for the record. |
| **Note** | Worth an eye. No decision required. Where the anomalies channel lands. |
| **Confirm** | One line back and work continues. |
| **Decide** | Stops here until ruled on. |

Rendered as: `Confirm — Probable | Bounded`

Mapping is judgement, not a lookup table. Local and Confident-or-better is Proceed. Foundational
plus Certain is Note or Confirm, not Decide — a blanket rule sending all Foundational items to
Decide would flood the channel with decisions on things that are not in question, which is how a
triage scheme degrades into noise. The middle is where the mapping will need tuning in use.

### Marking discipline

By exception, not on everything. Local plus high confidence is the default case; tagging it turns
the markers into wallpaper. The pair appears when either dimension is elevated. Guess at any
impact above Local surfaces explicitly rather than sitting in a list.

---

## 9. Fall-through layers

**Principle.** Where failure can occur, a minimum of three fall-through layers. Two for simple,
low-impact work. Three significantly increases the odds of an issue being identified.

**Current model:** Dave, lead AI, second-platform AI.

**Caveat — the layers are less independent than the count suggests.** Layers multiply the odds only
when their failure modes are uncorrelated.

- Lead AI and second AI share training distribution and inductive biases. On facts and internal
  consistency they are reasonably independent and the layering works. On taste, approach, and
  whether the thing is the right thing, they fail together — both over-trust plausible structure,
  both miss the unstated requirement, both elaborate into mechanism when the model should change.
- Dave is a strong detector but a sampling one — he catches what surfaces, and what surfaces is
  partly determined by the lead AI. So lead-AI failure and human failure are not fully independent
  either.

Honest count for the current model: roughly two-and-a-bit, not three.

**The fix is not more AI opinions.** It is a layer whose failure mode is genuinely different — a
mechanical check that involves nobody reading carefully. A test, a probe, a structural validation.
The argument is not that it catches more, but that it catches *differently*.

**Framing determines yield.** "Review this" recruits agreement. "Find the case where this breaks"
recruits information. Evaluative framing is the default and the weaker one.

**Divergence beats agreement.** Two independent attempts at the same problem, generated before
either sees the other, are more informative in where they differ than in where they match.
Divergence localises the underspecified part. This is the proactive-coworker use of the second AI —
advisor and sounding board rather than only checker — and is rated higher value than the review
use.

**Review needs its own feedback loop.** Track which review cycles changed anything. Cycles that
never change anything are ritual, and ritual is where trust quietly detaches from evidence.

---

## 10. Review and verification are different instruments

Review is a second opinion on an artefact. Verification is checking a claim against the world.

The corpus incidents to date were all of the second kind — a version registered that was never
authored, a stated completion that was a self-assessment rather than confirmed receipt. No amount
of reviewing the document catches those, because the document reads fine. That class needs a probe,
not an opinion.

---

## 11. Open items

**O1 — Rating scheme legibility.** The logic is settled and the purpose is defined, but the
translation to human uptake is not landing. Wording, combinations, and what the triple triggers at
a glance need work. To be revised against this document rather than iterated further in
conversation.

**O2 — Placement.** Where this material sits once the remodelled AIDE framework is issued. The
rating scheme in particular is a candidate to become a standard rather than a working convention.

**O3 — Triage mapping.** The confidence-and-impact to action mapping is expected to need tuning in
use. Corrections to be captured as they arise rather than pre-specified.

**O4 — Mechanical fourth layer.** What the non-reading verification layer actually is, per section
9. Not yet designed.

**O5 — Disambiguation device.** A short check line attached to points where misinterpretation is
likely — enough to confirm correct reading, not an explanation of the point. Agreed in principle;
form not settled.
