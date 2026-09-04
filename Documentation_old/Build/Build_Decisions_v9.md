# Build — Decisions

> **Version 9** (2026-09-03). Records the generic Build boundary for named Build Targets and specialised Profiles.
>
> Created: 2026-08-30 | Last modified: 2026-09-03

## D1 — Retain Build and define it behaviourally

**Decision.** Retain **Build** as the AIDE area for objective-driven execution/creation. It is not
software compilation, coding or any particular product.

**Reason.** The common behaviour is taking defined work and producing/validating artefacts.

## D2 — WorkPackage is the principal governed handoff into Build

**Decision.** Build consumes a WorkPackage containing work-specific intent, authority, inputs,
outputs and acceptance; Build environments supply reusable implementation/platform knowledge.

## D3 — Build has bounded implementation authority

**Decision.** Build may resolve ordinary implementation detail within authorised scope but returns
objective, major scope, acceptance, architecture, policy or reserved design changes to the owner.

## D4 — Build standards describe behaviour, not products

**Decision.** Codex, Claude Code, ChatGPT Work, Claude Co-work and future systems are Build
environments/implementations. Generic Build Standards do not encode their product mechanics.

## D5 — Every executed WorkPackage returns evidence

**Decision.** Build returns an Outcome recording actual work, outputs, validation, deviations,
unresolved issues and design feedback.

## D6 — Canonical meaning remains upstream of platform/consumption representation

**Decision.** When Build renders or packages governed capability material, the current canonical
Standard/Tool or other authoritative outcome supplies semantics. Build does not reconstruct missing
meaning from Decisions history or from an older derived Bundle/package.

**Rejected alternative.** Patch an older Bundle/package forward as the production baseline.
Rejected because that would make a derived artefact authoritative by accident.

## D7 — Build preserves composability and semantic role boundaries

**Decision.** Build may produce explicitly authorised subsets/combinations without assuming one
fixed full-AIDE package. Distinct upstream semantic roles remain distinct unless an authorised
representation combines them without changing meaning.

## D8 — Build output is not Deployment state

**Decision.** Build may produce target-compatible artefacts/packages, but successful production does
not claim installation, target reconciliation or runtime availability. AI Deployment owns those
states.

## D9 — Deployment-facing Build output is identifiable and composition-typed

**Decision.** A Build output intended for AI Deployment exposes:

- authoritative source identity/version provenance;
- concrete Build-output/package identity and integrity evidence; and
- `CompositionPosture: MemberContribution | AssembledConsumptionArtefact`.

`MemberContribution` is semantically produced and may be mechanically assembled by Deployment.
`AssembledConsumptionArtefact` has Build-owned internal semantic/member composition; a composition
change requires another Build output.

**Reason.** Deployment must not infer semantic composition authority from file shape or payload
structure.

## D10 — WorkPackage can map manageable execution chunks to WorkRegister obligations

**Trigger / problem.** A confirmed Design consequence may be larger than one safe/manageable Build
unit, while one Build unit may efficiently deliver several related consequences. A one-to-one
WorkRegister/WorkPackage rule would distort either the obligation or the execution chunk.

**Decision.** `AIDE_WorkPackage@v2` permits a WorkPackage to identify some or all of one or more
WorkRegister items. One WorkRegister item may be delivered through several WorkPackages. The
mapping states the covered portion when the package does not satisfy the full obligation.

**Boundary.** WorkRegister mapping is traceability and reconciliation input. It does not replace the
WorkPackage's complete executable contract and does not grant Build authority to reinterpret Design
or the source obligation.

## D11 — Build returns mapped WorkRegister results but does not close the register

**Trigger / problem.** The directing/owning topic needs to know which part of each source obligation
was actually delivered, especially after Partial/Blocked returns. A generic Outcome summary alone
can force manual reconstruction.

**Decision.** Where the WorkPackage carries WorkRegister mappings, the Outcome reports a result for
each mapped obligation/portion, including evidence and remaining work where applicable.

The owning/directing process reconciles the source WorkRegister. Build does **not** remove or close
its rows.

**Reason.** Build owns execution evidence; the top-level topic owns the full committed consequence
and is the only place that can judge whether that obligation is fully discharged.

## D12 — Issue Build v4 and WorkPackage v2

**Decision.** Publish `AIDE_Build@v4` and `AIDE_WorkPackage@v2` with migration posture `None`.

**Reason.** The release strengthens future handoff/return traceability while preserving Build v3's
deployment-facing production contract. Historical WorkPackages do not require rewriting.

## D13 — Deliberately split obligations require independently identifiable coverage

**Trigger / problem.** Review B found that the existing many-to-many mapping permits one
WorkRegister obligation to be delivered through several WorkPackages but does not explicitly ensure
that each package's claimed portion can be distinguished deterministically enough for later
reconciliation.

**Decision.** Where one WorkRegister obligation is deliberately split across multiple WorkPackages,
the source obligation's required changes must be independently identifiable, normally as an
owner-supplied enumerated/bulleted set. Each WorkPackage `Covers` identifies the exact required
changes/portion it claims. Equivalent clear prose is valid when unambiguous.

Do not introduce structured sub-obligation identifiers merely to support the split unless later
evidence establishes that they are necessary.

**Boundary.** This clarification does not transfer WorkRegister authority to Build, replace the
self-contained WorkPackage contract, move Outcome evidence into WorkRegister, or change the existing
per-mapped-obligation Outcome result/evidence/remaining-work return.

## D14 — Issue Build v5 and WorkPackage v3

**Decision.** Publish `AIDE_Build@v5` and `AIDE_WorkPackage@v3` with migration posture `None`.

**Reason.** The release makes the accepted Review B mapping rule explicit while preserving the
existing ownership, handoff and Outcome reconciliation model. Historical WorkPackages and Outcomes
do not require rewriting.


## D15 — Domain owners own specialised Build logic

Build owns the generic framework. The semantic owner of a buildable domain owns the specialised
Standards/Tools/logic that use it; Capabilities therefore owns Capability Build.

## D16 — Post-Build actions are explicit Tools

Invoke a named owner-defined Tool only after successful validation. Report production and post-Build
action results separately.

## D17 — Build owns ordinary output publication, not Deployment Registry registration

Build publishes the generic Tool for copying/publishing validated output to a nominated ordinary
location. AI Deployment owns its future registry publish/register Tool and contract.

## D18 — Direct corpus Build prefers transactions

Use versioned/transactional storage and coherent commits where practical; leave auto-commit/push to
environment configuration.

## D19 — Issue Build v6 without changing WorkPackage v3

Publish `AIDE_Build@v6`, posture `None`. `AIDE_WorkPackage@v3` remains unchanged.

## D20 — Registry publication uses the current AI Deployment Registry Tool

**Status: historical v1 release point; current Registry registration is revised by D24.**

**Decision.** A successfully validated Deployable Package may nominate `AIDE_DeploymentRegistryTool@v1` action `Register` as its explicit post-Build action. Registry receipt/lifecycle state is returned separately and is not written back into the immutable validated package.

**Reason.** AI Deployment has now closed the Registry contract that Build v6 deliberately left pending. Naming the current owner-defined Tool removes the placeholder without changing generic Build ownership or post-Build failure semantics.

**Boundary.** `AIDE_PublishBuildOutputTool@v1` remains ordinary filesystem/repository publication only. Release Batch provides a Registry-visibility boundary and does not create a generic cross-target runtime transaction.

## D21 — Build Target is not Deployment Target

**Decision.** A named Build Target identifies a producer-side output requirement. AI Deployment
Target identifies a concrete publication/install/runtime realisation. One Build Target output may
feed several Deployment Targets.

**Reason.** Output production must not be multiplied by account, local install, project or active
session state that can drift independently after Build.

## D22 — Specialised producers own Build Target Profiles/Definitions

**Decision.** Generic Build executes resolved Target requirements and supplies generic provenance,
identity, integrity and composition posture. The semantic/buildable domain owns reusable Target
Definitions/Profiles, applicability and conformance/degradation rules.

**Reason.** These requirements are domain production semantics, not generic WorkPackage mechanics.

## D23 — Deployment-facing handoff carries exact Build Target facts

**Decision.** Where a specialised contract uses named Build Targets, the handoff identifies the
Target, governing Definition/Profile revision, concrete output identity/integrity, source/Build
provenance, composition posture and required reach/applicability/conformance/Tags facts.

**Reason.** Registry/Deployment must resolve exact compatible built contributions without inferring
their meaning from filenames or payload shape.

## D24 — Post-Build request and result are workflow state

**Decision.** The nominated post-Build Tool request/intent is carried by the WorkPackage or equivalent producer-owned Build workflow. The actual post-Build result is carried by Outcome/Registry state. Neither is immutable Deployable Package content.

**Reason.** Package bytes identify the validated Build result. Mixing later workflow intent or result into that identity creates circular mutation and makes a package's integrity depend on activity after freeze.

## D25 — Coordinated Release Batch membership is owner-defined

**Decision.** When several package registrations form one coordinated producer change, the producer/directing workflow supplies one common Open Release Batch. Generic Build carries but does not infer that grouping.

**Reason.** Coordination is a semantic/workflow fact known by the producer or director, not something derivable safely from build timing or physical co-location.

## D26 — Issue Build v9; keep WorkPackage v3 and Publish Build Output Tool v1

**Decision.** Publish `AIDE_Build@v9` with transition posture `None`. Keep `AIDE_WorkPackage@v3` and `AIDE_PublishBuildOutputTool@v1` unchanged. Current Registry registration uses `AIDE_DeploymentRegistryTool@v2`.

**Reason.** Review D remediation changes the post-Build seam but requires no new generic WorkPackage field/mechanism and no change to ordinary filesystem/repository publication semantics.

---
Dependencies: !AIDE_DocumentationMethodology@v28, Build_Design_v9
References: ProjectDesign_Design_v6, AIDE_Deployment@v7, AIDE_DeploymentRegistryTool@v2, AIDE_WorkPackage@v3, AIDE_CapabilityBuild@v4
