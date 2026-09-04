# Build — Decisions

> **Version 5** (2026-09-01). Preserves the Build v4 boundaries and records the Review B
> clarification for deterministic-enough coverage of deliberately split WorkRegister obligations.
>
> Created: 2026-08-30 | Last modified: 2026-09-01

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

---
Dependencies: !AIDE_DocumentationMethodology@v21, Build_Design_v5
References: ProjectDesign_Design_v2, AIDE_Deployment@v4, AIDE_WorkPackage@v3
