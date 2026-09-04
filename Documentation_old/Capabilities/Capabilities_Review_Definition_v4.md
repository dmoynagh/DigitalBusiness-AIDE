# Review — Capability Definition

> **Version 4** (2026-09-03). Replaces prose production state with exact evaluated-input checkpoints.

## Identity, purpose and boundary

**Capability:** `Review@v2`

Provides independent assessment semantics, Profiles and orchestration.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Review.Standard` | Standard | `AIDE_Review@v4` | v2 |
| `Review.Profiles` | Standard | `AIDE_ReviewProfiles@v2` | v1 |
| `Review.Tool` | Tool | `AIDE_ReviewTool@v3` | v1 |

## Capability Release History

```text
Review@v1
  Review.Standard@v1 -> AIDE_Review@v3
  Review.Profiles@v1 -> AIDE_ReviewProfiles@v2
  Review.Tool@v1 -> AIDE_ReviewTool@v3

Review@v2
  Review.Standard@v2 -> AIDE_Review@v4
  Review.Profiles@v1 -> AIDE_ReviewProfiles@v2
  Review.Tool@v1 -> AIDE_ReviewTool@v3
```

This baseline adopts already-current canonical outcomes into the new Capability/Element release
model; it does not pretend those outcomes were newly changed on 2026-09-02.

## Element Release History

- `Review.Standard@v1` — baseline adoption of `AIDE_Review@v3`; no new semantic change asserted.
- `Review.Standard@v2` — defines Contents plus Review Result as the Summary-equivalent surface for substantial durable Review documents.
- `Review.Profiles@v1` — baseline adoption of `AIDE_ReviewProfiles@v2`; no new semantic change asserted.
- `Review.Tool@v1` — baseline adoption of `AIDE_ReviewTool@v3`; no new semantic change asserted.

## Element Production

```yaml
ElementProduction:
  Review.Standard:
    EvaluatedInputs: {Capabilities_Review_Design: v4, AIDE_DocumentationMethodology: v28}
    LastEvaluated: 2026-09-03
    Result: CurrentAtElementRelease-v2
  Review.Profiles:
    EvaluatedInputs: {Capabilities_Review_Design: v4, AIDE_Review: v4}
    LastEvaluated: 2026-09-03
    Result: CurrentAtElementRelease-v1
  Review.Tool:
    EvaluatedInputs: {Capabilities_Review_Tool_Design: v3, AIDE_Review: v4}
    LastEvaluated: 2026-09-03
    Result: CurrentAtElementRelease-v1
```

Update the mutable checkpoint when sources/contracts are reassessed. An input-version change does
not by itself increment an Element release; immutable release-source snapshots stay in history when
later releases are produced.

## Current Migration

None. Authoritative existing outcome migrations remain under `AIDE_Migration`. A future Element
change carries Current Migration until release confirmation.

## Platform Definition and Build Platforms

The Capability is platform-neutral. Current generic Working Surface evidence must be resolved before
a Capability Build request. Newly supported platforms are surfaced and retain designer selection
`Build: null` until explicitly decided; unsupported plus `Build:true` is blocking.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v3, AIDE_Dependencies@v3, AIDE_Migration@v3
References: Capabilities_Review_Design_v4, AIDE_Review@v4, AIDE_ReviewProfiles@v2, AIDE_ReviewTool@v3
