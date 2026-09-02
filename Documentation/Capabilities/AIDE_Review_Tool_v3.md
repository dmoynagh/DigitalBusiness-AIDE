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
