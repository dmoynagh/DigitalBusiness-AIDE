# Capabilities — Brief

> **Version 4** (2026-08-28). Adds Tags as an eighth peer component, confirms the Tags/Scope/
> Dependencies contracts, consumes the Core identity/bootstrap primitives, and separates the
> Capability Package payload from Deployment Manifest intent.
>
> Created: 2026-08-27 | Last modified: 2026-08-28

---

## Purpose

Capabilities owns the reusable infrastructure by which AI-facing capabilities are defined,
made applicable, connected to their dependencies, transitioned across versions, built into
canonical outcomes, realised for platforms, packaged, deployed, and reviewed.

Capabilities is a part of AIDE. Its Standards and Tools may apply on Design side, Build side,
or both according to Scope.

Everything in this model exists to empower the developer to use AI tools for better development.
A mechanism that does not add practical capability or reduce a demonstrated risk does not belong.

---

## Required architecture

Capabilities has eight peer components:

- **Standards** — defines Standards, their canonical production, and how sessions operate under
  them.
- **Tools** — defines invokable capability behaviour and commands, and their canonical
  production.
- **Tags** — defines the general tag-building, storage, ownership, and query substrate.
- **Scope** — defines where and when a capability or behaviour applies, using Tags plus contextual
  AI judgment.
- **Dependencies** — defines dependency declarations, required/startup-required presence,
  identity resolution, conformance checkpoints, and version-gap state.
- **Migration** — defines Required Migration and On-Update semantics, authoring/build rules,
  and transition execution.
- **Deployment** — accepts completed capability packages, composes named Deployment Sets, and
  distributes/publishes them to target platforms.
- **Review** — defines reusable independent assessment/challenge behaviour for insight and AI risk management.

These components cooperate through explicit contracts rather than absorbing one another's
responsibilities.

---

## Required production and handoff model

The design-side capability flow is:

```text
Capability Design
      ↓
Build Capability
      ↓
Canonical Standard / Tool
      ↓
effective Build Config
      ↓
Build WorkPackage
```

The canonical Standard or Tool contains the complete generic capability definition and, where
needed, capability-specific platform addenda. Absence of a platform addendum means the generic
definition applies unchanged.

Everything capability-specific that Build side needs is supplied with the Standard/Tool in the
Build WorkPackage. Build side must not need to reopen the internal Capability Design to discover
required behaviour.

The Build WorkPackage model itself is owned by the AIDE Build topic, not by Capabilities.

---

## Required build-side realisation

Build side combines:

- the canonical Standard or Tool;
- its capability-specific platform addenda;
- the effective Build Config;
- the Build WorkPackage;
- platform build Standards, Tools, and reference knowledge available in the Build environment.

Build side adapts the canonical capability into platform contributions, packages those
contributions, and may continue directly into Deployment.

Generic platform mechanics are not capability-design knowledge. The design side does not need to
know that a platform uses skills, plugins, repository structures, merged context bundles, or any
other concrete mechanism.

---

## Build Config requirements

Every buildable capability has an effective Build Config declaring:

- target platforms, or the current supported-platform default set;
- side applicability: Design, Build, or both, with **both** as the default;
- one or more named **Deployment Sets** the capability belongs to.

The configuration may be managed on Design side or Build side according to the chosen working
preference, but capability-affecting choices remain design intent.

---

## Tags, Scope, and Dependencies requirements

Tags must support Standards that contribute discoverable Tag Builders, builder-owned generated
output, compact artefact storage, and a small Boolean query language over flat tag values.
Semantic owners resolve their own inheritance/relationships before tag generation.

Scope must remain an applicability concern. Machine Scope is a Tags query; Context Scope is an
AI-interpreted natural-language condition. Missing layers impose no restriction; explicit disabled
means never applicable.

Dependencies must resolve identity before version, support normal / `!` required / `!!`
startup-required presence postures, record the last proven conformance checkpoint, expose version
gaps to Migration, and allow Dependency Builders to maintain generated declarations.

Core supplies the shared formal identity and `{bootstrap}` primitives used by these components.

---

## Migration requirements

Required Migration and On-Update declarations are authored with the canonical Standard or Tool.
They are unequivocally distinguished by posture.

The capability builder uses the Migration Build Standard to produce canonical transition
information. Build-side platform and Deployment Set builders extract and adapt that information
into whatever representations their target platform or deployment mechanism requires.

---

## Deployment requirements

A completed capability package is capability-local. Deployment is set-aware.

The hard producer-to-Deployment boundary is a **Capability Package plus Deployment Manifest**.
The Package is payload; the Manifest carries the machine-readable placement/lifecycle intent that
Deployment requires. Deployment must not reconstruct that intent from Capability Design.

A **Deployment Set** is a named logical destination/grouping. Platform-specific Deployment
configuration resolves that logical name to the concrete representation required on each target
platform.

For example, one Deployment Set may resolve to:

```text
Claude  → plugin
Codex   → corresponding Codex capability collection
ChatGPT → merged project bundle file
```

The capability Build Config names the Deployment Set; it does not need to know its physical
platform representation.

Deployment owns package consumption, Deployment Set composition, replacement/removal behaviour,
and distribution/publication. Host pickup/synchronisation remains external unless a platform
contract explicitly brings it into scope.

---

## Required boundaries

- Standards and Tools own capability meaning and canonical production.
- Build side owns platform adaptation and package/manifest construction.
- Tags owns classification/tag generation and matching, not applicability semantics.
- Scope owns applicability, not tag generation or build/deployment destination.
- Dependencies owns dependency state and conformance tracking, not installation.
- Migration owns transition semantics, production rules, and execution model; capability owners
  author their own transition declarations.
- Deployment starts from completed packages plus Deployment Manifests and owns Deployment Sets and publication.
- Review owns the reusable review method; components may supply profiles.
- WorkPackage belongs to AIDE Build and is consumed by Capabilities.

---

## Success signals

- A capability Design can produce a self-contained canonical Standard or Tool without generic
  platform implementation knowledge.
- A Build WorkPackage can be executed without reopening the Capability Design.
- Build side can realise the same canonical capability differently for each supported platform
  using platform Standards and Tools.
- Required Migration and On-Update information remains unambiguous through build and deployment.
- Deployment can assemble all packages assigned to a named Deployment Set without understanding
  capability semantics.
- Tags can be regenerated from owner-defined semantic source information without runtime
  inheritance traversal.
- Scope can determine applicability using simple machine tags plus AI context.
- Dependency checks distinguish missing identity from version gap and preserve the last proven
  conformance checkpoint.
- Review can create independent insight and surface material risk before important work is relied upon or locked in.

---

**Depends on:** `Capabilities_Decisions` v10.

**References:** `Core_System_Design` v3, `Capabilities_Design` v4.

**Methodology:** v17
