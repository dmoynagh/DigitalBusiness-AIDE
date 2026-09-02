# Capabilities Review Tool — Design

> **Version 1** (2026-08-29). First issuance. Specifies the platform-independent Tool that
> orchestrates one Review lifecycle under `AIDE_Review@v1` and
> `AIDE_ReviewProfiles@v1`.
>
> This document is the internal source for the canonical Review Tool outcome. Platform command
> rendering, packaging, direct invocation, and relay mechanics are Build-side concerns.
>
> Created: 2026-08-29 | Last modified: 2026-08-29

---

## §1 — Output and boundary

This Design produces one canonical **Review Tool** whose platform-independent job is:

> Execute one Review lifecycle using the Review Standard and the selected Review Profile.

The Tool orchestrates state and contracts. It does not perform the Reviewer reasoning on behalf of
the selected Reviewer, decide the substance of the Lead's work, own environment configuration, or
implement communication transport.

The canonical Tool carries the complete behaviour below plus capability-specific platform addenda
where later confirmed. The normal Capabilities Build flow turns it into platform contributions and
logical commands.

---

## §2 — Identity and invocation

```yaml
Tool:
  Identity: AIDE_ReviewTool@v1
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
Review while preserving Lead ownership, scope authority, Round evidence, and external transport
boundaries.

---

## §5 — Inputs

The Tool accepts partial Review Input Contract values and resolves the rest according to
`AIDE_Review@v1`.

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
| Returned response | Required for Receive | Communication return or manual AI Message reply | Correlate before acting; ask if ambiguous |

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

1. Hand the request and identifiers to the communication capability.
2. For a direct route, record send/delivery state and set `Awaiting Response`.
3. For an indirect/manual route, request an AI Message envelope and provide:
   - destination Reviewer/platform;
   - requested model/capability;
   - any execution instructions;
   - a ready-to-copy message, or Markdown file when exceptionally large; and
   - exact instructions for returning the response to the active Review.
4. Preserve route state without duplicating the communication implementation.

### 7. Receive and correlate

1. Accept the returned direct response or AI Message reply.
2. Correlate it to exactly one Review and Round.
3. Record actual Reviewer/model and the unchanged response.
4. Record `Complete`, `Partial`, `ClarificationNeeded`, or `Failed` response status.
5. Set lifecycle state to `Response Received` for a usable response.
6. For an uncorrelated or ambiguous response, hold it unchanged and request correlation; do not
   disposition it.

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

1. Build the `ReviewResult` required by `AIDE_Review@v1`.
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
- direct delivery state or a ready-to-relay AI Message handoff;
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

For manual relay, the destination/model/instructions and copy-ready AI Message are always clear
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

### Ambiguous correlation

Do not attach or disposition. Request Review/Round identity or work-owner confirmation.

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
- retrying delivery is safe only where the communication capability reports that duplicate-send
  handling is safe or prior delivery is known to have failed.

The Tool never assumes an externally sent message is safe to resend. Where delivery state is
uncertain, it reports uncertainty and seeks route-specific resolution.

---

## §14 — External contracts and open implementation seams

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

### Communication capability

Required logical behaviours:

- send a correlated request directly where a route exists;
- create a correlated AI Message handoff for manual/indirect relay;
- return delivery/awaiting/failure state;
- return or accept a correlated response; and
- expose packaging constraints and uncertain-delivery state.

The permanent communication owner and any broader Research use remain separate architecture work.

### Build-side realisation

Platform builders decide:

- command names and syntax;
- how active Review state is stored;
- how direct tools, agents, CLIs, connectors, or UI surfaces realise delivery;
- how AI Message copy blocks/files are presented;
- how actual model identity is captured; and
- how transient Review evidence integrates with WorkPackage Outcome or other work records.

These implementations must preserve the contracts and may not hard-code volatile mappings into the
canonical Tool.

---

**Depends on:** `Capabilities_Review_Design_v1`, `AIDE_Review_Standard_v1`,
`AIDE_ReviewProfiles_Standard_v1`, `Capabilities_Tools_Design_v1`.

**References:** `Capabilities_Design_v5`, `AIDE_Scope_Standard_v1`,
`DocumentationMethodology_Guide_v17`.

**Methodology:** v17
