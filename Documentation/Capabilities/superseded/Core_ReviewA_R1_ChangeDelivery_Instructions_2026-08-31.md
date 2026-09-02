# Core — Review A Round 1 — Change Delivery Instructions — 2026-08-31

## Purpose

Apply the Lead-dispositioned changes from `AIDE-Architecture-Review-A-Core-Substrate`, Round R1,
as one coherent Core substantive pass before Review A Round 2.

The current `Core_Binder_v1.md` is the authoritative baseline.

This is a correction/completion pass, not a replacement architecture. Preserve the load-bearing
Core model:

- an Index is authoritative for its registrations and Index-owned facts, not for registered-item internals;
- registration is selective and may stop at self-describing boundaries;
- Item Types are composable semantic classifications without a generic inheritance system;
- owner contributions are preserved by unrelated Index updates;
- Domain-defining authority is restricted to Core/Domain;
- ambiguity fails visibly rather than being silently merged/ranked;
- `No Domain context` is a valid state; and
- Bootstrap remains thin, subset-neutral and lazy.

## Review findings covered

Lead disposition:

- RA-R1-F1 — Change
- RA-R1-F2 — Change
- RA-R1-F3 — Change
- RA-R1-F4 — Change
- RA-R1-F5 — Change
- RA-R1-F6 — Change
- RA-R1-F7 — Change
- RA-R1-F8 — Change in part
- RA-R1-F9 — Change
- RA-R1-F10 — Change
- RA-R1-F11 — Change
- RA-R1-F12 — Change
- RA-R1-F13 — Decline
- RA-R1-F14 — Change, clarification only

## Required Core release set

Issue one coherent Core checkpoint with these replacements:

- `Core_Index_v5.md` replaces `Core_Index_v4.md`.
- `Core_System_Design_v8.md` replaces `Core_System_Design_v7.md`.
- `Core_System_Decisions_v7.md` replaces `Core_System_Decisions_v6.md`.
- `Core_Index_Design_v2.md` replaces `Core_Index_Design_v1.md`.
- `Core_Index_Decisions_v2.md` replaces `Core_Index_Decisions_v1.md`.
- `AIDE_Index_Standard_v2.md` replaces `AIDE_Index_Standard_v1.md`; formal identity becomes `AIDE_Index@v2`.
- `Core_Domain_Design_v3.md` replaces `Core_Domain_Design_v2.md`.
- `Core_Domain_Decisions_v3.md` replaces `Core_Domain_Decisions_v2.md`.
- `AIDE_Domain_Standard_v3.md` replaces `AIDE_Domain_Standard_v2.md`; formal identity becomes `AIDE_Domain@v3`.
- `Core_Bootstrap_Design_v3.md` replaces `Core_Bootstrap_Design_v2.md`.
- `Core_Bootstrap_Decisions_v3.md` replaces `Core_Bootstrap_Decisions_v2.md`.
- `AIDE_Bootstrap_Standard_v2.md` replaces `AIDE_Bootstrap_Standard_v1.md`; formal identity becomes `AIDE_Bootstrap@v2`.

Regenerate:

- `Core_Binder_v2.md`

Do not edit a generated Binder directly.

`AIDE_Domain@v3`, `AIDE_Index@v2` and `AIDE_Bootstrap@v2` use migration posture `None`. They change
the current semantic contract but do not require automatic transformation of existing governed
artefacts solely because the releases changed.

The coordinated Documentation Methodology pass is expected to issue
`AIDE_DocumentationMethodology@v22`. New Core documents created in this pass should use the truthful
current conformance dependency appropriate at issue time.

Do **not** rebuild the temporary common Standards/Tools Bundle as part of this checkpoint. Review A
must first re-review the revised architecture; broader runtime/deployment outputs remain deferred.

---

# 1. Core/Index — preserve generic recognition; remove the second registry concept

## Required model

Retain one optional generic runtime optimisation:

```text
Item Type Definitions
        ↓
optional ItemTypeRegistry
        ↓
recognised semantic Item Type identities/provisions
```

The registry remains a derived optimisation and is never semantic authority.

### Critical Domain authority constraint

The `ItemTypeRegistry` is **Domain-neutral**.

It must not contain a type-owner-controlled field whose presence can grant Domain authority.

In particular, an Item Type owner must not be able to publish:

```text
DomainCapable: true
domainDefining: true
DomainContainer: true
```

or an equivalent self-elevating declaration and thereby become a Domain root.

Domain eligibility is evaluated separately by `AIDE_Domain`, against the Domain-owned approved
recognition set.

Conceptually:

```text
Item Type owner
    defines:
    - identity
    - Identify
    - Provides

ItemTypeRegistry
    optionally accelerates:
    - recognition of the Item Type identity
    - provision lookup

AIDE_Domain
    separately defines:
    - which recognised semantic Item Type identities may establish/participate in Domain resolution
    - which native structure recognitions may establish/participate in Domain resolution
```

This preserves RA-R1-F5 simplification without weakening the Domain authority boundary.

## `Core_Index_Design_v2`

Carry forward the v1 Design except for the Domain/runtime seam.

Replace the current runtime/Domain wording so that:

1. `ItemTypeRegistry` is the only named generic compiled recognition projection.
2. The registry contains recognition/provision facts for Item Types, not Domain authority.
3. Domain may consume recognised Item Type identities from it, but Domain applies its own approved
   recognition set.
4. Domain may additionally use Domain-owned native recognisers that are not Item Types.
5. No separately named `DomainRecognitionRegistry` is part of the architecture.
6. Direct evaluation of authoritative Item Type definitions remains a valid fallback when no compiled
   registry is present/current.
7. Any persisted/built compiled registry is ordinary derived output and must retain enough source
   provenance to be invalidated/rebuilt safely; Core does not introduce a separate registry-build
   subsystem.

Update the deliberately-absent list if useful to state explicitly:

```text
- no owner-self-declared Domain-capable Item Type flag;
- no separate Domain Recognition Registry artefact.
```

## `Core_Index_Decisions_v2`

Preserve v1 decision history and add decisions recording:

### New decision — one generic Item Type projection

The optional `ItemTypeRegistry` remains the single generic compiled Item Type recognition
projection. Do not create a second Domain-specific registry for the same semantic recognitions.

Reason: Domain eligibility is an authority decision, not a second recognition system.

### New decision — runtime registry does not carry self-granted Domain authority

An Item Type owner cannot make itself Domain-capable through its definition or through registry
metadata. Domain owns the approved recognition set and filters recognised identities against it.

### New decision — direct recognition is the supported fallback

A compiled registry is optional optimisation. A conforming implementation may evaluate current
authoritative recognition definitions directly. Persisted compiled forms are derived outputs, not
required Core state.

## `AIDE_Index_Standard_v2`

Retain the v1 generic Index/Item/Item Type contract.

Change only the runtime/Domain seam:

- keep the optional `ItemTypeRegistry`;
- state that it contains Item Type recognition/provision facts and is Domain-neutral;
- remove the statement that Domain owns/derives a separate `Domain Recognition Registry`;
- state that `AIDE_Domain` alone owns the approved Domain recognition set;
- state explicitly that no Item Type owner or registry entry can self-grant Domain authority;
- permit Domain to consume a recognised Item Type identity from direct or compiled recognition and
  then apply Domain-owned eligibility separately.

Migration:

```yaml
Transition:
  Version: v2
  Posture: None
```

---

# 2. Core/Domain — finish the v2 refactor as v3

## Domain recognition model

Replace the incomplete "all Domain roots are semantic Item Types" model with the narrower honest
model:

```text
Domain-approved recognition
├── approved semantic Item Type identities
│   └── currently: DocumentationTopic
├── Domain-owned minimum native recognitions
│   ├── Solution
│   └── Project
└── explicit AIDE_Domain declaration
```

The list is owned and published by `AIDE_Domain`.

### Approval semantics

The Domain Standard must make the approval set explicit and versioned as part of the Standard itself.
Do not create another standalone approval-register artefact solely for this.

The first v3 approved recognition set should state:

| Recognition | Kind | Recognition owner | Domain authority owner |
|---|---|---|---|
| `DocumentationTopic` | semantic Item Type | Documentation Methodology | Core/Domain |
| `Solution` | native structural recognition | Core/Domain observes minimum native signature/authoritative membership relationship; native platform remains semantic authority | Core/Domain |
| `Project` | native structural recognition | Core/Domain observes minimum native signature/authoritative membership relationship; native platform remains semantic authority | Core/Domain |
| `AIDE_Domain` declaration entry | explicit Domain declaration | Core/Domain | Core/Domain |

The exact native platform formats are implementation observations, not AIDE ownership of solution or
project internals. Domain defines only the minimum recognition and containment/membership facts it
needs to resolve Domain context.

A generic `Index` is **not** in the approved set.

An Index may be the representation/host for a `DocumentationTopic` or may host Domain-owned
configuration for a Domain established by another approved recognition, but Index existence alone
never establishes Domain context.

## Remove generic `Index` from examples and explicit-root vocabulary

Reconcile every occurrence where current Domain text says or implies:

```text
Index | Solution | Project
```

as equivalent Domain root roles.

For documentation-backed roots use `DocumentationTopic`.

Examples should distinguish:

```text
Foo.sln + DocumentationTopic(Foo)     → one Foo Domain where authoritative identities match
Foo.sln + DocumentationTopic(Womble)  → separate Foo and Womble Domains where identities differ
```

A bare generic Index beside `Foo.sln` does not establish a Womble Domain.

## Explicit `AIDE_Domain.yaml` roots

Retain a root recognition assertion, but rename/define its semantics so it cannot grant authority.

Preferred canonical shape:

```yaml
Roots:
  - Recognition: Solution
    Path: Product.sln
  - Recognition: DocumentationTopic
    Path: docs/Product_Index_vN.md
```

`Recognition` means **expected approved Domain recognition**.

Rules:

- the token itself never creates Domain capability;
- the resolver independently recognises the target through the current authoritative/native/type
  recognition mechanism;
- the observed recognition must match the declared expected recognition;
- mismatch fails visibly;
- unknown/unapproved recognition fails visibly;
- generic `Index` is not a valid value merely because the path identifies an Index document.

If the existing field name `Type` is retained for compatibility/readability, give it exactly these
assertion semantics. Do not leave it in the current half-authoritative state.

## Propagation Stop

Retain the narrow:

```yaml
Domain:
  Propagation: Stop
```

model, but state its full consequence.

Canonical meaning:

> The enclosing effective Domain does not propagate through the marked structural boundary.
> Resolution below the boundary continues independently as though that enclosing Domain were absent.
> Independent resolution may therefore yield `No Domain`, an unresolved/error result, or another
> Domain. If another Domain is found below the stop, the current model defines no parent/child
> semantic relationship, inheritance, merge, settings propagation or precedence between the two.

Correct statements that currently say structural children *never* create implicit nested Domains.
The correct rule is:

> Under ordinary authoritative containment, structural children do not create a second implicit
> Domain. A deliberate `Propagation: Stop` terminates that containment propagation; independent
> resolution below the stop may establish another Domain, but it is not modelled as a child Domain.

### Stop representation

Do not add a generic filesystem marker file in v3.

v3 supports Stop on a recognised/registered Domain-aware structural boundary.

Where represented by an Index Item, the parent Index may register the significant boundary for the
purpose of locating/describing it and hosting the Domain-owned Stop property. That registration
does not transfer authority over the boundary internals.

Make traversal explicit:

1. while walking upward from the target, identify each crossed recognised structural boundary;
2. inspect the applicable Domain-owned boundary configuration, including a parent Index registration
   where that is the authoritative host;
3. if Stop applies to the crossed boundary, discard the enclosing Domain for content below it and
   continue independent resolution.

Arbitrary unregistered-folder exclusion remains deliberately absent until demonstrated.

## Domain settings/configuration host

Make explicit Domain declaration authority decisive.

Where an explicit `AIDE_Domain.yaml` Domain entry governs/composes the effective Domain:

- that Domain entry is the sole authoritative Domain metadata/settings host for that Domain;
- an Index-hosted `Domain:` configuration for the same effective Domain is not merged;
- duplicate/conflicting host state is an error requiring reconciliation.

Index-hosted Domain configuration remains valid for an applicable implicit Domain where no explicit
Domain entry governs it.

## Runtime recognition

Delete `DomainRecognitionRegistry` as a named architectural artefact.

Domain resolution may use:

- direct current semantic Item Type recognition;
- the optional generic `ItemTypeRegistry`;
- Domain-owned native Solution/Project recognisers;
- explicit Domain declaration parsing; and
- safe runtime caches.

Caching/compiled state is derived optimisation only.

No semantic Item Type definition can elevate itself to Domain authority. Domain must compare any
recognised semantic Item Type identity against its own current approved recognition set.

## `Core_Domain_Decisions_v3`

Preserve all historical decisions and add/reconcile decisions capturing:

1. **Approved recognition set is published by Domain.**
2. **Semantic Item Type indirection is used where a real reusable semantic owner exists; native
   Solution/Project recognition remains a minimum Domain observation, not a pair of invented AIDE
   Item Type owners.**
3. **Generic Index remains non-Domain-defining.**
4. **No separate DomainRecognitionRegistry.**
5. **Propagation Stop terminates propagation and may expose an independent Domain below without
   defining child-Domain semantics.**
6. **Stop is limited to recognised/registered structural boundaries in v3.**
7. **Explicit-root recognition field is a visible-failure assertion, never an authority grant.**
8. **Explicit Domain declaration is sole Domain metadata/settings host where present.**

Where older decisions state the pre-v3 literal kinds or imply every Domain-capable structure is an
Item Type, retain the historical entry but add a current decision that supersedes/refines that
specific part rather than rewriting history.

## `AIDE_Domain_Standard_v3`

Publish the reconciled contract above.

Dependencies should resolve to the current Core Index release (`AIDE_Index@v2`) and current
Documentation Methodology conformance at issue time.

Migration:

```yaml
Transition:
  Version: v3
  Posture: None
```

---

# 3. Core/Bootstrap — make Profile selection operational

## Effective Profile gates Contributions

The stable bootstrap flow becomes:

```text
persistent platform bootstrap
        ↓
resolve one effective Bootstrap Profile, if any
        ↓
establish the Profile startup set
        ↓
process applicable Bootstrap Contributions belonging to that startup set
        ↓
load full detail lazily when current work requires it
```

Rules:

- One effective Profile by default remains.
- No Profile remains valid.
- **No Profile means no Profile-selected AIDE startup set and therefore no automatic processing of
  deployed AIDE Bootstrap Contributions merely because they are physically available.**
- A Contribution is eligible for startup processing only when its owning material/capability is
  brought into play by the effective Profile, unless a future explicitly defined persistent
  bootstrap primitive says otherwise.
- Physical deployment/availability is not itself startup selection.

This is what makes Profiles genuinely subset-neutral on a host where several AIDE subsets are
deployed.

## Profile `Why`

Define:

- `What` — identity/material to bring into the startup set.
- `Why` — concise human/AI-readable rationale for why the Profile includes it.
- `Where` — locator/discovery information for the authoritative deployed material.

`Why` is **not executable conditional syntax** and does not create a second Scope/applicability
language.

If conditional applicability is needed within substantive capability behaviour, use the normal
owner/applicability mechanisms; Bootstrap does not invent another one.

## Contribution independence

Remove the undefined Bootstrap ownership claim for Contribution ordering.

Canonical rule:

> Bootstrap Contributions are order-independent. A Contribution must not require another peer
> Contribution to have executed first or depend on peer side effects. Required material presence is
> expressed through the normal Dependencies mechanism. If a future demonstrated startup case
> requires ordered actions, design that requirement explicitly rather than inferring platform file
> order.

This removes a prospective startup orchestration engine.

## `{bootstrap}` versus Item Type recognition

Add the explicit architecture note:

> `{bootstrap}` is deliberately a primitive pre-capability/pre-Index discovery cue. Bootstrap runs
> before richer AIDE Index/Item Type machinery can be assumed available, so it must not depend on
> Item Type recognition for its own initial discovery. The two recognition mechanisms are
> intentionally separate.

## `Core_Bootstrap_Design_v3`

Carry forward v2 and apply the changes above.

Also update any statement that Core/Bootstrap owns Contribution ordering to say it owns
Contribution discovery/eligibility and the order-independence contract.

## `Core_Bootstrap_Decisions_v3`

Preserve history and add decisions:

- effective Profile gates the Contribution startup set;
- no Profile does not activate every deployed Contribution;
- Profile `Why` is rationale, not an applicability expression;
- Contributions are order-independent;
- `{bootstrap}` remains deliberately pre-Index.

## `AIDE_Bootstrap_Standard_v2`

Publish these behaviours as the canonical runtime contract.

Migration:

```yaml
Transition:
  Version: v2
  Posture: None
```

---

# 4. Core system-level reconciliation

## `Core_System_Design_v8`

Update the reference architecture summary so it no longer claims a distinct
`DomainRecognitionRegistry`.

The Domain summary should state:

- Domain publishes/owns its approved recognition set;
- it consumes approved semantic Item Types where a genuine semantic owner exists;
- it owns the minimum native Solution/Project recognition needed for Domain resolution;
- generic Index remains non-Domain-defining;
- runtime recognition may reuse the generic `ItemTypeRegistry` without granting Domain authority.

Update Bootstrap summary so Profile gating of Contributions and no-Profile behaviour are clear.

Update Documentation Methodology seam text to match the coordinated v22 clarification:

- `DocumentationTopic` is the logical top-level-topic documentation boundary;
- its Index document declares/describes that boundary;
- subtopics are not independently DocumentationTopics merely because they have Design/Index state.

## `Core_System_Decisions_v7`

Preserve historical decisions.

Add system-level decisions only where necessary to record the cross-foundation consequence:

- Domain-approved recognition remains Domain-owned even after registry simplification;
- Profile selection is the startup subset authority inside Bootstrap;
- no new registry/startup ordering subsystem is introduced.

Do not duplicate all child Design reasoning already owned by Index/Domain/Bootstrap Decisions.

## `Core_Index_v5`

Update the current document register and references for all new versions.

Keep the operational container map unchanged.

Update the Core summary descriptions to reference:

- `AIDE_Index@v2`
- `AIDE_Domain@v3`
- `AIDE_Bootstrap@v2`

---

# 5. Explicitly declined Review finding

Do **not** implement RA-R1-F13.

Do not weaken stable Documentation Methodology Document Register authority based on the cited
Bootstrap dependency/reference lines.

The Lead disposition is:

- a Dependencies checkpoint below the newest available Documentation Methodology release may
  truthfully represent last saved/proven conformance; and
- a version-specific `References:` entry may intentionally identify the source version used.

This Review supplied no evidence of an actually stale stable Document Register row.

---

# 6. Validation before Binder regeneration

Before issuing `Core_Binder_v2.md`, verify at minimum:

1. No current Core source says generic Index existence can establish a Domain.
2. No current Domain example uses a bare Index as an independent implicit Domain root.
3. No current Core source defines or requires a separate `DomainRecognitionRegistry`.
4. `ItemTypeRegistry` contains no self-owned Domain authority field.
5. `AIDE_Domain@v3` contains the authoritative approved recognition set.
6. External Item Type owners cannot self-elevate to Domain capability.
7. Solution/Project native recognition has a named Domain-owned minimum contract without claiming
   ownership of native internals.
8. Propagation Stop explicitly permits independent resolution below the stop while defining no
   parent/child Domain semantics.
9. The Stop traversal/host rule is implementable for registered structural boundaries.
10. Explicit Domain root recognition is an assertion validated against observed recognition.
11. Explicit Domain declaration is sole settings/metadata host where it governs the Domain.
12. No Profile causes no automatic processing of unrelated deployed Contributions.
13. Profile `Why` is non-executable rationale.
14. Contributions are order-independent.
15. `{bootstrap}` is explicitly pre-Index.
16. All current document/version/dependency/reference rows are truthful at issue time.
17. Generated Binder manifest points only at the new Current masters.

## Review continuation

After application, return `Core_Binder_v2.md` to the Review A coordination context.

Review A remains `Continuing / High`; the revised Core substrate must be returned for a focused
Round 2 re-review before Review A can complete.
