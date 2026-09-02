# Messaging — Capability Definition

> **Version 2** (2026-09-02). Reconciles post-Build Registry intent to the current AI Deployment Registry contract without changing Element semantics.

## Identity, purpose and boundary

**Capability:** `Messaging@v1`

Provides AI-MESSAGE envelope/thread/source/receipt semantics and messaging actions.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Messaging.Standard` | Standard | `AIDE_Messaging@v2` | v1 |
| `Messaging.Tool` | Tool | `AIDE_MessagingTool@v2` | v1 |

## Capability Release History

```text
Messaging@v1
  Messaging.Standard@v1 -> AIDE_Messaging@v2
  Messaging.Tool@v1 -> AIDE_MessagingTool@v2
```

This baseline adopts already-current canonical outcomes into the new Capability/Element release
model; it does not pretend those outcomes were newly changed on 2026-09-02.

## Element Release History

- `Messaging.Standard@v1` — baseline adoption of `AIDE_Messaging@v2`; no new semantic change asserted.
- `Messaging.Tool@v1` — baseline adoption of `AIDE_MessagingTool@v2`; no new semantic change asserted.

## Element Production

| Element | Production inputs | LastEvaluated |
|---|---|---|
| `Messaging.Standard` | Current sources/contracts identified by Definition references | 2026-09-02 baseline |
| `Messaging.Tool` | Current sources/contracts identified by Definition references | 2026-09-02 baseline |

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
References: Capabilities_Messaging_Design_v3, AIDE_Messaging@v2, AIDE_MessagingTool@v2, AIDE_DeploymentRegistryTool@v1
