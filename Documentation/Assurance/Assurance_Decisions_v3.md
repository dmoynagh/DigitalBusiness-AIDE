> identity: Assurance_Decisions@v3 | doctype: decisions | updated: 2026-09-15

# Assurance — Decisions

## Summary

Reasoning and resolutions from the Assurance design pass. Fourteen decisions covering the confirmed sketch decisions, autonomy tier naming and semantics, confidence vocabulary, the low-friction governing constraint, learning loop deferral, the active identification obligation, and remediations from two rounds of cross-review.

---

## D1. Five sketch decisions upheld

The Assurance sketch carried five design decisions flagged for review at the full design pass. All five were reviewed and upheld without revision.

**Named tiers for autonomy levels.** Small number, chosen by either side within authorisation rules, AI judges default, human overrides. The shape is right — named tiers give a shared vocabulary without per-action negotiation. The alternative — per-action negotiation without tiers — was rejected as high-friction and inconsistent. Upheld.

**Anomalies channel is a behaviour routed through capture-and-place.** The alternative — a separate anomalies log, queue, or channel — would duplicate what capture-and-place already does and create a parallel routing mechanism. Anomalies are things that don't fit; the AI notices them and routes them through capture-and-place to their appropriate destination. Upheld.

**Confidence vocabulary uses the existing conversational vocabulary.** The alternative — a new confidence scale (high/medium/low, numeric percentages) — was rejected because the conversational vocabulary is already established practice. See D3 for the separation from the standards strength model and D13 for the formal definition. Upheld.

**Learnings queue is distinct from the task queue.** Different lifecycle, different purpose. Tasks are work to be done; learnings are observations whose value is in aggregate. Mixing pollutes both — tasks get buried in noise, learnings get triaged individually and discarded. The alternative — a single unified queue — was rejected on this basis. Upheld.

**Two escalation triggers.** Single high-impact instance for immediate human attention, accumulated pattern for Improvement's periodic review. The pair covers both ends — big lessons and small-but-recurring ones. Without the first, significant lessons wait for periodic review. Without the second, small lessons are lost because no single instance crosses the threshold. The alternative — a single threshold — was rejected because it necessarily misses one end. Upheld.

## D2. Three autonomy tiers named, with scope semantics

Three tiers: directed, collaborative, autonomous.

**Directed** — the AI proposes and waits. Every material action requires explicit agreement. For high-stakes, unfamiliar, or close-control situations.

**Collaborative** — the AI acts within the agreed model and surfaces decisions at natural points. The default for most design and structured work.

**Autonomous** — the AI executes against a clear specification and reports on completion. For well-understood work with a precise specification. Requires human authorisation — the AI may recommend Autonomous, but cannot select it unilaterally.

Three was chosen over two (too coarse — no middle ground between full control and full delegation) and four-plus (diminishing returns — the distinctions become hard to remember and hard to call). Three is the smallest number that covers the range.

The names were chosen for plain meaning. "Directed" says the human is directing. "Collaborative" says both sides are working. "Autonomous" says the AI is executing. No jargon, no numbered levels.

**Tier selection authority.** Cross-review round 2 (F16) identified a contradiction between "either side may choose the tier" and the restriction that the AI cannot grant itself Autonomous. The resolution: either side may select Directed or Collaborative; only the human can authorise Autonomous. This distinguishes selection (choosing a tier within available authority) from authorisation (granting the AI a level of trust it cannot claim for itself). The distinction matters because Autonomous is the tier where the AI acts without per-action agreement — that authority must come from the human.

**Scope and lifecycle semantics.** Cross-review round 2 (F4) identified that deferring all operational semantics to the standard left the design incomplete. The design-level constraints the standard works within:

- A tier applies to the current unit of work unless explicitly set for a broader scope
- A tier set for a specific task expires with that task; a broader setting persists until changed
- A tier does not override independent approval requirements — cross-review, acceptance tests, and other governing gates still apply regardless of tier
- A material action is one that would be difficult to reverse or that materially shapes the work's direction

The standard expresses these constraints operationally. Remaining operational detail — how tiers interact with specific workflow commands, how the AI announces tier state — is standard-level.

## D3. Confidence signalling separated from the standards strength model

Cross-review finding F1 identified that the v1 design incorrectly claimed confidence signalling adapted the standards strength model (required/recommended/optional/information). That model expresses compliance weight for standards items — a different dimension from epistemic certainty.

The conversational confidence vocabulary — strong, moderate, low — is established practice throughout the rebuild but is not part of the standards strength model. The v1 claim that they are "the same underlying concept" was wrong on the evidence. They share a purpose (expressing degree) but have different origins, different domains, and different semantics.

The remediated design states confidence signalling as its own convention using a defined conversational vocabulary owned by Assurance. No false equivalence with the compliance model is claimed.

The alternative — adopting the standards strength model for confidence — was rejected because compliance weight and epistemic certainty are different things. Saying "I'm recommended on this" would be incoherent. A separate numeric or named scale was also rejected because the conversational vocabulary already exists and works.

## D4. Low friction as proportionate overhead

Assurance conventions must have minimal disruptive intrusion on the flow of work. Most assurance behaviour should be near-invisible in a normal session — the AI following its obligations without announcing that it is doing so.

Cross-review finding F6 identified that the v1 formulation — "would following this slow down a normal working session? If yes, cut until it doesn't" — was too absolute. Some valuable assurance legitimately costs time. Verification, conformance checking, or surfacing a material uncertainty may slow work while producing more than enough trust to justify the cost.

The governing test is proportionality: does the overhead produce trust that justifies the cost? The alternative — zero measurable friction — was rejected because it would systematically remove precisely the controls Assurance exists to provide.

Specifically:

- Autonomy tiering is stated only when not obvious from context.
- Assumptions and gap-fill disclosure is proportionate to the significance of the gap. Small, obvious inferences are not flagged. Material assumptions always are.
- Confidence is signalled on material judgements where the human's decision depends on knowing the AI's degree of certainty — not on routine assertions.
- Verification is the AI's background responsibility. It checks what it can check and identifies uncertainty — it does not narrate the checking process.
- Drift detection surfaces departures, but only when there is a genuine departure to surface.
- Conformance checking uses whatever completion mechanism applies — it does not add a separate checking step.
- The anomalies channel uses capture-and-place, which already runs silently.

This directly serves the facilitate-not-police objective (O5) and the charter's facilitate-and-empower objective (O5 of the charter).

## D5. Learning loop designed, implementation deferred

The learning and feedback loop — measurable moments, quick comparison, learnings queue, two escalation triggers — is designed in the Assurance design document. Implementation depends on Orchestration to coordinate and invoke writes through Infrastructure's MCP server, and is deferred until Orchestration is built and tested.

The Improvement component, which owns the accumulated-pattern analysis of the learnings queue, will also depend on Orchestration's scheduling. Both Improvement and the learning loop's recording mechanism are deferred together.

The single high-impact escalation trigger can operate without Improvement or Orchestration — it surfaces to the human through capture-and-place, and the human decides whether it becomes a task. The accumulated-pattern trigger sleeps until Improvement arrives.

The design stands independently of implementation timing. The conventions are stated; the mechanism follows when the infrastructure exists.

## D6. Active identification is a cross-cutting obligation

The AI's obligation to identify and recommend opportunities for stronger assurance is cross-cutting — it operates alongside all three areas of concern, not as a fourth area.

The AI might notice opportunities while applying proactive conventions, while running detective checks, or while capturing learnings. The response is a recommendation surfaced through capture-and-place. The content is a recommendation, not an anomaly — capture-and-place is the routing mechanism, not the semantic category. No separate mechanism is needed.

The alternative — a fourth area of concern — was rejected because active identification has no conventions of its own that are distinct from the three areas. It is a standing obligation that applies while doing other work, not a separate kind of work.

This serves the charter's extensibility-from-learning objective (O4). Assurance evolves because the AI notices where it could be better, not only because failures are analysed after the fact.

## D7. Assurance does not make action decisions

Assurance identifies, captures, and surfaces. It does not decide what to act on.

Cross-review finding F3 identified that the v1 design contradicted itself: it said high-impact learnings "escalate directly to the task queue" while also saying Assurance only captures and Improvement owns escalation decisions. The contradiction was real.

The remediated design resolves it: high-impact learnings are surfaced to the human through capture-and-place. The human decides whether the learning becomes a task. For accumulated patterns, Improvement's periodic reviewer makes the analysis and escalation decisions. In both cases, someone other than Assurance makes the action decision.

The alternative — giving Assurance the authority to write directly to the task queue — was rejected because it breaks the observer-actor separation. The observer modifying the work queue based on its own assessment, without an independent decision, undermines the separation that makes both roles trustworthy.

Cross-review round 2 (F3 partial) further identified that the Improvement boundary wording was too broad, implying Improvement owned all escalation decisions including immediate human ones. The boundary has been narrowed: Improvement owns accumulated-pattern analysis, escalation decisions arising from that analysis, and subsequent action decisions. The human's immediate action decision on high-impact instances does not pass through Improvement.

## D8. Cross-cutting nature confirmed — component plus framework-wide requirement

Assurance is both a component in the Guidance role and a framework-wide requirement stated in Core. This was confirmed in the WP design pass (D1, D16) and is carried forward without revision.

The component owns the specific conventions described in this design. The framework-wide requirement is the lens: every component in the framework contributes to assurance. The brief-required gate, cross-review, operations test, acceptance test, strength model, capture-and-place, the design-check skill, and definition of done all contribute. They are not owned by Assurance — they are contributions to the assurance requirement from their owning components.

## D9. Sketch reference corrected — P7/P8/P9, not P7/P8/P10

The Assurance sketch's cross-cutting nature section referenced loud failure, verified truth, and "P10." There is no tenth premise. The detective conventions reference loud failure (P7), verified truth (P8), and confirmed state (P9). The cross-cutting reference is corrected to loud failure, verified truth, and confirmed state (P7/P8/P9).

## D10. Lifecycle weighting, not lifecycle restriction

Assurance runs across the full lifecycle. What shifts is the weighting, not the scope.

At the overview and approach level, proactive conventions carry the most weight — getting the model right matters more than catching errors in it. At build, detective conventions carry more weight — the specification exists and the question is whether build honours it. Learning opportunities arise wherever a measurable comparison exists, regardless of stage.

This was the scope correction confirmed in the scoping session and carried into the design as a model decision. The alternative — Assurance as primarily a build-side concern — was explicitly rejected because it would leave the highest-leverage work unprotected.

## D11. Overview-first discipline consumed, not redefined

The overview-first discipline is owned by Working Practices as a generic statement. Assurance recognises it as the highest-value proactive convention — the single most important thing Assurance can do is ensure the overview and approach are right — but does not redefine it.

Cross-review finding F11 identified that the v1 design reproduced the operational rule verbatim while D11 claimed it did not restate it. The remediated design replaces the reproduced rule with a consumption reference: it states that Assurance recognises the overview-first discipline and that the authoritative definition remains with WP. This follows the established pattern: WP owns the behaviour, consumers reference it.

## D12. Conformance checking added as a detective convention

Cross-review finding F2 identified that the detective model never explicitly required comparing delivered work against its governing specification. Verification checked facts; drift detection caught movement away from the model during work; but neither addressed whether the final result satisfied the original intent.

The remediated design adds conformance checking: the AI confirms delivered work satisfies its governing specification using whatever completion or acceptance mechanism applies — definition of done, acceptance test, work register reconciliation. Assurance states the expectation; it does not duplicate the mechanisms those components own.

The alternative — assuming verification and drift detection together cover conformance — was rejected because a result can verify cleanly, show no drift during production, and still fail to satisfy the specification. The intended-outcome-to-delivered-outcome comparison is a distinct detective concern.

## D13. Conversational confidence vocabulary defined and owned by Assurance

Cross-review round 2 (F15) identified that separating confidence signalling from the standards strength model (D3) left the conversational vocabulary without an authoritative definition or owner. "And so on" is not a defined vocabulary.

Assurance now owns and defines the conversational confidence vocabulary: three levels — strong, moderate, low — with natural intermediates permitted (moderate-to-strong). The semantics are plain English: strong means high certainty, moderate means reasonable confidence with genuine room for doubt, low means significant uncertainty.

This is deliberately small. A three-level vocabulary with permitted intermediates covers the range without false precision. The alternative — a larger or more graduated scale — was rejected because finer distinctions are unreliable (the AI cannot meaningfully distinguish seven levels of certainty) and would burden conversation. The alternative — leaving the vocabulary undocumented — was rejected because a convention that requires using a vocabulary must define it.

## D14. Queue-writing ownership: Infrastructure plumbing, Orchestration invocation

Cross-review round 2 (F17) identified inconsistent ownership formulations for the queue write path. The scope section assigned the MCP write mechanism to Infrastructure; the learning-loop section and boundaries assigned queue-writing transport to Orchestration.

The resolution: Infrastructure owns the MCP server, queue file format, and queue location — the plumbing. Orchestration coordinates and invokes writes requested by governing behaviours, and schedules periodic processing. The decision that a write should happen — what to capture and why — belongs to the governing behaviour (in this case, Assurance's learning capture conventions). This follows the established pattern across the framework: Infrastructure provides the mechanism, the governing behaviour decides, Orchestration coordinates the execution.

The alternative — single ownership by either component — was rejected because the three concerns are genuinely distinct. Infrastructure provides the plumbing; Orchestration coordinates execution; the governing behaviour owns the decision to write. Cross-review round 3 (F19) identified that the v3 wording "when and why a write happens" incorrectly gave Orchestration the semantic decision that belongs to Assurance. Corrected: Orchestration coordinates and invokes writes requested by governing behaviours, not decides them.

---

Version note: v3 — rounds 2 and 3 cross-review remediation. Seven findings addressed. D2 expanded with tier selection authority and scope/lifecycle semantics (F4, F16). D7 expanded with narrowed Improvement boundary (F3 partial). D13 added — confidence vocabulary defined and owned by Assurance (F15). D14 added and corrected — queue-writing ownership clarified, Orchestration coordinates writes requested by governing behaviours (F17, F19). D1 wording corrected — capture-and-place as routing mechanism (F18). 2026-09-15. Replaces v2.
