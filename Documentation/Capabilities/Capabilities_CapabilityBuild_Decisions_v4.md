# Capabilities Capability Build — Decisions

> **Version 4** (2026-09-03). Records WorkPackage mapping, tag-freeze ordering and post-Build workflow state.

## D1 — Capability Build is Capabilities-owned specialisation

Generic Build supplies the framework; Capabilities supplies domain rules and executor.

## D2 — Package completeness is external

Incremental/cached/reused implementation is allowed internally; every successful selected-platform
output is complete externally.

## D3 — Force build changes Package identity, not semantic release

PackageId/integrity records a rebuilt instance without lying about Element/Capability meaning.

## D4 — Registry contract is owned by AI Deployment v5

**Status: historical v1 Registry release point; current Registry registration is governed by D13 and `AIDE_DeploymentRegistryTool@v2`.**

Capability Package is the first specialised Deployable Package. Registry publication uses `AIDE_DeploymentRegistryTool@v1`; no separate capability-only Deployment Manifest is required.

## D5 — Post-Build request and result remain outside immutable PackageId bytes

The WorkPackage carries the nominated post-Build request/intent. Registry receipt/result and
lifecycle state remain external in Outcome/Registry state so registration failure can be retried
without rewriting the package.

## D6 — Registry envelope may preserve Tags, degradation and extensions

Package/member Tags, producer-declared surface support/conformance/variation/degradation and namespaced owner-specific extensions may be carried for downstream Deployment. Their detailed Build Target/Profile policy remains separate later design.

## D7 — Build Target and Deployment Target are distinct

A Build Target defines one producer output requirement. A Deployment Target is a concrete
publication/install/runtime realisation. One built output may feed several Deployment Targets.

## D8 — Build Target Profiles are reusable producer configuration

Profiles group named Build Target Definitions and may own explicit Capability membership. A
Capability Definition/request contributes only genuine producer-specific selection or overrides.

## D9 — Applicable required targets are complete package obligations

Every applicable required Profile target must be built and validated before the Capability Package
is issued. `NotApplicable` needs an explicit reason; degradation must be permitted and reported.

## D10 — AIDE Core Profile has four contribution targets

`AIDE_Core` initially requires `ClaudePlugin`, `ClaudeBundle`, `ChatGPTBundle` and `OpenAIPlugin`
contributions for each applicable member Capability. Outputs carry the `AIDE_Core` Tag for later
Registry selection; destinations and runtime mechanics remain AI Deployment configuration.

## D11 — Specialised facts map into generic WorkPackage fields

Keep `AIDE_WorkPackage@v3`. Capability Build maps its Definition/Elements/platform/Profile/source
snapshot into Inputs; target/Package obligations into RequiredOutputs; conformance, Tags, force and
post-Build request into Constraints; and validation/return facts into Acceptance and Return.

## D12 — Generated Tags freeze at the producer Build boundary

Run or validate applicable Tag Builders against the exact resolved Build source snapshot before
Package freeze. Downstream owners consume the frozen snapshot-relative Tags and evidence rather
than regenerating them from newer producer state.

## D13 — Coordinated changes require one Release Batch

Direct registration remains valid for an independent package. Once several packages form one
coordinated producer change, use one common Open Release Batch for all participating registrations.

---
Dependencies: !AIDE_DocumentationMethodology@v27
References: Capabilities_CapabilityBuild_Design_v4, Capabilities_Decisions_v21, Capabilities_AIDECore_BuildTargetProfile_v2, AIDE_DeploymentRegistryTool@v2
