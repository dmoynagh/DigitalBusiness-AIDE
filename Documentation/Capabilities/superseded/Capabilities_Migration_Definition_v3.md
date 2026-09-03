# Migration — Capability Definition

> **Version 3** (2026-09-02). Adds the aggregate Update Tool while preserving per-artefact Migration ownership.

## Identity, purpose and boundary

**Capability:** `Migration@v2`

Provides transition declaration, discovery, execution and progress semantics.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Migration.Standard` | Standard | `AIDE_Migration@v3` | v2 |
| `Migration.Tool` | Tool | `AIDE_MigrationTool@v3` | v2 |
| `Migration.UpdateTool` | Tool | `AIDE_UpdateTool@v1` | v1 |

## Capability Release History

```text
Migration@v1
  Migration.Standard@v1 -> AIDE_Migration@v2
  Migration.Tool@v1 -> AIDE_MigrationTool@v2

Migration@v2
  Migration.Standard@v2 -> AIDE_Migration@v3
  Migration.Tool@v2 -> AIDE_MigrationTool@v3
  Migration.UpdateTool@v1 -> AIDE_UpdateTool@v1
```

This baseline adopts already-current canonical outcomes into the new Capability/Element release
model; it does not pretend those outcomes were newly changed on 2026-09-02.

## Element Release History

- `Migration.Standard@v1` — baseline adoption of `AIDE_Migration@v2`; no new semantic change asserted.
- `Migration.Tool@v1` — baseline adoption of `AIDE_MigrationTool@v2`; no new semantic change asserted.
- `Migration.Standard@v2` — clarifies aggregate-operation/per-artefact ownership and authoritative-corpus treatment in `AIDE_Migration@v3`.
- `Migration.Tool@v2` — narrows `AIDE_MigrationTool@v3` to one artefact per invocation within aggregate orchestration.
- `Migration.UpdateTool@v1` — introduces `AIDE_UpdateTool@v1` for aggregate target resolution, selection, orchestration and reporting.

## Element Production

| Element | Production inputs | LastEvaluated |
|---|---|---|
| `Migration.Standard` | Current sources/contracts identified by Definition references | 2026-09-02 release v2 |
| `Migration.Tool` | Current sources/contracts identified by Definition references | 2026-09-02 release v2 |
| `Migration.UpdateTool` | Current sources/contracts identified by Definition references | 2026-09-02 release v1 |

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
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v2, AIDE_Dependencies@v3, AIDE_Migration@v3
References: Capabilities_Migration_Design_v3, AIDE_Migration@v3, AIDE_MigrationTool@v3, AIDE_UpdateTool@v1, AIDE_DeploymentRegistryTool@v1
