
# AIDE Standards Production — Standard

> **Identity:** `AIDE_StandardsProduction@v3`
> **Common name:** Standards Production
> **Version 3** (2026-09-02). Aligns Standard Element production with Capability Definition, Element releases and LastEvaluated checkpoints.

## Purpose and inputs

Produce or validate one canonical Standard Element from the current Capability Definition,
documented production inputs and applicable Scope/Dependencies/Migration contracts without inventing
meaning. Resolve Element identity/release, canonical outcome identity, prior release/history, Current
Migration and current production inputs.

## Rule

An input/document version change makes the Element potentially stale. Reassess it. If canonical
meaning is unchanged, advance only the Element Production `LastEvaluated` checkpoint. If meaning
changes, produce/validate the outcome, convert Current Migration into the immutable release entry and
confirm the next Element release. Document version and Element release are not the same.

Keep capability-reference roles distinct: Dependencies are conformance checkpoints, References are
reader/evidence pointers, and executable body references are versionless by default unless a specific
contract release is intentional.

## Output

Return the canonical Standard outcome plus production result, evaluated-input checkpoint and any
confirmed Element-release/history update. Do not perform platform Build/package/Deployment.

```yaml
MigrationSummary:
  CurrentVersion: v3
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v3
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v1, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
References: Capabilities_Standards_Design_v7, AIDE_UpdateCapabilityElementsTool@v1
