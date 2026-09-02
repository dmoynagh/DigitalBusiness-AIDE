# Capabilities Review — Design

> **Version 1** (2026-08-29). First issuance. Defines Review as the Capabilities component for
> independent insight, substantive integrity, better decisions, and proportionate risk
> management.
>
> This document states the confirmed internal position. The stable operating contract is
> published through `AIDE_Review_Standard_v1`; reusable review methods are published through
> `AIDE_ReviewProfiles_Standard_v1`; orchestration is defined by
> `Capabilities_Review_Tool_Design_v1`.
>
> Created: 2026-08-29 | Last modified: 2026-08-29

---

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
- communication transport, direct invocation, or AI Message implementation;
- research as a distinct inter-AI behaviour;
- internal self-checking or mechanical document conformance.

### Declared outputs

This Design produces:

- `AIDE_Review_Standard_v1` — stable Review semantics and lifecycle;
- `AIDE_ReviewProfiles_Standard_v1` — the five reusable Review Types and their defaults;
- `Capabilities_Review_Tool_Design_v1` — the specification for the Review orchestration Tool.

The canonical Review Tool produced from the Tool Design is consumed by AI environments through
the normal Capabilities production and Build flow. The Tool Design remains internal; the
resulting Tool is the executable outcome.

External handlers consumed by these outputs are:

- environment configuration capable of resolving reviewer/model/route availability; and
- a communication capability capable of sending a request and returning a correlated response.

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
Communication / routing capability
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
Communication         → delivery and return transport
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

Their detailed definitions and defaults belong only in `AIDE_ReviewProfiles_Standard_v1`.

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

## §10 — Communication and routing boundary

Review owns the exchange and its state. Communication owns delivery.

Review supplies the communication capability with:

- current surface/environment;
- selected Reviewer;
- Review and Round identity; and
- completed Review Request.

The route supplies:

- send and return mechanisms;
- synchronous/asynchronous/manual posture;
- packaging, attachment, context, or size constraints; and
- delivery/response state or failure.

Route resolution is data-driven:

```text
current surface + selected Reviewer → available route
```

Review does not embed rules such as how one named platform reaches another.

Where direct communication is unavailable, the communication capability uses the existing AI
Message format as the indirect envelope. The user-facing handoff includes the destination,
requested model/capability, any execution instructions, a ready-to-copy message, and exact return
instructions. Exceptionally large requests may be supplied as a Markdown file. Review owns the
substantive request and correlation identifiers; AI Message owns the envelope.

The communication capability's permanent owner and environment settings home remain open external
architecture seams. Review does not absorb them pending that work.

---

## §11 — Response, Round, and continuation lifecycle

Every response must be attributable to a specific Review and Round before Review acts on it.

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

## §19 — External dependencies and deliberately open seams

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

### Communication capability ownership

Review requires send/receive/correlation behaviour and AI Message relay for indirect routes. The
shared communication capability may also support Research and other inter-AI behaviours. Its
permanent ownership and full contract remain separate architecture work.

### No hidden ownership transfer

Temporary platform glue used to realise Review does not transfer either seam into Review. If
future work changes Type/Level/Mode/Reviewer separation or assigns these external mechanisms to
Review, that is a parent-model change and requires explicit confirmation rather than an
implementation convenience.

---

**Depends on:** `Capabilities_Review_Decisions_v1`, `Capabilities_Design_v4`,
`Capabilities_Decisions_v10`, `DocumentationMethodology_Guide_v17`.

**References:** `Capabilities_Overview_v10`, `Capabilities_Standards_Design_v3`,
`Capabilities_Tools_Design_v1`, `AIDE_Scope_Standard_v1`,
`AIDE_Dependencies_Standard_v1`.

**Methodology:** v17
