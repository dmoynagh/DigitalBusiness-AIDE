> identity: Capabilities_Development_Standard@v3 | doctype: standard | updated: 2026-09-24

# Capabilities — Development Standard

The shared base for designing, reviewing, building, and deploying any AIDE capability — standard, tool, service, or utility.

---

## Applicability

Information. This standard applies when designing, reviewing, building, or deploying any AIDE capability, and when authoring a type-specific development standard. Each type's own development standard extends this base with type-specific guidance.

---

## What a capability is

A capability extends the AIDE development environment. It adds functionality — to sessions, to processes, or to the corpus — that would otherwise have to be re-derived, re-built, or re-run each time. All four types are capabilities.

Every capability has a type, a design, an owning component, and a consumer. Each capability instance lives with the component that knows most about it, not with the methodological component for its type.

---

## The four types

Two properties classify capabilities into three groups. A third test separates the two types within one group.

**Execution context** — who performs the work. In-session capabilities are performed by the AI within the session. Out-of-session capabilities are performed by a separate process outside the session.

**Direction of service** — what the work serves. Session-serving capabilities are loaded into or called by sessions. Corpus-serving capabilities act on files and infrastructure on their own terms, not at a session's request. Direction does not imply lifecycle — a corpus-serving capability may run and exit or run persistently.

| Type | Execution | Direction | Authored doc | Delivered as |
|---|---|---|---|---|
| Standard | In-session | Serves sessions | Standard doc | Skill |
| Tool | In-session | Serves sessions | Tool doc | Skill |
| Service | Out-of-session | Serves sessions | — | Server |
| Utility | Out-of-session | Serves the corpus | — | Utility |

Standards and Tools share the same cell. The invocability test (owned by Tools) separates them: a standard shapes decisions and behaviour; a tool is a named invokable action. The direction-of-service test (service vs utility) is owned by Services.

When the type is ambiguous, apply the relevant boundary test. Each type's development standard states its boundary tests and classification guidance for edge cases.

---

## The development lifecycle

Every capability follows six phases. The content and density at each phase vary by type.

**Design.** Define what the capability does, why, and how. Governed by PD's design methodology. Each type component defines the design concerns specific to its type. Design is always required — no type has an exception for skipping it.

**Author.** Produce the in-session document from the design — the standard doc or tool doc. This phase applies only to standards and tools, because those types produce a document that is both the specification and the deployment payload. Services and utilities have no authored document; the design is the specification. The authored document is produced fresh from the design, not by modifying a previous version.

**Review.** Check the specification before it is built — the authored document for standards and tools, the design for services and utilities. Every type has two parts: a self-check by the developer (the acceptance test, for standards and tools) and cross-review by a separate AI directed to find defects against the design's definition of done. Out-of-session types also test the built deliverable against its design during build. Each type's development standard states what review and testing mean for that type.

**Build.** Create the deliverable from the specification. For standards and tools, build packages the authored doc as a skill. For services and utilities, build creates the server or utility from the design. Build follows Build's generic mechanism. Each type component defines build standards for its build domain, stated within its development standard.

**Deploy.** Get the built deliverable to where it runs, consuming Infrastructure's delivery model. Each type's development standard states the deployment path for its type.

**Consume.** What the user or developer needs to use or run the deployed capability — from a full consumption standard (standards) through user guides (services) to self-evident invocation (well-authored tools). Each type's development standard states what its type requires.

---

## Type-specific development standards

Each type component produces a development standard that extends this base. Each covers seven sections aligned with the lifecycle:

1. **What the type is** — definition and boundary tests.
2. **Design guidance** — the type-specific concerns the design must address.
3. **Author guidance** — standards and tools only.
4. **Review guidance** — what review and testing mean for the type.
5. **Build standards** — the type-specific build conventions.
6. **Deploy guidance** — how the deliverable reaches its target.
7. **Consumption guidance** — what the user or developer needs once deployed.

| Capability type | Development standard |
|---|---|
| Standard | `Standards_Development_Standard` |
| Tool | `Tools_Development_Standard` |
| Service | `Services_Development_Standard` |
| Utility | `Utilities_Development_Standard` |

Information. These are pointers, not dependencies — each type standard declares `uses` on this one, not the reverse. Each is named by identity only; the file name mirrors the identity, in the type's component folder.

Each development standard must be producible from its own design. The design holds everything the standard carries, plus the reasoning; the standard is its lean, deployable output.

---

## Build and Infrastructure

Build owns the generic build mechanism; each type component owns the domain knowledge of how to build its type. Infrastructure owns delivery — plugin structure, update propagation, and the delivery model for services. This standard does not restate either.

`uses` declares dependencies on standards only. Build and Infrastructure do not yet publish standards, so development standards reference their documents in prose. When either publishes a standard a development standard depends on, add the `uses` declaration then.

---

## Acceptance test

Given this standard: can a fresh AI correctly classify a capability's type, identify the lifecycle phases that apply to it, and locate the type-specific development standard it must follow? The standard passes if the AI can begin work on a capability of any type without further guidance about the shared methodology.

---

Version note: v1 — initial standard. Produced from Capabilities_Design@v2: six-phase lifecycle including review, seven-section development-standard structure, `uses` limited to standards. 2026-09-23.

Version note: v2 — the four type development standards named in a type-to-standard table with file locations. Produced from Capabilities_Design@v3. 2026-09-24. Replaces v1.

Version note: v3 — the type-to-standard table names each development standard by identity only, without version or file path. Produced from Capabilities_Design@v4 (D15). 2026-09-24. Replaces v2.
