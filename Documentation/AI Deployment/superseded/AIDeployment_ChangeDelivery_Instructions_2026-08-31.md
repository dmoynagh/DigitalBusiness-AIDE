# AI Deployment — Change Delivery Instructions — 2026-08-31

> Transfer/application artefact. Not an authoritative corpus master.

## Destination

Apply these changes to the AI Deployment master corpus at:

```text
AIDE/AI Deployment/
```

The current AI Deployment Binder v2/current masters are the authoritative baseline for this change.

## Replace Current

| New file | Replaces current master | Action |
|---|---|---|
| `AIDeployment_Index_v3.md` | `AIDeployment_Index_v2.md` | Replace Current; move v2 to `_superseded/`. |
| `AIDeployment_Design_v3.md` | `AIDeployment_Design_v2.md` | Replace Current; move v2 to `_superseded/`. |
| `AIDeployment_Decisions_v3.md` | `AIDeployment_Decisions_v2.md` | Replace Current; move v2 to `_superseded/`. |
| `AIDE_Deployment_Standard_v3.md` | `AIDE_Deployment_Standard_v2.md` | Replace Current; move v2 to `_superseded/`. |
| `AIDE_Deployment_Tool_v3.md` | `AIDE_Deployment_Tool_v2.md` | Replace Current; move v2 to `_superseded/`. |

## Unchanged Current master

Leave `AIDeployment_OpenAI_Reference_v2.md` current and unchanged. It remains the empirical baseline referenced by the v3 Design/Decisions and is embedded unchanged in the regenerated Binder.

## Binder change

Replace generated `AIDeployment_Binder_v2.md` with `AIDeployment_Binder_v3.md` in the AI Deployment project context/consumption location. The Binder is generated and must not be edited as a master.

Retain or move the old generated Binder according to the current Working Practices handling for superseded generated consumption artefacts.

## Standards/Tools Bundle consequence

The common generated AIDE Standards/Tools Bundle must ultimately be regenerated from current canonical masters so its AI Deployment entries use:

```text
AIDE_Deployment_Standard_v3.md
AIDE_Deployment_Tool_v3.md
```

Do **not** rebuild these entries from the older Bundle itself. This Change Delivery Package does not regenerate the cross-project Standards/Tools Bundle because that Bundle contains other standards whose update is being handled separately.

## Build Project Handoff

`AIDeployment_ProjectHandoff_Build_2026-08-31.md` is a transfer artefact for the Build project, not an AI Deployment master. Paste/deliver it into the Build project for reconciliation against the current Build Binder/current masters.

Do not modify Build masters as part of applying this AI Deployment package.

## What changed

No new Deployment mechanism was introduced. The v3 pass tightens the existing boundary so that:

- Build remains the semantic renderer/producer from current authoritative/canonical inputs;
- Deployment owns desired Set selection and target-state reconciliation;
- Deployment-time composition is only deterministic mechanical assembly of already built material;
- missing target-compatible semantic Build output is surfaced as a Build/material blocker;
- observed deployed content or older Bundles/packages are reconciliation evidence, never semantic production sources;
- canonical/source provenance, Build/package provenance and verified deployment/runtime state remain distinct; and
- Bootstrap/Profile/Contribution/Standard/Tool semantic roles are preserved through deployment.

The Standard and Tool advance to v3 with `Transition: None`; no persisted consumer-state migration is required.
