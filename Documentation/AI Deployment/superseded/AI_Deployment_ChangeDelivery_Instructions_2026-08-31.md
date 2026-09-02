# AI Deployment — Change Delivery Instructions

> Change Delivery Package: `AI_Deployment_ChangeDelivery_2026-08-31.zip`
>
> Purpose: apply the Bootstrap/runtime-requirements Handoff reconciliation to the AI Deployment corpus.

## Apply to `AIDE/AI Deployment/`

### Replace Current

1. Add `AIDeployment_Index_v2.md` as the current Index.
   - Replaces `AIDeployment_Index_v1.md`.
   - Move `AIDeployment_Index_v1.md` to the project's current `_superseded/` location.

2. Add `AIDeployment_Design_v2.md` as the current Design.
   - Replaces `AIDeployment_Design_v1.md`.
   - Move `AIDeployment_Design_v1.md` to `_superseded/`.

3. Add `AIDeployment_Decisions_v2.md` as the current Decisions document.
   - Replaces `AIDeployment_Decisions_v1.md`.
   - Move `AIDeployment_Decisions_v1.md` to `_superseded/`.

4. Add `AIDE_Deployment_Standard_v2.md` as the current canonical AI Deployment Standard.
   - Replaces `AIDE_Deployment_Standard_v1.md`.
   - Canonical identity advances from `AIDE_Deployment@v1` to `AIDE_Deployment@v2`.
   - Move `AIDE_Deployment_Standard_v1.md` to `_superseded/`.

5. Add `AIDE_Deployment_Tool_v2.md` as the current canonical Deploy Tool.
   - Replaces `AIDE_Deployment_Tool_v1.md`.
   - Canonical identity advances from `AIDE_DeploymentTool@v1` to `AIDE_DeploymentTool@v2`.
   - Move `AIDE_Deployment_Tool_v1.md` to `_superseded/`.

6. Add `AIDeployment_OpenAI_Reference_v2.md` as the current empirical OpenAI Reference.
   - Replaces `AIDeployment_OpenAI_Reference_v1.md`.
   - The empirical findings are unchanged; the reissue advances its Design dependency to `AIDeployment_Design_v2` so the active Binder does not depend on a superseded Design.
   - Move `AIDeployment_OpenAI_Reference_v1.md` to `_superseded/`.


## Binder / project-context change

- Replace the current AI Deployment project-context Binder with `AIDeployment_Binder_v2.md`.
- The Binder is generated/consumption material, not a master document.
- Remove the older Binder from active project context and disposition it under the current Binder supersession/working-practice convention.

## Common Standards/Tools Bundle consequence

The currently supplied `AIDE_Bundle_StandardsTools_v3.md` contains `AIDE_Deployment@v1` and `AIDE_DeploymentTool@v1` and becomes stale for AI Deployment once this package is applied.

Do **not** hand-edit that generated Bundle as part of this package.

In the next common Standards/Tools Bundle generation pass:

- replace `AIDE_Deployment_Standard_v1.md` with `AIDE_Deployment_Standard_v2.md`;
- replace `AIDE_Deployment_Tool_v1.md` with `AIDE_Deployment_Tool_v2.md`; and
- regenerate/version the Bundle under the current Bundle workflow.

Until that Bundle is regenerated, AI Deployment projects using the v2 Binder have the new authoritative project state, while consuming projects that only carry the old common Bundle still expose the older v1 deployment contract.

## No changes required in other project masters

This reconciliation does not require edits to Core, Bootstrap, Dependencies, Capabilities or Build masters.

The Handoff's boundary is satisfied by AI Deployment changes alone:

- Dependencies remains the semantic owner of required presence;
- Bootstrap remains discovery/surfacing only;
- environment/platform configuration owns concrete target policy/authority values; and
- AI Deployment consumes those facts for policy-aware reconciliation and verification.
