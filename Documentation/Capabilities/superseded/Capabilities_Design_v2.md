# Capabilities — Design

> **Version 2** (2026-08-28). Parent architecture rewrite. Establishes Standards, Tools, Scope,
> Dependencies, Migration, Deployment, and Review as peer components; replaces the publisher-
> centred production model with separate production and deployment flows; and defines Required
> Migration and On-Update as distinct transition postures.
>
> This document states the current position. Historical and superseded positions remain in
> `Capabilities_Decisions` v8.
>
> Created: 2026-08-27 | Last modified: 2026-08-28

---

## §1 — Scope

This design defines the parent architecture for reusable AI-facing capability infrastructure.
It establishes component responsibilities, their contracts, and the principal flows between
them. It is platform-agnostic.

Each component develops its own detailed design beneath this parent. A component design may add
internal structure, but it may not silently take ownership assigned to another component here.

---

## §2 — Architectural model

Capabilities is a system of seven cooperating components:

```text
Capabilities
├── Standards
├── Tools
├── Scope
├── Dependencies
├── Migration
├── Deployment
└── Review
```

The components are not a processing sequence. Standards and Tools create different capability
outcomes; Scope, Dependencies, Migration, Deployment, and Review are shared services used across
capability kinds and, where applicable, by other domains.

A concern becomes a component when it provides independently useful behaviour consumed by
multiple capability kinds or domains. Shared contracts remain at the parent level until their
own size and independent behaviour justify a component; the exact common identity/version and
package-manifest schemas are intentionally not promoted to further components at this stage.

### Governing principles

- **One owner per mechanism.** A consumer declares or invokes shared behaviour; it does not
  redefine it.
- **Generic meaning before platform rendering.** The base design says what must be true;
  platform design states only divergence needed to make it true on a named platform.
- **Production before deployment.** Builders create and package outcomes. Deployment distributes
  completed packages.
- **Declared transitions before inferred deltas.** The owner of a changed dependency expresses
  required downstream changes once; consumers do not reconstruct version differences ad hoc.
- **Review findings are evidence.** The lead remains responsible for the net architecture and
  may reshape or remove a need instead of adding machinery for every finding.

---

## §3 — Common design-to-outcome convention

Every capability kind uses the same platform-divergence pattern:

```text
Generic Design
      │
      ▼
Base outcome
      │
      ├── no platform divergence ───────────────► deployable outcome
      │
      └── apply Design_Platform_{Name}
                         │
                         ▼
                  Platform outcome
```

The generic Design is the complete current position independent of any platform. The base
outcome is built from that Design. A `Design_Platform_{Name}` contains only differences from the
generic design: additions, constraints, substitutions, or unavailable behaviour for that
platform. Applying it to the base outcome produces the platform outcome.

The platform design does not restate the generic design and may not contradict its intent. If a
platform cannot realise the generic intent, that is a design discrepancy to resolve explicitly,
not an invitation for a builder or deployer to invent behaviour.

The prior four-layer terminology of “agnostic document” and “platform document” is absorbed by
this convention. Outcomes need not be documents, and the convention therefore uses the broader
terms base outcome and platform outcome.

---

## §4 — Standards

### Responsibility

Standards defines what a Standard is and how standards are designed, authored, structured,
weighted, built, packaged, and used by an AI session. A Standard shapes what a session considers
or decides; it is not an invokable action.

Standards owns standard-specific production through the completed standard package. It uses
Scope to declare applicability, Dependencies to declare prerequisites, Migration to publish any
transitions caused by a new version, Review to assess its design and outputs, and Deployment to
distribute the completed package.

### Published standards

Standards publishes two generic standards under its own ownership:

- **Standards Production Standard** — how a standard is defined, authored, structured, built,
  reviewed, and packaged.
- **Standards Usage Standard** — how a session discovers and operates under applicable standards,
  including weights, conflict and deviation behaviour, and unavailable required standards.

The Standards Usage Standard is generic. It is not an AIDE-scoped standard and is not owned by
AIDE merely because AIDE is one consumer.

### Boundary

Standards declares logical scope but Scope owns the applicability model and its platform
realisation. Standards declares dependencies but Dependencies owns their syntax and runtime
meaning. Standards authors transition instructions for changes it introduces, while Migration
owns their form and execution. Standards builds and packages; it does not publish to platforms.

---

## §5 — Tools

### Responsibility

Tools defines invokable capability behaviour. A tool removes the need to decide where a defined
procedure can be executed reliably and repeatedly. It carries identity, purpose, scope, inputs,
preconditions, procedure, decision points, escalation, outputs, reporting, failure handling,
and idempotency.

Tools owns tool-specific production through the completed tool package. It consumes the same
shared components as Standards where applicable.

### Commands

A Tool design includes the logical commands or invocations the tool contributes. For each
command it states at least:

- command identity;
- purpose;
- invocation semantics and target inference;
- relationship to the tool's other commands, if any.

Platform design may change the concrete rendering, name, or availability needed on that
platform, but the command's logical behaviour is defined by Tools before platform realisation.

### Boundary with standards

A standard may describe a procedure but may not define a named invokable action. If an action is
run, it is a Tool and its commands are defined with it. A single source Design may produce
sibling standards and tools where one body of behaviour needs both consideration and invocation;
neither outcome becomes the source of the other.

---

## §6 — Scope

### Responsibility

Scope answers: **should this capability be considered or applied in this context?**

It owns the generic applicability model used by Standards, Tools, and other eligible artefacts.
The current model has two layers:

1. **Mechanical scope** — deterministic facts and declared properties that can be checked
   without judgment, such as platform, environment, domain, artefact type, document type, side,
   or tag.
2. **Context scope** — reasoned conditions about the activity and intended outcome.

Mechanical scope filters candidates; context scope determines whether a candidate is relevant to
the work occurring. A capability author declares where its capability applies. Scope defines how
that declaration is interpreted.

### Platform trigger and discovery realisation

Scope also owns translation of generic applicability into effective platform cues. A generic
scope declaration remains stable while `Scope_Design_Platform_{Name}` defines how the target
platform should express triggers, descriptions, metadata, or retrieval cues.

This keeps platform retrieval techniques out of individual Standard and Tool designs. It also
allows the same logical capability to be discovered differently on different platforms without
changing its meaning.

---

## §7 — Dependencies

### Responsibility

Dependencies answers: **what must be available, and against what version was this artefact last
conformed or validated?**

It owns:

- dependency identity and version declaration;
- the semantic distinction between a dependency and a non-obligating reference;
- runtime availability checks;
- comparison of an artefact's declared dependency version with the available version;
- when a dependency declaration may be advanced;
- the dependency region and dependency line used in document footers.

The dependent artefact declares its own dependencies because it knows what it relies on. A
declared version is a historical conformance fact, not a claim that the installed dependency is
still current. Installing a newer dependency does not automatically rewrite the declaration.

### Runtime behaviour

Before substantive use that requires a declared dependency, the session determines whether the
dependency is available. If it is unavailable, substantive work stops and the missing dependency
is reported. Dependencies identifies the requirement; it does not install or deploy it.

When the available dependency is newer than the declared version, Dependencies exposes the
version gap to Migration. The declaration advances only after all applicable transitions for
the target state have succeeded and the artefact has been conformed or validated.

### Document boundary

DocMeth may define a shared footer as a document component and use the Dependencies Standard
within it. It does not define dependency meaning merely because documents are one carrier. The
location and rendering of non-dependency document metadata remain DocMeth concerns unless moved
by a later DocMeth review.

---

## §8 — Migration

### Responsibility

Migration owns defined transitions of dependent artefacts from one dependency version state to
another. It supplies the transition formats, ordering rules, execution postures, checks, and
tools. The owner of the dependency that changed authors the actual transition instructions.

Every relevant change is classified as one of three cases:

- **Required Migration** — the existing dependent artefact cannot safely remain in its old state
  for the applicable work. The transition blocks that work until applied or explicitly deferred.
- **On-Update transition** (`OnUpdate` in identifiers) — the existing artefact remains usable,
  but when it is next modified the declared steps bring it forward.
- **No transition** — the change affects only new work or does not require an existing artefact
  to change.

Required Migration and On-Update instructions are stored as separate artefacts or unequivocally
separate package members. They are not mixed in one transition file. Exact filenames are a
component-design decision; separation and machine-discernible posture are parent requirements.

### Automatic On-Update path

The normal On-Update trigger is AI-oriented. When an artefact is being edited, revised,
regenerated, reviewed for update, or prepared for a changed output, and one of its declared
dependency versions is older than the available version, the session checks for applicable
On-Update transitions.

Applicable transitions run in version order. They complement the requested modification rather
than asking the AI to reinterpret every newer Standard and reconstruct the delta. A version gap
alone does not authorise gratuitous rewriting when the artefact is merely being read or
discussed.

### Explicit tools

Migration defines at least these logical commands:

- **`/migrations-check`** — identify and report pending Required Migrations.
- **`/migrations-apply`** — apply authorised Required Migrations in their defined order.
- **`/update-doc`** — force an On-Update reconciliation check on one or more target documents.

`/update-doc` is idempotent by design. It applies only pending On-Update transitions, advances
dependency declarations only after successful transition, and makes no substantive change when
the target is already current. In that case it reports that no On-Update actions were pending.

If `/update-doc` encounters a Required Migration, it stops or defers that target and reports the
required path. It never silently treats blocking work as On-Update. Automatic On-Update
triggering is the normal path; `/update-doc` is the explicit verification and recovery path when
the automatic trigger may have been missed.

---

## §9 — Deployment

### Responsibility

Deployment accepts a completed capability package and realises it for a target platform. Its
generic interface does not depend on whether Standards, Tools, or another producer created the
package.

The architecture separates two flows:

```text
CAPABILITY PRODUCTION
Design → build → package

CAPABILITY DEPLOYMENT
package → platform preparation → distribute/publish

HOST CONSEQUENCE
published release → host pickup/update
```

Standards and Tools own build and package for their outcomes. Deployment owns platform
preparation and distribution/publication. Host pickup or synchronisation is external to the AI
workflow unless a platform contract explicitly brings it into scope.

Deployment consumes a package contract that identifies contents, versions, platform
applicability, transition artefacts, and removals as needed. The exact manifest schema and shared
identity/version contract remain open for the component designs; the ownership boundary does
not.

Deployment does not reinterpret capability content, decide scope, author migrations, or repair a
defective package through judgment. A missing or contradictory input is reported back to the
producer.

---

## §10 — Review

### Responsibility

Review defines reusable behaviour for independent assessment of designs and outcomes. It is a
Capabilities component because the lead/reviewer pattern, review records, findings, and response
discipline are useful beyond any one workflow or domain.

The **lead** owns the current model or outcome and remains accountable for overall coherence and
simplicity. The **reviewer** identifies risks, omissions, conflicts, and alternatives without
becoming a second author. A finding and its proposed remedy are separate: the lead may accept the
finding while rejecting the remedy.

Before adding a mechanism in response to review, the lead considers whether the risk can be
accepted, the need removed, or the underlying model reshaped. Review quality includes challenging
net complexity, not only finding missing cases.

Lead and reviewer assignment is task-specific. It is not permanently attached to a model,
platform, or role across all work. A component may define a review profile for its outputs;
Review owns the shared execution and disposition model.

---

## §11 — Cross-component flows

### Produce and deploy a Standard or Tool

```text
Component Design
      │
      ├── declares applicability ─────────────► Scope
      ├── declares prerequisites ─────────────► Dependencies
      ├── declares transition content ────────► Migration
      └── is assessed with profile ───────────► Review
      │
      ▼
build base outcome
      │
      ├── apply platform divergence when needed
      ▼
package outcome
      │
      ▼
Deployment → platform preparation → publish/distribute
```

### Modify an older dependent document

```text
Document selected for modification
      │
      ▼
Dependencies compares declared and available versions
      │
      ├── dependency unavailable ──► stop and report
      ├── Required Migration ──────► stop/defer to migration path
      ├── On-Update pending ───────► apply in order, then update declaration
      └── nothing pending ─────────► perform requested modification
```

The explicit `/update-doc` command enters the same flow at the dependency comparison and ends
after reconciliation/reporting.

---

## §12 — Document types and DocMeth boundary

A domain may define the document types it needs for the artefacts it creates. A locally defined
type is owned and maintained by that domain. Recurrence across domains is evidence that a type
may belong in DocMeth, not a requirement to place it there in advance.

DocMeth owns shared document types and shared document components. Capabilities may therefore
define local package, build, transition, or review-support artefacts without first expanding
DocMeth. Items that may affect DocMeth are recorded in `Capabilities_DocMethReviewItems` v1 for
the separate DocMeth review; this design does not prescribe DocMeth's final shape.

---

## §13 — Deliberately open

- Exact identity and version contract shared across packages, dependencies, and deployed
  artefacts.
- Exact package-manifest schema.
- Detailed component designs for Scope, Dependencies, Migration, Deployment, and Review.
- Reconciliation of the existing Standards and Tools child designs with this parent architecture.
- Platform designs and empirical trigger/discovery techniques for each supported platform.
- Whether Tools publishes a standalone Tools Production Standard and the exact names of all
  produced standards beyond the two confirmed Standards outputs.

These open details do not alter the seven-component set or the ownership boundaries established
above.

---

**Depends on:** `Capabilities_Brief` v2, `Capabilities_Decisions` v8 (`D43`–`D53`).

**References:** `Capabilities_Overview` v7, `Capabilities_Standards_Design` v3 (revision
required), `Capabilities_Tools_Design` v1 (revision required),
`Capabilities_DocMethReviewItems` v1.

**Methodology:** v17
