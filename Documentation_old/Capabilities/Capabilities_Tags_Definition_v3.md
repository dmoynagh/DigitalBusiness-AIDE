# Tags — Capability Definition

> **Version 3** (2026-09-03). Releases snapshot-relative generated-tag freshness and exact production checkpoints.

## Identity, purpose and boundary

**Capability:** `Tags@v2`

Provides generated classification and Boolean query semantics.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Tags.Standard` | Standard | `AIDE_Tags@v3` | v2 |

## Capability Release History

```text
Tags@v1
  Tags.Standard@v1 -> AIDE_Tags@v2

Tags@v2
  Tags.Standard@v2 -> AIDE_Tags@v3
```

This baseline adopts already-current canonical outcomes into the new Capability/Element release
model; it does not pretend those outcomes were newly changed on 2026-09-02.

## Element Release History

- `Tags.Standard@v1` — baseline adoption of `AIDE_Tags@v2`; no new semantic change asserted.
- `Tags.Standard@v2` — defines producer-freeze and immutable snapshot-relative freshness for downstream consumers.

## Element Production

```yaml
ElementProduction:
  Tags.Standard:
    EvaluatedInputs:
      Capabilities_Tags_Design: v3
      AIDE_CapabilityBuild: v4
    LastEvaluated: 2026-09-03
    Result: ReleasedElement-v2
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
References: Capabilities_Tags_Design_v3, AIDE_Tags@v3, AIDE_CapabilityBuild@v4
