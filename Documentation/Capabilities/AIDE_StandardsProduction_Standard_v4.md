# AIDE Standards Production — Standard

> **Identity:** `AIDE_StandardsProduction@v4`
> **Common name:** Standards Production
> **Version 4** (2026-09-02). Adds value-based dual-audience Contents/Summary production for substantial Standards.

## Contents

- **Purpose and release rule** — inputs, Element reassessment and release/checkpoint distinction.
- **Canonical orientation** — when Standard Contents/Summary applies and what it carries.
- **Output** — validated canonical Standard plus production/release result.

## Summary

Produce or validate one canonical Standard Element from confirmed inputs without inventing meaning.
Reassessment may advance only `LastEvaluated`; semantic change produces a new Element release.
Substantial Standards receive useful Contents/Summary orientation where it improves comprehension
and navigation without duplicating the precise weighted rules.

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

## Canonical orientation

Apply `AIDE_DocumentationMethodology` and the Standards DocType rule. For a substantial canonical
Standard, provide:

- Contents — a concise semantic map of significant model/rule areas and stable locations; and
- Summary — the high-level operating model, principal rules/behaviours and important boundaries.

The detailed weighted body remains authoritative. Omit or use an equivalent structure where the
outcome is small/self-evident or the sections would add clutter, duplication or reduce usability.

## Output

Return the canonical Standard outcome plus production result, evaluated-input checkpoint and any
confirmed Element-release/history update. Do not perform platform Build/package/Deployment.

```yaml
MigrationSummary:
  CurrentVersion: v4
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v3
  Posture: None

Transition:
  Version: v4
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v2, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v3
References: Capabilities_Standards_Design_v8, AIDE_UpdateCapabilityElementsTool@v1
