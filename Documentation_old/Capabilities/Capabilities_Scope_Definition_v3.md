# Scope — Capability Definition

> **Version 3** (2026-09-03). Releases snapshot-relative Machine Scope and exact production checkpoints.

## Identity, purpose and boundary

**Capability:** `Scope@v2`

Provides applicability semantics using current Tags and contextual judgment.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Scope.Standard` | Standard | `AIDE_Scope@v3` | v2 |

## Capability Release History

```text
Scope@v1
  Scope.Standard@v1 -> AIDE_Scope@v2

Scope@v2
  Scope.Standard@v2 -> AIDE_Scope@v3
```

This baseline adopts already-current canonical outcomes into the new Capability/Element release
model; it does not pretend those outcomes were newly changed on 2026-09-02.

## Element Release History

- `Scope.Standard@v1` — baseline adoption of `AIDE_Scope@v2`; no new semantic change asserted.
- `Scope.Standard@v2` — evaluates Machine Scope over the frozen Tags of an immutable artefact snapshot.

## Element Production

```yaml
ElementProduction:
  Scope.Standard:
    EvaluatedInputs:
      Capabilities_Scope_Design: v3
      AIDE_Tags: v3
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
References: Capabilities_Scope_Design_v3, AIDE_Scope@v3, AIDE_Tags@v3
