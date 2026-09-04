# Review — Capability Definition

> **Version 2** (2026-09-02). Closes the Registry post-Build intent without changing Capability or Element semantics.

## Identity, purpose and boundary

**Capability:** `Review@v1`

Provides independent assessment semantics, Profiles and orchestration.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Review.Standard` | Standard | `AIDE_Review@v3` | v1 |
| `Review.Profiles` | Standard | `AIDE_ReviewProfiles@v2` | v1 |
| `Review.Tool` | Tool | `AIDE_ReviewTool@v3` | v1 |

## Capability Release History

```text
Review@v1
  Review.Standard@v1 -> AIDE_Review@v3
  Review.Profiles@v1 -> AIDE_ReviewProfiles@v2
  Review.Tool@v1 -> AIDE_ReviewTool@v3
```

This baseline adopts already-current canonical outcomes into the new Capability/Element release
model; it does not pretend those outcomes were newly changed on 2026-09-02.

## Element Release History

- `Review.Standard@v1` — baseline adoption of `AIDE_Review@v3`; no new semantic change asserted.
- `Review.Profiles@v1` — baseline adoption of `AIDE_ReviewProfiles@v2`; no new semantic change asserted.
- `Review.Tool@v1` — baseline adoption of `AIDE_ReviewTool@v3`; no new semantic change asserted.

## Element Production

| Element | Production inputs | LastEvaluated |
|---|---|---|
| `Review.Standard` | Current sources/contracts identified by Definition references | 2026-09-02 baseline |
| `Review.Profiles` | Current sources/contracts identified by Definition references | 2026-09-02 baseline |
| `Review.Tool` | Current sources/contracts identified by Definition references | 2026-09-02 baseline |

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

## Post-Build intent

No Registry publication is inferred automatically. A Capability Build request may nominate
`AIDE_DeploymentRegistryTool@v1` action `Register` with the configured Registry and optional open
Release Batch, or another applicable post-Build Tool/explicit none. Actual post-Build result remains
external to the immutable validated package.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
References: Capabilities_Review_Design_v3, AIDE_Review@v3, AIDE_ReviewProfiles@v2, AIDE_ReviewTool@v3, AIDE_DeploymentRegistryTool@v1
