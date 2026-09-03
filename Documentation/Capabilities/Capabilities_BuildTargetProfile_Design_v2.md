# Capabilities Build Target Profile — Design

> **Version 2** (2026-09-03). Clarifies producer-side RequiredReach and its evidence-feedback boundary.

## Purpose and ownership

A **Build Target Definition** states the producer-side requirements for one named deployment-facing
Capability Build output. A **Build Target Profile** groups compatible Definitions so the same
representation set can be applied consistently across several Capabilities.

Capabilities owns these specialised production semantics. Generic Build owns execution, provenance,
output identity and composition posture. AI Deployment consumes registered built results and owns
Set resolution, set-level mechanical assembly, delivery, target adapters and deployed state.

Build Targets and Deployment Targets are different:

```text
Build Target
  = what Capability Build must produce

Deployment Target
  = where/how a Deployment Output is published, installed or used
```

One Build Target output may therefore feed several Deployment Targets.

## Build Target Definition

Each Definition resolves at least:

```yaml
BuildTargetDefinition:
  Identity: <stable target identity>
  Representation: <required output representation>
  OutputRole: MemberContribution | AssembledConsumptionArtefact
  RequiredReach: [<surface or consumption reach>]
  AdditionalReach: [<optional supported reach>]
  Applicability: <default and permitted owner overrides>
  Conformance: <full requirement and permitted declared degradation>
  Tags: [<package/member selection tags>]
  VerificationInputs: [<facts downstream verification needs>]
```

The Definition describes required output meaning and acceptance, not repository paths, install
commands, accounts, credentials, refresh mechanics or runtime Target state.

`RequiredReach` means that the produced representation is required/intended to support the named
recognised Working Surface or consumption reach when its applicable platform/environment
conditions are satisfied. It is not a claim that every concrete Deployment Target is presently
configured, authorised, installable or runtime-active. Deployment failure therefore does not by
itself invalidate RequiredReach. Repeated or authoritative Deployment evidence that contradicts
the producer reach assumption is returned as design/platform-evidence feedback for reassessment.

## Profile application

A Profile may identify applicable Capabilities explicitly or by a stable governed selector. It may
also be selected by a Capability Definition or authorised Capability Build request. Resolution must
produce one unambiguous effective Profile/Definition set before Build begins.

Capability-specific overrides are delta-only and producer-owned. They may state that a target is
not applicable, strengthen requirements, or declare a permitted degradation/variation. They must
not redefine generic platform mechanics or silently weaken a Profile requirement.

## Applicability and conformance

For each selected Capability and Profile target, resolve:

- whether the target is applicable;
- whether required production support exists;
- whether full conformance is achieved;
- any explicitly permitted degradation/variation and its reason; and
- the evidence/metadata required for later verification.

`NotApplicable` is not a failed or degraded output, but it requires an explicit producer-owned
reason. An applicable required target without a valid output blocks the Package. A degraded output
is still applicable and is valid only where the governing Definition/Profile permits that
degradation and exposes it for downstream verification.

## Package result

Capability Builder produces every applicable required target as a complete output and records:

```text
Build Target identity + Definition/Profile revision
concrete output/member identity and integrity
source/Build provenance
CompositionPosture
effective Tags
reach/applicability/conformance/degradation facts
```

For the same Capability semantic release, a rebuild may create a different PackageId and therefore
a different exact downstream resolved state without creating a false Capability release.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v3, AIDE_CapabilityBuild@v4, AIDE_Build@v8
References: Capabilities_AIDECore_BuildTargetProfile_v2, AIDE_Deployment@v7
