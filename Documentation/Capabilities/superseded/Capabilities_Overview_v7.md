# Capabilities — Overview

> **Version 7** (2026-08-28). Rebuilt as the architecture review surface for the confirmed
> seven-component model. Shows current components, ownership boundaries, relationships,
> production/deployment flows, platform divergence, and migration/On-Update behaviour.
>
> Created: 2026-08-27 | Last modified: 2026-08-28

---

## Architecture at a glance

Capabilities provides reusable infrastructure for defining, applying, transitioning, packaging,
deploying, and reviewing AI-facing capabilities.

```text
Capabilities
│
├── Standards ────── standards: production + use
├── Tools ────────── invokable behaviour + commands
├── Scope ────────── applicability + platform discovery/trigger realisation
├── Dependencies ─── dependency declaration + availability/version meaning
├── Migration ────── Required Migration + On-Update transition execution
├── Deployment ───── package-to-platform distribution/publication
└── Review ────────── reusable lead/reviewer assessment
```

- Seven peer components; none is a sub-mechanism hidden inside Standards or Tools.
- Standards and Tools produce capability packages.
- Scope, Dependencies, Migration, and Review are shared services.
- Deployment consumes packages without caring which capability kind produced them.
- Platform differences are expressed as divergence from a generic design, not copied into it.

---

## Component ownership review

| Component | Owns | Consumes / hands off to | Does not own |
|---|---|---|---|
| **Standards** | Standard meaning, authoring, weights, build/package, Standards Production Standard, Standards Usage Standard | Scope, Dependencies, Migration, Review; package to Deployment | Platform publishing; dependency or trigger mechanics |
| **Tools** | Tool structure, invokable behaviour, logical commands, build/package | Scope, Dependencies, Migration where applicable, Review; package to Deployment | Shared scope model; platform publishing |
| **Scope** | Mechanical + context applicability; platform trigger/discovery rendering | Capability declarations; platform designs | Capability subject matter |
| **Dependencies** | Dependency identity/version declaration, availability checks, version-gap meaning, document dependency-footer semantics | Exposes version state to Migration; missing capability to Deployment/user | Installation; transition execution |
| **Migration** | Transition format, ordering, posture, checking and execution tools | Dependency version state; owner-authored transition instructions | Deciding content changes for another owner |
| **Deployment** | Platform preparation, distribution/publication, package consumption | Completed packages; platform designs | Build/package; capability semantics; host sync by default |
| **Review** | Lead/reviewer model, findings, response and disposition discipline | Component-specific review profiles | Owning the design under review |

### Boundary checks

- If it says **where or when something applies**, Scope owns the mechanism.
- If it says **what another artefact relies on**, Dependencies owns the declaration and meaning.
- If it says **how an existing dependent artefact moves between versions**, Migration owns the
  framework; the changed dependency's owner writes the steps.
- If it says **how a capability outcome is built and packaged**, its producer owns it.
- If it says **how a completed package reaches a platform**, Deployment owns it.
- If it says **how an independent assessment is conducted**, Review owns the shared model.

---

## Generic-to-platform outcome

```text
                     Generic Design
                           │
                           ▼
                      Base outcome
                           │
             ┌─────────────┴─────────────┐
             │                           │
      no divergence needed       Design_Platform_{Name}
             │                  (differences only)
             │                           │
             │                           ▼
             │                    Platform outcome
             │                           │
             └─────────────┬─────────────┘
                           ▼
                         package
```

- Generic Design is complete and platform-independent.
- Base outcome is built from the generic Design.
- `Design_Platform_{Name}` contains only additions, constraints, substitutions, or unavailable
  behaviour for that platform.
- Platform design applies to the base outcome, not back to the source Design.
- Contradiction or an unrealised generic intent is a design discrepancy, not a merge judgment.
- Outcomes may be documents, skills, commands, configuration, or other package content.

---

## Production and deployment

```text
CAPABILITY OWNER                              DEPLOYMENT                    HOST

Design → build → base/platform outcomes → package
                                              │
                                              ▼
                                  platform preparation → publish/distribute
                                                                       │
                                                                       ▼
                                                               pickup / update
```

### Production boundary

- Standards builds and packages Standard outcomes.
- Tools builds and packages Tool outcomes and their commands.
- Transition artefacts authored by the changed dependency's owner travel in the package.
- Review checks may run before a package crosses the boundary.
- Exact package/manifest schema remains open.

### Deployment boundary

- Input is a completed package plus the information needed to interpret it.
- Deployment selects or constructs the target-platform representation.
- Deployment publishes or distributes without reinterpreting capability meaning.
- Missing, contradictory, or unsupported package content returns to the producer.
- Host pickup/synchronisation is an external consequence unless a platform contract says
  otherwise.

### What changed from the previous model

- “Publisher” is no longer the parent organising concept.
- Build and package stay with the capability producer.
- Deployment starts at the package boundary.
- The former five-stage chain is represented as two owned flows plus a host consequence.

---

## Standards

```text
Standards Design
      ├──► Standards Production Standard
      └──► Standards Usage Standard
```

- **Production Standard** — defining, authoring, structuring, building, reviewing, and packaging
  standards.
- **Usage Standard** — how a session discovers, interprets, combines, and deviates from applicable
  standards.
- Both are generic Standards outputs.
- The Usage Standard is not AIDE-scoped; AIDE is a consumer.
- Standards declares applicability through Scope.
- Standards declares prerequisites through Dependencies.
- Standards authors any transition content caused by a new Standard version using Migration's
  formats.
- Existing weight and facilitation decisions remain part of Standards, pending child-design
  reconciliation.

---

## Tools

```text
Tool Design
├── behaviour
├── scope
├── inputs / procedure / decisions / escalation
├── outputs / reporting / failure / idempotency
└── commands
    ├── identity
    ├── purpose
    └── invocation semantics
```

- A Standard shapes decisions; a Tool provides a named invokable action.
- Commands are part of the Tool definition, not an after-the-fact platform detail.
- Platform design may alter command rendering or availability while preserving logical behaviour.
- Standards and Tools may be sibling outcomes of one source Design.
- Tools builds and packages its outcomes; Deployment publishes them.

---

## Scope

```text
Capability scope declaration
          │
          ▼
  mechanical candidate filter
          │
          ▼
   contextual applicability
          │
          ▼
Scope_Design_Platform_{Name}
          │
          ▼
platform trigger / discovery representation
```

- Mechanical scope: deterministic properties such as platform, environment, domain, artefact or
  document type, side, and tags.
- Context scope: reasoned conditions about the current activity and intended outcome.
- Capability owners state logical applicability.
- Scope owns how platforms are cued to retrieve or trigger that capability effectively.
- Platform-specific retrieval tricks stay out of Standards and Tools.

---

## Dependencies

```text
Dependent artefact
└── dependency identity + version last conformed against
                  │
                  ▼
         available dependency state
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
     missing    current    newer
       │                    │
       ▼                    ▼
 stop/report          expose gap to Migration
```

- The dependent artefact declares what it relies on.
- Declared version is the version last conformed or validated against.
- Installing a newer dependency does not silently advance the declaration.
- Dependency declaration and reference citation are distinct relationships.
- Document dependency-footer semantics move from DocMeth to Dependencies.
- DocMeth may still own the shared footer component and its non-dependency metadata.
- Dependencies detects and describes missing requirements; it does not install them.

---

## Migration and On-Update

### Change classification

| Change consequence | Transition posture | Existing artefact behaviour |
|---|---|---|
| Old state cannot safely continue for applicable work | **Required Migration** | Block/defer applicable work until migrated |
| Old state remains usable but should be altered when next modified | **On-Update** (`OnUpdate`) | Apply declared steps during the qualifying update |
| Affects only new work or requires no existing change | **No transition** | Use current dependency for future work |

- Required Migration and On-Update instructions are separate artefacts/package members.
- The owner of the changed dependency writes the transition steps.
- Migration defines their structure, sequence, posture, checking, and execution.
- Transitions run in version order.
- Dependency versions advance only after applicable transitions succeed.

### Automatic modification flow

```text
Older dependent artefact will be modified
                    │
                    ▼
      compare declared vs available versions
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
 dependency     Required      On-Update
 unavailable    Migration      pending
       │            │            │
       ▼            ▼            ▼
 stop/report    stop/defer    apply in order
                                  │
                                  ▼
                        perform requested change
                                  │
                                  ▼
                      advance dependency declaration
```

- The normal trigger is AI-oriented: editing, revising, regenerating, reviewing for update, or
  preparing a changed output.
- Merely reading or discussing an artefact does not trigger gratuitous reconciliation.
- On-Update gives the AI explicit deltas; it does not infer every change by comparing Standards.

### Explicit command set

| Command | Purpose | Critical behaviour |
|---|---|---|
| `/migrations-check` | Report pending Required Migrations | Diagnostic; does not apply them |
| `/migrations-apply` | Apply authorised Required Migrations | Follows the blocking transition path |
| `/update-doc` | Force On-Update reconciliation for target document(s) | Idempotent; stops/defers on Required Migration |

`/update-doc`:

- applies only pending On-Update transitions;
- updates dependency declarations only after success;
- makes no substantive change when already current;
- reports “no On-Update actions pending” in the no-op case;
- never downgrades a Required Migration into an On-Update action.

Automatic On-Update is the normal path. `/update-doc` is the recovery and verification path.

---

## Review

```text
Current proposal / outcome
          │
          ▼
 independent reviewer
          │
          ▼
 finding + evidence + optional remedy
          │
          ▼
 lead disposition
   ├── accept remedy
   ├── solve differently
   ├── reshape / remove need
   └── accept documented risk
```

- Review is reusable beyond AIDE and Workflow.
- Lead owns the current model and its net simplicity.
- Reviewer challenges gaps, conflicts, assumptions, regressions, and unnecessary complexity.
- A finding is evidence, not a requirement to implement the reviewer's proposed mechanism.
- Model assignment is task-specific; lead/reviewer roles are not permanently attached to one AI.
- Components may supply review profiles; Review owns the common method and disposition model.

---

## Document-methodology boundary

- Domains may define local document types for artefacts they create.
- DocMeth owns shared document types and shared document components only.
- Local recurrence across domains is a signal to consider promotion to DocMeth.
- The Capabilities architecture does not redesign DocMeth in this pass.
- Dependency-footer meaning moves to Dependencies; related DocMeth edits are review inputs.
- Package manifest and build record need not become DocMeth types merely because they are
  documents; their ownership and reuse should be decided during the separate review.
- All identified DocMeth implications are collected in `Capabilities_DocMethReviewItems` v1.

---

## Current architecture state

| Area | Current state |
|---|---|
| Parent Brief and Design | Rewritten for seven components |
| Overview | Current architecture review surface |
| Standards child design | Existing v3 retained as history/current source, revision required |
| Tools child design | Existing v1 retained as history/current source, revision required |
| Scope | Component confirmed; design pending |
| Dependencies | Component confirmed; design pending |
| Migration | Component confirmed; design pending |
| Deployment | Component confirmed; design pending |
| Review | Component confirmed; design pending |
| Shared identity/version contract | Open |
| Package/manifest schema | Open |
| Platform designs and trigger techniques | Open per platform |
| DocMeth redesign | Separate review; inputs recorded only |

---

## Architecture review questions

Use this Overview to check:

- Are all seven component responsibilities independently useful and correctly placed?
- Does any row in the ownership table duplicate another component's mechanism?
- Is every arrow between production, package, deployment, and host pickup owned by exactly one
  party?
- Can Required Migration and On-Update ever be confused by an AI or package consumer?
- Does the generic-to-platform flow permit necessary divergence without restating the base?
- Are any local document types being promoted to DocMeth before they are genuinely shared?
- Are open details truly component-level details rather than missing parent architecture?

If this Overview conflicts with the Brief, Design, or Decisions, those source documents win and
the Overview must be corrected in the same pass.

---

**Depends on:** `Capabilities_Brief` v2, `Capabilities_Design` v2,
`Capabilities_Decisions` v8.

**References:** `Capabilities_DocMethReviewItems` v1,
`Capabilities_Standards_Design` v3 (revision required),
`Capabilities_Tools_Design` v1 (revision required).

**Methodology:** v17
