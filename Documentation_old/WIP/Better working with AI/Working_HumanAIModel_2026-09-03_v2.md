# Working Document — Human-AI Working Model

Version: v2
Date: 2026-09-03
Status: working draft. Not a registered corpus document. No version register, index entry, or
corpus formatting conventions applied — placement to be decided once the remodelled framework is
deployed.

Supersedes: `Working_HumanAIModel_2026-09-03.md` (v1). v1 retained for supersession visibility.

**Relationship to the interaction document.** `Working_InteractionModel_2026-09-03_v2` is a branch
off this topic, not a parallel to it. It covers how information moves between Dave and the lead AI —
layering, channels, paging, the rating scheme, the recommendation convention. That material is not
repeated here.

**Versioning convention (established 2026-09-03).** Every update produces a **new version**
carrying the best current thinking and the complete resource. The current version is always
self-sufficient — it is not read alongside its predecessors. Superseded versions are retained
unaltered as point-in-time evidence, never edited in place. The evolution of thinking, journey
learning, positions considered and positions rejected are carried **forward into the current
version** (section 12) rather than being left behind in superseded ones, because the reasoning
behind a rejected option is often more valuable than the option itself.

**Change from v1.** v1 stated the goal, objective, two-part split, standing conditions, and an
agenda of open items. v2 adds the substance of the second design session: Dave's end-to-end
operating model (section 6), the mechanism of model correlation and the frame problem (section 7),
frame-passing as a structural integrity device (7.5), the unknown-unknown treatment (7.6),
criteria-building as a defined stage (7.7), and four pillars that reframe the whole model
(section 8) — realistic benchmark, learning-as-asset, adaptability-as-hedge, monitoring-as-sensor.
The agenda in section 10 is revised accordingly. Sections 12 and 13 (evolution of thinking, version
history) are new and are permanent fixtures from this version forward.

**Integrity note on v1.** During the second session, v1 was edited in place — a section added and
headings renumbered — without a version bump. This was caught by Dave on comparing his downloaded
copy against the working copy, not by any automated or self-applied check. It is the third recorded
instance of the same failure mode and the third caught only by human eye. v1 has since been restored
to its original state; the added material is carried in this version at 7.1, 7.2 and section 11.
Recorded here rather than quietly corrected, per the principle that a defect not recorded is a lost
asset (8.4).

---

## 1. The goal

Dave spends the majority of his time in business, concept and design mode — making impactful
decisions, learning, gaining insight, and applying it. AI takes the tasks and responsibilities it is
suited to, has a high probability of doing well, and can be given the checks, oversight and support
to do reliably.

For code specifically: AI does most or all of the build. Dave is involved in design and approach,
where he adds value.

The constraint on this is not AI capability. It is **assurance** — Dave can only hand work over to
the extent he has a high likelihood of seeing anything that should require his attention. Trust
without that is exposure, not delegation.

Stated in Dave's terms: the aim is to use AI to orchestrate delivery, but *not hands-off*. There
must be mechanisms that create friction and noise when things go off track, so that divergence gets
the chance to be **visible and seen**.

## 2. The objective

To structure the working relationship so that Dave's time is concentrated on the decisions and
insights only he can supply, while work delegated to AI is chosen for suitability, executed to
defined intent and standards, and returned in a form that makes its correctness **checkable rather
than merely plausible** — with the undescribed parts of the intent surfaced rather than silently
filled.

Two framing choices are load-bearing.

**Checkable, not reviewed.** Review is one instrument, not the centre. It scales badly with volume,
and agreement between correlated models is weak evidence. Where *done* has a testable meaning,
correctness stops depending on anyone reading carefully.

**Elicitation is in scope, not upstream of it.** The concept in Dave's head may not have been
described, resolved, or worked through. Drawing out and pinning down intent is part of what is
delegated, not a precondition to it.

Proportionality to risk is deliberately excluded from the objective. It is a property of the
mechanisms, not of the goal.

## 3. The two parts

**Part one — the why, what, who.** Correctness has no internal test. The artefact can be coherent,
well-structured and reviewable by any number of models and still be wrong, because nothing inside it
says whether it matches the concept in Dave's head or the actual business need. The only ground
truth is Dave. AI's role is elicitation and challenge.

**Part two — the how, when, where.** Correctness is checkable in principle. Given a settled why and
what, the how can be validated against it. This is where AI owns execution and verification beats
review.

**The boundary is a gate.** Part two should not start on an input part one has not declared settled.
Discovering the why was wrong is a signal to go back, not to patch forward. Most observed
dysfunction lives at this seam.

## 4. Conditions the model has to survive

Standing conditions, not problems to be solved once.

- **Scope evolves.** A percentage of the why, what and who will always be unknown, fluid or
  evolving. The goal is not fuller scope up front; it is making evolution *visible when it happens*.
  A detection problem, not a completeness problem.
- **Fire and forget is the primary risk.** By the time the result arrives, the shift is baked in.
- **Dave's judgement is partly non-verbal.** Feel and pattern recognition as much as conscious
  reasoning, running on specifics — the odd detail that does not sit right. Compression strips
  exactly these, because they look like noise.
- **Reasoning that exists only in a session is lost.** Anything decided in conversation and not
  recorded concurrently is gone when the session closes. (See 8.2 — this is why learning must be
  capitalised, not merely experienced.)
- **Silent gap-filling looks like success.** Competent execution against an incomplete brief
  produces a plausible artefact and no signal. The most common route to dysfunction.
- **Dave's attention is the scarce resource.** Any mechanism that improves integrity by spending
  more of his focus, energy or concentration is solving one problem by creating another. Mechanisms
  must add integrity **structurally**, at the AI layer, not through human labour.

---

## 5. What is settled — assurance fundamentals

### 5.1 Review and verification are different instruments

Review is a second opinion on an artefact. Verification is checking a claim against the world.

Historical integrity incidents — a version registered that was never authored, a stated completion
that was a self-assessment rather than confirmed receipt — were all of the second kind. No amount of
reviewing the document catches them, because the artefacts read fine. That class needs a probe, not
an opinion.

### 5.2 Fall-through layers and their real independence

**Principle.** Where failure can occur, a minimum of three fall-through layers; two for simple,
low-impact work.

**Caveat.** Layers multiply the odds only when their failure modes are uncorrelated. Lead AI and
second AI are reasonably independent on facts and internal consistency, and correlated on taste,
approach, and whether the thing is the right thing. Dave is a strong but *sampling* detector — he
catches what surfaces, and what surfaces is partly determined by the lead AI.

Honest count for the current model: roughly two-and-a-bit, not three.

**The fix is not more AI opinions.** It is a layer whose failure mode is genuinely different — a
mechanical check that involves nobody reading carefully. Not that it catches more, but that it
catches *differently*.

### 5.3 How the second AI is used

- **Framing determines yield.** "Review this" recruits agreement. "Find the case where this breaks"
  recruits information.
- **Divergence beats agreement.** Two independent attempts generated before either sees the other
  are more informative in where they differ than where they match. Divergence localises the
  underspecified part.
- **Proactive use is higher value than review use.** Second AI as coworker, advisor and sounding
  board is rated above its use as a checker. Currently under-exploited.
- **Review needs its own feedback loop.** Cycles that never change anything are ritual, and ritual
  is where trust quietly detaches from evidence.

### 5.4 Surfacing obligations on the lead AI

1. **Per-item confidence**, not per-response.
2. **Assumptions and gap-fills as a standing report.** Present even when empty — an empty report is
   itself a claim.
3. **Drift detection** against the settled baseline, reported when it fires.
4. **An anomalies channel** — things noticed but unrankable, raised without needing to be
   defensible. Feeds Dave's pattern-sense; would not survive an impact filter.
5. **Definition of done**, established before the work, in checkable terms (see 7.7 — drafted by AI,
   decided by Dave).
6. **Checkpoint density** set at commission time, proportional to risk.

**Caveat.** Items 1, 2 and 4 depend on the lead AI introspecting accurately on its own uncertainty,
which is imperfect. Items 3 and 5 do not carry that dependency, which is why they are weighted
heavily despite being less interesting.

### 5.5 Mechanism and criteria are separated

Separate stable **mechanism** from tunable **criteria and boundaries** — not as separate documents,
but as isolated, addressable definitions within the one standard. Criteria are subjective and will
evolve with use; editing a boundary should be a cheap change. The criteria block is a scoped,
overridable layer: company policy sets floors and ceilings; workgroup, machine or individual user
adjust within them.

---

## 6. The operating model (spine)

Dave's end-to-end flow, as articulated in session. This is the structure everything else attaches
to.

### 6.1 Top-weighted investment

Dave invests heavily at tiers one and two — the most defining tiers of structure:

- Intent, goal, outcome, and the *why*
- Approach, pattern, technical model, high-level breakdown
- Component assignment, roles, methodologies, underpinning resources
- **Key transformative roles** — what makes this successful versus unsuccessful
- Points of difference, added value, where insight and innovation are applied
- Key risk points and how they will be dealt with
- Extensibility and forward investment
- Style and way of working — intangible, but representable through intrinsic, traceable elements:
  the choices made and the weighted balance of decisions

### 6.2 Why the investment is top-weighted

Below tier two, Dave adds progressively less than his signature, and the work becomes repetition.
Worse, the **volume of level-two-and-below detail actively erodes** the judgement that makes him
valuable at the top. So descending is not merely low-value, it is corrosive — it drowns the faculty
required for the high-level work.

At the top, by contrast, the information volume is manageable and the decisions are maximally
defining. This is also where Dave is willing and engaged, which matters: any model that depends on
him doing something he finds arduous will fail in practice.

**This is a well-established pattern, not an idiosyncrasy.** It recurs as the delegation principle
in management (work *on* the system, not *in* it), as Deming's build-quality-into-the-process rather
than inspect-at-the-end, and as management-by-exception and abstraction in software. The one
genuinely new element is that AI collapses the *authoring cost* of the criteria — which is the part
that historically made this break down.

### 6.3 Cascade, then sample

Criteria and standards set at the top cascade downward. Dave does not descend to *author* lower
layers; he **samples** them to confirm the cascade held, and dives in only where risk and weight
justify it.

Because everything below is nonetheless *defined*, the lower layers are not a moving target or a
floating feather. Dave can dive into any part at any time and find something real. He simply chooses
which parts justify his attention.

### 6.4 Collaboration gradient

This is joint work throughout, not handover. Dave steers more at the top; the AI steers
progressively more further down. The transition is a gradient, not a cliff.

### 6.5 Dependent review at each translation

At each translation — high design to detailed design, detailed design to functional model, plan to
implementation — a second model reviews against the same information.

- **Concurrence** indicates a reasonably valid (or at least not invalid) option.
- **Divergence** gives points of comparison, and localises what deserves closer examination.

Dave's threshold argument: two concurring models on an implementation approach is a well
risk-weighted option, and likely exceeds what a senior-to-high-level developer produces on an
average day. The relevant question is not "is this optimal" but "what threshold is being exceeded,
given the alternatives actually available."

### 6.6 Bookend overview lenses

An overview lens at the start and an overview lens at the conclusion. This lets Dave spot divergence
and patterns without being overwhelmed by volume — the compression is at the ends, where he engages,
not through the middle, where he does not.

### 6.7 Intent review, distinct from conformance

Beyond "did it pass the tests," a separate check: *given the stated intent and purpose, did this
deliver in the best way?* Something can tick every box technically and still miss on style,
methodology, or scope of intent. This review is permitted to challenge on that basis, and can be
dismissed quickly when it does not add value — but it frequently raises the most valuable insights.

**Dependency (flagged).** The intent review is only as good as the intent it checks against. Thin
articulation at tier one leaves it nothing real to pull on, and it degrades into vibes. Its quality
is entirely downstream of section 6.1.

### 6.8 Design bias

Strong weight toward **smart design over brute-force code**. Good balance of delivered
functionality, high extensibility and reuse, delivering the outcome simply and effectively by being
smart in design.

Note the connection to 8.3: smart design *is* the adaptability hedge. A smart design bends when an
unknown surfaces; a brute-force one shatters.

### 6.9 Comparison to established practice

Where relevant, compare the design against existing conventions and established methodologies — is
what we are doing better or worse than a norm deemed to work? This is a cheap sanity check against
inventing something worse than the standard answer.

---

## 7. Where integrity is built structurally

The mechanisms that add assurance without spending Dave's attention.

### 7.1 The stance on single-sourcing

Dave will not commit to a single, opaque source for consequential work. This is sound risk
management, and it is *more* justified with AI than with most tools for a specific reason: when the
lead AI is wrong, it is wrong **confidently and plausibly** — the output reads exactly as well as a
correct one. Self-assessment cannot be trusted from the inside. A second source is the cheapest
thing that breaks this, because it fails in different places.

**Consequence.** The second source is not invoked when Dave feels worried — he cannot tell from the
inside which cases needed it. It is a standing part of how consequential work is done, applied
proportionally.

**Empirical note.** Every occasion Dave has brought in an external AI has yielded benefit, including
cases the lead AI predicted would not. The lead AI's estimate of when a second model helps is
therefore biased toward "won't help" — under-recommending the thing that most protects Dave. See
watch-points.

### 7.2 Proportional application

Scales on **likelihood** of a vulnerability and **severity** if it lands. High on both: heavy
prevention and cross-checking. Low on both: let it run. A genuine cost-benefit call — human time,
machine time, token cost all real.

**Calibration is a feedback loop, not a fixed table.** The starting model can be set from reasoning.
What makes it improve rather than merely age is capturing where a cross-check actually caught
something and where it never did.

**Order of build (settled).** Do not systematise the metric first. Work Package outcomes already
record reviews. Read across them *ad hoc* to see what review actually catches; formalise a measure
only if it earns it. Formalising now means guessing the field set before seeing the data.

**Two behaviours adopted:**

- **Standing habit.** Periodically read across recorded review results for what review actually
  caught. Treat as the empirical basis for tuning the risk model.
- **Standard review behaviour.** Wherever a review is done, record some assessable trace of its own
  result — enough that the review can later be evaluated *as a review*, not just its findings
  applied. Candidate measures if formalised: findings by severity; **whether any changed the
  outcome** (the key field — a review that changes nothing is either ritual or genuine confirmation,
  and the pattern over time distinguishes them); agreement versus divergence.

### 7.3 Why models are correlated — the shared-well mechanism

**Not collusion.** Vendors do not coordinate, share weights, or compare notes. Anthropic and OpenAI
are rivals.

**The actual mechanism.** Models are trained on overlapping slices of the same world — the public
internet, books, code, papers. There is only one internet. Two models independently learn "how
software is usually built" from largely the same source material. Nobody coordinated it; they drank
from the same well because it is the only well.

**The consequence.** If the source material carries a bias — a popular pattern that is a bad idea, a
widely-repeated claim that is wrong, a blind spot the field shares — both models absorb it
separately and both reproduce it confidently. Two students taught from the same flawed textbook make
the same mistake without ever meeting.

**Correction to an overstatement.** Models are *more* different than "they fail together" implies.
Reasoning paths, what gets surfaced, what gets worried about, which edge cases are reached for —
these genuinely differ, which is why two models together produce a wider edge-case set than either
alone. The correlation is narrow and specific: **shared blind spots**, not shared thinking.

**Practical split:**

- For **generating, exploring, cross-checking** — genuinely additive. The two-model approach is
  well-founded and the value is real, not marginal.
- For **confirmation** — partially correlated. Two correlated witnesses agreeing is weaker evidence
  than two independent ones, even when both are usually right.

**Breaking the correlation** requires varying the *input*, not just the model: Dave's own domain
knowledge and context (the thing no model was trained on, and the single most effective break);
adversarial framing; genuinely different data or emphasis between the two models; and reality
contact for the highest stakes.

### 7.4 The frame problem — where divergence and overconfidence actually live

**Dave's observation, and the sharpest thing surfaced in the session.**

The lead AI operates in two modes. First, gathering the information it judges necessary and relevant.
Second, reasoning within it. Once gathering closes, **the gathered context becomes the world**.

Two consequences:

**Compounding, path-dependent divergence.** Each decision about what to pull in shapes what gets
looked for next. Over three or four layers of context-building, two models can end up reasoning
soundly over *materially different worlds*. The logic is fine in both; the inputs diverged silently.
So the divergence is at the context step, not the reasoning step.

**Absolute trust in the frame.** Once the viewport is set, it is treated as complete. There is no
residual weighted element of doubt — no background "am I even looking at the right thing" — which is
a characteristically human process that keeps flickering after a decision is made. The boundary of
the viewport becomes invisible to the thing operating inside it.

**Why this matters.** The risk is not only "they agree because they are similar." It is also "they
may disagree for a reason neither can see, because each trusts its own viewport absolutely."

**Rejected mitigation.** Making Dave the inspector of the frame. It relocates the bottleneck onto
the scarcest resource and violates section 4's constraint — solving one problem by creating another.

### 7.5 Frame-passing between models

**The mechanism.** Stop passing only *conclusions* between models. Pass the **frame**.

A conventional handover is: here is the problem, here is my answer, here is my justification. The
enriched handover adds:

- What was pulled **into scope**
- What was **weighted heavily**
- What was **deliberately excluded**
- What **thinking model, pattern or methodology** was applied

**Why it is better than conclusion-review.** Two models comparing answers can only say "agree" or
"I'd do it differently." Two models comparing frames can say "you did not consider X and it is
material," or "you weighted this heavily and I did not — that is the real fork between us." It turns
a yes/no into a **diagnosis**, and it attacks divergence at the layer where it actually lives. The
second model gets to challenge the *boundary* — the one thing the first model was structurally blind
to.

**Why it is viable.** It runs machine-to-machine, at the AI layer, on automated handovers, with no
human attention consumed. The payload is a paragraph, not a document, so token cost is low.

**Limit 1 — the introspection ceiling.** A model reporting its own frame can only report the
boundary it is *aware* of. What it never thought to consider will not appear in the frame report
either. Powerful against *visible* frame differences; weak against *mutual* blindness.

**Limit 2 — anchoring, and the sequencing rule.** Passing A's frame to B anchors B toward A's world
— the exact correlation being fought. Sharing the frame buys richer critique at the cost of
independence.

**Resolution: sequence it.** B forms its own frame first, blind. Then the two frames are compared.
This buys independence *and* diagnosis, at the cost of B doing the work before it sees A's. **This
ordering is part of the policy, not an afterthought** — anchoring by default would quietly convert
an independent second source into an echo, and it would still feel like confirmation.

**Triage.** Not every frame element is worth passing. Highest-return candidates, to be tested rather
than assumed: **what was weighted heavily** and **what was deliberately excluded** — because that is
where invisible divergence concentrates. Start there, measure whether critique quality improved,
expand only if it earns it.

### 7.6 Unknown unknowns — the honest treatment

Nobody has solved "know what you don't know." It is not all-or-nothing, but it does not fully close.

**On adding more models — diminishing returns.** Two models: one may catch what the other missed.
Three: better again, but the gain per model *shrinks*, and shrinks faster the more correlated they
are. A third model drinking from the same well mostly overlaps the first two — full price for a
sliver of coverage.

**Therefore: differentiate rather than multiply.** A third *source of difference* — a human expert,
a real-world test, a genuinely contrarian frame — is worth more than a second identical model was.

**Structural techniques that partially work:**

- **Coverage checklists (highest return).** Rather than hoping a gap is noticed, walk a checklist of
  *categories*: failure modes, second-order effects, the stakeholder not in the room, the case where
  the assumption inverts. It does not say what was missed, but it drags a searchlight across
  territory that would otherwise never be pointed at. Converts "did anyone happen to think of it"
  into "did we deliberately look there." Policy cost, not labour cost.
- **Inversion / pre-mortem.** Not "is this right" but "assume this failed badly — what caused it."
  Recruits a different search and reliably surfaces what a forward review misses. Cheapest technique
  with the best ratio.
- **Assigned outside view.** One model whose *only* job is "what is being taken for granted, what is
  outside the frame." Adversarial, pointed at the boundary rather than the conclusion. Subject to
  the same ceiling, but pointing a model at the frame catches more than pointing it at the answer.

**The honest floor.** All of these operate inside the space of things that *can be thought of*. The
true unknown-unknown — outside everyone's frame, named by no checklist category — is caught by
reality, not cleverness. A test that fails. A user who does the unimagined thing. Time.

This is why **reality contact is not optional at the top of the risk scale**: it is the only thing
that catches what no amount of reasoning could, because it is not drawn from anyone's frame.

**And why section 8.3 matters more than closing the gap:** since the gap never closes, the
higher-value investment is reducing the *cost of discovering* an unknown, rather than trying to
eliminate unknowns.

### 7.7 Criteria-building as a defined stage

**The problem with definition-of-done in theory versus practice.** Empirical checks are the gold
standard, and in practice they fail — not because they are wrong but because authoring them is
arduous, boring, and lands entirely on Dave at the worst moment. Often defining all the checks is a
bigger task than doing the work. So it gets skipped, exactly as developers skip tests when things
get busy. Any policy depending on Dave cheerfully doing the horrible thing every time will fail.

**The resolution — Dave stops authoring, starts reacting.** AI drafts the definition of done, the
test criteria, the checks. Dave edits, approves, rejects, adds. This flips the economics: AI can
produce a check set that exceeds what a reasonable developer does on a good day, in seconds, at no
effort to Dave. Reacting to a proposed set is a fraction of the cost of authoring from blank page.

**This is the genuinely new element.** In every historical version of this pattern (6.2), the person
at the top still had to author the criteria by hand, which is why it always broke down. AI
collapsing the authoring cost is what might make it stick.

**Cross-check the criteria, not just the work.** A second model pulls at the proposed criteria —
what did this miss, where is the gap — *before* any work is done against them. The arduous thing
becomes cheap and gets better scrutiny than hand-authoring would give it.

**Cascade so it is not per-task.** Most criteria are inherited from standards by class of work. The
per-task effort is only the **delta** — what is special about this one. Defining thinking once at a
global or hierarchical level, cascading down, rather than chiselling validation requirements at
every point.

**Two forms of criteria — this is what makes it work beyond code:**

- **Checkable tests**, where the matter is objective. Pass/fail.
- **Guiding questions**, where the matter is subjective — "does this handle the case where scope
  changed mid-way," "is this the simplest thing that meets the need." These capture judgement
  without pretending it is arithmetic.

The second form is what lets criteria-building extend to design review, delivery of outcomes, and
other subjective work. **Criteria are not optional for subjective work — they are more necessary
there.** Comparing three parallel model outputs against no criteria is measuring string against
wind.

**Split honestly.** At commission, divide "done" into the checkable and the genuine judgement call.
State the checkable as criteria up front. Name the judgement part explicitly as "this one Dave
decides when he sees it" — so it is flagged as needing his eye rather than quietly assumed. That
naming matters as much as the tests: it says where the real risk sits.

### 7.8 Commissioning — the handoff

The handoff carries at minimum:

1. **Definition of done** (drafted by AI, decided by Dave, per 7.7)
2. **Checkpoint density** — how often progress surfaces, proportional to risk
3. **The rule for hitting the unknown** — stop and ask, or make the call and flag it. The single
   biggest source of quiet dysfunction is a gap filled plausibly, never seen, surfacing three steps
   later.

---

## 8. Four pillars

Reframings that change the shape of the whole model rather than refining a part of it.

### 8.1 A realistic benchmark, with a stated "enough"

Absolute integrity is a rabbit hole with no bottom. The target is a **defined benchmark with a
stated stopping point**, not perfection.

**The calibration.** Even a base-level implementation of this model plausibly lands at the level a
strong design or development team operated at pre-AI. Most teams will not invest in process at all —
they chase prompt tricks, attempting to out-think the system rather than making it **structurally
better**, which is not realistic. The relevant comparison is not perfection; it is the credible
alternative.

**Why the stopping point is itself part of integrity.** A model with no defined "enough" quietly
consumes all the time it was meant to save.

**Open question (agenda item).** What *is* the benchmark for AI-assisted development today, and what
constitutes enough beyond it?

### 8.2 Learning as asset, not ambience

**The centre of gravity of the whole model.** The difference between a team that has run ten years
and is still winging it, and one where every scar became a standard.

Insight from a session evaporates when the session closes. Turning learning into **structure** — a
policy, a methodology, a standard, a checklist category — means the lesson is applied automatically
forever after, without anyone remembering it.

**Why this is the highest-value pillar:** every other benefit in this document is linear.
Capitalised learning **compounds**, because each lesson permanently raises the floor.

This is why the instinct toward standards and cascade is not a stylistic preference — it is the
capitalisation mechanism. Learning applied in structural context, not ambient context.

### 8.3 Adaptability as the hedge against the unknown

**The reframe that actually beats "you don't know what you don't know."** You cannot eliminate the
unknown. You can make the **cost of discovering it trivial**.

Extensibility, encapsulation, easy model-swapping, flexible structures — these are not neatness.
They convert "we were wrong" from a catastrophe into an afternoon.

**The measure that matters is time-to-adapt**, not count-of-unknowns. And it is testable in
retrospect: when something changed, how much had to change with it?

Connects directly to 6.8 — smart design over brute force *is* this principle. Smart design bends;
brute-force design shatters.

### 8.4 Monitoring as the sensor

The intake pipe on which the learning-as-asset engine depends. Without it, the compounding machine
starves because it never sees what to learn from.

**Detection.** An unforeseen event that is not detected is a **lost asset**. The failure already
happened; the only question is whether the lesson was harvested or the cost paid for nothing.

**Recording.** Individual occurrences must be captured to establish that they happened at all.

**Aggregation — the real prize.** There is a large difference between a one-off and what is visible
in aggregate. A one-off is noise. The same anomaly seen fifty times is a **pattern**, and a pattern
is a standard waiting to be written. Trend and pattern analysis turns accumulated observations into
something that should be considered, learned from, and applied — which feeds 8.2.

**Status.** Identified as important and under-developed. Agenda item.

---

## 9. The model whole (overview lens)

- **Spine:** invest at the top, cascade down, sample rather than descend.
- **Integrity structurally, not by labour:** frame-passing with blind-first sequencing,
  differentiated multiplicity, coverage checklists and pre-mortems, reality contact at the top of
  the risk scale, criteria drafted by AI and decided by Dave.
- **Target:** a defined benchmark with a stated *enough*, measured against the credible alternative
  rather than perfection.
- **Learning capitalised into structure**, so it compounds instead of evaporating.
- **Adaptability designed in**, so the cost of being wrong is small.
- **Monitoring as the sensor** that feeds the whole thing — catching the unforeseen, aggregating
  one-offs into patterns worth standardising.

---

## 10. Items to work through

Revised from v1. Ordered by dependency, then value.

### A. The mechanical verification layer
**Question.** What is the fourth, genuinely independent layer — probes, tests, structural
validation, claims checked against actual state?
**Why.** The only layer whose failure mode does not correlate with the others, and the only thing
that catches the true unknown-unknown (7.6). Every historical integrity incident falls here.
**Blocked on.** Nothing. Highest-value open item.

### B. Frame-passing design
**Question.** What exactly travels with a decision? Field set, the blind-first sequencing rule,
where it applies, token cost versus critique-quality gain.
**Why.** Attacks divergence and frame-blindness at the layer they live, machine-to-machine, at no
cost to Dave's attention. Newly surfaced and high leverage.
**Blocked on.** Nothing. Start with weighted-heavily and deliberately-excluded, measure, expand.

### C. Criteria-building as a defined stage
**Question.** How are criteria drafted, cross-checked, cascaded from standards, and split between
checkable tests and guiding questions? What is the per-task delta?
**Why.** The mechanism that makes definition-of-done survive real life, and the one that extends
assurance to subjective work. Broadest applicability of anything here.
**Blocked on.** Nothing, though the cascade hook depends on the standards framework currently being
redeployed.

### D. Monitoring and aggregation
**Question.** What is detected, how is it recorded, how are one-offs aggregated into patterns, and
what triggers promotion of a pattern into a standard?
**Why.** The sensor for 8.2. Without it, learning cannot be capitalised because it is never seen.
Identified as under-developed.
**Blocked on.** Nothing.

### E. Learning-to-asset pipeline
**Question.** How does an insight become a standard, checklist category, or policy — reliably,
cheaply, without becoming a chore that gets skipped?
**Why.** The compounding mechanism; the highest-value pillar.
**Blocked on.** Benefits from D.

### F. Commissioning / handoff brief
**Question.** Definition of done, checkpoint density, engagement level, scope, rule on hitting the
unknown.
**Why.** Where Dave's time converts most efficiently into assurance; the natural home for the
part-one/part-two gate.
**Blocked on.** Wants C first.

### G. The realistic benchmark
**Question.** What is the current benchmark for AI-assisted development, and what is *enough*?
**Why.** Without a stated stopping point the model consumes the time it was meant to save.
**Blocked on.** Nothing, but partly an external-research question.

### H. Elicitation method for part one
**Question.** How does AI actively draw out intent not yet described or resolved? What does
challenge look like, and how is "the input is thin" reported without being obstructive?
**Why.** Named in the objective as in-scope, currently undesigned. Also determines the quality
ceiling of the intent review (6.7).
**Blocked on.** Nothing.

### I. Review triggers and proportionality
**Question.** At what points does work go to review, with what scope and depth — scaled by
consequence, risk of decision error, and likelihood of decision error.
**Why.** Currently judgement-based. Under-triggering leaves gaps; over-triggering produces ritual,
which is worse than nothing because it manufactures unearned confidence.
**Blocked on.** Benefits from B.

### J. Second AI as coworker
**Question.** Proactive use — parallel independent attempts, adversarial framing, sounding board —
rather than only checking after the fact.
**Why.** Rated higher value than the review use and under-exploited.
**Blocked on.** Nothing.

### K. Drift detection in practice
**Question.** What is checked against, how often, what triggers a report, how is a settled baseline
represented?
**Why.** Replaces fire-and-forget without replacing it with constant check-ins.
**Blocked on.** Partly F.

### L. Trust calibration
**Question.** How does trust in a delegation move over time? What evidence increases it, what
withdraws it, how is it recorded rather than felt?
**Why.** The model bets that oversight can reduce as reliability is demonstrated. Without explicit
calibration, trust drifts on impression.
**Blocked on.** A and I.

### M. Code specifically
**Question.** What does "AI does most or all of the build" require beyond general delegation?
**Why.** The stated end state, and where verification is most achievable.
**Blocked on.** A and F.

### N. Durability of reasoning
**Question.** How does session reasoning — especially voice — reliably land in a durable record
without becoming a skipped chore?
**Why.** Standing condition. Voice makes it acute. Feeds E.
**Blocked on.** Nothing.

### O. Failure taxonomy
**Question.** What actually goes wrong, in categories, with observed instances? Which layer should
have caught each?
**Why.** Every mechanism above is a bet about which failures matter. A taxonomy from real incidents
tests those bets against evidence and would likely reorder this list.
**Blocked on.** Nothing, but most useful after operating under the other mechanisms for a period.

---

## 11. Standing watch-points

- **Introspective honesty.** Confidence reporting, gap-fill reporting, the anomalies channel, and
  frame reporting all depend on the lead AI accurately reading its own state. It cannot fully do
  this. Absence of low-confidence signals over a long run is suspicious, not reassuring.
- **Self-serving boundary calls.** Where a rating boundary turns on "does this need Dave?", the lead
  AI has a quiet incentive to answer no.
- **Correlated agreement.** Two models agreeing feels like strong evidence and often is not,
  particularly on judgement and on whether the thing being built is the right thing.
- **Consensus that arrives too easily.** Dave has never observed a stalemate between two models —
  once reasoning is shared they converge. Some of that is truth winning; some is models being
  *agreeable* and yielding to a confidently-argued position. The unobservable part is whether the
  model that yielded was right to yield. Worth occasionally having a disagreement **adjudicated**
  (by Dave or a third source) rather than resolved between the two. A smooth path to consensus every
  single time is exactly what it would look like if convergence were partly artificial.
- **Anchoring via frame-passing.** See 7.5. Sharing a frame before the second model has formed its
  own converts an independent source into an echo, and it still feels like confirmation.
- **Ritual.** Any check that never changes an outcome is manufacturing confidence rather than
  testing anything.
- **Routing around a rule is data.** Where a design rule is routinely bypassed, that is evidence the
  rule needs revisiting, not a discipline failure.
- **The lead AI under-recommends the second source.** Empirically, external cross-checks have paid
  off even when the lead predicted they would not. The lead's own judgement of "this will not need a
  second look" is not a trustworthy trigger. Favour second-source-by-default on consequential work
  over lead-AI discretion.
- **Mechanisms that spend Dave's attention.** Any proposed improvement should be tested against
  section 4's last condition: does this add integrity structurally, or does it relocate the
  bottleneck onto the scarcest resource?

---

## 12. Evolution of thinking — positions considered, revised and rejected

Retained deliberately. A rejected option with its reasoning is a guard against re-adopting it later
on the same flawed grounds, and against re-litigating settled ground from scratch. Carried forward
into every subsequent version.

### 12.1 Review as the centre of assurance — displaced

**Original position.** Assurance comes from review: more eyes, more rounds, more models.

**Why it moved.** Review scales badly with volume, and agreement between correlated models is weak
evidence. More decisively, every historical integrity incident was invisible to review because the
artefact read fine.

**Current position.** Correctness should be **checkable** wherever possible; review is one
instrument among several, best spent on judgement and approach rather than conformance. Verification
against the world is a different instrument and the one the model was missing (5.1).

### 12.2 Three fall-through layers as adequate — revised

**Original position.** Dave, lead AI, second AI gives three independent layers.

**Why it moved.** Layers multiply odds only when failure modes are uncorrelated. Lead and second AI
correlate on taste and approach; Dave is a *sampling* detector dependent on what the lead surfaces.

**Current position.** Honestly two-and-a-bit. The remedy is a layer that fails *differently* — a
mechanical check — not more AI opinions (5.2, agenda A).

### 12.3 "The models are so similar you will get the same outcome" — overstated, corrected

**Position as stated by the lead AI, and wrong as stated.** Framed model correlation broadly enough
to imply Opus and GPT would produce substantially the same result.

**Why it moved.** Dave challenged it directly. On examination the correlation is narrow: reasoning
paths, what is surfaced, what is worried about and which edge cases are reached for genuinely
differ — which is why two models together produce a wider edge-case set than either alone.

**Current position.** Additive for generation and exploration; **partially correlated for
confirmation**, and specifically correlated on *shared blind spots* inherited from common training
material (7.3). The practical consequence is unchanged — vary the input, not just the model — but
the two-model approach is better founded than the overstatement implied.

**Learning.** The lead AI's caveats can be miscalibrated in the direction of overstating risk, which
is as misleading as understating it. Challenge on a caveat is as warranted as challenge on a claim.

### 12.4 Vendor collusion as an explanation for correlation — considered and rejected

**Hypothesis raised.** Whether correlation implied collaboration or collusion between vendors.

**Rejected.** No coordination, shared weights or comparison of notes; the vendors are rivals. The
mechanism is mundane: overlapping training corpora drawn from the same public material. Two students
taught from the same flawed textbook make the same mistake without meeting.

**Why worth retaining.** The distinction changes the mitigation. Collusion would be unfixable from
the outside; shared source material is addressed by varying the *input*.

### 12.5 Dave as the inspector of the frame — considered and rejected

**Proposal.** Surface each decision's viewport — what was pulled in, what was excluded — for Dave to
inspect before trusting the reasoning.

**Rejected by Dave.** It relocates the bottleneck onto the scarcest resource. Returning every
decision with its full scope for human evaluation consumes the brainpower needed for the next
decision. Solving one problem by creating another.

**What replaced it.** Frame-passing **between models**, machine-to-machine, at no cost to human
attention (7.5). The insight was retained; the delivery mechanism was inverted.

**Generalised as a test.** Any proposed improvement is now checked against: does this add integrity
structurally, or does it spend Dave's attention? (Section 4, final condition; section 11.)

### 12.6 Definition of done authored by Dave — rejected in that form

**Proposal.** Dave writes the definition of done, before work, in checkable terms.

**Rejected by Dave on practicality, not principle.** Authoring checks is arduous and boring; it
frequently exceeds the work itself; it therefore gets skipped, exactly as developers skip tests when
busy. Any policy depending on him cheerfully doing the horrible thing every time will fail.

**What replaced it.** AI drafts, Dave reacts. Second model cross-checks the criteria before work
begins. Standards cascade so per-task effort is only the delta (7.7).

**Why this is the pivotal reformulation.** The pattern (top-weighted definition, cascade, sample) is
centuries old across management, manufacturing and software, and it has always broken down at the
same point: the person at the top had to author the criteria by hand. AI collapsing the authoring
cost is the genuinely new element and the reason this attempt may hold.

### 12.7 Criteria as pass/fail tests only — widened

**Original framing.** Definition of done as empirical, testable criteria.

**Why it moved.** That framing confines the mechanism to objective work, when the highest-value
reviews are subjective — design, approach, delivery of outcomes. Dave's point: comparing three
parallel model outputs against no criteria is measuring string against wind.

**Current position.** Two forms — **checkable tests** where objective, **guiding questions** where
subjective. The second captures judgement without pretending it is arithmetic, and is what extends
the mechanism beyond code (7.7).

### 12.8 More models as the answer to unknown unknowns — partially rejected

**Proposal considered.** If two models raise the odds of catching what one missed, three raises them
further, and so on — a statistical approach to coverage.

**Partially rejected.** The gain per model diminishes, and diminishes faster the more correlated the
models are. A third drawn from the same well mostly overlaps the first two: full cost, sliver of new
coverage.

**Current position.** **Differentiate rather than multiply.** A third *source of difference* — human
expert, real-world test, genuinely contrarian frame — is worth more than a second identical model
was. Structural techniques (coverage checklists, pre-mortem, assigned outside view) buy more per
unit cost than additional models, and reality contact is the only floor under the genuinely
unforeseeable (7.6).

### 12.9 Frame-passing by default — refined, not adopted as first stated

**Initial form.** Pass the frame along with the conclusion on every handover.

**Problem identified.** Passing A's frame anchors B toward A's world — reintroducing the correlation
the second source exists to break, while still feeling like independent confirmation.

**Current position.** **Blind first, then compare.** B forms its own frame before seeing A's. This
buys independence *and* diagnosis, at the cost of B doing the work first. The sequencing is part of
the policy, not an implementation detail (7.5).

### 12.10 Systematising review metrics now — deferred, not rejected

**Proposal.** Define a fixed measure set on every review — findings by severity, whether the outcome
changed, agreement versus divergence — so review yield can be aggregated and calibrated.

**Deferred by Dave.** The data is already being recorded. Formalising the metric now means guessing
the field set before seeing the data.

**Current position.** Read across existing outcomes *ad hoc*; let the useful signal show itself;
formalise only if it earns it. In the meantime, adopt the lighter behaviour: any review, anywhere,
leaves an assessable trace (7.2). Same empirical discipline as the failure taxonomy — build from
real incidents, not from reasoning.

### 12.11 "No stalemate has ever occurred" as reassurance — reframed

**Offered as.** Evidence that two-model consensus reliably converges on the truth.

**Reframed as a watch-point.** Models are agreeable and yield to confidently-argued positions. Some
convergence is truth winning; some is a correct instinct being talked out of. Which one occurred is
not observable from the transcript. Frictionless consensus every time is also exactly what partly
artificial convergence would look like.

**Current position.** Retained as a watch-point (section 11), with the mitigation of occasionally
having a disagreement **adjudicated** rather than resolved between the two models.

**Note.** This reframe was the lead AI's judgement call, not Dave's position, and is flagged as such.

### 12.12 Recommendations built on stale corpus state — withdrawn

**What happened.** The lead AI carried forward a picture of outstanding work items from a superseded
framework and made a prioritisation recommendation on that basis. Dave identified the picture as
obsolete; the recommendation was withdrawn.

**Learning.** Retained context is not automatically current context. Where a recommendation rests on
remembered state rather than stated state, that dependency should be surfaced with the
recommendation so it can be checked cheaply.

### 12.13 Journey learning — observations about the working relationship itself

- **The most valuable insight of the second session came from Dave, not the lead AI.** The frame
  problem — that divergence originates in context-building rather than reasoning, and that the
  viewport is trusted absolutely once closed — was Dave's observation. The lead AI had located the
  risk one layer away, in shared training. This is direct evidence for the elicitation-and-challenge
  model of part one: the human is the source of the frame the AI cannot see.
- **The lead AI systematically under-recommends the second source.** Every external cross-check Dave
  has run has paid off, including those predicted not to. Its discretion is therefore not a
  trustworthy trigger (section 11).
- **In-place editing recurred despite being a known failure mode.** Knowing about a failure mode did
  not prevent it. Only a structural change — versioning convention, restated at the head of every
  document — has a chance of preventing recurrence, which is the learning-as-asset principle (8.2)
  applied to this document itself.

---

## 13. Version history

| Version | Date | Change |
|---|---|---|
| v1 | 2026-09-03 | Initial. Goal, objective, two-part split, standing conditions, settled assurance fundamentals, ten-item agenda, watch-points. |
| — | 2026-09-03 | *(Defect)* v1 edited in place: cross-checking section added, headings renumbered, no version bump. Caught by Dave on comparison. v1 subsequently restored to original state; material carried into v2. |
| v2 | 2026-09-03 | Operating model added as spine (6). Structural integrity mechanisms consolidated (7), including shared-well correlation mechanism, the frame problem, frame-passing with blind-first sequencing, unknown-unknown treatment, criteria-building as a defined stage. Four pillars added (8). Agenda rebuilt and reordered, ten items to fifteen. Evolution of thinking (12) and version history (13) established as permanent sections. Versioning convention stated at head. |
