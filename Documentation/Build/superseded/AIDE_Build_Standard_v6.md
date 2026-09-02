# AIDE Build — Standard

> **Identity:** `AIDE_Build@v6`
> **Common name:** Build
> **Version 6** (2026-09-02). Adds specialised-Build ownership, explicit post-Build Tools and transaction guidance.
>
> **Default weight:** Requirement

---

## Purpose

Execute defined work through a WorkPackage, produce the required artefacts/state, validate the actual result, and return evidence without silently taking design authority.

## Applicability

Apply when an AI/environment is acting as the executor of a governed WorkPackage or equivalent explicitly defined Build task.

Build is behavioural. Coding agents, document/work agents and future execution environments may all implement this contract.

## Accept the handoff

Before consequential state change:

- resolve the WorkPackage and authoritative work-specific inputs;
- confirm Objective, Authorised Scope, Required Outputs and Acceptance are materially clear;
- load applicable Standards/Tools needed for the work;
- where WorkRegister mappings are supplied, resolve the mapped item IDs and covered portions;
- where one source obligation is deliberately split across multiple WorkPackages, confirm its required changes are independently identifiable and this package's `Covers` is unambiguous; and
- return `NotReady`/Blocked if a substantive design gap prevents safe execution.

A WorkRegister mapping supplies traceability to a confirmed outstanding obligation; it does not
replace the WorkPackage's own Objective, Scope, Inputs, Outputs or Acceptance. For a deliberately
split obligation, independently identifiable required changes are normally supplied by the owner as
an enumerated/bulleted set; equivalent clear prose is valid. Do not require synthetic structured
sub-obligation identifiers unless a later governing contract establishes them.

Do not use design-history material as permission to invent a result that the current handoff does not determine.

When the required output is a platform or consumption representation of governed capability material, resolve the current canonical Standard/Tool or other authoritative outcome as the semantic source. Do not use an older Bundle, generated package or deployed copy to determine current canonical meaning/version where a current authoritative source establishes otherwise.

## Plan proportionately

Establish a coherent execution sequence proportionate to the work. Trivial work need not generate ceremonial plan artefacts.

Apply configured/governing Review before execution where required or recommended.

## Execute within authority

Resolve ordinary implementation detail autonomously where it remains within scope and does not alter objective, acceptance, major architecture/policy or reserved decisions.

If execution exposes a design-level problem, stop/contain affected work and return the issue rather than adding compensating machinery without authority.

If canonical/authoritative semantics are insufficient to produce a correct derived representation, return the defect to the owning Design/capability. Do not repair it by inventing capability meaning during Build.

## Build derived representations

Where authorised, Build may render, transform, assemble or package authoritative material into target-compatible forms such as skills, plugin contributions, instruction representations, Bundle members, merged Bundles, platform-specific files or other supported representations.

For such output:

- preserve the semantics of the authoritative source;
- build only the explicitly authorised subset/composition rather than assuming the full AIDE system;
- preserve distinct upstream roles and boundaries even when a platform rendering places several artefacts in one physical package;
- do not copy full Standards/Tools into thin contributions merely for packaging convenience; and
- record the authoritative source identity/version set used sufficiently for reproducibility and provenance.

A derived representation is a consumption/build artefact, not an authoritative replacement for its sources.

## Prepare deployment-facing Build output

When the Build output is intended for AI Deployment, expose these semantic handoff facts directly or through the applicable representation/package contract:

```yaml
BuildOutputHandoff:
  SourceProvenance: <authoritative/canonical source identities and versions>
  BuildOutput:
    Identity: <identity of the concrete built artefact/package>
    Integrity: <representation-appropriate integrity evidence>
  CompositionPosture: MemberContribution | AssembledConsumptionArtefact
```

Equivalent clear representation is valid; this Standard does not require one universal manifest format.

`MemberContribution` means the supplied item is already semantically produced by Build and may be mechanically included, arranged or assembled with other built members by AI Deployment as part of target reconciliation. Mechanical assembly must not redefine the member's semantics.

`AssembledConsumptionArtefact` means Build has already produced the authorised semantic/member composition. AI Deployment may deliver/reconcile that artefact but must not treat its contents as authority to semantically rebuild or change that composition. If the semantic/member composition must change, produce another Build output.

The Build output identity/integrity must be sufficient for the concrete result to be distinguished from another build or substituted/changed payload using the mechanism appropriate to that representation or package.

## Validate the result

Test actual outputs/state against the WorkPackage Acceptance and applicable Standards. Validation evidence should be sufficient to support the returned status.

For a derived representation, validation includes confirming that the selected authoritative sources and their material semantics are represented correctly for the target form. Where a deployment-facing handoff is required, also validate that the Build output identity/integrity and composition posture describe the actual produced output.

Apply result Review where required/recommended.

## Return outcome

Return an `AIDE_WorkPackage@v3` Outcome with truthful status, work performed, outputs, validation, deviations, remaining work, out-of-scope findings and design feedback. Where the WorkPackage mapped WorkRegister obligations, return a result/evidence/remaining-work entry for each mapped obligation or covered portion. Build reports this evidence; the owning/directing process reconciles and closes the WorkRegister.

`Complete` means the defined acceptance is satisfied, not merely that execution ended.

For deployment-facing built material, include or reference the required `BuildOutputHandoff` facts so downstream Deployment does not need to infer provenance, concrete build identity or composition authority from payload structure.

## Failure and resumption

Use `Partial`, `Blocked` or `Failed` distinctly. Preserve safe successful work where appropriate and state the actual resulting state. Re-running should resume or reproduce intentionally and avoid duplicate side effects where practicable.

## Platform and Deployment boundary

Target-platform commands, plugin/skill structures, repositories, toolchains and environment mechanics belong in platform Build Standards/Tools/configuration. They may vary without changing this contract.

Build may produce a platform-compatible artefact, representation or package. Successful Build does **not** mean that artefact is installed, deployed, reconciled with a target environment or verified as runtime-usable.

AI Deployment owns target-state reconciliation, delivery/install/update/remove actions and target/runtime verification. It may mechanically assemble outputs declared `MemberContribution`; it does not semantically reconstruct an `AssembledConsumptionArtefact`. Build must not report Deployment states unless they were separately established under the governing Deployment operation.

```yaml
MigrationSummary:
  CurrentVersion: v6
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None

Transition:
  Version: v4
  Posture: None

Transition:
  Version: v5
  Posture: None
```


## Domain-specialised Build

Generic Build owns WorkPackage, execution, validation, provenance and output identity. Apply the
buildable domain's specialised Build Standard/Tools for domain semantics. Generic Build must not
reconstruct or absorb those rules.

## Post-Build actions

After successful output validation, invoke only the nominated explicit Tool with its declared
inputs. Report the post-Build result separately from production. A post-Build failure does not
misreport successful output production as absent.

Use `AIDE_PublishBuildOutputTool` for generic publication/copy to an ordinary nominated location.
Do not use it to infer or implement an AI Deployment Registry contract. That action requires the
future AI-Deployment-owned Tool.

For direct authoritative corpus editing, prefer versioned/transactional storage and coherent
multi-file semantic commits. Commit/push automation is environment configuration.

```yaml
Transition:
  Version: v6
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v27, Build_Design_v6, AIDE_Review@v3
References: AIDE_WorkPackage@v3, AIDE_StandardsProduction@v3, AIDE_PublishBuildOutputTool@v1
