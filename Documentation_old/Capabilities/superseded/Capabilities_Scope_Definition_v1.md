# Scope — Capability Definition

> **Version 1** (2026-09-02). Establishes the required current Capability Definition and baseline
> semantic release composition for the existing canonical outcomes.

## Identity, purpose and boundary

**Capability:** `Scope@v1`

Provides applicability semantics using current Tags and contextual judgment.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Scope.Standard` | Standard | `AIDE_Scope@v2` | v1 |

## Capability Release History

```text
Scope@v1
  Scope.Standard@v1 -> AIDE_Scope@v2
```

This baseline adopts already-current canonical outcomes into the new Capability/Element release
model; it does not pretend those outcomes were newly changed on 2026-09-02.

## Element Release History

- `Scope.Standard@v1` — baseline adoption of `AIDE_Scope@v2`; no new semantic change asserted.

## Element Production

| Element | Production inputs | LastEvaluated |
|---|---|---|
| `Scope.Standard` | Current sources/contracts identified by Definition references | 2026-09-02 baseline |

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

No AI Deployment Registry action is inferred. A Build request must nominate an applicable post-Build
Tool and inputs; the final Registry seam awaits AI Deployment.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v1, AIDE_Dependencies@v3, AIDE_Migration@v2
References: Capabilities_Scope_Design_v2, AIDE_Scope@v2
