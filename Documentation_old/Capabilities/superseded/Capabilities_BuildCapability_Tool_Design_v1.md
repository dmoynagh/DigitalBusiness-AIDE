# Capabilities Build Capability Tool — Design

> **Version 1** (2026-08-30). First issuance. Formalises `Build Capability` as the design-side
> Tool that converts confirmed Capability Design into canonical Standard/Tool outcomes without
> absorbing platform Build or Deployment.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

---

## §1 — Purpose and output

This Design produces one canonical **Build Capability Tool**.

Its job is:

```text
confirmed Capability Design
        ↓
Build Capability Tool
        ↓
canonical Standard / Tool outcome(s)
```

The Tool makes the existing production step explicit and repeatable. It applies the production
contract appropriate to each declared capability outcome and validates that the result is a
complete canonical handoff.

## §2 — Boundary

Build Capability is a **design-side canonical-production Tool**.

It owns:

- resolving the Design's declared canonical outputs;
- applying the Standards Production contract for Standard outcomes;
- applying the canonical Tool contract for Tool outcomes;
- preserving confirmed shared Scope/Dependencies/Migration/Review semantics;
- validating identity/release/output completeness; and
- producing canonical outcomes or a precise production defect report.

It does not own:

- capability design decisions or repair of incomplete Design;
- Build Config selection;
- WorkPackage creation/execution;
- target-platform skill/plugin/bundle/command implementation;
- Platform Contributions;
- Capability Package or Deployment Manifest construction; or
- Deployment Set composition/publication.

Those remain later Build/Deployment responsibilities.

## §3 — Identity and logical actions

```yaml
Tool:
  Identity: AIDE_BuildCapabilityTool@v1
  CommonName: Build Capability
  PrimaryInvocation: build-capability
  LogicalActions:
    - Build
    - Validate
    - Status
```

Platform invocation syntax is a Build-side representation detail.

## §4 — Trigger

Run when confirmed Capability Design is ready to produce/rebuild one or more canonical Standard or
Tool outcomes, or when the user/Lead asks to validate whether the Design can produce those outcomes
without reopening design.

The Tool may recommend itself when an outcome is about to be manually authored from Design and the
repeatable production contract would reduce drift.

## §5 — Inputs

Required/resolved inputs:

- target Capability Design;
- declared output set and output kinds;
- formal identity/common name for each canonical output;
- intended capability release version for each output;
- applicable canonical production contracts/shared Standards;
- previous canonical release and supported transition history where rebuilding a release line; and
- current work authority for producing the outcomes.

Release version is semantic capability state, not a file/package counter. If the intended release
identity/version is genuinely unresolved, the Tool asks/escalates rather than invents one.

## §6 — Build procedure

1. Read the confirmed Design and its declared outputs. Decisions may inform future Design changes
   but are not production input.
2. Confirm each output has one supported canonical kind: Standard or Tool.
3. Resolve formal identity and intended capability release version.
4. For a Standard outcome, execute `AIDE_StandardsProduction@v1` against the Design.
5. For a Tool outcome, apply the canonical Tool contract from `Capabilities_Tools_Design_v2`:
   identity/logical actions, trigger/Scope, purpose, inputs, preconditions, procedure, decision and
   escalation boundaries, outputs/effects, reporting, failure handling, and idempotency.
6. Preserve shared `AIDE_Scope`, `AIDE_Dependencies`, `AIDE_Migration`, and Review semantics exactly
   where confirmed by the Design.
7. Ensure later platform implementation has not leaked into the canonical outcome except for
   capability-specific platform addenda explicitly confirmed by Design.
8. Validate each outcome independently and the sibling set for contradiction/omission.
9. Produce the complete canonical outcome set or return production defects to the work owner.

The Tool does not repair Design by making a new substantive decision. If a required canonical
behaviour is not determined, the result is `DesignIncomplete` with the unresolved point identified.

## §7 — Tool outcome validation

A canonical Tool must contain enough platform-independent information to implement the same logical
action contract on any supported platform:

- stable identity/common name and logical actions;
- trigger/applicability;
- purpose;
- inputs and resolution/confirmation posture;
- preconditions;
- ordered procedure;
- explicit decision and escalation boundaries;
- outputs/effects and persistent state;
- reporting contract;
- failure/partial-completion behaviour; and
- idempotency/resumption semantics.

A Tool may orchestrate bounded declared judgment. It must not silently acquire substantive
authority absent from its Design.

## §8 — Validate action

`Validate` performs the same input/output completeness checks without producing/replacing the
canonical outcomes. Report at least:

- Design and declared output set;
- identity/release resolution;
- applicable production contract per output;
- missing/ambiguous canonical information;
- shared-contract consistency;
- cross-output contradiction; and
- Ready / NotReady result.

## §9 — Status and reporting

`Status` reports the target Design, declared outputs, current canonical output versions where
available, validation state, and next required production action.

Normal Build reporting is concise: outcomes produced, identities/releases, validation result, and
anything requiring attention. A production defect is always surfaced regardless of narration
preference.

## §10 — Idempotency

Building the same confirmed Design for the same capability release with unchanged production
contracts should produce substantively equivalent canonical outcomes. Re-running must not create a
new capability release merely because generation is repeated.

Package identity and physical platform output do not exist at this stage.

## §11 — Handoff

Successful output is the canonical capability set. The next boundary is:

```text
canonical capability
   + effective Build Config
   + Build WorkPackage
   + platform Build knowledge
        ↓
Platform Contribution(s)
```

Build Capability stops before that boundary.

---

**Depends on:** `Capabilities_Design_v6`, `Capabilities_Standards_Design_v4`,
`Capabilities_Tools_Design_v2`.

**References:** `AIDE_StandardsProduction@v1`, `AIDE_Scope@v1`, `AIDE_Dependencies@v2`,
`AIDE_Migration@v1`.

**Methodology:** v17
