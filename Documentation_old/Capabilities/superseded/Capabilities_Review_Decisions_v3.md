# Capabilities Review — Decisions

> **Version 3** (2026-09-01). Adds the Review C correlation-integrity rule while preserving the established Review lifecycle and Messaging ownership boundary.

---

## D1 — Review is for independent insight, integrity, decisions, and risk

**Decision.** Review introduces a meaningfully separate reasoning path to improve substantive
integrity, support better decisions, and manage risk. Its objective is confidence proportionate to
the consequence and uncertainty of the work, not conformance checking or agreement for its own
sake.

**Reason.** A single AI can produce a coherent path that shares its own assumptions and blind
spots. A second AI can contribute different inputs, interpretations, alternatives, and challenge.
Review is valuable when it changes understanding or makes residual risk explicit.

---

## D2 — The Lead retains ownership

**Decision.** The Lead owns the work, its net coherence and simplicity, Finding disposition, and
the final decision. The Reviewer owns Findings and may offer remedies, but Findings are evidence,
not requirements.

**Reason.** Transferring design authority to the Reviewer turns review observations into
uncontrolled change and encourages solving every theoretical imperfection. The Lead is responsible
for whether accepting risk, removing a need, reshaping the design, or applying a change creates the
best net outcome.

---

## D3 — Review is a small lifecycle component

**Decision.** Review owns initiation, input resolution, request construction, exchange state,
Round correlation, continuation, disposition records, and the Review Result. It does not own the
work, environment configuration, communication transport, research, or platform-specific routing.

**Reason.** Review's intrinsic task is managing a review cycle. Keeping external mechanisms behind
contracts preserves one owner per mechanism and allows the same Review model to operate from Chat,
Work, Codex, and future surfaces.

---

## D4 — Trigger criteria remain with the source that owns the work or risk

**Decision.** User/Lead instruction, AI recommendation, Standards/workflows/project rules,
WorkPackage configuration, and consequence/risk conditions can trigger Review. Each Trigger is
Required, Recommended, or Optional. Review consumes the Trigger rather than owning every criterion.

**Reason.** The source that understands the work knows when Review adds value. Centralising all
criteria in Review would duplicate domain and workflow policy. The posture distinction prevents an
AI recommendation from silently becoming a mandate.

---

## D5 — AI recommendation is a first-class trigger source

**Decision.** An AI should recommend Review when consequence, reach, difficulty of reversal,
uncertainty, novelty, evidence weakness, or a valuable independent perspective makes the expected
benefit material.

**Reason.** Risk and Review value often become visible during work rather than at configuration
time. The AI is well placed to surface that moment, while the Lead/user still decides unless a
governing rule requires Review.

---

## D6 — One Review resolves a Review Input Contract

**Decision.** An instantiated Review resolves Trigger, Subject, Objective, Authorised Scope, Type,
Level, Mode, Reviewer, Review Material, Response Expectations, and Continuation/Stop posture.
Direct instruction, work configuration, Profiles, operating defaults, and environment data supply
values in explicit precedence order.

**Reason.** A contract makes the mechanism complete without forcing every caller to supply every
field. It also supports one-off Reviews by allowing the equivalent profile content to be supplied
directly rather than requiring a new named Type.

---

## D7 — Type, Level, Mode, and Reviewer are separate dimensions

**Decision.** Type defines the question/lens; Level defines the justified assurance strength; Mode
defines exposure to the Lead's current reasoning/solution; Reviewer defines the independent source.

**Reason.** The previous model's gains came from keeping these controls separable. Mixing them
creates multiplying variants such as deep/robust types and makes model/provider choices part of
stable semantics. A critical Check and a quick Robust challenge must both remain possible.

---

## D8 — The initial Type set has five purpose-defined profiles

**Decision.** The reusable Types are Check, Inspect, Evaluate, Robust, and Stress Test. Their
boundaries are criterion, artefact, outcome, design/framing, and environment/adversary respectively.

**Reason.** The progression states how far outside the current work the Reviewer may step:

> Check the claim → Inspect the artefact → Evaluate the outcome → Challenge the design → Stress it
> against external or adversarial reality.

Each asks a materially different question. Depth remains a Level concern.

---

## D9 — Stress Test is exceptional and user-activated

**Decision.** Stress Test defaults to Extreme and begins only on explicit user direction. An AI
may recommend it, but a Standard, workflow, WorkPackage default, or risk trigger cannot silently
start it.

**Reason.** Stress Test is the occasional maximum-strength adversarial/competitive option. Its
cost, breadth, and external scrutiny posture make user activation an intentional boundary. The
later Extreme default reflects its purpose; the earlier High proposal is superseded.

---

## D10 — Profile defaults form a deliberate progression

**Decision.** Default Type mappings are:

```text
Check       → Low      + Full
Inspect     → Standard + Full
Evaluate    → Medium   + Full
Robust      → High     + Full
Stress Test → Extreme  + Full
```

Evaluate commonly uses Blind for an independent approach; Robust may use Blind for blank-sheet
framing. Defaults are starting points only.

**Reason.** Common invocation should be cheap, while the actual work's consequence and uncertainty
must be able to raise or lower intensity. Full is the safe general default because most Reviews
assess current work; Blind is deliberately chosen where anchoring would defeat the objective.

---

## D11 — Level is consequence/risk based and dynamic

**Decision.** Level runs Low, Standard, Medium, High, Extreme and is assessed through consequence,
reach, reversibility, and uncertainty. Use judgment rather than a score; do not average away one
serious factor. Reassess after material Findings and record escalation/de-escalation with a short
reason.

**Reason.** Work size is a poor proxy for assurance need. A small prescribed algorithm or contract
can have broad, hard-to-reverse consequences. New evidence can change the risk picture, so fixed
initiation-time Level would misallocate review effort.

---

## D12 — Level scales assurance dimensions, not just model cost

**Decision.** Higher Level progressively increases model/reviewer capability, depth/breadth,
evidence verification, independence, iteration persistence, re-review expectation, and completion
confidence. Actual model mappings remain environment data.

**Reason.** Model strength is only one way review intensity changes. Hard-coding current model
names into Review semantics would create churn and would not express the behavioural difference
between Levels.

---

## D13 — Full and Blind are the initial Modes

**Decision.** Full exposes the current approach and relevant reasoning. Blind withholds selected
Lead solution/reasoning content to reduce anchoring while still supplying everything needed to
answer the objective.

**Reason.** Independent Approach is useful but does not need another Type. `Evaluate + Blind` or
`Robust + Blind` expresses the intended question and information boundary without multiplying the
Type set.

---

## D14 — Lead/Reviewer assignment is contextual and models are recorded per Round

**Decision.** The AI/platform owning or initiating the current work is normally Lead; environment
configuration selects a separate Reviewer. The current intended mapping is Claude Lead to
GPT/Codex Reviewer and GPT/Codex Lead to Claude Reviewer. The roles can reverse across tasks. Each
Round records the actual Lead and Reviewer models because either can change between Rounds.

**Reason.** Reviewer is a role/source, not a model version. Round-level model history preserves
reproducibility and independence evidence without coupling the stable Review model to volatile
provider catalogues.

---

## D15 — Requests are purpose-shaped, attackable, and non-persuasive

**Decision.** Build each Review Request to maximise effective and accurate review for the stated
purpose. Supply sufficient relevant material, expose assumptions and constraints, and avoid
unnecessary content or advocacy for the Lead's answer.

**Reason.** An independent model cannot compensate for a biased, incomplete, or context-dumped
request. Blind Mode controls intentional exposure, but all modes need accurate and attackable
framing.

---

## D16 — Communication is an external seam and AI Message owns indirect envelopes

**Status:** Refined by `D26`; transport remains external to Review, but its reusable owner is now Messaging.

**Decision.** Review supplies destination, Review/Round identity, and substantive request. A shared
communication capability resolves delivery/return. Indirect/manual routes use the existing AI
Message format with user-facing destination/model instructions and a copy-ready message or large
Markdown file.

**Reason.** Review should not embed platform-to-platform route rules or invent another messaging
format. The same communication infrastructure is expected to support Research and other inter-AI
behaviours later.

---

## D17 — Rounds are append-only and have no fixed cap

**Decision.** Each Round preserves its complete request, supplied material, unchanged response,
actual Lead/Reviewer models, outcome, dispositions, changes, and continuation reason. Continue
while materially useful new information is emerging and the Level justifies it; stop at sufficient
confidence, marginal value, or an explicit judgment/risk boundary.

**Reason.** Practical Review has produced valuable new perspectives across several Rounds. A hard
cap would cut off useful convergence. Unlimited pursuit of theoretical imperfections would create
disproportionate complexity. Material new value and Level provide the correct stopping discipline.

---

## D18 — Higher Levels re-review substantive Review-driven changes

**Decision.** Re-review expectation increases by Level. High and Extreme normally return
substantive material changes to the Reviewer before completion; Extreme treats material
remediation as part of the Review cycle.

**Reason.** The reviewed thing has changed. Verifying only that the Lead attempted a fix does not
establish that the revised outcome resolves the Finding or avoids new problems. Low-level work
does not justify the same cost for every edit.

---

## D19 — Findings and disposition remain distinct

**Decision.** Reviewer Findings preserve observation, materiality, evidence/reasoning,
uncertainty, consequence/risk, and optional remedy. The Lead records Accept, Decline, Defer,
Supersede, Investigate, Change, or Escalate and any resulting change/re-review decision.

**Reason.** Preserving the original Finding maintains an auditable independent view. Separating
remedy from Finding prevents the Reviewer's preferred mechanism from becoming the problem
definition.

---

## D20 — Review discovery cannot silently expand authorised execution

**Decision.** Review may identify issues beyond Authorised Scope. Neither Lead nor Reviewer may
implement them under the current work authority. They return as explicit out-of-scope Findings to
the director/work owner for re-scope, separate work, deferral, or decline.

**Reason.** A useful Finding is not permission. This prevents WorkPackage and directed work from
drifting into unauthorised design changes.

---

## D21 — Review has a concise Result and complete reconstructable evidence

**Decision.** The Review Result summarises identity, subject/scope, Type/Level/Mode,
Reviewer/model history, outcome, Findings/dispositions, changes, re-review, out-of-scope issues,
residual risk, and completion reason. Round records retain the exchanges.

**Reason.** The director of work needs a usable hand-back without reconstructing the conversation,
while later assurance still needs to know exactly what was asked, returned, and acted upon.

---

## D22 — Persistence can be transient or durable

**Decision.** Every Review preserves the semantic/evidence minimum. Routine Review may live in the
surrounding work record. A separate Documentation Methodology Review document is normally used for
substantive design-side, High/Extreme, materially multi-Round, significantly unresolved or
out-of-scope, required-evidence, or explicitly requested Review.

**Reason.** Forcing a separate file for every machine-driven code check makes Review expensive and
duplicative. Omitting durable evidence for consequential Review loses the independent assessment.
The surrounding record versus point-in-time Review document supplies both postures without a new
document type.

---

## D23 — Five use cases are the acceptance surface

**Decision.** The model is accepted only if the same mechanism supports design exploration,
pre-confirmation design Review, WorkPackage authoring Review, Build-plan Review, and
post-execution Review.

**Reason.** These cover the main design-to-build lifecycle in which Review has demonstrated value.
They test Review against forming work, durable decisions, handoff fidelity, execution planning,
and completed outcomes without introducing stage-specific Review mechanisms.

---

## D24 — Research remains separate

**Decision.** Research is not a Review Type or sixth primary use case. Research may gather
evidence inside a Review or reuse the same communication capability, but standalone Research has a
different purpose and future owner.

**Reason.** Sharing transport does not make behaviours the same. Folding Research into Review
would enlarge the lifecycle and repeat the ownership problem the Capabilities architecture is
designed to avoid.

---

## D25 — Environment settings and communication ownership remain explicit open seams

**Status:** Partly superseded by `D27`; environment settings remain open, communication ownership does not.

**Decision.** The Review corpus specifies the factual resolver/transport contracts it needs but
does not choose the storage home for environment settings or the permanent owner of shared
communication.

**Reason.** Both questions reach beyond Review and affect other components/behaviours. Choosing an
owner locally for implementation convenience would silently change the parent architecture.


---

## D26 — Messaging is the reusable communication owner consumed by Review

**Decision.** Review continues to own Review/Round/request/response lifecycle and correlation.
`AIDE_Messaging` owns AI-MESSAGE envelope, relay/receipt/reconciliation and messaging actions for
manual/indirect cross-context transport. Direct route mechanics remain environment/platform Build
facts and may optimise transport without changing the ownership split.

**Reason.** The prior design deliberately left the reusable communication owner unresolved. The
new Messaging capability now supplies that owner without requiring any change to Type, Level, Mode,
Reviewer, Findings, disposition or continuation semantics.

---

## D27 — Only the environment settings/route home remains an open external seam

**Decision.** Review still consumes factual environment data for reviewer/model/capability/route
availability, fallback, preferences and access/cost constraints without defining where that state is
stored. Communication ownership is no longer open.

**Reason.** Messaging resolves one of the two former D25 seams. Conflating that resolution with the
separate environment configuration question would create an unnecessary ownership change.



---

## D28 — Review payload correlation is authoritative; transport disagreement is quarantined

**Decision.** Review/Round identity in the Review request/response payload is authoritative for
Review lifecycle semantics. Messaging Thread/Message-ID/In-Reply-To remains transport-level
correlation. When both are positively available and disagree, the response is quarantined for
clarification rather than attached/dispositioned under either interpretation.

**Reason.** Review and Messaging correctly own separate identity layers. Manual relay can pair the
right envelope with the wrong Review body; treating a positive mismatch as an integrity failure
closes that gap without moving Review semantics into Messaging.

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Review_Design_v3, Capabilities_Design_v10, Capabilities_Decisions_v16, AIDE_Messaging@v2
References: Capabilities_Overview_v15, AIDE_ReviewProfiles@v2
