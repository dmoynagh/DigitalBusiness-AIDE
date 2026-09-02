# Capabilities — Brief

> **Version 2** (2026-08-28). Rewritten around the confirmed seven-component architecture.
> Replaces the earlier Standards-and-Tools-centred model with explicit shared components for
> Scope, Dependencies, Migration, Deployment, and Review, and separates capability production
> from deployment.
>
> Created: 2026-08-27 | Last modified: 2026-08-28

---

## Purpose

Capabilities owns the reusable infrastructure by which AI-facing capabilities are defined,
made applicable, connected to their dependencies, transitioned across versions, built,
packaged, deployed, and reviewed across platforms.

Its purpose is to make capability behaviour understandable, portable, and dependable without
forcing every domain to reinvent the same mechanisms. Domains remain responsible for the
content they create; Capabilities provides the shared component model those domains use.

Everything in this model exists to empower the developer to use AI tools for better development
(`Workflow-D106`, the empowerment premise). A mechanism that does not add practical capability
or reduce a demonstrated risk does not belong.

---

## Required architecture

Capabilities has seven top-level components:

- **Standards** — defines how standards are designed, authored, built, and packaged, and how
  sessions operate under them.
- **Tools** — defines invokable capability behaviour, including the commands a tool contributes,
  and how tools are built and packaged.
- **Scope** — defines where and when a capability applies and how that applicability is realised
  effectively on each platform.
- **Dependencies** — defines how artefacts declare versioned dependencies, what those declarations
  mean, and how availability and version state are checked at runtime.
- **Migration** — defines and executes declared transitions between dependency states, separating
  blocking Required Migrations from non-blocking On-Update transitions.
- **Deployment** — accepts capability packages, prepares them for a target platform, and
  distributes or publishes them.
- **Review** — defines reusable lead/reviewer behaviour for assessing designs and outcomes while
  keeping findings distinct from proposed remedies.

These components are peers under Capabilities. They cooperate through explicit contracts rather
than absorbing one another's responsibilities.

---

## Required boundaries

- Standards and Tools own the production of their outcomes through build and package.
- Deployment begins at a completed package; it owns platform preparation, distribution, and
  publication, not capability meaning.
- Scope owns applicability and platform trigger/discovery realisation; individual capability
  components declare their scope but do not each reinvent platform retrieval machinery.
- Dependencies owns dependency identity, version meaning, declaration syntax, runtime checks,
  and document dependency-footer semantics.
- Migration owns transition format and execution posture; the owner of the changed dependency
  authors the actual transition instructions.
- Review owns the reusable review model; individual components may define review profiles or
  checks specific to their outputs.
- Each domain may define document types needed for its own work. DocMeth owns only shared
  document types and shared document components.

---

## Required outcomes

The architecture must support:

- a generic Design producing a base outcome;
- an optional `Design_Platform_{Name}` expressing only platform divergence;
- the platform design being applied to the base outcome to produce a platform outcome;
- Standards publishing both a generic **Standards Production Standard** and a generic
  **Standards Usage Standard**;
- Tools declaring the logical commands they add as part of their design;
- separate Required Migration and On-Update transition artefacts;
- AI-oriented automatic On-Update checks when an older dependent artefact is being modified;
- an explicit, idempotent `/update-doc` path for forced On-Update reconciliation;
- `/update-doc` stopping and deferring when a Required Migration is encountered;
- an Overview that exposes current components, boundaries, relationships, flows, and unresolved
  architecture for human review.

---

## What Capabilities does not own

- The subject-matter content of standards, tools, migrations, or reviews created by other
  domains.
- Domain-specific document types unless they become shared across domains.
- Host-platform synchronisation after publication.
- Platform facts that belong in platform reference material.
- The pending redesign of Documentation Methodology; this corpus records inputs for that review
  separately and does not redesign DocMeth in this pass.

---

## Success signals

- A reviewer can use the Overview to see the whole architecture and identify a misplaced or
  missing responsibility.
- Each shared concern has one clear owner and consumers reference that owner rather than duplicate
  the mechanism.
- Capability authors can move from generic design to base and platform outcomes without putting
  platform detail into the generic model.
- An AI can distinguish a blocking migration from a safe On-Update transition without inferring
  urgency from mixed prose.
- Re-running `/update-doc` on a current document makes no substantive change and reports that no
  On-Update actions were pending.

---

**Depends on:** `Capabilities_Decisions` v8 (`D43`–`D53`).

**References:** `Workflow-D106`–`Workflow-D113` (capability model seed),
`Capabilities_DocMethReviewItems` v1.

**Methodology:** v17
