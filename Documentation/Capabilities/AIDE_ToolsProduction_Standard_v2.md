
# AIDE Tools Production — Standard

> **Identity:** `AIDE_ToolsProduction@v2`
> **Common name:** Tools Production
> **Version 2** (2026-09-02). Aligns Tool Element production with Capability Definition, Element releases and LastEvaluated checkpoints.

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

## Output

Return the canonical Tool plus production/checkpoint/release result. Platform Build/package/
Deployment remain later concerns.

```yaml
MigrationSummary:
  CurrentVersion: v2
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v2
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v1, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
References: Capabilities_Tools_Design_v4, AIDE_UpdateCapabilityElementsTool@v1
