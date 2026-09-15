> identity: Assurance_Decisions@v2 | doctype: decisions | updated: 2026-09-15

# Assurance — Decisions

## Summary

Reasoning and resolutions from the Assurance design pass. Twelve decisions covering the confirmed sketch decisions, autonomy tier naming, confidence vocabulary, the low-friction governing constraint, learning loop deferral, the active identification obligation, and remediations from cross-review.

---

## D1. Five sketch decisions upheld

The Assurance sketch carried five design decisions flagged for review at the full design pass. All five were reviewed and upheld without revision.

**Named tiers for autonomy levels.** Small number, chosen by either side, AI judges default, human overrides. The shape is right — named tiers give a shared vocabulary without per-action negotiation. The alternative — per-action negotiation without tiers — was rejected as high-friction and inconsistent. Upheld.

**Anomalies channel is a behaviour with capture-and-place as destination.** The alternative — a separate anomalies log, queue, or channel — would duplicate what capture-and-place already does and create a parallel routing mechanism. Anomalies are things that don't fit; the AI notices them and places them. Upheld.

**Confidence vocabulary uses the existing conversational vocabulary.** The alternative — a new confidence scale (high/medium/low, numeric percentages) — was rejected because the conversational vocabulary is already established practice. See D3 for the separation from the standards strength model. Upheld.

**Learnings queue is distinct from the task queue.** Different lifecycle, different purpose. Tasks are work to be done; learnings are observations whose value is in aggregate. Mixing pollutes both — tasks get buried in noise, learnings get triaged individually and discarded. The alternative — a single unified queue — was rejected on this basis. Upheld.

**Two escalation triggers.** Single high-impact instance for immediate attention, accumulated pattern for periodic review. The pair covers both ends — big lessons and small-but-recurring ones. Without the first, significant lessons wait for periodic review. Without the second, small lessons are lost because no single instance crosses the threshold. The alternative — a single threshold — was rejected because it necessarily misses one end. Upheld.

## D2. Three autonomy tiers named

Three tiers: directed, collaborative, autonomous.

**Directed** — the AI proposes and waits. Every material action requires explicit agreement. For high-stakes, unfamiliar, or close-control situations.

**Collaborative** — the AI acts within the agreed model and surfaces decisions at natural points. The default for most design and structured work.

**Autonomous** — the AI executes against a clear specification and reports on completion. For well-understood work with a precise specification. Requires the human to have indicated trust — the AI may recommend Autonomous, but does not grant it to itself.

Three was chosen over two (too coarse — no middle ground between full control and full delegation) and four-plus (diminishing returns — the distinctions become hard to remember and hard to call). Three is the smallest number that covers the range.

The names were chosen for plain meaning. "Directed" says the human is directing. "Collaborative" says both sides are working. "Autonomous" says the AI is executing. No jargon, no numbered levels.

Operational scope rules — what granularity a tier applies at (turn, task, session), how inherited tiers expire, interaction with other approval requirements — are standard-level detail, not design-level decisions. They are deferred to standard authoring.

## D3. Confidence signalling separated from the standards strength model

Cross-review finding F1 identified that the v1 design incorrectly claimed confidence signalling adapted the standards strength model (required/recommended/optional/information). That model expresses compliance weight for standards items — a different dimension from epistemic certainty.

The conversational confidence vocabulary — strong, moderate, moderate-to-strong — is established practice throughout the rebuild but is not part of the standards strength model. The v1 claim that they are "the same underlying concept" was wrong on the evidence. They share a purpose (expressing degree) but have different origins, different domains, and different semantics.

The remediated design states confidence signalling as its own convention using the established conversational vocabulary. No new system is introduced; no false equivalence with the compliance model is claimed.

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

The learning and feedback loop — measurable moments, quick comparison, learnings queue, two escalation triggers — is designed in the Assurance design document. Implementation depends on Orchestration's MCP for queue-writing and is deferred until Orchestration is built and tested.

The Improvement component, which owns the periodic pattern analysis of the learnings queue, will also depend on Orchestration's scheduling and MCP features. Both Improvement and the learning loop's recording mechanism are deferred together.

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

The remediated design resolves it: high-impact learnings are surfaced to the human through capture-and-place. The human decides whether the learning becomes a task. For accumulated patterns, Improvement's periodic reviewer makes the decision. In both cases, someone other than Assurance makes the action decision.

The alternative — giving Assurance the authority to write directly to the task queue — was rejected because it breaks the observer-actor separation. The observer modifying the work queue based on its own assessment, without an independent decision, undermines the separation that makes both roles trustworthy.

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

---

Version note: v2 — cross-review remediation. Fourteen findings addressed. D3 rewritten (confidence signalling separated from strength model, F1). D4 rewritten (proportionate overhead replaces zero-friction test, F6). D5 updated (high-impact escalation through human, F3). D7 rewritten (Assurance does not make action decisions, F3). D11 updated (consumption reference replaces reproduced rule, F11). D12 added (conformance checking, F2). D1 expanded with alternatives considered (F14). D2 expanded with scope deferral and Autonomous human-indication requirement (F4). D6 expanded with anomalies-vs-recommendation distinction (F12). All decisions reviewed for alternatives considered (F14). 2026-09-15. Replaces v1.
