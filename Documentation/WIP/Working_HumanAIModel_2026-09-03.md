# Working Document — Human-AI Working Model

Status: working draft. Not a registered corpus document. No version register, index entry, or
corpus formatting conventions applied — placement to be decided once the remodelled AIDE framework
is deployed.

Date: 2026-09-03
Source: design conversation, Workflow project.

**Relationship to the interaction document.** `Working_InteractionModel_2026-09-03_v2` is a branch
off this topic, not a parallel to it. It covers how information moves between Dave and the lead AI —
layering, channels, paging, the rating scheme, the recommendation convention. That material is not
repeated here. This document covers the working model itself: what is delegated, on what basis,
with what assurance, and how trust in it is earned rather than assumed.

---

## 1. The goal

Dave spends the majority of his time in business, concept and design mode — making impactful
decisions, learning, gaining insight, and applying it. AI takes the tasks and responsibilities it
is suited to, has a high probability of doing well, and can be given the checks, oversight and
support to do reliably.

For code specifically: AI does most or all of the build. Dave is involved in design and approach,
where he adds value.

The constraint on this is not AI capability. It is **assurance** — Dave can only hand work over to
the extent he has a high likelihood of seeing anything that should require his attention. Trust
without that is exposure, not delegation.

## 2. The objective

To structure the working relationship so that Dave's time is concentrated on the decisions and
insights only he can supply, while work delegated to AI is chosen for suitability, executed to
defined intent and standards, and returned in a form that makes its correctness **checkable rather
than merely plausible** — with the undescribed parts of the intent surfaced rather than silently
filled.

Two framing choices in that statement are load-bearing.

**Checkable, not reviewed.** Review is one instrument, not the centre. Review scales badly with
volume: as AI does more of the build, reviewing becomes a load on Dave or on a second model whose
agreement is only weakly informative. Where *done* has a testable meaning, correctness stops
depending on anyone reading carefully, and review is spent where it is strong — judgement and
approach, not conformance.

**Elicitation is in scope, not upstream of it.** The concept in Dave's head may not have been
described, resolved, or worked through. Drawing out and pinning down intent is part of what is
delegated, not a precondition to it. If this is not named in the objective it will not be designed
for, and everything downstream will assume a well-formed input that often will not exist.

Proportionality to risk is deliberately excluded from the objective. It is a property of the
mechanisms, not of the goal.

---

## 3. The two parts

The work divides into two parts with different contexts, issues and challenges. They need different
conventions, not one convention applied twice.

**Part one — the why, what, who.** Building and defining clear outcomes.

Correctness here has no internal test. The artefact can be coherent, well-structured and reviewable
by any number of models and still be wrong, because nothing inside it says whether it matches the
concept in Dave's head or the actual business need. The only ground truth is Dave. AI's role is
almost entirely elicitation and challenge: drawing the thing out, finding where it is
underspecified, testing it against cases, reporting when the input is thin. The failure mode is
producing something plausible enough that the gap never surfaces.

**Part two — the how, when, where.** Designing, defining, planning, build, delivery, lifecycle.

Correctness here is checkable in principle. Given a settled why and what, the how can be validated
against it. This is where AI can own execution, where verification beats review, and where Dave's
involvement should concentrate at approach and acceptance rather than through the middle.

**The boundary is a gate.** Part two should not start on an input part one has not declared settled.
Part two discovering the why was wrong is a signal to go back, not to patch forward. Most observed
dysfunction lives at this seam.

---

## 4. Conditions the model has to survive

These are not problems to be solved once. They are standing conditions the mechanisms must work
under.

**Scope evolves.** A percentage of the why, what and who will always be unknown, fluid or evolving.
Projects change as learning grows. The goal is therefore not fuller scope up front; it is making
evolution **visible when it happens** — noticing that an assumption made several steps back is no
longer holding, while it is still cheap to act on. A detection problem, not a completeness problem.

**Fire and forget is the primary risk.** Hand off, see you when it is done. It structurally cannot
detect drift, because by the time the result arrives the shift is baked in.

**Dave's judgement is partly non-verbal.** Much of what he contributes is feel and pattern
recognition as much as conscious reasoning — less tangible, less definable, no less valuable. It
runs on specifics: the odd detail, the thing that does not sit right. Compression strips exactly
these, because they look like noise. So the model must preserve some texture, not only distil.

**Reasoning that exists only in a session is lost.** Anything decided in conversation and not
recorded concurrently is gone when the session closes.

**Silent gap-filling looks like success.** Competent execution against an incomplete brief produces
a plausible artefact and no signal. This is the single most common route to dysfunction.

**Corpus integrity has historically been caught only by a human eye.** Prior incidents — a version
registered that was never authored, a stated completion that was a self-assessment rather than
confirmed receipt — were not caught by review, because the artefacts read fine.

---

## 5. What is settled

### 5.1 Review and verification are different instruments

Review is a second opinion on an artefact. Verification is checking a claim against the world.

The incidents above were all of the second kind. No amount of reviewing the document catches them.
That class needs a probe, not an opinion. The current model has review and no verification.

### 5.2 Fall-through layers, and their real independence

**Principle.** Where failure can occur, a minimum of three fall-through layers. Two for simple,
low-impact work. Three significantly increases the odds of an issue being identified.

**Current model:** Dave, lead AI, second-platform AI.

**Caveat.** Layers multiply the odds only when their failure modes are uncorrelated.

- Lead AI and second AI share training distribution and inductive biases. On facts and internal
  consistency they are reasonably independent and the layering works. On taste, approach, and
  whether the thing is the right thing, they fail together — both over-trust plausible structure,
  both miss the unstated requirement, both elaborate into mechanism when the model should change.
- Dave is a strong detector but a **sampling** one. He catches what surfaces, and what surfaces is
  partly determined by the lead AI. So lead-AI failure and human failure are not fully independent
  either.

Honest count for the current model: roughly two-and-a-bit, not three.

**The fix is not more AI opinions.** It is a layer whose failure mode is genuinely different — a
mechanical check that involves nobody reading carefully. A test, a probe, a structural validation.
The argument is not that it catches more, but that it catches *differently*.

### 5.3 How the second AI is used

**Framing determines yield.** "Review this" recruits agreement. "Find the case where this breaks"
recruits information. Evaluative framing is the default and the weaker one.

**Divergence beats agreement.** Two independent attempts at the same problem, generated before
either sees the other, are more informative in where they differ than in where they match.
Divergence localises the underspecified part.

**Proactive use is higher value than review use.** The second AI as coworker, advisor and sounding
board — contributing a different thinking model — is rated above its use as a checker. This is the
under-exploited half of the current arrangement.

**Review needs its own feedback loop.** Track which review cycles changed anything. Cycles that
never change anything are ritual, and ritual is where trust quietly detaches from evidence.

### 5.4 Surfacing obligations on the lead AI

Six elements, established in the interaction document and restated here as obligations of the
working model rather than as formatting:

1. **Per-item confidence**, not per-response. Uneven confidence within one piece of work is the
   normal case; averaging destroys the information.
2. **Assumptions and gap-fills as a standing report.** Where the instruction ran out and a call was
   made. Present even when empty — an empty report is itself a claim.
3. **Drift detection against the settled baseline**, reported when it fires, not at delivery.
4. **An anomalies channel** — things noticed but unrankable, raised without needing to be
   defensible. Feeds Dave's pattern-sense; would not survive an impact filter.
5. **Definition of done, written before the work, by Dave**, in checkable terms.
6. **Checkpoint density set at commission time**, proportional to risk.

**Caveat.** Elements 1, 2 and 4 depend on the lead AI introspecting accurately on its own
uncertainty, which is imperfect. They shift the odds substantially; they do not close the gap.
Elements 3 and 5 do not carry that dependency, which is why they are weighted heavily despite being
less interesting.

### 5.5 Mechanism and criteria are separated

Separate the stable **mechanism** from the tunable **criteria and boundaries** — not as separate
documents, but as isolated, addressable definitions within the one standard.

Criteria are subjective and will evolve with use; editing a boundary should be a cheap change. The
criteria block is a scoped, overridable layer: company policy sets floors and ceilings; workgroup,
machine or individual user adjust within them. The right threshold genuinely differs by person.

---

## 6. Items to work through

Ordered by dependency, then by value. Each states the question, why it matters, and what it is
blocked on.

### A. The mechanical verification layer

**Question.** What is the fourth, genuinely independent layer? What can be checked without anyone
reading carefully — probes, tests, structural validation, assertion of claimed facts against actual
state?

**Why it matters.** It is the only proposed layer whose failure mode does not correlate with the
other three. Every historical integrity incident falls in its territory. Without it the assurance
count stays at two-and-a-bit regardless of how much review is added.

**Blocked on.** Nothing. Highest-value open item.

### B. Commissioning — the handoff brief

**Question.** What must be established before work is delegated? Definition of done in checkable
terms, checkpoint density, engagement level, what is in and out of scope, what to do on hitting an
unknown.

**Why it matters.** It is where Dave's time converts most efficiently into assurance, and it is the
precondition for verification substituting for review. Also the natural home for the part-one to
part-two gate.

**Blocked on.** Nothing, though it will want revision once (A) exists.

### C. Elicitation method for part one

**Question.** How does AI actively draw out intent that has not been described, resolved or worked
through? What does challenge look like, and how is "the input is thin" reported without being
obstructive?

**Why it matters.** Named in the objective as in-scope. Currently undesigned. The failure mode it
addresses — competent execution against an incomplete brief — is the most common route to
dysfunction.

**Blocked on.** Nothing.

### D. Drift detection in practice

**Question.** What does the lead AI actually check against, how often, and what triggers a report?
How is a settled baseline represented so drift is detectable?

**Why it matters.** It is the mechanism that replaces fire-and-forget without replacing it with
constant check-ins. Directly addresses the evolving-scope condition.

**Blocked on.** Partly (B) — there must be a declared baseline to detect drift against.

### E. Review triggers and proportionality

**Question.** At what points does work go to review, with what scope and depth? Scaled by
consequence, by the risk of decision error, and by the likelihood of decision error — three
different things.

**Why it matters.** Currently judgement-based and inconsistent. Under-triggering leaves gaps;
over-triggering produces ritual, which is worse than nothing because it manufactures unearned
confidence.

**Blocked on.** Benefits from (F) being defined first.

### F. Second AI as coworker

**Question.** How is the second AI used proactively — parallel independent attempts for divergence,
adversarial framing, sounding board, advisor — rather than only as a checker after the fact?

**Why it matters.** Rated higher value than the review use and currently under-exploited. Divergence
is the strongest available signal for locating underspecification.

**Blocked on.** Nothing.

### G. Trust calibration

**Question.** How does trust in a delegation move over time? What evidence increases it, what
withdraws it, and how is that recorded rather than felt?

**Why it matters.** The whole model is a bet that oversight can be reduced as reliability is
demonstrated. Without an explicit calibration mechanism, trust drifts on impression — which is how
ritual review persists and how genuine reliability goes unrewarded.

**Blocked on.** (A) and (E) — needs evidence to calibrate on.

### H. Code specifically

**Question.** What does "AI does most or all of the build" require that general delegation does not?
Acceptance criteria as the human-owned artefact, test-first framing, what Dave reviews and what he
never sees.

**Why it matters.** The stated end state, and the domain where verification is most achievable —
correctness is more nearly testable here than anywhere else.

**Blocked on.** (A) and (B).

### I. Durability of reasoning

**Question.** How does reasoning produced in session — especially voice — reliably land in a durable
record without becoming a chore that gets skipped?

**Why it matters.** A standing condition, not a solved one. Voice makes it more acute. Decisions
made and not recorded concurrently are lost.

**Blocked on.** Nothing.

### J. Failure taxonomy

**Question.** What actually goes wrong, in categories, with observed instances? Which layer should
have caught each?

**Why it matters.** Every mechanism above is a bet about which failures matter. A taxonomy built
from real incidents tests those bets against evidence rather than intuition, and would likely
reorder this list.

**Blocked on.** Nothing, but most useful after a period of operating under the other mechanisms.

---

## 7. Standing watch-points

Things that will not be fixed by design, and need ongoing attention.

- **Introspective honesty.** Confidence reporting, gap-fill reporting and the anomalies channel all
  depend on the lead AI accurately reading its own uncertainty. It cannot fully do this. Absence of
  low-confidence signals over a long run is suspicious, not reassuring.
- **Self-serving boundary calls.** Where a rating boundary turns on "does this need Dave?", the lead
  AI has a quiet incentive to answer no.
- **Correlated agreement.** Two models agreeing feels like strong evidence and often is not,
  particularly on judgement and on whether the thing being built is the right thing.
- **Ritual.** Any check that never changes an outcome is manufacturing confidence rather than
  testing anything.
- **Routing around a rule is data.** Where a design rule is routinely bypassed, that is evidence the
  rule needs revisiting, not a discipline failure.
