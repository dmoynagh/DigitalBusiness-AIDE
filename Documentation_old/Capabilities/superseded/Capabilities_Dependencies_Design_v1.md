# Capabilities Dependencies — Design

> **Version 1** (2026-08-28). Establishes compact dependency declarations, identity-first
> resolution, conformance-version tracking, required/startup-required presence checks, Dependency
> Builders, and the Dependency Query result contract.
>
> Created: 2026-08-28 | Last modified: 2026-08-28

---

## §1 — Purpose

A Dependency declares that an artefact relies on another identified artefact or capability for
some part of its correct **schema, design, content, interpretation, conformance, maintenance, or
execution**.

Dependencies makes that relationship explicit and machine-usable. It answers:

```text
What do I rely on?
Can that identity be resolved now?
What version was I last conformed against?
What version is available?
Is there a version gap?
```

Dependencies reports state. It does not install, deploy, migrate, or decide every operation's
blocking policy.

The formal published Standard identity is **`AIDE_Dependencies`**. `Dependencies` is the common
name.

---

## §2 — Identity contract consumed by Dependencies

Dependency resolution uses the AIDE system identity convention.

A referenceable artefact may expose one or more identities in compact header metadata:

```text
Identity: primary-id@v2, alternate-id@v7, included-id
```

The first entry is primary. Later entries are alternate identities exposed by the same artefact.
A version, where present, belongs to that identity entry.

Resolution matches the **identity name first, ignoring version**. Version is compared only after
identity resolution.

If more than one available artefact matches the same identity, resolution fails visibly rather
than guessing.

---

## §3 — Compact dependency declaration

For a governed Markdown document, Dependencies uses one compact footer metadata property:

```text
Dependencies: abc, !def@v4, !!ghi@!v7, builder:[jkl@v2, !mno]
```

Documentation Methodology owns the footer metadata container and its physical placement.
`AIDE_Dependencies` owns the syntax and behaviour of the `Dependencies:` property.

The declaration forms are:

```text
dependency
!dependency
!!dependency
dependency@version
!dependency@version
!!dependency@version
dependency@!version
!dependency@!version
!!dependency@!version
ownerkey:[dependency, ...]
```

---

## §4 — Presence levels

### Normal dependency

```text
abc
```

Records the relationship. Resolve/check when relevant to the operation.

### Required dependency

```text
!abc
```

Availability must be checked when the artefact is accessed or used for a relevant operation. If
the identity cannot be resolved, the failure is raised prominently.

`!` defines the minimum reporting/check posture. Another Standard, Tool, or operation may state
that it cannot proceed when a required dependency is missing.

### Startup-required dependency

```text
!!abc
```

Expresses a best-effort requirement to check availability at session start and report a missing
identity prominently. On chat platforms without enforceable startup hooks, implementations use
the strongest available mechanism.

A `!!` dependency is also a normal required (`!`) dependency thereafter, so first-use checking
remains the fallback if startup discovery did not occur.

`!!` is intent, not a claim that every platform can technically guarantee startup execution.

---

## §5 — Version semantics

A version attached to a dependency is a **conformance checkpoint**, not part of identity equality.

```text
abc@v8
```

means the dependent artefact was last successfully conformed against `abc` version `v8`.

Resolution is:

```text
1. resolve abc by identity name
2. read the available version on the matched identity
3. compare available version with v8
4. report the relationship and any gap
```

If `abc@v12` is available, `abc@v8` still resolves successfully and reports the `v8 → v12` gap.
That gap is handed to Migration/update logic.

If the available version is older than the recorded conformance version, identity still resolves
but the version state is not acceptable/current and is reported accordingly.

If the dependency is unversioned, no version comparison is requested.

### Exact-version requirement

`!` immediately after `@` means the available identity must expose exactly that version:

```text
abc@!v8
```

`abc@v12` still resolves as the same identity, but the exact-version requirement fails.

The two positions of `!` are independent:

```text
!abc@v8   → required presence, conformed at v8
abc@!v8   → normal presence posture, exact v8 required
!abc@!v8  → required presence and exact v8 required
```

---

## §6 — Dependency Query

A **Dependency Query** resolves one or more dependency declarations against identities available
in the current execution environment.

For each declaration it reports factual state including:

- requested identity;
- primary identity of the resolved artefact where found;
- resolved / not resolved;
- requirement level: normal / required / startup-required;
- declared conformance version, if any;
- available version, if any;
- version relation: same / newer / older / unknown / not-applicable;
- version gap where relevant;
- exact-version requirement and whether it passed.

Example:

```text
Dependency: !abc-standard@v8
Available:  Identity: abc-standard@v12
```

returns conceptually:

```text
Identity match: yes
Required presence: satisfied
Conformed version: v8
Available version: v12
Version relation: newer
Version gap: v8 → v12
```

The existence requirement is satisfied even though the dependent artefact is not current against
v12.

Dependencies does not decide what the gap requires. Migration and the current operation consume
the query result.

---

## §7 — Conformance advancement

A dependency declaration does **not** advance merely because a newer dependency version exists.

The recorded version advances only after the dependent artefact has successfully completed all
applicable migration/update/conformance work through the version being recorded.

Example:

```text
Dependencies: !abc-standard@v8
Available: abc-standard@v12
Required Migration at v10
```

After the required migration succeeds, the artefact may record the proven checkpoint:

```text
!abc-standard@v10
```

When the artefact is next updated/saved and all remaining applicable On-Update or conformance
steps through v12 have completed successfully, it records:

```text
!abc-standard@v12
```

If required work fails or is deferred, the declaration remains at the last proven conformance
checkpoint.

---

## §8 — Dependency Builder

A **Dependency Builder** lets another Standard derive dependency declarations from information on
an artefact.

The owning Standard embeds an `AIDE_DependencyBuilder` YAML block. Example:

```yaml
AIDE_DependencyBuilder:
  Id: DocumentationDependencies
  Owner: AIDE_DocumentationMethodology

  AppliesWhen:
    Description: Run when the artefact is a governed document.

  Source:
    Description: Read the document information defined by this Standard.

  Generate:
    Description: Generate the dependencies required by the current document state.

  OutputOwnership:
    Group: "docmeth"
```

As with Tag Builders, the builder owns detection, source interpretation, generation, and cleanup
inside its declared ownership boundary.

A builder may own a group or a distinctive dependency-identity prefix where that representation
is appropriate.

Groups are maintenance metadata only. Every consumer except the owning builder ignores the group
key and sees the contained entries simply as dependencies.

---

## §9 — Builder discovery and execution

Dependency Builder discovery mirrors Tags:

```text
available Standards
      ↓
find AIDE_DependencyBuilder definitions
      ↓
run builders against artefact in hand
      ↓
each builder maintains only its own output
```

No separate authoritative registry is required.

Builders are idempotent. A builder that determines it applies but cannot derive correct output
fails visibly rather than silently leaving misleading declarations.

---

## §10 — Bootstrap relationship

Startup-required (`!!`) checking uses the AIDE system bootstrap convention.

Dependencies may contribute a `{bootstrap}` instruction telling the environment to check
available `!!` dependencies. The generic `{bootstrap}` marker and session-start discovery rule
are system-level Core behaviour, not owned by Dependencies.

Platform implementations use the strongest available persistent/custom/project/plugin/repository
instruction mechanism, without claiming stronger enforcement than the platform provides.

---

## §11 — References

A Reference remains distinct from a Dependency: it is material drawn on or mentioned without the
reassessment/conformance relationship carried by a Dependency.

Document-specific rendering of References remains a Documentation Methodology concern until the
separate DocMeth review reconciles the existing footer model with this generic dependency model.

---

## §12 — Ownership boundary

`AIDE_Dependencies` owns:

- dependency declaration semantics and compact syntax;
- normal / required / startup-required presence posture;
- conformance-version and exact-version syntax;
- identity-first resolution and version comparison;
- Dependency Query result semantics;
- conformance checkpoint advancement rules;
- Dependency Builder declaration/discovery/execution contract.

Core owns the shared Identity and bootstrap primitives.

Migration owns transition classification, ordering, and execution for version gaps.

Deployment owns installation/distribution, not Dependencies.

The current operation may impose stronger blocking behaviour than Dependencies' minimum loud
reporting requirement.

---

**Depends on:** `Capabilities_Design` v4, `Capabilities_Decisions` v10,
`Core_System_Design` v3.

**References:** `Capabilities_Migration` (design pending), `DocumentationMethodology_Guide` v17.

**Methodology:** v17
