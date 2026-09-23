> identity: Capabilities_Development_Standard@v1 | doctype: standard | updated: 2026-09-23
> uses: Standards_Authoring_Standard@v8

# Capabilities — Development Standard

Version 1. 2026-09-23.

---

## Applicability

This standard applies when designing, building, or deploying any AIDE capability, and when authoring a type-specific development standard. It provides the shared development methodology that all four type components consume. Each type's own development standard extends this base with type-specific guidance.

---

## What a capability is

A capability extends the AIDE development environment. It adds functionality — to sessions, to processes, or to the corpus — that would otherwise have to be re-derived, re-built, or re-run each time. All four types are capabilities.

Every capability has a type, a design, an owning component, and a consumer. Each capability instance lives with the component that knows most about it, not with the methodological component for its type.

---

## The four types

Two properties classify capabilities into three groups. A third test separates the two types within one group.

**Execution context** — who performs the work. In-session capabilities are performed by the AI within the session. Out-of-session capabilities are performed by a separate process outside the session.

**Direction of service** — what the work serves. Session-serving capabilities are loaded into or called by sessions. Corpus-serving capabilities act on files and infrastructure.

| Type | Execution | Direction | Authored doc | Delivered as |
|---|---|---|---|---|
| Standard | In-session | Serves sessions | Standard doc | Skill |
| Tool | In-session | Serves sessions | Tool doc | Skill |
| Service | Out-of-session | Serves sessions | — | Server |
| Utility | Out-of-session | Serves the corpus | — | Utility |

Standards and Tools share the same cell. The invocability test (owned by Tools) separates them: a standard shapes decisions and behaviour; a tool is a named invokable action. The direction-of-service test (service vs utility) is owned by Services.

When the type is ambiguous, apply the relevant boundary test. Each type component's development standard states its boundary tests and classification guidance for edge cases.

---

## The development lifecycle

Every capability follows five phases. The content and density at each phase vary by type.

**Design.** Define what the capability does, why, and how. Governed by PD's design methodology. Each type component defines the design concerns specific to its type. Design is always required — no type has an exception for skipping it.

**Author.** Produce the in-session document from the design — the standard doc or tool doc. This phase applies only to in-session capabilities (standards and tools) because those types produce a document that is both the specification and the deployment payload. Out-of-session capabilities (services and utilities) have no intermediate authored document; the design goes directly to build.

Authoring is governed by each type component's rules. The authored document is produced fresh from the design, not by modifying a previous version.

**Build.** Create the deliverable from the specification. For standards and tools, the authored doc is the specification and build packages it as a skill. For services and utilities, the design doc is the specification and build creates the server or utility. Build follows Build's generic mechanism — build packages, callers, returns, work levels.

Each type component defines build standards for its build domain — the type-specific conventions composed into profiles on top of Build's base. Build standards are stated within the type's development standard.

**Deploy.** Get the built deliverable to where it runs. Deployment consumes Infrastructure's delivery model. Each type component states the deployment path for its type without restating Infrastructure's mechanisms.

**Consume.** What the user or developer needs to use or run the deployed capability. Consumption needs vary by type — from a full consumption standard (standards) through user guides and connection setup (services) to self-evident invocation (well-authored tools). Each type component determines what consumption guidance its type requires.

---

## Type-specific development standards

Each type component (Standards, Tools, Services, Utilities) produces a development standard that consumes this base and adds type-specific content. Each covers six sections aligned with the lifecycle:

1. **What the type is** — definition and boundary tests.
2. **Design guidance** — the type-specific concerns the design must address.
3. **Author guidance** — where applicable (standards and tools only).
4. **Build standards** — the type-specific build conventions for the type's build domain.
5. **Deploy guidance** — how the type's deliverable reaches its target.
6. **Consumption guidance** — what the user or developer needs once deployed.

For Standards and Tools, the development standard supersedes the existing authoring standard — broader scope, settled authoring content embedded unchanged, build/deploy/consumption sections added. For Services and Utilities, the development standard is authored fresh.

---

## Relationship to Build and Infrastructure

Build defines the generic build mechanism. This standard does not restate it. The connection is through build standards and build domains: each type component produces build standards for its build domain, stated within the type's development standard. Build's profile mechanism determines how to compose them. The type component owns the domain knowledge; Build owns the mechanism.

Infrastructure owns delivery — the plugin structure, settings merge, update propagation, and the delivery model for services. This standard does not restate it. Each type component states what gets delivered and where for its type, consuming Infrastructure's model.

---

## Acceptance test

Given this standard: can a fresh AI correctly classify a capability's type, identify the applicable development lifecycle phases, and locate the type-specific development standard it must follow? The standard passes if the AI can begin work on a capability of any type without further guidance about the shared methodology.

---

Version note: v1 — initial standard. Authored from Capabilities_Design@v1. Shared development methodology for all four capability types. 2026-09-23.
