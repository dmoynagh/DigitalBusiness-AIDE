# AIDE Tools Production — Standard

> **Identity:** `AIDE_ToolsProduction@v3`
> **Common name:** Tools Production
> **Version 3** (2026-09-02). Adds value-based dual-audience Contents/Summary production for substantial Tools.

## Contents

- **Purpose and canonical contract** — complete platform-independent Tool semantics.
- **Release rule** — reassessment, LastEvaluated and semantic Element release behaviour.
- **Canonical orientation and output** — Contents/Summary applicability plus returned result.

## Summary

Produce or validate one complete canonical Tool Element from confirmed behaviour without inventing
authority or leaking platform mechanics. Reassessment may advance only `LastEvaluated`; changed
semantics produce a new Element release. Substantial Tools receive useful Contents/Summary
orientation where it improves comprehension and navigation.

## Purpose and inputs

Produce or validate one complete platform-independent canonical Tool Element from the current
Capability Definition, confirmed Tool behaviour and documented production inputs. Resolve Element
identity/release, logical actions, Scope, Dependencies, Migration, prior history and Current Migration.

## Canonical Tool contract

Specify stable outcome identity/common name; actions and triggers; inputs/defaults/preconditions;
ordered procedure and decision authority; escalation; outputs/effects; reporting; failure/partial/
idempotency/resumption semantics. Do not leak generic platform mechanics or infer new authority.

## Release rule

Reassess changed inputs. If Tool meaning is unchanged, update only `LastEvaluated`. If meaning
changes, validate the new canonical outcome, convert Current Migration and confirm the next Element
release. Document version, Element release and Capability release remain distinct.

## Canonical orientation

Apply `AIDE_DocumentationMethodology` and the Tools DocType rule. For a substantial canonical Tool,
provide:

- Contents — a concise map of significant action/decision areas and stable locations; and
- Summary — intended outcome, overall flow, principal decision/effect points and constraints.

Detailed inputs, procedure, failure and idempotency sections remain authoritative. Omit or use an
equivalent structure where the Tool is small/self-evident or the sections would add clutter,
duplication or reduce usability.

## Output

Return the canonical Tool plus production/checkpoint/release result. Platform Build/package/
Deployment remain later concerns.

```yaml
MigrationSummary:
  CurrentVersion: v3
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v2, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v3
References: Capabilities_Tools_Design_v7, AIDE_UpdateCapabilityElementsTool@v1
