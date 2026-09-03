# AIDE Review D R1 remediation — continuation handoff

## Purpose

Continue and complete the coordinated Review D R1 remediation pass started in Codex Work mode.
Do not restart from the original binders: use the attached checkpoint as the working state and the
current project-context binders as authority for comparison.

## Authoritative baseline supplied to the originating pass

- current Capabilities project sources:
  - `Capabilities_Binder_Core_v9.md`
  - `Capabilities_Binder_StandardsTools_v6.md`
  - `Capabilities_Binder_Runtime_v4.md`
  - `Capabilities_Binder_Review_v6.md`
  - `Capabilities_Binder_Messaging_v5.md`
  - `Capabilities_Binder_Set_Index_v4.md`
  - `Capabilities_WIP_v19.md`
  - `Capabilities_WorkRegister_v19.md`
  - `Capabilities_OpenItems_v16.md`
  - `AIDE_Bundle_StandardsTools_v9.md`
- `AIDeployment_Binder_v6.md`
- `Build_Binder_v8.md`
- `ProjectDesign_Binder_v4.md`
- `WorkingPractices_Binder_v5.md`

The user confirmed that the AIDE documentation now lives in:

```text
Repository: https://github.com/dmoynagh/DigitalBusiness-AIDE
Local root: C:\Users\david\dev\repos\DigitalBusiness-AIDE
Documentation root: C:\Users\david\dev\repos\DigitalBusiness-AIDE\Documentation
```

GitHub `main` was inspected and is behind the current supplied Capabilities binders. Do not directly
overwrite the remote from its stale Capabilities baseline. Produce a repository-relative change
delivery package for application to the user's current local authoritative repo.

## Confirmed Lead dispositions being implemented

Implement the previously accepted Review D R1 remediation as one pass:

1. fixed Deployment Sets own explicit required/desired members; supply selectors only select
   eligible Registry supply; dynamic selector-defined membership must be explicit;
2. missing required fixed-Set supply blocks rather than silently shrinking the Set;
3. generated Tags are validated before Capability Package freeze against the exact Build source
   snapshot; downstream consumers use frozen snapshot-relative Tags;
4. immutable Set releases preserve required-presence facts; satisfaction is evaluated per Target;
5. Element Production uses exact evaluated-input vectors (identity + version/revision/digest plus
   evaluation date/status), not prose plus a date;
6. specialised Capability facts map into generic `AIDE_WorkPackage@v3`; do not create v4;
7. `RequiredReach` is producer representation intent under applicable conditions, not a claim of
   concrete Target success; contradictory evidence returns for ordinary reassessment;
8. coordinated multi-package producer changes require one common Open Release Batch;
9. post-Build request/intent and result are WorkPackage/Outcome workflow state, not immutable
   package content;
10. fix Build Capability migration wording, Registry Tool conformance version, Deployment Tool step
    numbering, Project Design v4/v5 transition wording, the Capability Definition dependency drift,
    and preservation of required member-level facts through mechanical assembly.

Also record the user's output feedback in Working Practices: Change Delivery instructions must
identify the target repository/root and repository-relative destinations, preserve the target tree,
and must not rely on a stale absolute path or ambiguous current working directory. The package for
this pass must include concise application instructions.

## Work already completed in the checkpoint

The checkpoint contains extracted source masters plus partially completed replacement versions.
Completed substantive edits include:

- Capabilities core model:
  - `AIDE_Capability_Standard_v3.md`
  - `Capabilities_Capability_Design_v3.md`
  - `Capabilities_Capability_Decisions_v2.md`
  - `Capabilities_BuildTargetProfile_Design_v2.md`
  - `Capabilities_AIDECore_BuildTargetProfile_v2.md`
- Capability Build:
  - `AIDE_CapabilityBuild_Standard_v4.md`
  - `Capabilities_CapabilityBuild_Design_v4.md`
  - `Capabilities_CapabilityBuild_Decisions_v4.md`
  - `AIDE_BuildCapability_Tool_v6.md`
  - `Capabilities_BuildCapability_Tool_Design_v6.md`
  - `AIDE_CapabilityBuilder_Tool_v4.md`
  - `Capabilities_CapabilityBuilder_Tool_Design_v4.md`
- Tags/Scope:
  - `AIDE_Tags_Standard_v3.md`
  - `Capabilities_Tags_Design_v3.md`
  - `AIDE_Scope_Standard_v3.md`
  - `Capabilities_Scope_Design_v3.md`
- all eight current Capability Definitions were advanced and given explicit evaluated-input vectors;
  Tags, Scope and Tools releases were advanced where semantics changed; post-Build boilerplate was
  removed from Definitions;
- Capabilities parent/live state:
  - `Capabilities_Index_v24.md`
  - `Capabilities_Brief_v14.md`
  - `Capabilities_Overview_v20.md`
  - `Capabilities_Design_v15.md`
  - `Capabilities_Decisions_v21.md`
  - `Capabilities_WIP_v20.md`
  - `Capabilities_WorkRegister_v20.md`
- AI Deployment:
  - `AIDeployment_Index_v7.md`
  - `AIDeployment_Design_v7.md`
  - `AIDeployment_Decisions_v7.md`
  - `AIDeployment_SetRelease_Design_v2.md`
  - `AIDeployment_AIDECore_Reference_v2.md`
  - `AIDE_Deployment_Standard_v7.md`
  - `AIDE_Deployment_Tool_v7.md`
  - `AIDE_DeploymentRegistry_Tool_v2.md`

The AIDE Core bundle publication path was changed to:

```text
C:\Users\david\dev\repos\DigitalBusiness-AIDE\Documentation\_deploymentPackages
```

with superseded outputs under `_deploymentPackages\_superseded`.

## Work still required

1. Review every completed edit for semantic/version/reference consistency. Correct errors rather
   than assuming the partial files are final. In particular, replace the accidental phrase
   `pencils-down Inspect R2 baseline` in `Capabilities_WIP_v20.md` with ordinary wording.
2. Finish the bounded Build pass without creating `AIDE_WorkPackage@v4`:
   - advance `Build_PostBuild_Design_v2` to v3 to state that post-Build request and result are
     workflow state outside immutable package bytes and coordinated batches are owner-defined;
   - update Build parent Index/Design/Decisions only as needed and keep historical version mentions
     historical;
   - do not treat valid old dependency checkpoints or `References:` pointers as drift;
   - determine whether `AIDE_PublishBuildOutputTool@v1` needs any semantic release (prefer no change
     unless a current executable contradiction exists).
3. Finish Project Design's accepted small correction:
   - in the replacement Design, correct the current v4/v5 transition explanation so it says v4 was
     the WorkPackage preflight correction and v5 added flexible Design contribution/hosting;
   - update Index/register only as needed; do not change `AIDE_ProjectDesign@v5` semantics unless
     evidence requires it.
4. Update Working Practices to record the change-file output feedback described above. Advance the
   Design/Decisions/Standard and Index coherently; include a concise application-instructions file
   in this delivery.
5. Check whether AI Deployment Registry Design v2 or Target Adapter Design v1 needs a replacement;
   prefer leaving unchanged if the v7 Design/Standard/Tool/Set Release documents already close the
   accepted findings.
6. Regenerate:
   - `Capabilities_Binder_Core_v10.md`
   - `Capabilities_Binder_StandardsTools_v7.md`
   - `Capabilities_Binder_Runtime_v5.md`
   - `Capabilities_Binder_Review_v7.md`
   - `Capabilities_Binder_Messaging_v6.md`
   - `Capabilities_Binder_Set_Index_v5.md`
   - next `AIDE_Bundle_StandardsTools` (expected v10)
   - `AIDeployment_Binder_v7.md`
   - next Build, Project Design and Working Practices binders according to the final changed masters.
7. Run consistency checks for stale current executable references, duplicate current identities,
   Binder manifests/hashes, step numbering and accidental post-Build intent inside package content.
8. Produce one ZIP preserving repository-relative paths under `Documentation/`, with instructions
   stating exactly which files replace/supersede which current masters and generated artefacts.
9. Return the ZIP and a succinct “what you need to do” block. Then prepare Review D R2 as
   Inspect / High / Full against the accepted R1 dispositions; do not run another Robust round.

## Checkpoint layout

```text
scripts/binder_tools.py
work/masters/capabilities/
work/masters/ai-deployment/
work/masters/build/
work/masters/project-design/
work/masters/working-practices/
```

Old extracted current masters and new candidate versions coexist. Select only the intended current
replacement version of each document when regenerating Binders. Do not edit generated Binders
directly.

