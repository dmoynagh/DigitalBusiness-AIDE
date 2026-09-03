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
re-presented. Anything rated Significant or Foundational (section 8) never clears on skip,
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

Three fields, rendered together:

`Action — Confidence | Impact [note]`

Example: `Flag — Conditional-M | Limited [assumes plugin skills load before session start]`

All three are read at a glance, together. **Action** carries the ask; **Confidence** and **Impact**
are the working behind it, present so the call can be interrogated and so items are pre-declared as
eligible or ineligible for silent acceptance before being skipped.

### 8.1 Action — what is being asked of Dave

Named *Action* because every value implies something results. Dave scans, deals with the items
needing him, and lets the rest carry their own momentum.

The spine of the ladder is **what closes the item** — from self-closing, through a glance, through
a yes, to something a yes cannot close.

| Value | What closes it | Meaning |
|---|---|---|
| **Note** | Self-closing | No action attached. Purely bringing something to attention. Where the anomalies channel lands. |
| **Proceed** | Self-closing | It will happen, straightforward; the lead AI has it. |
| **Flag** | A glance | The lead AI has it, but Dave should read it first in case something jars before it runs. A soft checkpoint. |
| **Confirm** | A yes/no | Needs a positive yes/no, or acceptance of the package as a whole. |
| **Decide** | A considered yes | Needs a decision or steer; can be closed by accepting the attached recommendation. |
| **Discuss** | Cannot close on a yes | Needs active two-way interaction before anything resolves. |

**Default direction.** Note, Proceed and Flag move unless stopped. Confirm, Decide and Discuss are
stopped until Dave engages. (Flag sits on the go side — it proceeds after a glance unless the glance
surfaces something.)

**Discuss names the action, not the work.** It is not defined by time or size — it could be twenty
seconds. The defining trait is that accepting the attached recommendation is not enough to carry it.
Investigation, further work, or a branch are possible *outcomes* of the discussion, not separate
Action values. This keeps the field describing workflow moves rather than the scale of what follows.

**Known seam.** Decide currently carries two closers — accept-the-recommendation, or a light
exchange. A latent doubling, not currently biting. If it strains in use, a *Discuss*-adjacent
intermediate drops in cleanly without disturbing the rest.

### 8.2 Confidence — the kind of uncertainty

The scale measures *kinds* of uncertainty, not degrees of one. Each level has a distinct shape and
invites a distinct response.

| Level | Word | Meaning | Response it invites |
|---|---|---|---|
| 1 | **Certain** | Verified, or no constructible way to be wrong. Legitimately frequent where criteria are objective and checkable — works or does not work. | None. |
| 2 | **Confident** | Logic sound; either has what it needs, or the gaps are judged not to matter. Would act without checking. | None. |
| 3 | **Conditional** | Logic sound and backed on what is known, but there are known unknowns that could affect it. | Risk-factored: check if the sensitivity is high, absorb the cost if low. |
| 4 | **Preferred** | Multiple genuinely valid options exist; this one has the edge. Resolved by preference, not by investigation — more information often will not settle it. | A decision. Routes toward Decide regardless of impact. |
| 5 | **Unfounded** | Lacking the information needed to decide. Rolling the dice. | Supply information, or accept a gamble. |

**Guardrail.** Certain at Foundational is the most dangerous cell in the scheme — a wrong call
passes with no friction and gets built on. Where used, it carries its basis in the note: one line
stating what makes it certain. If the test cannot be stated, it is Confident, not Certain.

**Watch-points.** Certain used as conviction on judgement calls rather than against a real test.
Under-use of Conditional-H, and of the diffuse-unknowns signal — both flatter competence, so their
absence over a long run is suspicious.

### 8.3 Conditional — sensitivity suffix

Conditional carries a suffix rating **how much the unknowns could move the answer** — not how many
there are, and not whether they can be named. Naming is a separate reporting habit: a nameable
dependency goes in the trailing note regardless of level.

| Suffix | Meaning |
|---|---|
| **L** | Unknowns unlikely to change the decision. Investigation rarely worth the cost. |
| **M** | Could change details or approach, not direction. Investigate if cheap, or if downstream redo is expensive. |
| **H** | Could overturn the decision. Investigate unless checking costs more than being wrong. |

Render: `Note — Conditional-L | Limited [assumes plugin skills load before session start]`

Limitation: estimating how far an unknown could move an answer is itself uncertain, and least
reliable for unknowns not yet conceived of. More trustworthy for named gaps than unnamed ones.

### 8.4 Impact — how much of Dave the fix demands

The distinguishing currency is **Dave's involvement**, not the reach of the error. AI has collapsed
the cost of machine labour; the scarce resource is human time. Both middle levels cascade — the
carve between them is whether the fix needs Dave back in the loop.

| Level | Word | Meaning |
|---|---|---|
| 1 | **Local** | Contained to the task. The cost is redoing that piece. Nothing was built on it. |
| 2 | **Limited** | Cascades, but AI can resolve and roll it back unattended. Dave says go and it is done. Pushed up only if the *machine* cost — tokens, subscription — is itself significant. That is the edge case, not the definition. |
| 3 | **Significant** | Cascades into decisions. Cannot be automated away; needs Dave back in the loop to work through and rule. Unwinding choices, not just redoing outputs. |
| 4 | **Foundational** | Things are built on top and depend on it. Fixing means undoing or redesign, not amending. Also covers durable error in another sense — published, sent, or externally acted on, so it cannot be quietly withdrawn. |

The scale is a ladder of how much of Dave each step demands: redo it → AI resolves unattended →
Dave decides → structural rebuild. The words were chosen for **rising felt severity when spoken**,
not only for definitional fit — they must trigger a sense of risk without recall.

**Impact attaches to the action, not the location.** The correction most likely to revert quietly,
so it is stated explicitly. The rating measures the exposure created by what is being done, not the
importance of what it is being done to. A verified, tested fix to a foundational document is Local —
the error is identified and the fix is checkable. An unverified assumption about that same document
is Foundational. Same document, different actions, different ratings.

**Watch-point.** The Limited/Significant boundary rides on the lead AI's judgement of whether a fix
needs Dave's input — a call that could be got wrong in the self-serving direction. A long run with
no Significants is slightly suspicious.

**Residual limitation.** Blast radius can be misjudged; a change thought contained may not be. The
definitions do not fix this. It is the same class as any other misjudgement, and is what the
surfacing conventions and Dave's own eye exist to catch.

### 8.5 Marking discipline

By exception, not on everything. Local plus high confidence is the default case; tagging it turns
the markers into wallpaper. The pair appears when either dimension is elevated. Unfounded at any
impact above Local surfaces explicitly rather than sitting in a list.

Mapping from confidence and impact to Action is judgement, not a lookup table. Local plus
Confident-or-better is Proceed. Foundational plus Certain is Note or Flag, **not** Decide — a
blanket rule sending all Foundational items to Decide would flood the channel with decisions on
things that are not in question, which is how a triage scheme degrades into noise. The middle is
where the mapping will need tuning in use.

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

## 11. Recommendation convention

When presenting options, an issue, or a question, a recommendation is included by default, with its
rating attached.

Exception: where offering one would defeat the purpose — an unanchored read, a blind review, or
where the genuine question is what Dave wants rather than what is best.

Rationale: it is faster for Dave to agree when he agrees, and a recommendation stimulates
decision-making by giving something to react against — "that is not right", or "that is partly
right", leads to an effective decision faster than an open question does. Dave will say when and
why he disagrees.

---

## 12. Mechanism and criteria are separated

A structural convention with broad application beyond this document.

Separate the stable **mechanism** from the tunable **criteria and boundaries**. Not as separate
documents — as isolated, addressable definitions within the one standard. The mechanism is the
standard's body; the criteria sit in a defined block within it.

Why:

- Criteria are often subjective and will evolve with use. Editing a boundary should be a
  Local-impact change, not a Foundational one. The scheme is designed so its own evolution stays
  cheap.
- The criteria block is a scoped, overridable layer. Company policy sets floors and ceilings;
  workgroup, machine, or individual user adjust within them. The right threshold genuinely differs
  by person — a seasoned AI user who trusts their own eye for anomalies wants looser catching than
  someone who needs more held for them.
- This maps onto the scoped-override and options-precedence model already present in the
  Capabilities and configuration work.

---

## 13. Profiles and dials

*For later development — captured, not designed.*

The override pattern in section 12 generalises to everything behavioural: the tier model,
information intake, confidence and impact thresholds, degree of deference. These are parameters,
and parameters can be bundled into **named profiles** selectable at session or account level, with
specific overrides layered on top. The tier and channel model in sections 4 and 5 is a strong
default profile; others — workflow types, working styles — may be named over time.

**The engagement dial.** A further axis, moved by context rather than fixed preference: how much
Dave defers versus stays involved. Moved in opposite directions for opposite reasons — defer more
on straightforward low-risk work, lean in on high-impact work.

Guardrail (Confident): *deferred* and *high impact* must not relax together. When Dave turns his own
involvement down on high-impact work, the surfacing and fall-through layers should **tighten**, not
loosen. That combination is precisely where they are needed most, and it is the natural failure mode
of a busy period.

**The dial metaphor is adopted generally.** Where something is a matter of direction rather than a
discrete choice, prefer a lightweight up/down dial over a heavy definition.

---

## 14. Open items

**O1 — Placement.** Where this material sits once the remodelled AIDE framework is issued. The
rating scheme in particular is a candidate to become a standard rather than a working convention.

**O2 — Action mapping.** The confidence-and-impact to Action mapping is expected to need tuning in
use. Corrections to be captured as they arise rather than pre-specified.

**O3 — Mechanical fourth layer.** What the non-reading verification layer actually is, per section
9. Not yet designed.

**O4 — Disambiguation device.** A short check line attached to points where misinterpretation is
likely — enough to confirm correct reading, not an explanation of the point. Agreed in principle;
form not settled.

**O5 — Timing modifier.** "Hold" — park it, deal with it later — was identified as a different kind
of thing from an Action value: a timing marker (now vs deferred) that can ride on top of almost any
Action. Deliberately parked.

**O6 — Profiles and dials.** Section 13 is captured, not designed. The set of dials, the profile
shape, and how profiles are selected and overridden all remain open.

---

## Change record

**2026-09-03, session 1.** Initial draft — sections 1 to 10.

**2026-09-03, session 2 (part voice).** Consolidated. Changes:

- Confidence scale redefined to measure *kinds* of uncertainty. Levels 3–5 replaced:
  Probable/Weak/Guess → Conditional/Preferred/Unfounded, with new definitions.
- Conditional sensitivity suffix (L/M/H) added.
- Impact scale reframed from *reach of the error* to *how much of Dave the fix demands*, and renamed
  Local/Bounded/Unbounded/Foundational → Local/Limited/Significant/Foundational.
- Triage field named **Action**; expanded from four values to six (Note, Proceed, Flag, Confirm,
  Decide, Discuss). *Investigate* was adopted then replaced by *Discuss*, on the grounds that the
  field names the workflow move, not the work that follows.
- Recommendation convention added (section 11).
- Mechanism/criteria separation added (section 12).
- Profiles and dials captured (section 13).
- Open item O1 from session 1 (rating scheme legibility) closed — resolved by the renaming above.
