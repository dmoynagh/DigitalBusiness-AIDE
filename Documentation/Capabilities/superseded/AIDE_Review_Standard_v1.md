# AIDE Review — Standard

> **Identity:** `AIDE_Review@v1`
> **Common name:** Review
> **Version 1** (2026-08-29). First published contract for purposeful independent assessment,
> proportionate assurance, lifecycle control, and disposition.

---

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
- Review owns the exchange and its state. Communication owns delivery.
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

The standard profiles are defined only in `AIDE_ReviewProfiles@v1`:

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

Review hands an external communication capability:

```yaml
ReviewDelivery:
  CurrentSurface: <surface>
  Reviewer: <resolved reviewer>
  ReviewId: <identity>
  RoundId: <identity>
  Request: <complete review request>
```

The communication capability owns route selection, send/return mechanics, packaging constraints,
delivery state, and failures.

For indirect/manual communication, use the existing AI Message format as the envelope. Supply the
user with destination, requested model/capability, instructions, a ready-to-copy message, and exact
return instructions. Use a Markdown file where the request is exceptionally large.

Do not embed platform-to-platform routes or transport implementation in Review.

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

## Failure handling

- Preserve request, identity, and route state after delivery failure so the same Round can be
  retried or rerouted.
- Do not report delivery success as Review completion.
- Do not silently skip Required Review; record an authorised exception and accepted consequence.
- Do not mark a Finding resolved because a change was attempted.
- Do not infer permission to expand scope from a Finding.
- Surface unavailable independence/capability rather than claiming the selected Level was met.

## External seams

Review consumes but does not own:

- environment configuration for reviewer/model/route availability and local mappings; and
- a shared communication capability for direct delivery, indirect AI Message relay, and response
  return/correlation.

These seams remain explicit until their architecture owners and storage contracts are separately
confirmed.

---

**Depends on:** `Capabilities_Review_Design_v1`.

**References:** `AIDE_ReviewProfiles_Standard_v1`, `Capabilities_Design_v5`,
`Capabilities_Tools_Design_v1`, `DocumentationMethodology_Guide_v17`.

**Type:** `Standard` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
