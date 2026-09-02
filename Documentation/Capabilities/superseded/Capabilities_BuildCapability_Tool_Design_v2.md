# Capabilities Build Capability Tool — Design

> **Version 2** (2026-09-01). Consumes the published AIDE_ToolsProduction contract for Tool outcomes and removes duplicated/internal Tool-production ownership.

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
- applying the published Tools Production contract for Tool outcomes;
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
  Identity: AIDE_BuildCapabilityTool@v2
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
4. For a Standard outcome, execute `AIDE_StandardsProduction` against the Design.
5. For a Tool outcome, execute `AIDE_ToolsProduction` against the confirmed Design.
6. Preserve shared `AIDE_Scope`, `AIDE_Dependencies`, `AIDE_Migration`, and Review semantics exactly
   where confirmed by the Design.
7. Ensure later platform implementation has not leaked into the canonical outcome except for
   capability-specific platform addenda explicitly confirmed by Design.
8. Validate each outcome independently and the sibling set for contradiction/omission.
9. Produce the complete canonical outcome set or return production defects to the work owner.

The Tool does not repair Design by making a new substantive decision. If a required canonical
behaviour is not determined, the result is `DesignIncomplete` with the unresolved point identified.

## §7 — Tool outcome validation

For a Tool outcome, `AIDE_ToolsProduction@v1` owns the canonical Tool contract and validation rules.
Build Capability validates that the published production contract was applied successfully and that
the sibling canonical outcome set is mutually coherent; it does not maintain another copy of the
Tool structure.

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
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Design_v10, AIDE_StandardsProduction@v2, AIDE_ToolsProduction@v1
References: AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
