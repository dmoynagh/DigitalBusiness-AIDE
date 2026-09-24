> identity: Capabilities_Design@v4 | doctype: design | updated: 2026-09-24

# Capabilities — Design

## Brief

**Purpose.** Produce the Capabilities Development Standard — the base development methodology that governs how capabilities are designed, reviewed, built, and deployed. The four type components (Standards, Tools, Services, Utilities) consume it to shape their own development standards. Anyone developing a capability uses it alongside the relevant type's development standard.

**Objectives.**

1. A definition of capability that covers all four types.
2. A taxonomy of the four types with the properties that distinguish them.
3. A shared development lifecycle applicable to all four types.
4. The relationship to Build and Infrastructure stated without restating their content.
5. A base that each type-specific development standard can consume.

**Definition of done.**

1. A developer can classify any capability as a standard, tool, service, or utility, using the two properties and the boundary tests.
2. A developer knows the lifecycle phases — design, author (where applicable), review, build, deploy, consumption — and which apply to each type.
3. A developer can find, for each phase, the type-specific development standard that governs it.
4. The relationship to Build (build standards per build domain) and Infrastructure (delivery) is clear, including how dependencies on them are declared.
5. Each type component can produce a development standard that extends this base, using the common section structure.
6. The Capabilities Development Standard can be produced entirely from this design.

**Linked build outcome.** Capabilities Development Standard, deployed as a skill in the `aide-dev` plugin. Consumed by each type-specific development standard via `uses`.

**Target / outcome.** A deployed standard that any capability designer uses when designing, building, and deploying a capability of any type. Each type component's own development standard extends this base.

**Scope.** The capability definition, the four-type taxonomy, the shared development lifecycle, and the base relationship to Build and Infrastructure. Type-specific design concerns, authoring rules, boundary tests, build specifics, and consumption guidance are owned by each type's component.

**Boundaries.** Does not own: type-specific design guidance (Standards, Tools, Services, Utilities). Build's generic mechanism. Infrastructure's delivery model. PD's design methodology. Individual capability instances. DocMeth's document structure.

---

## What a capability is

A capability extends the AIDE development environment. It adds functionality — to sessions, to processes, or to the corpus — that would otherwise have to be re-derived, re-built, or re-run each time. All four types are capabilities.

A capability is defined by its type, designed within a design project, and governed by its owning component. Every capability has a design. Every capability is built and deployed. Every capability has a consumer.

Each type has a methodological component that defines how to design, build, and deploy that type. Individual capability instances live with the component that knows most about them, not with the methodological component.

---

## The four types

Two properties distinguish the types.

**Execution context** — who performs the work. In-session capabilities are performed by the AI within the session. Out-of-session capabilities are performed by a separate process outside the session.

**Direction of service** — what the work serves. Session-serving capabilities are loaded into or called by sessions. Corpus-serving capabilities act on files and infrastructure, on their own terms rather than at a session's request. Direction does not imply lifecycle — a corpus-serving capability may run and exit or run persistently.

| Type | Execution | Direction | Authored doc | Delivered as |
|---|---|---|---|---|
| Standard | In-session | Serves sessions | Standard doc | Skill |
| Tool | In-session | Serves sessions | Tool doc | Skill |
| Service | Out-of-session | Serves sessions | — | Server |
| Utility | Out-of-session | Serves the corpus | — | Utility |

The two properties distinguish three groups: in-session session-serving (Standards and Tools), out-of-session session-serving (Services), and out-of-session corpus-serving (Utilities). Within the in-session group, the invocability test (owned by Tools) separates Standards from Tools — a standard shapes decisions and behaviour; a tool is a named invokable action. The direction-of-service test (service vs utility) is owned by Services. These tests settle classification when the type is ambiguous.

---

## The development lifecycle

Every capability follows six phases. The phases are the same across all four types; the content and density at each phase vary by type, and the author phase applies only to in-session types.

### Design

Define what the capability does, why, and how. Governed by PD's design methodology. Each type component defines the design concerns specific to its type — the things a designer must address in the design document.

Design is always required. No type has an exception for skipping design. Even the simplest capability resolves questions that need to be worked through before build.

### Author

Produce the in-session document from the design — the standard doc or tool doc. This phase applies only to in-session capabilities (standards and tools) because those types produce a document that is both the build specification and the deployment payload. Build packages it; the authored doc is what gets deployed.

For out-of-session capabilities (services and utilities), the design document is the build specification. There is no intermediate authored document — the design goes directly to build. The design phase carries more weight for these types because there is no authoring pass to refine the specification.

Authoring is governed by each type component's authoring rules. The authored document is produced fresh from the design, not by modifying a previous version.

### Review

Check the specification before it is built. The specification is the authored document for standards and tools, and the design for services and utilities. Review has two parts for every type: a self-check by the developer (for standards and tools, the acceptance test) and cross-review by a separate AI directed to find defects, tested against the design's definition of done. The separate AI provides independence — the developing session shares the developer's assumptions.

Review sits before build because a defect found in the specification is cheaper to fix than one found in the built deliverable. Out-of-session types also test the built deliverable against its design during build — that is part of build, not a replacement for reviewing the specification. Each type component states what review and testing mean for its type; the cross-review process itself is a Working Practices convention.

### Build

Create the deliverable from the specification. Build follows Build's generic mechanism — build package, caller, return, work levels, the commitment-and-return loop.

Each type component defines **build standards** for its **build domain** — the type-specific conventions composed into profiles on top of Build's base. Build standards carry the "how to build this type" knowledge: what the build target looks like, what patterns to use, what validation to apply.

The specification that enters build differs by type:
- Standards and tools: the authored doc is the specification. Build packages it as a skill.
- Services: the design doc is the specification. Build creates the server.
- Utilities: the design doc is the specification. Build creates the utility.

### Deploy

Get the built deliverable to where it runs. Deployment consumes Infrastructure's delivery model. Each type component states the deployment path for its type without restating Infrastructure's mechanisms.

### Consumption

What the user or developer needs to use or run the deployed capability. Consumption needs vary by type — from a full consumption standard (standards) through user guides and connection setup (services) to self-evident invocation (well-authored tools). Each type component determines what consumption guidance its type requires.

---

## Relationship to Build

Build defines the generic build mechanism. Capabilities does not restate it. The connection is through build standards and build domains — Build's own model for type-specific build guidance.

Each type component produces build standards for its build domain, stated within the type's development standard. These follow the Standards methodology (same authoring rules, same delivery) and are composed into profiles. Build's profile mechanism determines how to compose them, whether embedded or — if conventions grow substantial — separated into standalone standards. The type component owns the domain knowledge; Build owns the mechanism.

Build explicitly deferred the first build standard (D32) until conventions are stable enough to standardise. The capability development standards are a natural home for those first build standards — each type's build domain is a demonstrated consumer.

### Declaring dependencies on Build and Infrastructure

`uses` declares dependencies on standards only. Neither Build nor Infrastructure currently publishes a standard — Build's first standard is deferred, and Infrastructure's delivery model is a reference document, not a standard. A development standard therefore references their documents in prose (the MCP delivery model, Build's design) rather than declaring `uses`. When either publishes a standard that a development standard depends on, the `uses` declaration is added at that point.

The Capabilities Development Standard itself declares no `uses`. It is the foundation the type standards extend — they declare `uses` on it, and a reverse declaration would create a cycle. Nothing in it depends on the standards authoring rules at the moment of application.

---

## Relationship to Infrastructure

Infrastructure owns delivery — the MCP marketplace pipeline, plugin structure, settings merge, update propagation. Capabilities does not restate this. Each type component states what gets delivered and where for its type, consuming Infrastructure's model.

Infrastructure's component scope may evolve. Currently it holds delivery machinery and individual utility instances. As capability methodology develops, individual utilities may move to the components that know most about them. Infrastructure's durable contribution is the delivery and operational machinery.

---

## What each development standard covers

Each type component (Standards, Tools, Services, Utilities) produces a **development standard** that consumes this base and adds type-specific content. Each covers seven sections aligned with the lifecycle:

1. **What the type is** — definition and boundary tests.
2. **Design guidance** — the type-specific concerns the design must address.
3. **Author guidance** — where applicable (standards and tools only).
4. **Review guidance** — what review and testing mean for the type.
5. **Build standards** — the type-specific build conventions for the type's build domain.
6. **Deploy guidance** — how the type's deliverable reaches its target.
7. **Consumption guidance** — what the user or developer needs once deployed.

For Standards and Tools, the development standard supersedes the existing authoring standard — broader scope, same authoring content embedded, review/build/deploy/consumption sections added. For Services and Utilities, the development standard is authored fresh.

The four type standards, so a developer can go straight from the type to the standard that governs it:

| Capability type | Development standard |
|---|---|
| Standard | `Standards_Development_Standard` |
| Tool | `Tools_Development_Standard` |
| Service | `Services_Development_Standard` |
| Utility | `Utilities_Development_Standard` |

These are pointers, not `uses` declarations — the type standards depend on this base, not the other way round (D13, D14). They name each standard by identity only, with no version or file, so the table does not go stale when a type standard is versioned (D15).

Each type's development standard must be producible from its own design. The design holds everything the standard carries, plus the reasoning, alternatives, and explanation; the standard is its lean, deployable output.

---

## Applicability and acceptance

The Capabilities Development Standard applies when designing, reviewing, building, or deploying any AIDE capability, and when authoring a type-specific development standard.

**Acceptance test.** Given the standard, can a fresh AI correctly classify a capability's type, identify the lifecycle phases that apply to it, and locate the type-specific development standard it must follow? The standard passes if the AI can begin work on a capability of any type without further guidance about the shared methodology.

---

Version note: v1-draft1 — initial design. Four-type taxonomy, five-phase lifecycle, relationships to Build and Infrastructure. 2026-09-23.

Version note: v1 — cross-review remediation. F1: taxonomy corrected to three groups plus invocability test. F3: boundary ownership clarified. F6: build standards artifact model stated. 2026-09-23. Replaces v1-draft1.

Version note: v2 — definition of done reframed around the development cycle. Review added as a lifecycle phase (six phases) and as a section in the development-standard structure (seven sections). "Then exit" removed from direction of service, aligning with Services F9. Dependency declaration corrected: `uses` points at standards only, so Build and Infrastructure are referenced in prose until they publish standards. Applicability and acceptance test added so the standard can be produced from the design. 2026-09-23. Replaces v1.

Version note: v3 — second cross-review remediation. The four type development standards named in a type-to-standard table with file locations (F1, D14). 2026-09-24. Replaces v2.

Version note: v4 — the type-to-standard table names each development standard by identity only, without version or file path; it is a locator, not a conformance stamp (D15). 2026-09-24. Replaces v3.
