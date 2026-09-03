# AIDE Architecture Peer Review — Review D — Round 2 remediation verification

> Transfer-only Review request. Do not adopt as an authoritative corpus master.

**Review:** Review D — design-to-production  
**Round:** R2  
**Type:** Inspect  
**Level:** High  
**Mode:** Full

## Trigger

Review D R1 completed as a Robust / High / Full assessment. The Lead accepted a bounded set of
findings and has now applied the coordinated R1 remediation across Capabilities, AI Deployment,
Build, Project Design and Working Practices.

Because the Review level is High, the substantive Review-driven changes must survive focused
re-review before Review D completes. This is the remediation verification round. **Do not run
another Robust/blank-sheet round unless the remediated material itself exposes a new material
architectural defect.**

## Objective

Determine whether the remediated current corpus:

1. resolves the accepted R1 findings as dispositioned;
2. preserves the intended semantic ownership boundaries from Design through Build, Registry,
   Deployment Set resolution and concrete Target verification;
3. contains no remaining current executable contradiction or package/workflow state conflation;
4. preserves exact/reproducible producer and deployment evidence without adding unnecessary generic
   machinery; and
5. is now coherent enough for Review D to complete at High.

## Current authoritative R2 material

Use the **post-application current** sources, not the pre-remediation binders:

### Capabilities
- `Capabilities_Binder_Core_v10.md`
- `Capabilities_Binder_StandardsTools_v7.md`
- `Capabilities_Binder_Runtime_v5.md`
- `Capabilities_Binder_Review_v7.md`
- `Capabilities_Binder_Messaging_v6.md`
- `Capabilities_Binder_Set_Index_v5.md`
- `Capabilities_WIP_v20.md`
- `Capabilities_WorkRegister_v20.md`
- `Capabilities_OpenItems_v16.md`

### Cross-topic owners
- `AIDeployment_Binder_v7.md`
- `Build_Binder_v9.md`
- `ProjectDesign_Binder_v6.md`
- `WorkingPractices_Binder_v6.md`

The temporary `AIDE_Bundle_StandardsTools_v10.md` may be checked as a generated consumption
artefact but is not semantic authority over its current source masters/Binders.

## Accepted R1 dispositions to verify

### RD-R1-1 — fixed Set membership and supply selection
A fixed Deployment Set owns explicit required/desired members. Selectors select eligible Registry
supply for those members; selector-defined/dynamic membership is permitted only when explicitly
defined as dynamic.

Verify that missing eligible supply for a required fixed-Set member blocks candidate resolution
rather than silently shrinking the Set.

### RD-R1-2 — generated Tag freshness at Package freeze
Applicable generated Tags are run/validated against the exact resolved Build source snapshot before
Capability Package freeze. The package freezes snapshot-relative Tag state/provenance; downstream
Registry/Deployment/runtime consumers use that frozen state rather than regenerating producer Tags
against newer source.

### RD-R1-3 — immutable Set required-presence facts and Target satisfaction
An immutable Set release preserves member-level required/dependency/Migration/Scope/Tag facts or
deterministic provenance through mechanical assembly. Required-presence satisfaction is assessed
per concrete Deployment Target; a Set-level member fact does not claim every Target is satisfied.

### RD-R1-4 — exact Element Production evaluated-input vector
Current Capability Definitions carry explicit evaluated-input vectors identifying the evaluated
source/contracts by stable identity plus exact version/revision/digest as applicable, with evaluation
date/status. Prose such as “current sources identified by references” is not the production
checkpoint.

### RD-R1-5 — specialised Capability facts map into WorkPackage v3
Capability Build maps specialised Definition/Element/platform/Profile/source facts into generic
`AIDE_WorkPackage@v3` Inputs/RequiredOutputs/Constraints/Acceptance/Return. No WorkPackage v4 or
parallel specialised WorkPackage schema is introduced.

### RD-R1-6 — RequiredReach is producer representation intent
`RequiredReach` expresses producer representation intent/obligation under the applicable supported
conditions. It does not claim that a concrete Deployment Target currently succeeds. Contradictory
repeated/authoritative deployment evidence is returned for ordinary producer reassessment rather
than silently rewriting RequiredReach in Deployment.

### RD-R1-7 — coordinated producer changes share one Open Release Batch
Independent package registration may remain direct. Once several packages are defined by the
producer/directing workflow as one coordinated change, all participating registrations use one
common Open Release Batch. Build/Registry must not infer coordination solely from timing or
co-location.

### RD-R1-8 — post-Build request/result are workflow state
Post-Build request/intent is WorkPackage or equivalent producer workflow state; Registry/publication
result is Outcome/Registry state. Neither becomes immutable Capability/Deployable Package content.

### RD-R1-9 — bounded current-reference and procedure corrections
Verify the accepted corrections without treating historical references, footer conformance
checkpoints or reader `References:` pointers as current-reference drift:

- Build Capability migration wording treats v3 as the Required transition checkpoint, not a pin for
  current invocations;
- current Registry Tool is v2 and validates the v7 Deployment contract;
- Deployment Tool procedure numbering is coherent;
- Project Design records the true sequence: v4 WorkPackage preflight correction, v5 flexible Design
  contribution/hosting, v6 document orientation;
- Capability Definition dependency/reference drift is not reintroduced; and
- mechanical Deployment assembly preserves required member-level facts.

### RD-R1-10 — Change Delivery application location
Working Practices now requires material Change Delivery instructions to identify the target
repository/application root, use repository-relative destinations and preserve the target tree.
Absolute local paths are supplemental only; instructions cannot depend on stale absolute paths or
an ambiguous current working directory.

## Explicit non-findings / boundaries to preserve

- `AIDE_WorkPackage@v3` remains current; do not recommend v4 merely for these specialised facts.
- `AIDE_PublishBuildOutputTool@v1` remains the generic ordinary path/repository publication Tool.
- `AIDeployment_Registry_Design_v2` and `AIDeployment_TargetAdapter_Design_v1` remain current unless
  this Inspect finds a real executable semantic contradiction not already closed by Deployment v7.
- Valid older dependency conformance checkpoints are not stale merely because a newer release exists.
- `References:` pointers are not current executable instructions.
- `ProjectDesign_Decisions_v5` and `AIDE_ProjectDesign@v6` remain current; the Review D correction
  advanced only Project Design Index/Design documentation.

## Response requested

Return:

1. overall assessment: `Resolved`, `Resolved with minor clarification`, or `Not resolved`;
2. findings with severity/materiality and exact current source evidence;
3. explicit disposition against each R1 item above;
4. any regression introduced by remediation;
5. whether another round would add material value; and
6. whether Review D can complete at High.

Do not convert stylistic preference, historical wording or non-current references into remediation
unless they create a current semantic/executable contradiction.
