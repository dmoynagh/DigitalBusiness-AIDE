# Standards — Capability Definition

> **Version 2** (2026-09-02). Reconciles post-Build Registry intent to the current AI Deployment Registry contract without changing Element semantics.

## Identity, purpose and boundary

**Capability:** `Standards@v1`

Defines canonical Standard production and runtime usage contracts.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Standards.Production` | Standard | `AIDE_StandardsProduction@v3` | v1 |
| `Standards.Usage` | Standard | `AIDE_StandardsUsage@v2` | v1 |

## Capability Release History

```text
Standards@v1
  Standards.Production@v1 -> AIDE_StandardsProduction@v3
  Standards.Usage@v1 -> AIDE_StandardsUsage@v2
```

This baseline adopts already-current canonical outcomes into the new Capability/Element release
model; it does not pretend those outcomes were newly changed on 2026-09-02.

## Element Release History

- `Standards.Production@v1` — baseline adoption of `AIDE_StandardsProduction@v3`; no new semantic change asserted.
- `Standards.Usage@v1` — baseline adoption of `AIDE_StandardsUsage@v2`; no new semantic change asserted.

## Element Production

| Element | Production inputs | LastEvaluated |
|---|---|---|
| `Standards.Production` | Current sources/contracts identified by Definition references | 2026-09-02 baseline |
| `Standards.Usage` | Current sources/contracts identified by Definition references | 2026-09-02 baseline |

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

No Registry publication is inferred automatically. A Capability Build request may nominate `AIDE_DeploymentRegistryTool@v1` action `Register` with the configured Registry and optional open Release Batch, or nominate another applicable post-Build Tool/explicit none. Actual post-Build result remains external to the immutable validated package and is reported through Registry state/WorkPackage Outcome. This Definition update does not by itself change the Capability or Element semantic release.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v1, AIDE_Dependencies@v3, AIDE_Migration@v2
References: Capabilities_Standards_Design_v7, AIDE_StandardsProduction@v3, AIDE_StandardsUsage@v2, AIDE_DeploymentRegistryTool@v1
