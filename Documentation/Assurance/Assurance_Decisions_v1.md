> identity: Assurance_Decisions@v1 | doctype: decisions | updated: 2026-09-15

# Assurance — Decisions

## Summary

Reasoning and resolutions from the Assurance design pass. Eleven decisions covering the confirmed sketch decisions, autonomy tier naming, confidence vocabulary, the low-friction governing constraint, learning loop deferral, and the active identification obligation.

---

## D1. Five sketch decisions upheld

The Assurance sketch carried five design decisions flagged for review at the full design pass. All five were reviewed and upheld without revision.

**Named tiers for autonomy levels.** Small number, chosen by either side, AI judges default, human overrides. The shape is right — named tiers give a shared vocabulary without per-action negotiation. Upheld.

**Anomalies channel is a behaviour with capture-and-place as destination.** The alternative — a separate log or queue — would duplicate what capture-and-place already does. Anomalies are things that don't fit; the AI notices them and places them. Upheld.

**Confidence vocabulary uses the existing strength model.** Inventing a parallel system would create two ways of expressing degree-of-certainty. Using what exists keeps cognitive load down. Upheld.

**Learnings queue is distinct from the task queue.** Different lifecycle, different purpose. Tasks are work to be done; learnings are observations whose value is in aggregate. Mixing pollutes both. Upheld.

**Two escalation triggers.** Single high-impact instance for immediate action, accumulated pattern for periodic review. The pair covers both ends — big lessons and small-but-recurring ones. Upheld.

## D2. Three autonomy tiers named

Three tiers: directed, collaborative, autonomous.

**Directed** — the AI proposes and waits. Every material action requires explicit agreement. For high-stakes, unfamiliar, or close-control situations.

**Collaborative** — the AI acts within the agreed model and surfaces decisions at natural points. The default for most design and structured work.

**Autonomous** — the AI executes against a clear specification and reports on completion. For well-understood work with a precise specification.

Three was chosen over two (too coarse — no middle ground between full control and full delegation) and four-plus (diminishing returns — the distinctions become hard to remember and hard to call). Three is the smallest number that covers the range.

The names were chosen for plain meaning. "Directed" says the human is directing. "Collaborative" says both sides are working. "Autonomous" says the AI is executing. No jargon, no numbered levels.

## D3. Strength model adapted for conversational confidence

The framework's strength vocabulary — strong, moderate, moderate-to-strong — is used for conversational confidence signalling. This is an adaptation, not a new system.

The adaptation is in usage, not in the vocabulary itself. In standards, strength governs compliance weight. In conversation, the same words express the AI's degree of certainty about a judgement or recommendation. The AI says "strong" when it means "I'm confident this is right" and "moderate" when it means "this is my best reading but there's genuine room for doubt."

The alternative — a separate confidence scale (high/medium/low, or numeric percentages) — was rejected because it would introduce a parallel vocabulary for the same underlying concept.

## D4. Low friction is a governing constraint

Assurance conventions must have minimal disruptive intrusion on the flow of work. Most assurance behaviour should be near-invisible in a normal session — the AI following its obligations without announcing that it is doing so.

This governs how the standard is authored. Specifically:

- Autonomy tiering is stated only when not obvious from context. Most of the time the tier is apparent and nothing needs saying.
- Assumptions and gap-fill disclosure is proportionate to the significance of the gap. Small, obvious inferences are not flagged. Material assumptions always are.
- Verification is the AI's background responsibility. It checks what it can check and identifies uncertainty — it does not narrate the checking process.
- Drift detection surfaces departures, but only when there is a genuine departure to surface.
- The anomalies channel uses capture-and-place, which already runs silently.

The test for the standard: would following this slow down a normal working session? If yes, cut until it doesn't.

This directly serves the facilitate-not-police objective (O5) and the charter's facilitate-and-empower objective (O5 of the charter).

## D5. Learning loop designed, implementation deferred

The learning and feedback loop — measurable moments, quick comparison, learnings queue, two escalation triggers — is designed in the Assurance design document. Implementation depends on Orchestration's MCP for queue-writing and is deferred until Orchestration is built and tested.

The Improvement component, which owns the periodic pattern analysis of the learnings queue, will also depend on Orchestration's scheduling and MCP features. Both Improvement and the learning loop's recording mechanism are deferred together.

The single high-impact escalation trigger can operate without Improvement — it escalates directly to the task queue. The accumulated-pattern trigger sleeps until Improvement arrives.

The design stands independently of implementation timing. The conventions are stated; the mechanism follows when the infrastructure exists.

## D6. Active identification is a cross-cutting obligation

The AI's obligation to identify and recommend opportunities for stronger assurance is cross-cutting — it operates alongside all three areas of concern, not as a fourth area.

The AI might notice opportunities while applying proactive conventions, while running detective checks, or while capturing learnings. The response is a recommendation surfaced through the anomalies channel, using capture-and-place. No separate mechanism is needed.

This serves the charter's extensibility-from-learning objective (O4). Assurance evolves because the AI notices where it could be better, not only because failures are analysed after the fact.

## D7. Assurance does not change its own conventions

Assurance captures learnings and identifies opportunities. It does not act on them — it does not modify its own conventions, create new ones, or retire old ones.

That responsibility belongs to Improvement, which analyses patterns and decides what to act on. The separation is deliberate: the observer should not be modifying itself based on its own observations without an independent analysis step.

Assurance recommendations (from active identification) and learnings (from the capture loop) both flow outward — to the human via the anomalies channel, or to the Improvement component via the learnings queue. The decision about whether to change a convention is never Assurance's.

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

The overview-first discipline is owned by Working Practices as a generic statement. Assurance recognises it as the highest-value proactive convention — the single most important thing Assurance can do is ensure the overview and approach are right — but does not redefine or restate it.

This follows the established pattern: WP owns the behaviour, consumers reference it. No duplication of mechanism.

---

Version note: v1 — initial decisions from the Assurance design pass. 2026-09-15.
