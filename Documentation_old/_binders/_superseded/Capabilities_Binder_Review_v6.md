# Capabilities Binder Review

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.
> **Binder Version 6** (2026-09-02). Adds durable Review orientation through Contents and the Review Result summary surface.

This Binder is a current-context consumption artefact; authoritative masters remain individual files.

## Binder manifest

- `Capabilities_Review_Definition_v3.md` — sha256 `7eed81f8f6a8`
- `Capabilities_Review_Design_v4.md` — sha256 `b9d8b0d50217`
- `Capabilities_Review_Decisions_v4.md` — sha256 `134909c568ec`
- `AIDE_Review_Standard_v4.md` — sha256 `272fb0adfa48`
- `AIDE_ReviewProfiles_Standard_v2.md` — sha256 `c319a69f77fb`
- `Capabilities_Review_Tool_Design_v3.md` — sha256 `9606d87841a2`
- `AIDE_Review_Tool_v3.md` — sha256 `07d08b5a97d6`

---

<!-- BEGIN SOURCE: Capabilities_Review_Definition_v3.md -->
# Review — Capability Definition

> **Version 3** (2026-09-02). Releases durable Review document orientation through AIDE Review v4.

## Identity, purpose and boundary

**Capability:** `Review@v2`

Provides independent assessment semantics, Profiles and orchestration.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Review.Standard` | Standard | `AIDE_Review@v4` | v2 |
| `Review.Profiles` | Standard | `AIDE_ReviewProfiles@v2` | v1 |
| `Review.Tool` | Tool | `AIDE_ReviewTool@v3` | v1 |

## Capability Release History

```text
Review@v1
  Review.Standard@v1 -> AIDE_Review@v3
  Review.Profiles@v1 -> AIDE_ReviewProfiles@v2
  Review.Tool@v1 -> AIDE_ReviewTool@v3

Review@v2
  Review.Standard@v2 -> AIDE_Review@v4
  Review.Profiles@v1 -> AIDE_ReviewProfiles@v2
  Review.Tool@v1 -> AIDE_ReviewTool@v3
```

This baseline adopts already-current canonical outcomes into the new Capability/Element release
model; it does not pretend those outcomes were newly changed on 2026-09-02.

## Element Release History

- `Review.Standard@v1` — baseline adoption of `AIDE_Review@v3`; no new semantic change asserted.
- `Review.Standard@v2` — defines Contents plus Review Result as the Summary-equivalent surface for substantial durable Review documents.
- `Review.Profiles@v1` — baseline adoption of `AIDE_ReviewProfiles@v2`; no new semantic change asserted.
- `Review.Tool@v1` — baseline adoption of `AIDE_ReviewTool@v3`; no new semantic change asserted.

## Element Production

| Element | Production inputs | LastEvaluated |
|---|---|---|
| `Review.Standard` | Current sources/contracts identified by Definition references | 2026-09-02 release v2 |
| `Review.Profiles` | Current sources/contracts identified by Definition references | 2026-09-02 baseline |
| `Review.Tool` | Current sources/contracts identified by Definition references | 2026-09-02 baseline |

Update the mutable checkpoint when sources/contracts are reassessed. An input-version change does
not by itself increment an Element release; immutable release-source snapshots stay in history when
later releases are produced.

## Current Migration

None. Authoritative existing outcome migrations remain under `AIDE_Migration`. A future Element
change carries Current Migration until release confirmation.

## Platform Definition and Build Platforms

The Capability is platform-neutral. Current generic Working Surface evidence must be resolved before
a Capability Build request. Newly supported platforms are surfaced and retain designer selection
`Build: null` until explicitly decided; unsupported plus `Build:true` is blocking.

## Post-Build intent

No Registry publication is inferred automatically. A Capability Build request may nominate
`AIDE_DeploymentRegistryTool@v1` action `Register` with the configured Registry and optional open
Release Batch, or another applicable post-Build Tool/explicit none. Actual post-Build result remains
external to the immutable validated package.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v2, AIDE_Dependencies@v3, AIDE_Migration@v3
References: Capabilities_Review_Design_v4, AIDE_Review@v4, AIDE_ReviewProfiles@v2, AIDE_ReviewTool@v3, AIDE_DeploymentRegistryTool@v1
<!-- END SOURCE: Capabilities_Review_Definition_v3.md -->

---

<!-- BEGIN SOURCE: Capabilities_Review_Design_v4.md -->
# Capabilities Review — Design

> **Version 4** (2026-09-02). Defines durable Review document orientation using Contents and the Review Result summary surface.

---

## Contents

- **Purpose and architecture** — Review ownership, value, roles and lifecycle model. §1–§4
- **Review inputs and selection** — triggers, Input Contract, Type/Level/Mode/Reviewer and requests. §5–§9
- **Transport and assessment lifecycle** — routing, Rounds, Findings, dispositions, re-review and scope. §10–§14
- **Records and persistence** — Review/Round/Result semantics, durable evidence and orientation. §15–§16, §20
- **Use cases, failures and seams** — acceptance surface, integrity rules and external dependencies. §17–§19

## Summary

Review introduces a meaningfully independent reasoning path to improve substantive integrity,
decision quality and risk management without transferring ownership of the work. The Lead owns the
work and dispositions; the Reviewer owns Findings. Type, Level, Mode and Reviewer are independent
inputs, and each Round preserves the actual request, response and model identities.

The lifecycle moves from a resolved Review Input through one or more Rounds, Finding dispositions,
authorised changes and re-review to a concise Review Result. Routine evidence may remain in a
surrounding work record; substantive, High/Extreme, multi-Round, materially unresolved or explicitly
requested Review normally gets a durable Review document.

For a substantial durable Review document, Contents maps the significant evidence/round areas and
the Review Result is positioned at the top as the Summary-equivalent surface. This avoids a second
competing summary while letting a reader understand the outcome before examining detailed Round,
Finding and evidence history.

## §1 — Scope and outputs

Review is the peer Capabilities component that manages a purposeful independent assessment
exchange. It exists to introduce a second reasoning path before consequential work is confirmed,
relied upon, handed off, or accepted as complete.

Review owns:

- stable Review semantics and lifecycle;
- the Lead and Reviewer roles;
- the Review Input Contract;
- Type, Level, Mode, and Reviewer as separate dimensions;
- request-construction rules;
- Review, Round, Finding, Disposition, and Review Result semantics;
- continuation, re-review, completion, and escalation discipline;
- the boundary between discovery and authorised execution.

Review does not own:

- the work being reviewed or its substantive design;
- trigger criteria belonging to a Standard, workflow, project, or WorkPackage;
- environment storage for available platforms, models, reviewers, routes, or local preferences;
- Messaging transport/envelope implementation or platform route mechanics;
- research as a distinct inter-AI behaviour;
- internal self-checking or mechanical document conformance.

### Declared outputs

This Design produces:

- `AIDE_Review_Standard_v4` — current stable Review semantics, lifecycle and durable-document orientation;
- `AIDE_ReviewProfiles_Standard_v2` — the five reusable Review Types and their defaults;
- `Capabilities_Review_Tool_Design_v3` — the current specification for the Review orchestration Tool.

The canonical Review Tool produced from the Tool Design is consumed by AI environments through
the normal Capabilities production and Build flow. The Tool Design remains internal; the
resulting Tool is the executable outcome.

External handlers consumed by these outputs are:

- environment configuration capable of resolving reviewer/model/route availability; and
- `AIDE_Messaging`, which supplies AI-MESSAGE relay/receipt semantics for indirect/manual exchange while platform routes may provide direct transport.

---

## §2 — Purpose, need, value, and role

Review exists to improve the substantive integrity of work, support better decisions, and manage
risk by bringing a second, meaningfully independent reasoning source into the work.

One AI can produce a coherent answer while sharing its own framing, assumptions, omissions, and
blind spots. A second AI can contribute different interpretations, evidence, alternatives, and
challenge. Review makes that contribution deliberate, correctly framed, and traceable.

The value is not agreement for its own sake. Review adds value when it:

- exposes an error, gap, assumption, risk, or unintended consequence;
- contributes a materially different framing or alternative;
- tests whether an outcome follows from its governing intent;
- improves the quality of a decision before it becomes expensive to reverse;
- establishes justified confidence proportionate to consequence and uncertainty; or
- makes a residual disagreement or accepted risk explicit.

Review can be collaborative while an approach is forming or challenging once an artefact or
position exists. In both cases, the Lead owns the current work, its net coherence, and the final
disposition. Reviewer findings are evidence and input, not instructions.

The governing completion principle is:

> Review seeks enough independent insight and challenge to justify the confidence appropriate to
> the consequence and risk of the work.

Review does not pursue perfection. Before adding a mechanism to answer a finding, the Lead
considers accepting the risk, removing the need, or reshaping the model. A theoretically removable
weakness does not automatically justify more complexity.

---

## §3 — Architectural model

```text
Trigger source
    ↓
Resolve Review Input Contract
    ↓
Type + Level + Mode + Reviewer
    ↓
Purpose-shaped Review Request
    ↓
Messaging / platform route
    ↓
Reviewer response
    ↓
Lead disposition and scoped change
    ↓
Continue / re-review / complete / escalate
    ↓
Review Result
```

The mechanism remains small because each concern has one owner:

```text
Review Standard       → stable semantics and lifecycle
Review Profiles       → reusable review methods and behavioural defaults
Review Tool           → lifecycle orchestration
Environment config    → available reviewers, models, capabilities, and routes
Messaging             → AI-MESSAGE relay/receipt semantics
Platform/environment   → concrete route availability/direct transport mechanics
Lead/work owner       → work changes, disposition, and risk decisions
```

---

## §4 — Roles and independence

### Lead

The Lead is the AI or agent responsible for the current work and for handling the Review. It:

- states the objective and authorised scope;
- supplies or validates the Review inputs;
- exposes the work accurately;
- receives and interprets the response;
- owns every Finding disposition;
- applies or directs accepted changes within scope;
- decides when user/work-owner judgment is required; and
- preserves the work's net simplicity and coherence.

### Reviewer

The Reviewer is the separate reasoning source selected for a Review Round. It:

- applies the selected Type, Level, and Mode;
- reports findings, evidence, uncertainty, consequences, and possible remedies;
- distinguishes material weaknesses from theoretical imperfections;
- does not silently modify the work or convert advice into a requirement; and
- may signal that clarification or another round would add material value.

### Role reversal and model identity

Lead and Reviewer are task-specific roles, not permanent properties of a provider or model. The
AI/platform that owns or initiates the current work is normally the Lead; environment
configuration selects a meaningfully separate Reviewer. In the current two-AI operating pattern,
the intended mapping is:

```text
Claude initiates/owns the work   → Claude is Lead; GPT/Codex is default Reviewer
GPT/Codex initiates/owns the work → GPT/Codex is Lead; Claude is default Reviewer
```

That mapping is current environment configuration rather than Review semantics.

Roles may reverse in another task or Review. A Review may also change the actual model used for
either role between Rounds. Each Round therefore records the actual Lead model and actual Reviewer
model used for that exchange; Review-level defaults are not an adequate model history.

Independence is functional rather than ceremonial. Selecting a different label that follows the
same context and reasoning path may not add the second view the Review requires. Level increases
the preference for a genuinely separate model family, context path, and evidence source.

---

## §5 — Trigger model

A Trigger answers only whether a Review should start now. The source that owns the relevant work
or risk condition owns the trigger criteria; Review consumes the result.

Primary trigger sources are:

1. direct user or Lead instruction;
2. AI recommendation when a second view is likely to add material value;
3. a Standard, workflow, or project rule;
4. WorkPackage configuration; and
5. a consequence/risk condition encountered during work.

A trigger carries a posture:

- **Required** — governing work cannot pass the relevant checkpoint without Review or an
  authorised exception;
- **Recommended** — Review is expected to add value, but the user/work owner may decline or alter
  it; or
- **Optional** — Review is available without a positive expectation.

A trigger supplies the subject, trigger basis, posture, and any suggested Type or Level. It does
not decide the full Review.

AI recommendation is a first-class trigger source. An AI should recommend Review when consequence,
reach, difficulty of reversal, uncertainty, novelty, weak evidence, or a valuable independent
perspective makes the expected benefit material. Recommendation remains distinct from requirement.

Stress Test is the deliberate exception to general triggerability: it may be recommended, but it
starts only after explicit user direction.

---

## §6 — Review Input Contract

The Review Input Contract defines the resolved information one Review needs. It is not a separate
configuration system and does not require every value to be manually supplied.

An instantiated Review resolves:

- **Trigger** — source, basis, and Required/Recommended/Optional posture;
- **Subject** — the question, decision, artefact, plan, implementation, or outcome under review;
- **Objective** — what this Review is trying to learn or determine;
- **Authorised scope** — the boundary within which Review-driven execution may occur;
- **Type** — the reusable review purpose/lens, or equivalent direct instructions for an ad hoc
  Review;
- **Level** — current assurance intensity;
- **Mode** — how much of the Lead's existing reasoning or solution is exposed;
- **Reviewer** — selected independent source and required capabilities;
- **Review material** — context, artefacts, evidence, constraints, assumptions, and uncertainties
  supplied to the Reviewer;
- **Response expectations** — what a useful response contains; and
- **Continuation/stop posture** — the Level- and Type-informed basis for further Rounds.

Resolution precedence is:

1. direct instruction for this Review;
2. trigger or work-item configuration;
3. selected Review Profile defaults;
4. shared Review operating defaults; and
5. environment-local availability/defaults.

Defaults fill gaps; they do not silently override explicit choices. A conflict between
authoritative sources is surfaced rather than guessed through. A caller may provide the profile
content directly for a one-off Review without first creating a new reusable Type.

---

## §7 — Type, Level, Mode, and Reviewer

The four dimensions remain independent:

| Dimension | Question answered | Owner of stable meaning |
|---|---|---|
| Type | What are we trying to learn, and through what lens? | Review Profiles |
| Level | How much assurance effort and capability are justified? | Review Standard / Profiles defaults |
| Mode | How much of the Lead's current solution should the Reviewer see? | Review Standard |
| Reviewer | Who supplies the independent reasoning path? | Resolved from environment data |

Type never means intensity. A `Check + High` can be extremely rigorous; a `Robust + Low` can be a
quick blank-sheet challenge. Level strengthens the selected method without changing its question.

The five initial Types are:

> **Check the claim → Inspect the artefact → Evaluate the outcome → Challenge the design →
> Stress it against external or adversarial reality.**

Their detailed definitions and defaults belong only in `AIDE_ReviewProfiles_Standard_v2`.

Mode has two values:

- **Full** — the Reviewer sees the current approach, reasoning, artefacts, and relevant context.
- **Blind** — selected Lead reasoning or solution content is withheld to reduce anchoring and
  obtain a more independent approach.

Blind Mode withholds anchoring material, not information needed to answer the objective
accurately.

---

## §8 — Level assessment and dynamic change

Level is the current judgment of how much review effort, capability, independence, evidence, and
iteration are justified. It is based primarily on:

- **Consequence** — how bad the outcome could be if the work is wrong;
- **Reach** — how much downstream work or how many consumers could be affected;
- **Reversibility** — how difficult or costly correction would be later; and
- **Uncertainty** — how novel, ambiguous, assumption-heavy, or weakly evidenced the work is.

Use judgment, not arithmetic. Do not average away one serious factor. Size and complexity can
inform the assessment but are not primary drivers.

The scale is:

```text
Low → Standard → Medium → High → Extreme
```

Higher Levels progressively increase:

- reviewer/model capability;
- depth and breadth;
- evidence inspection and verification;
- independence expectation;
- persistence while material new information is emerging;
- re-review expectation after substantive change; and
- the confidence threshold for completion.

Level is dynamic. A material Finding can expose greater or lower consequence, reach,
reversibility, or uncertainty. A change of Level is recorded with a short reason and affects
subsequent behaviour; it does not invalidate completed Rounds. Reviewer/model/route resolution may
be repeated for the next Round after a Level change.

---

## §9 — Review Request construction

A Review Request is built to maximise the chance of an effective and accurate review for the
stated purpose and need.

It contains:

- Review and Round identity;
- subject, objective, and authorised review scope;
- Type purpose, learning objective, and lens;
- effective Level and its relevant expectations;
- Mode and any deliberate withholding;
- the material needed to perform the Review;
- relevant constraints, assumptions, uncertainties, and evidence;
- specific questions or instructions; and
- response expectations.

The request is:

- **accurate** — it does not distort the work or hide material weakness;
- **sufficient** — the Reviewer has what is needed to answer the question;
- **relevant** — unrelated context is omitted;
- **attackable** — assumptions and claims can be tested; and
- **non-persuasive** — it does not argue the Lead's conclusion or anchor the Reviewer beyond what
  Full Mode requires.

Mode controls exposure, but purpose controls construction. Review material is not included merely
because it exists.

---

## §10 — Messaging and routing boundary

Review owns the assessment exchange and its Review/Round state. `AIDE_Messaging` owns AI-MESSAGE
envelope, relay/receipt, message correlation and reconciliation semantics used for indirect/manual
cross-context transport.

Review supplies Messaging/the route with:

- current surface/environment;
- selected Reviewer;
- Review and Round identity; and
- completed Review Request.

Environment/platform routing supplies factual route availability and concrete transport mechanics:

- send and return mechanism;
- synchronous/asynchronous/manual posture;
- packaging, attachment, context, or size constraints; and
- delivery/response state or failure where the route can expose it.

Route resolution remains data-driven:

```text
current surface + selected Reviewer → available route
```

Review does not embed named platform-to-platform rules. Where manual/indirect relay is used,
Messaging produces the AI-MESSAGE envelope and consumes the correlated return. The user-facing
handoff includes destination, requested model/capability, any execution instructions, a ready-to-
copy message, and exact return instructions. Exceptionally large Review material may accompany the
message as a Markdown file. Review owns the substantive Review Request and Review/Round correlation;
Messaging owns the message envelope and receipt/reconciliation semantics.

A direct platform route may transport the Review content without visibly rendering an AI-MESSAGE
where the implementation preserves equivalent Review correlation. That optimisation does not
transfer route mechanics into Review or change Messaging ownership of the reusable messaging
semantics.

---

## §11 — Response, Round, and continuation lifecycle

Every response must be attributable to a specific Review and Round before Review acts on it.
Review/Round identity carried by the substantive Review request/response is authoritative for Review
lifecycle semantics. Messaging correlation is transport-level evidence. Where both are positively
available and disagree, quarantine the response for clarification; do not choose one layer and
continue.

A response reports:

- Review and Round identity;
- Reviewer and actual model;
- status: Complete, Partial, Clarification Needed, or Failed;
- the response payload defined by the Type; and
- an optional signal that another Round would add material value.

Each Round is an append-only record of one request/response cycle. It preserves:

- Round identity and number;
- actual Lead identity/model;
- actual Reviewer identity/model;
- effective Type, Level, and Mode for that Round;
- request sent and material supplied;
- route/transport reference where relevant;
- response received unchanged;
- Lead disposition and changes arising from the Round;
- Round outcome; and
- reason for continuing, completing, or escalating.

After a response, the Lead/handler asks:

- Did the response materially change understanding?
- Are there unresolved findings material to the current Level?
- Would another Round likely add useful information?
- Did Review-driven changes materially alter the reviewed state?
- Has the remaining issue become a user/work-owner judgment rather than a Review question?

The result is:

- **Continue** — prepare another Round;
- **Complete** — confidence is sufficient for the current Level and required re-review is done;
  or
- **Escalate** — unresolved difference, risk, scope, or authority requires work-owner/user
  judgment.

There is no hard Round cap. Continue while materially useful new information is emerging and the
Level justifies the effort. Stop when further work is marginal/speculative, sufficient confidence
has been reached, or the residual issue is an explicit judgment. Repeatedly exposing theoretical
imperfections is not itself a reason to continue.

---

## §12 — Findings, disposition, and change

The Reviewer owns Findings. A material Finding records:

- observation;
- why it matters;
- evidence or reasoning;
- uncertainty;
- likely consequence or risk; and
- an optional possible remedy.

The Lead owns Disposition. Normal values are:

- Accept;
- Decline;
- Defer;
- Supersede;
- Investigate;
- Change;
- Escalate.

A Finding is evidence, not an instruction. A possible remedy remains advisory until adopted by
the Lead. The original Finding and response are preserved; later disagreement or resolution does
not rewrite them.

Review can drive a change only through Lead disposition. The Lead records the disposition,
resulting change or reason for no change, and whether the revised state needs re-review.

---

## §13 — Re-review after change

Re-review tests the revised outcome, not merely whether the Lead reports that a change was made.
It assesses whether the change resolves the Finding and whether it introduced new problems.

The expectation rises with Level:

- **Low** — re-review when the Lead judges the change material;
- **Standard** — re-review material changes or significant Finding resolutions;
- **Medium** — normally re-review substantive changes in the reviewed scope;
- **High** — substantive Review-driven changes are returned before completion; and
- **Extreme** — material remediations are part of the Review cycle; completion normally means the
  resulting state has survived Review.

An editorial or strictly local change that does not materially alter what was assessed need not
create another Round. Type-specific continuation guidance may strengthen but not weaken a Level's
required posture.

---

## §14 — Authorised-scope boundary

Review may discover beyond the authorised scope, but execution may not silently expand beyond it.

- **Within scope** — the Lead may apply accepted changes normally.
- **Outside scope** — neither Lead nor Reviewer implements the change as part of the current work.

An out-of-scope Finding records the issue, why it matters, likely consequence/risk, and a useful
direction where available. It is marked explicitly and returned with the Review Result to the
director/work owner for re-scope, separate work, deferral, or decline.

This boundary is especially strict for WorkPackages and directed work: useful review insight does
not authorise design drift.

---

## §15 — Review, Round, and Result records

The Review record is the lifecycle container. It includes:

- Review identity;
- subject, objective, trigger, and authorised scope;
- initial/effective Type, Level, Mode, and Reviewer;
- Level changes and reasons;
- current/terminal state;
- ordered Round records;
- Finding/disposition summary; and
- the final Review Result.

Stable lifecycle states are:

```text
Initiated
Awaiting Response
Response Received
Continuing
Complete
Escalated
```

The Review Result is a concise hand-back rather than a substitute for Round history. It contains:

- Review identity;
- subject and scope reviewed;
- Type, final Level, and Mode;
- Reviewer(s) and actual models used;
- outcome: Complete, Escalated, or Unresolved;
- material Findings and Lead dispositions;
- changes made within scope;
- re-review status;
- out-of-scope Findings;
- residual risks or accepted differences; and
- completion reason.

Completion reasons include convergence, sufficient confidence for Level, diminishing material
value, accepted difference/residual risk, or escalation for judgment.

---

## §16 — Transient and durable persistence

Review always preserves enough evidence to reconstruct what happened, but it does not always
require a separate Review document.

### Transient Review

A routine or machine-driven Review may store the Review Result and required Round evidence in the
surrounding work record, such as a WorkPackage Outcome. The containing record must preserve the
same semantic minimum and identify where the complete exchanges can be recovered while needed.

### Durable Review

A separate Documentation Methodology `Review` document is normally justified when the Review is:

- substantive design-side evidence;
- High or Extreme;
- multi-Round with material evolution;
- carrying significant unresolved or out-of-scope Findings;
- required as durable assurance evidence; or
- explicitly requested for preservation.

The durable document carries the Review Result and either the complete Round exchanges or stable
references to them. It follows Documentation Methodology v17's point-in-time Review naming,
immutability, Finding-status, distribution, and archival rules.

The Review Tool decides the storage location from the governing work context and persistence
rule; it does not invent a parallel document type.

---

## §17 — Five primary use cases

The design must support these without special-case lifecycle machinery:

| Use case | Typical Type / Mode | Design requirement |
|---|---|---|
| Design exploration | Evaluate; Blind where an independent approach is wanted; Robust where framing itself is suspect | Send the issue, objective, scope, current thinking as Mode permits, and relevant material while the approach is still forming. |
| Pre-confirmation design review | Evaluate or Robust | Prompt before a key/impactful position becomes durable; set Level from consequence, reach, reversibility, and uncertainty. |
| WorkPackage authoring review | Check or Inspect | Test the WorkPackage against the authoritative Design/Brief/contract, not Decisions history; skip or offer for genuinely low-risk/simple work. |
| Build-plan review | Evaluate; Robust at stronger challenge postures | Review the proposed implementation before execution where the WorkPackage's review posture calls for it; broader challenge grows with Type and Level. |
| Post-execution review | Inspect; Robust where deeper structural assurance is justified | Verify validity, conformance to the WorkPackage contract, scope control, and material implementation problems; apply Level-driven re-review. |

For plan and execution Review, Type determines what is examined and Level determines how far and
how deeply the Reviewer should look beyond immediate implementation detail while still respecting
authorised scope.

Research is not a sixth Review use case. It may reuse the same communication infrastructure but
has a different purpose and lifecycle owner.

---

## §18 — Failure and integrity rules

- A response that cannot be correlated to Review and Round is quarantined for clarification; it
  is not dispositioned.
- A positive disagreement between Review/Round payload identity and Messaging transport correlation
  is likewise quarantined; transport identity does not override Review semantics and Review identity
  does not rewrite the transport record.
- A partial or clarification-needed response keeps the Review open and records what is missing.
- Delivery failure preserves the Review Request and route state so the same Round can be retried
  or rerouted without losing identity.
- A Reviewer/model change is explicit in the next Round record.
- A required Review cannot be silently skipped. Any authorised exception records who authorised
  it and the consequence accepted.
- Review never presents transport success as substantive completion.
- Review never marks a Finding resolved solely because a change was attempted.
- Review never broadens authorised execution from a Finding alone.

---

## §19 — External dependencies and remaining open seam

### Environment settings home

Review needs factual environment data for:

- available AI platforms/reviewer families;
- actual models and capability tiers;
- available surfaces and routes;
- fallback order and local preferences;
- cost, usage, access, and capability constraints; and
- requested-versus-actual model reporting where available.

Where this information is stored and which architecture component owns it remain separate work.
Review consumes a resolver; it does not define the settings store.

### Messaging dependency

Review consumes `AIDE_Messaging` for AI-MESSAGE relay/receipt/reconciliation semantics. Messaging's
platform implementations may support Review, Research and other inter-AI behaviours without moving
their substantive lifecycles into Messaging.

### No hidden ownership transfer

Temporary platform glue used to realise Review does not transfer either seam into Review. If
future work changes Type/Level/Mode/Reviewer separation or assigns environment routing/settings mechanisms to
Review, that is a parent-model change and requires explicit confirmation rather than an
implementation convenience.

## §20 — Durable Review document orientation

Review consumes Documentation Methodology's value-based Contents/Summary model and defines a
specialised equivalent for its durable DocType.

For a substantial durable Review document:

1. use a concise semantic Contents block where it improves navigation across Rounds, Findings,
   dispositions, evidence and residual issues; then
2. place the current Review Result near the top as the Summary-equivalent surface.

The Review Result already communicates subject/scope, Type/Level/Mode, material Findings and
dispositions, changes, re-review, residual risks and completion reason. Do not add a duplicative
generic Summary when the Result performs that role. Detailed Round/Finding/evidence records remain
the authoritative basis and must be preserved under the normal Review contract.

Small/transient Review stored in a surrounding work record need not acquire document-level
orientation sections when that record already provides sufficient context.

---
Dependencies: !AIDE_DocumentationMethodology@v28, Capabilities_Review_Decisions_v4, Capabilities_Design_v14, Capabilities_Decisions_v20, AIDE_Messaging@v2
References: Capabilities_Overview_v19, Capabilities_Standards_Design_v8, Capabilities_Tools_Design_v7, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_ReviewProfiles@v2
<!-- END SOURCE: Capabilities_Review_Design_v4.md -->

---

<!-- BEGIN SOURCE: Capabilities_Review_Decisions_v4.md -->
# Capabilities Review — Decisions

> **Version 4** (2026-09-02). Records durable Review document orientation and AIDE Review v4.

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

## D29 — Review Result is the durable document's Summary-equivalent surface

**Decision.** A substantial durable Review document uses a semantic Contents block where useful and
positions its current Review Result near the top as the Summary-equivalent surface. Do not add a
duplicative generic Summary when Result already provides the high-level outcome. Detailed
Rounds/Findings/evidence remain authoritative.

**Reason.** Review already owns a concise hand-back contract. Reusing it gives human and machine
readers the needed high-level understanding without creating a second potentially inconsistent
interpretation layer.

## D30 — Issue AIDE Review v4 prospectively

**Decision.** Publish `AIDE_Review@v4` with transition posture `None`. Existing Review records are
not mass-rewritten; new/substantively updated durable Review documents apply the orientation rule
where it adds value.

---
Dependencies: !AIDE_DocumentationMethodology@v28, Capabilities_Review_Design_v4, Capabilities_Design_v14, Capabilities_Decisions_v20, AIDE_Messaging@v2
References: Capabilities_Overview_v19, AIDE_ReviewProfiles@v2
<!-- END SOURCE: Capabilities_Review_Decisions_v4.md -->

---

<!-- BEGIN SOURCE: AIDE_Review_Standard_v4.md -->
# AIDE Review — Standard

> **Identity:** `AIDE_Review@v4`
> **Common name:** Review
> **Version 4** (2026-09-02). Defines Contents and Review Result as the orientation surface for substantial durable Review documents.

---

## Contents

- **Purpose and roles** — applicability, governing principles, Lead/Reviewer responsibilities and trigger contract.
- **Review definition** — Input Contract, Type, Level, Mode, Reviewer resolution and request construction.
- **Lifecycle and evidence** — routing, response, states, Rounds, Findings, disposition, re-review and scope.
- **Result and persistence** — high-level outcome, durable document orientation and evidence retention.
- **Safety and seams** — failure handling and external environment/Messaging dependencies.

## Summary

Review introduces a proportionate independent reasoning path while keeping the Lead responsible for
the work and every disposition. A resolved Input Contract drives one or more recorded Rounds through
Findings, authorised change and re-review to a concise Review Result.

Substantial durable Review documents use Contents where navigation adds value and position Review
Result near the top as the Summary-equivalent surface. Detailed Round/Finding/evidence records remain
authoritative; no duplicative Summary is required.

## Purpose

Provide a stable way to bring a meaningfully independent reasoning source into work, obtain
insight or challenge shaped to the actual objective, manage the exchange proportionately to risk,
and return a clear result without transferring ownership of the work to the Reviewer.

## Applicability

Apply this Standard whenever an activity is identified as a Review, whether initiated directly,
recommended by an AI, required or recommended by a governing Standard/workflow, configured by a
WorkPackage, or triggered by consequence/risk.

A mechanical self-check, document-format validation, or independent research task is not a Review
merely because it tests something. It uses this Standard only when it creates the Lead/Reviewer
assessment lifecycle defined here.

## Governing principles

- Review introduces a second reasoning path to improve substantive integrity, decisions, and risk
  management.
- The Lead owns the work and its final disposition. The Reviewer owns Findings.
- A Finding is evidence, not an instruction.
- Type, Level, Mode, and Reviewer are independent Review inputs.
- Review effort and stopping confidence are proportionate to Level.
- Review may discover beyond authorised scope; execution may not silently expand beyond it.
- Review owns the assessment exchange and its Review/Round state. Messaging owns AI-MESSAGE relay/receipt semantics; environment/platform routes own concrete delivery mechanics.
- A separate Review document is optional; reconstructable Review evidence is not.
- Review stops at justified confidence or explicit judgment, not perfection.

## Roles

### Lead

The Lead owns the current work, states or validates the Review objective and authorised scope,
supplies an accurate account of the work, handles the response, owns Finding disposition, and
preserves the net coherence and simplicity of the resulting work.

### Reviewer

The Reviewer provides the separate reasoning path. It applies the effective Type, Level, and Mode;
reports material Findings with evidence/reasoning and uncertainty; and may offer possible remedies
without treating them as requirements.

### Role assignment

Roles are contextual. The AI/platform responsible for or initiating the current work is normally
the Lead. The environment resolver supplies a meaningfully independent default Reviewer and may be
overridden explicitly.

The same AI family is not permanently Lead or Reviewer. Roles can reverse across work, and actual
models may change between Rounds. Every Round records the actual Lead model and Reviewer model.

## Trigger contract

A Trigger provides:

- `Source` — user/Lead, AI recommendation, governing Standard/workflow/project rule, WorkPackage,
  or risk/consequence condition;
- `Basis` — why Review is warranted now;
- `Posture` — `Required`, `Recommended`, or `Optional`;
- `Subject`; and
- optional suggested `Type` and `Level`.

The trigger source owns its criteria. Review resolves and executes the resulting Review.

An AI should recommend Review where consequence, reach, difficulty of reversal, uncertainty,
novelty, weak evidence, or a valuable second perspective makes the expected benefit material.
Recommendation does not become requirement unless the governing source makes it one.

`Stress Test` may be recommended but starts only after explicit user direction.

## Review Input Contract

Before the first request is sent, resolve:

```yaml
ReviewInput:
  Trigger:
    Source: <identity>
    Basis: <reason>
    Posture: Required | Recommended | Optional
  Subject: <thing or question under review>
  Objective: <what the Review is trying to learn or determine>
  AuthorisedScope: <execution boundary>
  Type: Check | Inspect | Evaluate | Robust | Stress Test | <omitted when DirectProfile is used>
  DirectProfile: <optional purpose, learning objective, lens/method, response expectations>
  Level: Low | Standard | Medium | High | Extreme
  Mode: Full | Blind
  Reviewer:
    Identity: <review source>
    RequiredCapabilities: <where applicable>
  ReviewMaterial: <context, artefacts, evidence, constraints, assumptions, uncertainties>
  ResponseExpectations: <useful payload>
  ContinuationPosture: <Type and Level informed>
```

`DirectProfile` lets the caller supply the profile content for a one-off Review. It does not add a
sixth Type or create a new reusable Profile.

Values resolve in this order:

1. direct instruction for this Review;
2. trigger or work-item configuration;
3. selected Review Profile defaults;
4. shared Review operating defaults;
5. environment-local availability/defaults.

Defaults fill gaps and never silently override an explicit value. Surface a conflict between
authoritative sources rather than choosing one without notice. Ask only for input that cannot be
safely resolved from the work and available configuration.

## Type

Type defines why the Review is being performed, what it is trying to learn, the lens/method the
Reviewer applies, and the expected response.

The standard profiles are defined only in `AIDE_ReviewProfiles@v2`:

```text
Check → Inspect → Evaluate → Robust → Stress Test
```

This ordering describes increasing distance from the current claim/artefact/design, not increasing
thoroughness. Level controls intensity.

## Level

Level defines the assurance effort, capability, independence, evidence, iteration, and stopping
confidence justified by the work.

Assess Level over four factors:

- `Consequence` — severity if wrong;
- `Reach` — downstream breadth;
- `Reversibility` — cost/difficulty of correction; and
- `Uncertainty` — novelty, ambiguity, assumption load, and evidence weakness.

Use judgment, not a score. Do not average away one serious factor. Work size and complexity may
inform but do not determine Level.

| Level | Meaning | Review posture |
|---|---|---|
| Low | Low consequence; easy to reverse | Quick focused pass; surface obvious/material issues; stop early. |
| Standard | Normal consequence and uncertainty | Normal independent review with reasonable evidence checking and further Rounds where useful. |
| Medium | Material consequence, uncertainty, reach, or difficulty of reversal | Stronger capability; broader examination; challenge assumptions; normally re-review substantive change. |
| High | Significant consequence or systemic risk | Deep independent review; substantial evidence; high confidence threshold; persist while material issues remain. |
| Extreme | Exceptional or critical consequence | Best justified available capability; maximum practical independence/evidence; very high confidence threshold; rare. |

Higher Level increases strength, not Type. Actual model names and routes are environment data.

### Dynamic Level

Reassess Level when a material Finding changes the understood consequence, reach, reversibility,
or uncertainty. Escalate or de-escalate accordingly, record a short reason, and re-resolve
Reviewer/model/route for the next Round when needed.

A Level change affects subsequent behaviour and does not invalidate completed Rounds.

## Mode

Mode controls exposure to the Lead's existing solution or reasoning:

- `Full` — expose the current approach, reasoning, artefacts, and relevant context.
- `Blind` — withhold selected solution/reasoning content to reduce anchoring and elicit an
  independent approach.

Blind Mode does not withhold information needed to answer the objective accurately. Record what
was deliberately withheld.

## Reviewer resolution

Resolve Reviewer after Type, Level, Mode, and required evidence/capabilities are known, and before
final request packaging.

The Reviewer is a review source/family, not a permanently pinned model version. Environment data
supplies:

- available reviewer identities/families;
- actual models and capability tiers;
- evidence/file/repository/web capabilities;
- independence characteristics;
- routes from the current surface;
- availability, usage, access, and cost constraints; and
- fallbacks.

Review does not define where that environment data is stored.

## Review Request

Build the request to maximise the chance of an effective and accurate Review for the objective.
Include:

- Review and Round identity;
- Subject, Objective, and AuthorisedScope;
- effective Type purpose/lens and Level expectations;
- Mode and deliberate withholding;
- sufficient relevant ReviewMaterial;
- constraints, assumptions, uncertainties, and evidence;
- specific questions/instructions; and
- ResponseExpectations.

The request is accurate, sufficient, relevant, attackable, and non-persuasive. It exposes the work
without arguing the Lead's conclusion or including context merely because it exists.

## Routing and communication

Review hands Messaging/the resolved route:

```yaml
ReviewDelivery:
  CurrentSurface: <surface>
  Reviewer: <resolved reviewer>
  ReviewId: <identity>
  RoundId: <identity>
  Request: <complete review request>
```

Environment/platform routing owns concrete route selection/send-return mechanics and packaging constraints; Messaging owns reusable AI-MESSAGE envelope/receipt/reconciliation semantics,
delivery state, and failures.

For indirect/manual communication, use `AIDE_Messaging` and its AI-MESSAGE envelope. Supply the
user with destination, requested model/capability, instructions, a ready-to-copy message, and exact
return instructions. Use a Markdown file where the request is exceptionally large.

Do not embed platform-to-platform routes or transport implementation in Review.

Review/Round identity in the substantive Review payload is authoritative for Review lifecycle
semantics; Messaging correlation remains transport-level evidence. Positive disagreement between
the two is a quarantine condition, not a tie to resolve.

## Response contract

Act on a response only after it is correlated to one Review and Round.

```yaml
ReviewResponse:
  ReviewId: <identity>
  RoundId: <identity>
  Reviewer: <actual reviewer identity>
  ActualModel: <actual model, if known>
  Status: Complete | Partial | ClarificationNeeded | Failed
  Payload: <Type-defined review response>
  ContinuationSignal: <optional material-value signal>
```

Preserve the response unchanged in the Round record. A partial or clarification-needed response
keeps the Review open. An uncorrelated response is held for clarification and is not dispositioned.

## Lifecycle and states

The stable Review states are:

```text
Initiated
Awaiting Response
Response Received
Continuing
Complete
Escalated
```

Normal flow:

```text
Initiated
  → request resolved and sent
Awaiting Response
  → correlated response returned
Response Received
  → Lead handles Findings and change
Continuing | Complete | Escalated
```

There is no hard Round limit. After every handled response, determine whether:

- another Round is likely to add material information;
- unresolved Findings remain material to the current Level;
- Review-driven changes require verification;
- sufficient confidence has been reached; or
- the remaining matter is a user/work-owner judgment.

Continue, complete, or escalate from that assessment. Do not continue merely because further
imperfections can be imagined.

## Round record

Rounds are append-only. Each Round records:

- Review/Round identity and number;
- actual Lead identity/model;
- actual Reviewer identity/model;
- effective Type, Level, and Mode;
- request and supplied material;
- route/transport reference where useful;
- response unchanged;
- Findings and Lead dispositions arising from the Round;
- changes made;
- outcome; and
- reason for continuing, completing, or escalating.

Later Rounds may refer to earlier Rounds but do not replace them.

## Findings and disposition

A Finding preserves:

- observation;
- materiality/why it matters;
- evidence or reasoning;
- uncertainty;
- likely consequence/risk; and
- optional remedy.

The Lead records one or more dispositions:

```text
Accept | Decline | Defer | Supersede | Investigate | Change | Escalate
```

The Finding remains unchanged. A remedy is advisory until adopted. The Lead records the resulting
change or reason for no change and the re-review decision.

## Re-review

Re-review evaluates the revised outcome and whether it resolves the Finding without introducing
new problems.

| Level | Re-review expectation |
|---|---|
| Low | Re-review when the Lead judges the change material. |
| Standard | Re-review material changes or significant Finding resolutions. |
| Medium | Normally re-review substantive changes in reviewed scope. |
| High | Return substantive Review-driven changes before completion. |
| Extreme | Re-review material remediations as part of the cycle; the resulting state normally must survive Review. |

Minor editorial/local change that does not materially alter what was assessed does not require a
new Round.

## Scope control

Review may identify an issue outside AuthorisedScope. Neither Lead nor Reviewer may implement it
under the current authority.

Mark the Finding `OutOfScope` and return:

- the Finding;
- why it matters;
- likely consequence/risk; and
- suggested direction where useful.

The director/work owner decides re-scope, separate work, defer, or decline. This rule applies
strictly to WorkPackages and directed work.

## Review Result

Every completed or escalated Review returns:

```yaml
ReviewResult:
  ReviewId: <identity>
  Subject: <subject>
  ScopeReviewed: <scope>
  Type: <named Type, or DirectProfile>
  FinalLevel: <level>
  Mode: <mode>
  ReviewersAndModels: <actual Round history summary>
  Outcome: Complete | Escalated | Unresolved
  MaterialFindings: <summary with dispositions>
  ChangesWithinScope: <summary>
  ReReviewStatus: <required/completed/not required/outstanding>
  OutOfScopeFindings: <summary>
  ResidualRisks: <accepted or unresolved differences>
  CompletionReason: <why Review stopped>
```

The Result tells the director of work what was reviewed, what mattered, what changed, what remains,
and what needs attention without requiring reconstruction of the exchange.

## Persistence

Every Review preserves the Review Result and enough Round evidence to reconstruct what happened.

Use the surrounding work record for routine/transient Review where it can preserve the required
semantics, including a WorkPackage Outcome.

Create a separate Documentation Methodology `Review` document where Review is substantive
design-side evidence, High/Extreme, materially multi-Round, carries significant unresolved or
out-of-scope Findings, is required as assurance evidence, or is explicitly requested.

A durable Review document follows the governing document methodology. It contains the Review
Result and the complete Rounds or stable references to them. Review does not create a competing
record type.

For a substantial durable Review document, include a concise semantic Contents block when it adds
navigation value and place the current Review Result near the top after Contents as the
Summary-equivalent surface. Do not add a separate duplicative Summary when Result already performs
that role. Detailed Round/Finding/evidence records remain authoritative. Transient Review embedded
in a surrounding record may use that record's existing orientation.

## Failure handling

- Preserve request, identity, and route state after delivery failure so the same Round can be
  retried or rerouted.
- Quarantine a response whose Review/Round payload identity positively disagrees with Messaging
  transport correlation; do not attach or disposition it until clarified.
- Do not report delivery success as Review completion.
- Do not silently skip Required Review; record an authorised exception and accepted consequence.
- Do not mark a Finding resolved because a change was attempted.
- Do not infer permission to expand scope from a Finding.
- Surface unavailable independence/capability rather than claiming the selected Level was met.

## External dependencies

Review consumes but does not own:

- environment configuration for reviewer/model/route availability and local mappings; and
- `AIDE_Messaging` for AI-MESSAGE relay/receipt/reconciliation on indirect/manual cross-context
  transport.

Concrete direct-route mechanics remain environment/platform Build concerns. Communication ownership
is no longer an open architecture seam; the environment settings/storage home remains external.

```yaml
MigrationSummary:
  CurrentVersion: v4
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v4
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v28, Capabilities_Review_Design_v4, AIDE_Messaging@v2
References: AIDE_ReviewProfiles@v2, Capabilities_Design_v14, Capabilities_Tools_Design_v7
<!-- END SOURCE: AIDE_Review_Standard_v4.md -->

---

<!-- BEGIN SOURCE: AIDE_ReviewProfiles_Standard_v2.md -->
# AIDE Review Profiles — Standard

> **Identity:** `AIDE_ReviewProfiles@v2`
> **Common name:** Review Profiles
> **Version 2** (2026-09-01). Makes current Review contract references versionless while preserving the five established Review Types/defaults.

---

## Purpose

Define reusable Review methods over the `AIDE_Review` Input Contract so a caller can select a
purposeful review lens without rebuilding its instructions each time.

## Profile contract

Every reusable Review Profile defines:

- `Name` — stable Type identity;
- `Purpose` — why the Type exists;
- `LearningObjective` — what the Review is trying to find out;
- `Boundary` — how far outside the current claim/artefact/design it may step;
- `LensMethod` — how the Reviewer approaches the work;
- `EvidenceExpectations` — what verification, comparison, or external evidence is expected;
- `ExpectedResponse` — what a useful payload contains;
- `DefaultLevel`;
- `DefaultMode`; and
- `ContinuationGuidance`.

Type defaults fill unresolved inputs. They do not override an explicit value or the effective Level
assessment for the actual task.

## Shared Type rules

- Choose Type from what the Review is trying to learn, not how important the work is.
- Type determines method; Level scales how strongly that method is applied.
- A Type may expose a more serious issue and justify switching Type in a later Round. Record the
  change and reason rather than silently broadening the active Type.
- Report material issues first. Do not propose complexity merely because an imperfection can be
  removed.
- Evidence and remedies are proportionate to Level and the Review objective.
- Level-based re-review rules in `AIDE_Review` apply to every Type.

## Default matrix

| Type | Boundary | Default Level | Default Mode | Core question |
|---|---|---:|---|---|
| Check | Criterion-bound | Low | Full | Is this specific proposition or condition correct/satisfied? |
| Inspect | Artefact-bound | Standard | Full | What is wrong, missing, inconsistent, weak, or materially improvable? |
| Evaluate | Outcome-bound | Medium | Full | Does this approach deliver the intended outcomes well, and how could it be better? |
| Robust | Design/framing-bound | High | Full | Is the design itself sound, and where could its assumptions or structure fail? |
| Stress Test | Environment/adversary-bound | Extreme | Full | How does this withstand capable adversarial, competitive, or demanding external scrutiny? |

`Evaluate + Blind` is the normal form for an independent approach before the Lead's solution is
shown. Blind Mode remains an explicit selection because many Evaluate Reviews need to assess the
current approach directly.

## Check

### Purpose

Determine whether a specific proposition, requirement, calculation, contract point, expected
result, or condition is correct or satisfied.

### Learning objective

> Is the stated criterion met, and what evidence supports that answer?

### Boundary

Check is criterion-bound. It verifies the stated target and does not become a general search for
defects. If the check exposes a broader material issue, report it and recommend an appropriate
Type/Level change.

### Lens and method

- identify the exact claim or criterion;
- establish the authoritative evidence or test;
- verify the result and relevant assumptions;
- distinguish pass, fail, qualified/conditional result, and unknown;
- identify any evidence gap that prevents a reliable answer.

### Evidence expectations

Use evidence directly relevant to the criterion. At higher Levels, independently verify the
source, calculation, test, or trace from requirement to result rather than accepting an assertion.

### Expected response

- answer: Pass, Fail, Qualified, or Unknown;
- criterion applied;
- supporting evidence/test;
- defect or unmet condition where present;
- uncertainty/evidence gap; and
- any broader issue requiring another Type.

### Defaults and continuation

- `DefaultLevel: Low`
- `DefaultMode: Full`
- normally complete after a reliable answer;
- continue for missing evidence, material ambiguity, or verification of a material correction;
- do not broaden into Inspect without an explicit Type change.

## Inspect

### Purpose

Examine an existing artefact, implementation, document, code change, plan, or outcome for defects,
omissions, inconsistencies, drift, and meaningful improvement.

### Learning objective

> What is wrong, missing, inconsistent, weak, or materially improvable in what exists?

### Boundary

Inspect is artefact-bound. It accepts the authorised design/intent as the governing frame and
tests the artefact against it. It can identify a better local approach, but it does not redesign
the governing model unless a Finding justifies an Evaluate or Robust escalation.

### Lens and method

- inspect the artefact itself rather than only its description;
- compare against authoritative requirements, intent, scope, interfaces, and expected outcomes;
- find defects, omissions, inconsistencies, weak implementation choices, and scope drift;
- consider straightforward alternatives where they materially improve the outcome;
- prioritise by materiality rather than volume.

### Evidence expectations

Use the artefact and its authoritative contract. At higher Levels, inspect supporting tests,
source material, dependency behaviour, execution evidence, and relevant adjacent effects.

### Expected response

- material Findings in priority order;
- affected location or element;
- evidence/reasoning and consequence;
- contract/intent comparison where applicable;
- uncertainty; and
- possible local improvement where useful.

### Defaults and continuation

- `DefaultLevel: Standard`
- `DefaultMode: Full`
- continue where material defects remain, accepted fixes materially change the artefact, or the
  current artefact cannot yet be tested reliably;
- recommend Evaluate/Robust when the defect appears to originate in the governing approach rather
  than the artefact.

## Evaluate

### Purpose

Assess whether a concept, design, decision, plan, or proposed approach delivers the intended
outcomes well and how it could be improved.

### Learning objective

> Does this approach meet the objective well, where does it fall short, and are there materially
> better alternatives?

### Boundary

Evaluate is outcome-bound. It may challenge important assumptions and compare credible
alternatives, but it begins from the premise that the proposed direction is a plausible design
worth assessing. It improves within or around that design; Robust may reject the design/framing
itself.

### Lens and method

- test fitness against objective, success criteria, constraints, and authorised scope;
- examine trade-offs, consequences, dependencies, and key assumptions;
- identify strengths, weaknesses, gaps, and avoidable complexity;
- compare credible alternatives where they could materially improve outcomes;
- avoid redesigning for marginal gains;
- distinguish decision input from a mandatory remedy.

### Evidence expectations

Use stated outcomes, constraints, evidence, and alternatives already considered. At higher Levels,
verify important assumptions and compare stronger external or internal approaches where available.

### Expected response

- overall assessment;
- material strengths and weaknesses;
- outcome/constraint fit;
- key trade-offs and consequences;
- credible alternatives and comparative advantage where relevant;
- recommendation or decision input;
- unresolved uncertainties.

### Defaults and continuation

- `DefaultLevel: Medium`
- `DefaultMode: Full`
- prefer `Blind` where the objective is an independent approach and exposure to the current
  solution would anchor the Reviewer;
- continue while materially different evidence, alternatives, or revised decisions are changing
  the assessment;
- complete when the Lead has sufficient decision-quality input for the Level, including an
  explicit residual uncertainty where necessary;
- change to Robust where the design/framing itself becomes the central question.

## Robust

### Purpose

Find material weaknesses normal inspection or evaluation may miss, including weaknesses caused by
the chosen design or framing itself.

### Learning objective

> Is this the right design, where can it fail or behave unexpectedly, and would a materially
> different design avoid the problem?

### Boundary

Robust is design/framing-bound. It may step back from the current design, challenge the problem
framing and foundational assumptions, and perform a blank-sheet comparison where consequence or
Findings justify it.

### Lens and method

- challenge foundational and operational assumptions;
- probe edge cases, unusual interactions, degraded states, and failure paths;
- look for hidden dependencies, second-order effects, and invalid safeguards;
- distinguish material failure modes from theoretical imperfections;
- step back and ask whether the problem is being solved in the wrong way;
- compare materially different designs when that exposes or avoids structural weakness;
- test whether added safeguards create disproportionate complexity.

### Evidence expectations

Inspect available evidence for assumptions, failure behaviour, interfaces, and safeguards. At
higher Levels, seek independent verification, precedents, or simulations where they materially
improve confidence. External threat/comparator research is not mandatory unless the objective
requires it; that is a defining Stress Test emphasis.

### Expected response

- material weaknesses/failure modes;
- trigger conditions and affected outcomes;
- evidence/reasoning and uncertainty;
- likely consequence and reach;
- challenged assumptions or framing;
- materially different design alternatives where justified;
- whether action appears proportionate; and
- residual risks or areas requiring judgment.

### Defaults and continuation

- `DefaultLevel: High`
- `DefaultMode: Full`
- use `Blind` where an independent blank-sheet framing is more valuable than direct critique;
- continue while material structural Findings, changed assumptions, or revised designs warrant
  further examination;
- substantive review-driven changes are normally returned under the High re-review posture;
- complete when material failure paths and design alternatives are adequately understood for the
  Level, not when every theoretical risk is removed.

## Stress Test

### Activation

Stress Test is user-activated only. An AI may recommend it and explain the expected value, but no
Standard, workflow, WorkPackage default, or autonomous risk trigger starts it without explicit
user direction.

### Purpose

Determine how well the subject withstands deliberate, intelligent, and sustained challenge,
including exploitation of weakness and comparison against strong external alternatives.

### Learning objective

> What could a capable adversary, competitor, hostile environment, demanding customer, auditor,
> or expert discover, exploit, outperform, or use against this?

### Boundary

Stress Test is environment/adversary-bound. It steps outside the current design to test the work
against hostile or demanding reality, known failures, credible threats, strong comparators, and
external scrutiny.

### Lens and method

- assume weaknesses will be actively sought rather than encountered accidentally;
- challenge foundational assumptions and combine weaknesses into realistic paths;
- identify plausible adversary/challenger objectives and capabilities;
- test technical, architectural, operational, commercial, process, and human surfaces selected by
  the Review objective;
- seek relevant known attacks, failures, precedents, solutions, benchmarks, and competitors;
- compare resilience against credible stronger approaches;
- distinguish theoretical possibilities from realistically exploitable/material weakness;
- identify where the subject is stronger as well as weaker;
- assess whether proposed mitigation is proportionate to the protected outcome.

### Optional Stress Test parameters

- `AdversaryOrChallenger`
- `AdversaryObjective`
- `SubjectScope`
- `ProtectedOutcomesOrAssets`
- `ChallengeSurfaces`
- `ComparatorSet`
- `Constraints`
- `AssumptionsToAttack`
- `EvidenceAccess`
- `MaterialityThreshold`

Resolve only the parameters relevant to the actual objective.

### Evidence expectations

Actively seek external examples, comparators, known failures, threat paths, benchmarks, or stronger
solutions where the Reviewer has the capability and the scope permits it. If required evidence
access is unavailable, state the limitation; do not present a speculative scan as an Extreme
Stress Test.

Research performed to support the Review remains evidence gathering inside this Review. A
standalone request to discover options or facts without the Review lifecycle belongs to Research,
not this Type.

### Expected response

- strongest material weaknesses first;
- realistic challenge/exploitation or outperformance scenarios;
- external examples/comparators and their relevance;
- consequence, likelihood/materiality, and uncertainty;
- performance of current safeguards/design against the challenge;
- comparative strengths as well as weaknesses;
- residual risks that cannot reasonably be eliminated;
- proportionate mitigation directions; and
- questions requiring user/Lead judgment.

### Defaults and continuation

- `DefaultLevel: Extreme`
- `DefaultMode: Full`
- continue while material challenge paths, combined weaknesses, comparator evidence, or material
  remediations remain insufficiently tested for Extreme confidence;
- re-review material remediations as part of the cycle;
- stop when major paths are adequately explored and dispositioned, further Findings are marginal
  or speculative, or the residual issue is an explicit strategic/risk judgment;
- never pursue complexity solely to eliminate a theoretical weakness.

## Type changes and combined objectives

Use one primary Type per Round so the request has a clear learning objective. Where a Review needs
multiple lenses:

- sequence them as separate Rounds or separate Reviews when each needs a distinct response;
- state the primary Type and a narrow secondary question where separation would add no value; or
- change Type after a Finding exposes a materially different question.

Record each Round's effective Type. Do not create hybrid names such as `Robust-Deep`; Level already
expresses intensity.

## Five-use-case defaults

| Use case | Normal starting profile | Common variation |
|---|---|---|
| Design exploration | Evaluate + Medium + Full | Blind for an independent approach; Robust when framing itself is uncertain. |
| Pre-confirmation design | Evaluate + Medium | Robust + High for foundational or hard-to-reverse design. |
| WorkPackage authoring | Check + Low or Inspect + Standard | Raise Level when incorrect scope/contract would have material downstream reach. |
| Build plan | Evaluate + Medium | Robust + High for consequential architecture or weak assumptions. |
| Post-execution | Inspect + Standard | Robust + High where implementation or design integrity requires broader challenge. |

These are starting defaults. Effective Level follows consequence, reach, reversibility, and
uncertainty; explicit work configuration or instruction may select another Type/Mode.

```yaml
MigrationSummary:
  CurrentVersion: v2
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Review_Design_v3, AIDE_Review@v3
<!-- END SOURCE: AIDE_ReviewProfiles_Standard_v2.md -->

---

<!-- BEGIN SOURCE: Capabilities_Review_Tool_Design_v3.md -->
# Capabilities Review Tool — Design

> **Version 3** (2026-09-01). Adds quarantine when Review/Round payload identity disagrees with Messaging transport correlation.

---

## §1 — Output and boundary

This Design produces one canonical **Review Tool** whose platform-independent job is:

> Execute one Review lifecycle using the Review Standard and the selected Review Profile.

The Tool orchestrates state and contracts. It does not perform the Reviewer reasoning on behalf of
the selected Reviewer, decide the substance of the Lead's work, own environment configuration, or
implement Messaging transport or platform route mechanics.

The canonical Tool carries the complete behaviour below plus capability-specific platform addenda
where later confirmed. The normal Capabilities Build flow turns it into platform contributions and
logical commands.

---

## §2 — Identity and invocation

```yaml
Tool:
  Identity: AIDE_ReviewTool@v3
  CommonName: Review
  PrimaryInvocation: review
  LogicalActions:
    - Start
    - Receive
    - Continue
    - Status
    - Complete
```

`review` starts a Review when none is active for the supplied identity/subject, or resumes the
identified Review when lifecycle state already exists.

Logical actions may render as subcommands, arguments, UI actions, or conversational intent on a
target platform. This Design does not prescribe slash-command syntax.

---

## §3 — Trigger

The Tool fires when:

- a user or Lead explicitly requests Review;
- an AI recommends Review and the recommendation is accepted;
- an applicable Standard, workflow, project rule, or WorkPackage supplies a Review Trigger;
- a consequence/risk condition owned by the current work supplies a Trigger; or
- a correlated response is returned for an active Review.

The Tool may proactively recommend Review where it detects material consequence, reach,
irreversibility, uncertainty, novelty, weak evidence, or likely value from a second view. It states
the basis and suggested Type/Level. It does not turn a recommendation into a requirement.

Stress Test is never started without explicit user direction, though the Tool may recommend it.

### Scope

```yaml
Scope:
  Context: >
    Apply when a purposeful independent assessment exchange is requested, accepted, required,
    recommended for decision, plan, artefact, implementation or outcome risk, or resumed from a
    correlated Review response.
```

---

## §4 — Purpose

Initiate, resolve, construct, route, record, continue, and conclude a proportionate independent
Review while preserving Lead ownership, scope authority, Round evidence, and Messaging/platform transport
boundaries.

---

## §5 — Inputs

The Tool accepts partial Review Input Contract values and resolves the rest according to
`AIDE_Review@v3`.

| Input | Requirement | Resolution | Confirmation posture |
|---|---|---|---|
| Review identity | Derived unless resuming | Existing correlated identity; otherwise generate a stable identity | Proceed on inference; always report |
| Trigger/source/basis/posture | Required | Explicit request, governing trigger, accepted recommendation, or ambient work rule | Proceed when authoritative; surface conflict |
| Subject | Required | Explicit target or current work context | Proceed on strong low-cost inference; otherwise ask |
| Objective | Required | Explicit question, trigger purpose, Type purpose plus work context | Confirm if materially ambiguous |
| Authorised scope | Required for directed work; otherwise resolved | WorkPackage/work directive/project boundary or explicit instruction | Confirm if scope expansion risk exists |
| Type/profile content | Required | Explicit named Type, work trigger, Profile default, or direct one-off profile instructions | Proceed where objective maps clearly; confirm consequential ambiguity |
| Level | Required | Explicit value, work configuration, profile default, then consequence assessment | Proceed with stated assessment; confirm user override only where required by governing rule |
| Mode | Required | Explicit value or profile default | Proceed unless Blind/Full choice materially changes the objective |
| Reviewer | Required before send | Explicit selection then environment resolver | Proceed on available default; report fallback |
| Review material | Required | Supplied artefacts/context plus purpose-shaped gathering | Ask only when missing material prevents useful Review |
| Response expectations | Required | Profile, direct instructions, or objective-derived | Proceed on profile/default |
| Continuation posture | Required | Type guidance plus Level re-review/stopping rules | Proceed on Standard |
| Returned response | Required for Receive | Messaging return or manual AI-MESSAGE reply | Correlate before acting; ask if ambiguous |

Inputs can be supplied incrementally across lifecycle actions. The Tool asks for genuinely missing
information in one batched request unless the user prefers sequential interaction.

---

## §6 — Preconditions

Before sending Round 1, verify:

- the Trigger posture is known;
- Subject, Objective, and AuthorisedScope are sufficiently clear;
- a named Type or DirectProfile content is complete;
- Level has been assessed against consequence, reach, reversibility, and uncertainty;
- Mode is resolved and any Blind withholding is explicit;
- Reviewer capability and independence are suitable for the effective Level;
- an available route or first-class manual relay exists;
- the Review Request is accurate, sufficient, relevant, attackable, and non-persuasive; and
- durable/transient persistence destination is known or can be determined from the work context.

Before handling a response, verify:

- Review and Round identity correlate to an active record;
- the actual Reviewer/model is known or recorded as unavailable;
- response status is identified; and
- the unchanged response can be preserved.

A failed precondition is reported. Ask where missing information can solve it; escalate where a
genuine authority, scope, independence, or conflict judgment is required.

---

## §7 — Procedure

### 1. Initiate the Review

1. Accept the Trigger or explicit request.
2. Create or locate the Review identity.
3. Record Trigger source, basis, posture, Subject, and current work authority.
4. Set lifecycle state to `Initiated`.
5. If Stress Test was selected without explicit user direction, stop at recommendation and request
   that direction.

### 2. Resolve the Review Input Contract

1. Apply direct instruction.
2. Apply trigger/work-item configuration to unresolved fields.
3. Apply Review Profile defaults.
4. Apply shared operating defaults.
5. Query environment configuration for available Reviewer/model/route facts.
6. Assess Level from consequence, reach, reversibility, and uncertainty; do not use task size as
   the primary driver.
7. Identify missing or conflicting values.
8. Infer safe values and state them; ask once for unresolved inputs; escalate genuine conflicts.
9. Record the resolved contract and any departure from profile defaults.

### 3. Resolve Reviewer, model capability, and route

1. Translate effective Level and Review needs into required Reviewer capabilities.
2. Prefer a meaningfully independent Reviewer family from the Lead where available.
3. Resolve an actual or requested model capability from environment data.
4. Resolve route from current surface plus Reviewer.
5. Apply environment fallback order where the preferred choice is unavailable.
6. Report any fallback and any reduced independence/capability.
7. If the selected Level cannot be met, obtain a lower-Level decision or escalate; do not claim the
   original Level was performed.

### 4. Gather and shape Review material

1. Locate the authoritative subject material and governing context.
2. Include constraints, assumptions, uncertainties, evidence, and success criteria needed for the
   objective.
3. Exclude unrelated material.
4. In Blind Mode, withhold the Lead's selected reasoning/solution only to the degree needed to
   reduce anchoring while preserving accuracy.
5. Record every artefact/reference supplied and any deliberate withholding.

### 5. Build the Review Request

1. Assign the next Round identity and number.
2. State Review/Round identity, Subject, Objective, AuthorisedScope, Type, Level, and Mode.
3. Translate the selected Profile into purpose, learning objective, lens/method, evidence
   expectations, and expected response.
4. Add the shaped material and specific questions.
5. Remove persuasive framing, unsupported conclusions, and unnecessary context.
6. Validate the request against the construction principles.
7. Preserve the final request and supplied-material list in the Round record before delivery.

### 6. Route or relay

1. Hand the request and identifiers to the Messaging/route implementation.
2. For a direct route, record send/delivery state and set `Awaiting Response`.
3. For an indirect/manual route, request an AI-MESSAGE envelope and provide:
   - destination Reviewer/platform;
   - requested model/capability;
   - any execution instructions;
   - a ready-to-copy message, or Markdown file when exceptionally large; and
   - exact instructions for returning the response to the active Review.
4. Preserve route state without duplicating the communication implementation.

### 7. Receive and correlate

1. Accept the returned direct response or AI-MESSAGE reply.
2. Correlate the substantive payload to exactly one Review and Round.
3. Where Messaging transport correlation is also available, compare it with the payload identity;
   positive disagreement is quarantined for clarification and is not attached/dispositioned.
4. Record actual Reviewer/model and the unchanged response.
5. Record `Complete`, `Partial`, `ClarificationNeeded`, or `Failed` response status.
6. Set lifecycle state to `Response Received` for a usable response.
7. For an uncorrelated, ambiguous, or positively cross-layer-mismatched response, hold it unchanged
   and request correlation; do not disposition it.

### 8. Surface Findings and obtain Lead disposition

1. Present material Findings to the Lead in priority order.
2. Preserve Reviewer ownership of Finding text/evidence.
3. Separate possible remedies from findings.
4. Obtain or record the Lead disposition: Accept, Decline, Defer, Supersede, Investigate, Change,
   or Escalate.
5. Record changes made or directed within AuthorisedScope.
6. Mark out-of-scope Findings and return them to the director/work owner; do not implement them.
7. Assess whether Review-driven changes materially alter the reviewed state.

The Tool does not itself own or authorise the substantive changes. Where the same AI is both Tool
handler and Lead, it acts under the Lead role and current work authority, and the Round record
keeps that role boundary visible.

### 9. Reassess Level and continuation

1. Reassess consequence, reach, reversibility, and uncertainty after material Findings/changes.
2. Record any Level escalation/de-escalation and short reason.
3. Re-resolve Reviewer/model/route for the next Round when Level or capability needs changed.
4. Apply Level-specific re-review expectations to the revised state.
5. Determine whether another Round is likely to add material value.
6. Set:
   - `Continuing` when another Round is justified;
   - `Complete` when confidence is sufficient and required re-review is done; or
   - `Escalated` when scope, authority, unresolved difference, accepted risk, or judgment requires
     user/work-owner direction.
7. Do not impose a fixed Round cap or continue for speculative/marginal imperfections.

### 10. Produce and persist the Review Result

1. Build the `ReviewResult` required by `AIDE_Review@v3`.
2. Summarise actual Reviewer/model history from all Rounds.
3. Separate material Findings, Lead dispositions, in-scope changes, re-review status,
   out-of-scope Findings, and residual risks.
4. State outcome and completion reason.
5. Store the result and reconstructable Round evidence in the surrounding record for a transient
   Review, or produce/update the durable Documentation Methodology Review artefact where required.
6. Report what needs the director/work owner's attention.

---

## §8 — Decision points

### Whether to recommend Review

Recommend when a second reasoning path has material expected value from consequence, reach,
reversibility, uncertainty, novelty, weak evidence, or impact. State the basis and suggested
Type/Level. Do not recommend automatically for every non-trivial task.

### Type selection

Select by learning objective:

```text
specific criterion → Check
existing artefact → Inspect
outcome/approach quality → Evaluate
design/framing/failure challenge → Robust
explicit adversarial/competitive/external challenge → Stress Test
```

Use a DirectProfile only when one-off profile content is supplied and no reusable Type fits. This
does not create another Type.

### Level selection

Start from the Profile default and adjust using consequence, reach, reversibility, and uncertainty.
One serious factor can justify a higher Level. Record changes from default.

### Mode selection

Use Full when the Reviewer must assess the current work. Use Blind when the objective is a more
independent approach and exposure would create anchoring. Confirm when choosing incorrectly would
materially defeat the Review purpose.

### Whether to apply change

The Lead decides. The Tool records but does not transform a Finding into an instruction. Before
adding complexity, test whether accepting risk, removing the need, or reshaping the model is
better.

### Whether re-review is required

Assess material change against the active Level. High and Extreme substantive changes normally
cannot complete without return to the Reviewer. Minor/editorial change normally does not require a
new Round.

### Whether to continue

Continue when materially useful new information is likely or required re-review remains. Complete
at sufficient confidence for Level. Escalate when the remaining issue is a scope, authority,
strategy, or accepted-risk judgment.

### Persistence mode

Use the surrounding work record when it preserves the full semantic minimum. Produce a separate
durable Review document for substantive design-side, High/Extreme, materially multi-Round,
significantly unresolved/out-of-scope, required-evidence, or explicitly requested Review.

---

## §9 — Escalation conditions

Stop and hand back when:

- authoritative Review inputs conflict;
- Required Review is declined without an identified authority to accept the exception;
- Stress Test lacks explicit user activation;
- AuthorisedScope is absent/ambiguous and Review-driven action could expand work;
- no available Reviewer/route can satisfy the effective Level or required evidence/independence;
- Lead and Reviewer remain materially apart and the difference is a judgment/risk decision;
- a proposed action lies outside scope;
- the Reviewer response cannot be correlated after reasonable clarification;
- external evidence or access essential to the selected Type/Level is unavailable; or
- environment or communication seams supply contradictory factual state.

The Tool does not resolve these through hidden fallback.

---

## §10 — Outputs and effects

The Tool produces or updates:

- a resolved Review Input Contract;
- Review lifecycle state;
- append-only Round records;
- purpose-shaped Review Requests;
- direct delivery state or a ready-to-relay AI-MESSAGE handoff;
- correlated response records;
- Finding/disposition/change/re-review records;
- Level-change history;
- a Review Result; and
- transient or durable persistence as governed by the Review Standard.

The Tool may recommend a Review or another Round. It changes substantive work only when the
current AI is acting separately as Lead under existing authority; those changes are effects of the
Lead disposition, not ownership transferred to the Tool.

The Tool does not change environment settings, communication routes, model inventories, or the
definition of a Review Profile.

---

## §11 — Reporting

Reporting verbosity does not change the Review record. Failures, fallbacks, Level changes,
out-of-scope Findings, unresolved risk, and escalation always surface.

### Minimal

- Review identity and state;
- action needed now;
- terminal outcome when complete/escalated.

### Summary (default)

- subject, Type, Level, Mode, and Reviewer;
- what was sent/received or what the user must relay;
- material Findings and disposition state;
- whether changes/re-review are outstanding;
- completion/escalation reason.

### Detailed

Summary plus:

- resolved inputs and assessment rationale;
- supplied material and withholding;
- Round-by-Round outcome;
- Level/Reviewer changes;
- in-scope/out-of-scope split.

### Verbose

Detailed plus the complete lifecycle/route state and full preserved exchanges where safe and
appropriate.

For manual relay, the destination/model/instructions and copy-ready AI-MESSAGE are always clear
regardless of verbosity.

---

## §12 — Failure handling

### Missing input

Ask once for all missing resolvable inputs. Preserve the initiated Review and resume after reply.

### Delivery failure

Preserve the exact Round request, identifiers, and route state. Retry the same delivery where safe
or resolve an alternate route without creating a new Round unless the request changes.

### Partial or clarification response

Preserve it, record status, and continue the same Review. A clarification exchange can remain in
the Round if it completes the original request; create a new Round when the Lead sends materially
new review instructions or revised work.

### Ambiguous or cross-layer correlation

Do not attach or disposition an uncorrelated/ambiguous response. When Review/Round payload identity
positively disagrees with Messaging transport correlation, quarantine it under the same rule. Request
clarification or work-owner confirmation; neither identity layer silently overrides the other.

### Model mismatch

Record requested and actual model where known. Reassess whether the actual capability satisfies
the Level. If not, reroute or escalate.

### Interrupted lifecycle

Resume from the persisted Review/Round state. Do not rebuild completed Rounds from memory or
silently resend a request whose delivery/response state is uncertain.

### Persistence failure

Do not report completion until the required Review Result and Round evidence have been preserved.
Report what remains unsaved and retain recoverable state where possible.

---

## §13 — Idempotency

The Tool is conditionally idempotent by identity and lifecycle action:

- resolving the same Review inputs without new authoritative information produces the same
  effective contract;
- rebuilding an unsent Round request from unchanged inputs produces the same substantive request;
- receiving the same correlated response does not create a duplicate Round or duplicate Finding;
- producing the Review Result from unchanged records replaces/refreshes the same result state;
- retrying delivery is safe only where the Messaging/route implementation reports that duplicate-send
  handling is safe or prior delivery is known to have failed.

The Tool never assumes an externally sent message is safe to resend. Where delivery state is
uncertain, it reports uncertainty and seeks route-specific resolution.

---

## §14 — External contracts and implementation seams

### Environment resolver

Required logical query:

```yaml
ResolveReviewer:
  CurrentSurface: <surface>
  LeadIdentity: <identity/family>
  RequiredLevel: <level>
  RequiredCapabilities: <capabilities>
  PreferredReviewer: <optional>
```

Expected factual return:

- available Reviewer(s);
- candidate/requested actual model(s);
- capabilities and independence characteristics;
- available route(s) and constraints;
- fallback order; and
- any access/usage/cost limitation relevant to execution.

The owner and storage home for this configuration are not defined here.

### Messaging and route contract

Review consumes `AIDE_Messaging` for the reusable messaging behaviours it needs:

- create a correlated AI-MESSAGE handoff for manual/indirect relay;
- process the returned AI-MESSAGE and its receipt/reconciliation evidence;
- support explicit acknowledgement/query/reconciliation where receipt state requires it; and
- preserve message identity/correlation without granting message Content special authority.

Environment/platform route implementations additionally expose direct-send/return capability,
packaging constraints and route delivery/failure state where available. A direct route may avoid a
visible AI-MESSAGE envelope while preserving Review/Round correlation.

### Build-side realisation

Platform builders decide:

- command names and syntax;
- how active Review state is stored;
- how direct tools, agents, CLIs, connectors, or UI surfaces realise delivery;
- how AI-MESSAGE copy blocks/files are presented;
- how actual model identity is captured; and
- how transient Review evidence integrates with WorkPackage Outcome or other work records.

These implementations must preserve the contracts and may not hard-code volatile mappings into the
canonical Tool.

---
Dependencies: !AIDE_DocumentationMethodology@v26, AIDE_Review@v3, Capabilities_Review_Design_v3, AIDE_Messaging@v2, AIDE_ReviewProfiles@v2
References: Capabilities_Tools_Design_v3
<!-- END SOURCE: Capabilities_Review_Tool_Design_v3.md -->

---

<!-- BEGIN SOURCE: AIDE_Review_Tool_v3.md -->
# AIDE Review — Tool

> **Identity:** `AIDE_ReviewTool@v3`
> **Common name:** Review
> **Version 3** (2026-09-01). Quarantines positive disagreement between Review/Round payload identity and Messaging transport correlation.

---

## Purpose

Initiate, resolve, construct, route, record, continue, and conclude one proportionate independent
Review lifecycle while preserving Lead ownership, authorised scope, Round evidence, and the
external communication boundary.

## Logical actions

```yaml
Tool:
  Identity: AIDE_ReviewTool@v3
  CommonName: Review
  PrimaryInvocation: review
  LogicalActions: [Start, Receive, Continue, Status, Complete]
```

Platform Build may render these actions through commands, skills, UI actions, or conversational
intent without changing their semantics.

## Trigger and Scope

Run on explicit Review request, accepted AI recommendation, governing Review Trigger, WorkPackage
Review posture, qualifying consequence/risk trigger, or receipt of a correlated response for an
active Review.

The Tool may recommend Review when consequence, reach, reversibility, uncertainty, novelty, weak
evidence, or a valuable second reasoning path makes the expected benefit material. It must not
turn recommendation into requirement. Stress Test starts only on explicit user direction.

```yaml
Scope:
  Context: >
    Apply when a purposeful independent assessment exchange is requested, accepted, required,
    recommended for material value, or resumed from a correlated Review response.
```

## Start

1. Resolve the Review Trigger, Subject, Objective, Authorised Scope, Type/profile, Level, Mode,
   Reviewer requirements, material, response expectations, and continuation posture under
   `AIDE_Review@v3`.
2. Use direct instruction, work configuration, Review Profile defaults, shared defaults, then
   environment data in that precedence.
3. Infer strong low-risk facts and state them; batch questions for genuinely missing inputs;
   escalate authoritative conflicts.
4. Resolve a meaningfully independent Reviewer/model/route from the environment. If the requested
   Level cannot be met, surface the shortfall rather than claiming it was performed.
5. Shape sufficient relevant, attackable, non-persuasive material. In Blind Mode withhold only the
   anchoring content needed to achieve the objective.
6. Create Review/Round identity and the purpose-shaped Review Request.
7. Preserve the request/material list before handing it to the `AIDE_Messaging` / resolved route.
8. Record route/delivery state and set the Review to `Awaiting Response`.

For an indirect/manual route, use `AIDE_Messaging` and provide a copy-ready request plus
exact return instructions; Review does not implement transport itself.

## Receive

1. Correlate the substantive payload to exactly one Review and Round.
2. Where Messaging transport correlation is available, compare it with the payload identity; a
   positive disagreement is quarantined and is not attached/dispositioned.
3. Preserve the response unchanged and record actual Reviewer/model.
4. Record response status: Complete, Partial, ClarificationNeeded, or Failed.
5. Hold an uncorrelated, ambiguous, or positively cross-layer-mismatched response for clarification; do not disposition it.
6. Surface material Findings to the Lead while preserving Reviewer ownership of Finding text.
7. Record Lead disposition, in-scope changes, re-review need, out-of-scope findings, and residual
   risk.

## Continue

After a usable response/change:

1. reassess consequence, reach, reversibility, and uncertainty;
2. record any Level change and reason;
3. re-resolve Reviewer/model/route if needed;
4. apply Level-specific re-review expectations;
5. continue only while another Round is likely to add material value; and
6. set `Continuing`, `Complete`, or `Escalated` without imposing a fixed Round cap.

Review discovery never silently expands authorised execution scope.

## Status

Return Review identity/state, Subject, current Type/Level/Mode, Reviewer/model/route where known,
Round count/current Round, response state, unresolved material Findings/dispositions, re-review
requirement, out-of-scope findings, and next action.

## Complete

Produce the `ReviewResult` required by `AIDE_Review@v3`: scope reviewed, effective Type/final Level/
Mode, actual Reviewer/model history, outcome, material Findings and Lead dispositions, changes,
re-review state, out-of-scope Findings, residual risks, and completion reason.

Store the result and reconstructable Round evidence in the surrounding work record for transient
Review or in a durable Documentation Methodology Review artefact where the persistence rule
requires it.

## Failure and integrity

- Required Review cannot be silently skipped; authorised exception and consequence are recorded.
- Delivery failure preserves request/route state for retry/reroute.
- Partial/clarification response keeps Review open.
- Positive disagreement between Review/Round payload identity and Messaging transport correlation is
  quarantined until clarified.
- Transport success is not substantive Review completion.
- A Finding is not resolved merely because a fix was attempted.
- Reviewer/model change is explicit in the next Round.
- Re-running status/receive handling must not duplicate Round evidence or dispositions.

```yaml
MigrationSummary:
  CurrentVersion: v3
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v26, AIDE_Review@v3, Capabilities_Review_Tool_Design_v3, AIDE_Messaging@v2, AIDE_ReviewProfiles@v2
<!-- END SOURCE: AIDE_Review_Tool_v3.md -->
