# AIDE Closure — File Placement and Project Loading

Generated: 2026-08-30

## Operating model

The filesystem/GPT Project folders are **working context containers**. They are intentionally
allowed to be more granular than the conceptual AIDE ownership tree.

This resolves two otherwise awkward cases:

- canonical topic **Project Design** lives in the physical/GPT Project folder `Design Project`;
- Documentation Methodology and AI Deployment each have dedicated GPT Projects because their
  context is substantial, even though they participate in broader design/environment concerns.

## Where each file goes

### `AIDE/Core/` — GPT Project: Core

Copy current files:
- `Core_Index_v1.md`
- `Core_System_Design_v4.md`
- `Core_System_Decisions_v3.md`

Project context:
- `Core_Binder.md`
- common `AIDE_Bundle_StandardsTools_v1.md`

Move existing prior issued versions to `Core/superseded/`:
- `Core_System_Design_v3.md`
- `Core_System_Decisions_v2.md`

### `AIDE/Design Project/` — GPT Project: Design Project

Canonical topic name: **Project Design**.

Copy current files:
- `ProjectDesign_Index_v1.md`
- `ProjectDesign_Design_v1.md`
- `ProjectDesign_Decisions_v1.md`
- `AIDE_ProjectDesign_Standard_v1.md`

Project context:
- `ProjectDesign_Binder.md`
- common `AIDE_Bundle_StandardsTools_v1.md`

### `AIDE/Build/` — GPT Project: Build

Copy current files:
- `Build_Index_v1.md`
- `Build_Design_v1.md`
- `Build_Decisions_v1.md`
- `Build_WorkPackage_Design_v1.md`
- `AIDE_Build_Standard_v1.md`
- `AIDE_WorkPackage_Standard_v1.md`

Project context:
- `Build_Binder.md`
- common `AIDE_Bundle_StandardsTools_v1.md`

### `AIDE/Capabilities/` — GPT Project: Capabilities

Replace current master versions with:
- `Capabilities_Index_v14.md`
- `Capabilities_Brief_v7.md`
- `Capabilities_Overview_v13.md`
- `Capabilities_Design_v8.md`
- `Capabilities_Decisions_v14.md`
- `Capabilities_WorkRegister_v12.md`
- `Capabilities_OpenItems_v14.md`
- `Capabilities_DocMethReviewItems_v4.md`

Move the corresponding previous versions to `Capabilities/superseded/`.

Project context:
- `Capabilities_Binder_Core.md`
- `Capabilities_Binder_Work.md`
- `Capabilities_Binder_StandardsTools.md`
- `Capabilities_Binder_Runtime.md`
- `Capabilities_Binder_Review.md`
- common `AIDE_Bundle_StandardsTools_v1.md`

`Capabilities_Binder_Set_ReadMe.md` is a local helper/readme, not required as GPT Project context.

### `AIDE/AI Deployment/` — GPT Project: AI Deployment

Copy current files:
- `AIDeployment_Index_v1.md`
- `AIDeployment_Design_v1.md`
- `AIDeployment_Decisions_v1.md`
- `AIDeployment_OpenAI_Reference_v1.md`
- `AIDE_Deployment_Standard_v1.md`
- `AIDE_Deployment_Tool_v1.md`

Project context:
- `AIDeployment_Binder.md`
- common `AIDE_Bundle_StandardsTools_v1.md`

### `AIDE/Document Methodology/` — GPT Project: Document Methodology

Copy/update:
- `DocumentationMethodology_Index_v1.md`
- `DocumentationMethodology_Decisions_v14.md`
- `DocumentationMethodology_Guide_v18.md`

If your existing DocMeth master folder contains unchanged internal Design/history documents, keep
them; this package does not replace files that were not part of the supplied/current corpus.

Move `DocumentationMethodology_Guide_v17.md` to `Document Methodology/superseded/`.

Project context:
- `DocumentationMethodology_Binder.md`
- common `AIDE_Bundle_StandardsTools_v1.md`

### `AIDE/bundles/`

Store generated:
- `AIDE_Bundle_StandardsTools_v1.md`

This file is a consumption artefact, not an authoritative master. Regenerate it whenever a
canonical AIDE Standard or Tool changes.

## GPT Project loading pattern

For each GPT Project:

1. Add its Binder(s).
2. Add `AIDE_Bundle_StandardsTools_v1.md`.
3. Do not add the same individual master files as well unless temporarily debugging context;
   Binder + Bundle are the normal consumption surface.

## Important v18 migration rule

Documentation Methodology v18 is **OnUpdate**. Do not mass-edit unchanged v17 documents merely
to replace `Methodology: v17`. When an existing document is next modified/saved, apply the v18
metadata/dependency transition as part of that update.

## Deferred follow-up, not an operational blocker

- broader hosted/account/public OpenAI deployment routes;
- Claude/other target adapters and empirical verification details;
- general Environment configuration/storage architecture beyond the facts consumed here;
- shared inter-AI communication ownership;
- richer temporary-state schema unless demonstrated necessary.
