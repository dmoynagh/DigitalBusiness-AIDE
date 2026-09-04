# Capabilities — Brief

> **Version 3** (2026-08-28). Reconciles the seven-component architecture with the confirmed
> design-side capability build, Build WorkPackage handoff, build-side platform adaptation,
> embedded transition declarations, and Deployment Set model.
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

Capabilities has seven peer components:

- **Standards** — defines Standards, their canonical production, and how sessions operate under
  them.
- **Tools** — defines invokable capability behaviour and commands, and their canonical
  production.
- **Scope** — defines where and when a capability applies.
- **Dependencies** — defines versioned dependency declarations, availability, and conformance
  state.
- **Migration** — defines Required Migration and On-Update semantics, authoring/build rules,
  and transition execution.
- **Deployment** — accepts completed capability packages, composes named Deployment Sets, and
  distributes/publishes them to target platforms.
- **Review** — defines reusable lead/reviewer behaviour and review profiles.

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

## Migration requirements

Required Migration and On-Update declarations are authored with the canonical Standard or Tool.
They are unequivocally distinguished by posture.

The capability builder uses the Migration Build Standard to produce canonical transition
information. Build-side platform and Deployment Set builders extract and adapt that information
into whatever representations their target platform or deployment mechanism requires.

---

## Deployment requirements

A completed capability package is capability-local. Deployment is set-aware.

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
- Build side owns platform adaptation and package construction.
- Scope owns applicability, not build/deployment destination.
- Dependencies owns dependency meaning and availability, not installation.
- Migration owns transition semantics, production rules, and execution model; capability owners
  author their own transition declarations.
- Deployment starts from completed packages and owns Deployment Sets and publication.
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
- A reviewer can identify one owner for every mechanism in the design-to-deployment flow.

---

**Depends on:** `Capabilities_Decisions` v9.

**References:** `Core_System_Design` v2, `Capabilities_Design` v3.

**Methodology:** v17
