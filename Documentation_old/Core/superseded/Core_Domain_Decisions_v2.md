# Core Domain — Decisions

> **Version 2** (2026-08-31). Preserves the v1 Domain decision history and records the Item Type recognition boundary, Domain-owned approval/registry and propagation-stop model.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## D1 — Domain is redesigned from a blank sheet

**Decision.** The current Domain model has no compatibility obligation to the earlier
`AIDE_Domain` design/decision corpus.

**Reason.** The earlier model was never implemented or deployed. Preserving its declaration,
activation, scope, standards-composition or membership mechanisms would add constraints without a
real consumer to protect.

**Consequence.** Earlier Domain documents are historical reasoning only. No migration path,
schema bridge or behavioural compatibility layer is required.

---

## D2 — Domain belongs under Core

**Decision.** Domain is a Core-owned system foundation.

**Reason.** Project Design, Build, Capabilities, Documentation Methodology, Environment/AI
Deployment and future AIDE concerns may all need the same Domain context. No one of those concerns
should own the common boundary model.

**Consequence.** Development/product Domains remain outside the AIDE system tree and consume AIDE;
Core owns only the Domain contract.

---

## D3 — Domain is a semantic context, not inherently a file

**Decision.** A Domain is a named AIDE operating/governance context. It may be implicit or explicit.

**Reason.** Existing structures already provide useful natural boundaries. Requiring a declaration
artefact for every Domain would create ceremony and duplicate information.

**Consequence.** `AIDE_Domain.yaml` is an explicit representation, not a prerequisite for Domain
existence.

---

## D4 — Domain has three demonstrated jobs

**Decision.** Domain exists to provide:

1. a common name/vocabulary for an AIDE operating boundary;
2. a standard Domain settings host/convention; and
3. explicit composition/clarification when native structures do not express the intended Domain.

**Reason.** These are the demonstrated needs not cleanly owned by Index, project/solution or other
existing AIDE mechanisms.

**Consequence.** Do not add Domain machinery where an existing structure already answers the
question.

---

## D5 — Domain owns recognition needed for Domain resolution

**Decision.** The Domain Standard defines the recognised Domain-capable structure types and the
minimum structural relationships needed to resolve them consistently.

Initial types are:

```text
AIDE Index
solution
project
explicit AIDE Domain declaration
```

**Reason.** A single deployable Domain Standard should behave the same on Design and Build sides
rather than relying on several separate component-specific resolvers.

**Boundary.** Domain learns only Domain-relevant structure. It does not absorb Documentation
Methodology, build-system or project-system semantics.

---

## D6 — Natural authoritative containment beats local implicit roots

**Decision.** A contained recognised structure inherits its enclosing effective Domain rather than
creating another implicit Domain.

Examples:

- a solution's member project remains in the solution Domain;
- a delegated/child Index remains in the root Index Domain.

**Reason.** The authoritative containment relationship already states the larger structure.
Creating an additional Domain would conflate structural subdivision with governance.

---

## D7 — Structural children never create child Domains implicitly

**Decision.** Child Domains require explicit declaration.

**Reason.** Child Indexes, projects and other contained structures are frequently created for
retrieval, organisation or implementation reasons that do not imply a new governance context.

**Consequence.** Child-Domain inheritance, settings propagation, precedence and nesting remain
undefined until a real use case requires them.

---

## D8 — Matching co-root identities form one implicit Domain

**Decision.** Recognised co-root structures whose authoritative identities match are one implicit
Domain.

Example:

```text
Foo.sln
Foo_Index
→ Foo Domain
```

**Reason.** Same structural root plus matching authoritative identity is strong enough evidence
that the structures describe the same contextual boundary.

**Detail.** Index declared project/topic identity is authoritative over filename-only matching.

---

## D9 — Different co-root identities remain separate Domains

**Decision.** Recognised co-root structures with different identities are separate implicit Domains
unless an explicit Domain declaration says otherwise.

Examples:

```text
Foo.sln + Womble_Index → Foo Domain + Womble Domain
Foo.csproj + Bar.csproj with no solution → two Domains
```

**Reason.** Physical co-location is not composition.

**Consequence.** If the default is not the intended model, `AIDE_Domain.yaml` is the clarification
mechanism rather than adding type-specific exceptions.

---

## D10 — A matching Index is the preferred AIDE Domain metadata/settings host

**Decision.** When an Index and solution/project represent the same Domain, the Index is the
preferred AIDE-controlled Domain metadata/settings host.

**Reason.** AIDE controls the Index representation and can safely extend it without modifying
native project/solution formats merely to carry AIDE settings.

**Boundary.** The Index does not become authoritative over native solution/project membership or
semantics.

---

## D11 — Domain membership is distinct from native/corpus membership

**Decision.** Domain answers "what AIDE operating context does this target belong to?" Native
structures answer their own membership questions.

**Reason.** A solution may define project membership while AIDE documents beside/within the
solution still need the solution Domain context. An Index may define its governed document corpus
without becoming the sole definition of the wider Domain.

**Consequence.** AIDE-governed artefacts inside an unambiguous Domain container may inherit the
Domain even when they are not native solution/project members. Documentation Methodology still
owns document registration/governance.

---

## D12 — Artefacts do not normally carry Domain identity

**Decision.** Domain is contextual, not artefact-owned.

Ordinary documents/files do not normally store:

```text
Domain: Foo
```

**Reason.** It duplicates resolvable context, creates rename maintenance and couples artefacts to a
concept they may never need to use.

**Consequence.** Resolve Domain only when an operation needs Domain context.

---

## D13 — Prefer relative references to "the Domain"

**Decision.** Where the actual Domain name is not semantically important, Standards/documents/tools
refer to the effective `Domain` rather than embedding the current name.

**Reason.** Relative reference is portable and rename-safe.

**Exception.** Explicit names remain appropriate for navigation, cross-Domain references,
composition and provenance where identity matters.

---

## D14 — Renames and aliases belong in Domain metadata

**Decision.** Where rename continuity is needed, the authoritative Domain metadata may record
previous names/aliases.

**Reason.** Names are often used for conversational navigation and reference resolution, while
ordinary member artefacts should not require rewrites after a rename.

**Consequence.** Alias/previous-name schema is part of the Domain Standard/detail, not a
document-by-document migration mechanism.

---

## D15 — `AIDE_Domain.yaml` is the explicit composition/clarification mechanism

**Decision.** Use `AIDE_Domain.yaml` when natural implicit rules do not express the intended
Domain.

**Reason.** A dedicated explicit mechanism is simpler than proliferating exceptions across Index,
solution and project rules.

**Examples.** Compose several solutions/projects/Indexes, combine differently named roots, or
deliberately separate structures that would otherwise resolve together.

---

## D16 — One Domain file may contain multiple independent Domain declarations

**Decision.** One physical `AIDE_Domain.yaml` contains a `Domains` collection and may declare
multiple Domains.

**Reason.** A folder may legitimately contain multiple explicit Domains. Restricting one file to
one Domain would require arbitrary extra filenames or directory structure.

**Consequence.** A Domain entry, not the physical file, is the authoritative individual
declaration. Co-location in one YAML file implies no relationship.

---

## D17 — Domain hosts settings but does not define them

**Decision.** Domain defines the location, format and coexistence conventions for Domain-context
settings. Each setting owner defines its own schema and behaviour.

**Reason.** Domain needs a shared context store, but absorbing Review/Build/Deployment/etc.
configuration semantics would turn it into a generic configuration subsystem.

**Consequence.** Domain does not define setting defaults, validation, precedence, inheritance or
combination rules.

---

## D18 — `Branch` is the structural selector for Domain settings

**Decision.** Settings may be attached to the Domain root or to a Domain-relative structural
`Branch`.

Conceptual form:

```yaml
Branch: docs/api
Settings:
  SomeSetting1:
    ...
  SomeSetting2:
    ...
```

No Branch means Domain-root attachment.

**Reason.** `Scope` is already a defined AIDE applicability concept. `Branch` expresses structural
placement without semantic collision.

**Consequence.** The setting owner decides how declarations found on different Branches combine,
inherit or override, if at all.

---

## D19 — Discovery is target-based, not session-based

**Decision.** Resolve Domain for the current target/focus when needed. Do not assume one session
has one Domain.

**Reason.** A session may work across several Domains or with domainless material.

---

## D20 — Domain discovery searches upward

**Decision.** Starting from the current target/focus, Domain discovery considers available enclosing
paths and recognised structures before allowing a local project/solution/Index to establish an
implicit Domain.

**Reason.** Opening a nested folder or project must not change the effective Domain when a higher
solution or explicit Domain already contains it.

**Consequence.** Do not stop at the nearest marker. Collect enough enclosing evidence to establish
the authoritative effective Domain.

---

## D21 — Upward discovery has meaningful stop boundaries

**Decision.** Upward search stops at the nearest appropriate operational discovery boundary rather
than scanning unbounded ancestors.

Common boundaries include:

- explicit supplied boundary;
- workspace/container root;
- repository/worktree root;
- Documents;
- Desktop where relevant;
- AppData/application-data root or equivalent;
- other recognised user/application storage root; and
- filesystem/mount root as fallback.

**Reason.** Unrestricted ancestor scanning creates surprising governance and accidental matches.

**Consequence.** A discovery boundary limits search only; explicit Domain composition may reference
roots beyond that boundary where supported.

---

## D22 — Repository root is initially a discovery boundary, not an implicit Domain type

**Decision.** Repository/worktree root is not automatically a Domain merely because it is a
repository.

**Reason.** The current demonstrated Domain boundaries are Index, solution, project and explicit
Domain. Repository Domain semantics should be added only if a real case shows value beyond those
structures.

---

## D23 — Ambiguity fails visibly

**Decision.** Domain resolution does not silently merge, rank or guess between contradictory
authoritative claims.

**Reason.** The value of Domain depends on deterministic context resolution.

**Examples.** Conflicting explicit claims, unresolved membership where multiple Domains share a
folder, or broken explicit root references produce an unresolved/error result.

---

## D24 — No Domain is a valid state and does not disable AIDE

**Decision.** Absence of a resolvable Domain means only that Domain context/settings are unavailable.

**Reason.** AIDE Standards, Tools, Documentation Methodology and other behaviours can operate
without a Domain.

**Consequence.** Domain is not an AIDE activation switch.

---

## D25 — Domain produces one canonical Standard

**Decision.** The Domain Design is intended to produce `AIDE_Domain@v1` as the common AI-facing
contract.

**Reason.** Domain resolution must behave consistently across Design-side and Build-side contexts.
One canonical Standard is easier to deploy and reason about than separate local implementations.

**Consequence.** No dedicated Domain Tool is currently justified; add one only if a demonstrated
repeatable action requires it.

## D26 — Domain-capable structures are semantic Item Types

**Trigger / problem.** The v1 Domain contract hard-codes `AIDE Index`, solution and project as
recognised structure kinds. The new generic Index framework introduces an owner-defined Item Type
contract that can classify the same structures without Domain duplicating their full recognition
semantics.

**Decision.** Domain consumes semantic Item Types and maintains the system-approved subset that may
establish Domain context.

**Consequence.** Type owners define recognition/provisions; Domain defines only Domain eligibility
and the Domain-relevant structural relationship contract.

## D27 — Generic Index is not automatically Domain-defining

**Trigger / problem.** Once Index becomes generic, many valid Indexes describe repositories,
collections or other boundaries that should not automatically become governance Domains.

**Decision.** Remove generic `Index` from the implicit Domain-defining rule. A semantic type such as
`DocumentationTopic`, a native `Solution`/`Project`, or explicit Domain declaration must supply
the approved boundary evidence.

**Consequence.** An Index may still host Domain metadata/settings for a Domain established by an
approved type. An unusual Index-backed Domain can use an approved semantic type or explicit
`AIDE_Domain.yaml` rather than relying on generic Index existence.

## D28 — Domain-defining assignment is restricted to Core/Domain

**Decision.** Item Type Definitions cannot set their own `domainDefining: true`-style authority.
Domain owns the approved type list and any derived recognition registry.

**Reason.** Domain context affects governance and must not be obtainable as an accidental extension
privilege.

## D29 — Compile a thin Domain Recognition Registry

**Decision.** Runtime implementations may derive a compact recognition projection from the current
Domain-approved Item Types.

**Reason.** Domain resolution sits on a frequent path and should not repeatedly load every full
Standard or type definition.

**Constraint.** The registry is derived optimisation state. Domain Design plus the owning Item Type
Definitions remain authoritative.

## D30 — Add a Domain propagation-stop boundary without designing inheritance

**Trigger / problem.** An enclosing Domain sometimes must not propagate through a structural
boundary, even though the content below may not yet define its own Domain. Waiting for a full child
Domain inheritance model would leave no clean way to express that current need.

**Decision.** Introduce Domain-owned `DomainPropagation: Stop` semantics. It blocks enclosing Domain
propagation below the marked structure and forces independent resolution beneath it.

**Non-goals.** The marker does not create a child Domain, define inheritance/merge, or set generic
precedence.

## D31 — Issue Domain v2

**Decision.** Publish the reconciled contract as `AIDE_Domain@v2` with migration posture `None`.

**Reason.** The semantic recognition/authority model changes, but no existing governed document
requires automatic content transformation merely to adopt the new release. Indexes and Domain
representations are reconciled when next substantively updated or when an operation specifically
needs the v2 semantics.

---
Dependencies: !AIDE_DocumentationMethodology@v21, Core_Domain_Design_v2, AIDE_Index@v1
References: Core_Index_Decisions_v1, DocumentationMethodology_Decisions_v19
