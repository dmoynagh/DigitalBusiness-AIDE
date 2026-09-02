# Capabilities Standards — Design

> **Version 4** (2026-08-29). Reconciles the Standards child design with the eight-component
> parent architecture, retaining the weight/facilitation model while consuming Tags, Scope,
> Dependencies, Migration, Review, Build, Package/Manifest, and Deployment boundaries.
>
> Created: 2026-08-27 | Last modified: 2026-08-29

---

## §1 — Scope

Standards defines the Standard capability kind: role, rule/weight structure, canonical production,
and generic usage behaviour. It does not own individual domain Standards or shared mechanisms that
now have peer components.

## §2 — Role and purpose

A Standard provides guides, rules, advice and support focused on adding value and facilitating
effective work. Enforcement may be one of its roles but is never its primary lens; requirements are
framed through the consequence/value of meeting them.

A Standard shapes decisions and behaviour over a context. A named invokable action is a Tool.

## §3 — Weight system

Four weights remain:

- **Requirement** — must be met for the stated outcome/consumer to work; not open to ordinary
  judgment.
- **Expectation** — default position; departure is allowed but must be declared visibly.
- **Guidance** — default/best practice; departure is allowed and its consequences are owned.
- **Context** — information/reasoning with no obligation.

Every weighted unit states enough reason/consequence to preserve facilitation rather than bare
authority.

## §4 — Weight attachment and chunkability

Weight is a semantic property of addressable/chunkable Standard content.

- optional document default;
- every addressable section/unit carries its effective weight;
- statement-level override only where genuinely different.

Nearest declaration wins. Platform builders may render the semantic weight differently where the
target retrieval/chunking model needs another representation, but must not change its meaning.

## §5 — Outputs and audiences

Standards produces:

1. **Standards Production Standard** — for authors/builders of Standards.
2. **Standards Usage Standard** — for AI sessions operating under Standards.
3. Optional human **Guide** outcomes declared by individual capability designs.

The Standard is terse and complete; a Guide is explanatory. Both derive from the same Design and
may not disagree about substance.

## §6 — Canonical Standard contract

A canonical Standard contains only the capability meaning needed by consumers and Build, including
where applicable:

- formal identity/common name/release version;
- purpose and rules with effective weights;
- `AIDE_Scope` declarations;
- `AIDE_Dependencies` declarations;
- `AIDE_Migration` summary/transition declarations;
- owner-defined Tag/Dependency Builder definitions;
- Review expectations/profiles where the capability requires them; and
- capability-specific platform addenda.

Generic platform skill/plugin/bundle metadata does not belong in the canonical design contract.

## §7 — Production

```text
Capability Design
      ↓
Build Capability
      ↓
canonical Standard
      ↓
effective Build Config
      ↓
Build WorkPackage
```

Build Capability applies the Standards Production contract to confirmed design. The resulting
canonical Standard is the authoritative capability outcome passed to Build side. If Build side must
reopen the internal Capability Design to understand required capability behaviour, the canonical
outcome/WorkPackage is incomplete.

Platform realisation, contribution packaging, package/manifest construction, and Deployment belong
Build/Deployment side.

## §8 — Scope, Tags, and Dependencies

Standards consumes `AIDE_Scope`; it does not define another applicability language.

Standards may embed `AIDE_TagBuilder` or `AIDE_DependencyBuilder` blocks where that Standard owns the
semantics from which generated tags/dependencies are derived. Tags/Dependencies own builder
execution/storage/query contracts.

## §9 — Migration and release

Standards may change existing consumers. Each capability release therefore follows
`AIDE_Migration` and positively declares its version-level posture: Required, OnUpdate, or None.

The capability release version is distinct from the DocMeth version of the Design/Brief/source
documents used to author it. Package identity/build integrity and deployment state are also distinct
concepts under the parent contract.

## §10 — Review

Standards uses `AIDE_Review` rather than defining a local review mechanism. Production may select an
appropriate Review Profile for substantive integrity, weight justification, conflict, or other
capability-specific concerns.

Tone/facilitation quality is assessed through Review/judgment, not a mechanical publishing gate.

## §11 — Usage, conflict, and deviation

The Standards Usage outcome defines generic runtime behaviour. The retained resolution principles
are:

1. combine compatible Standards;
2. where genuine opposition exists, higher weight governs the point;
3. equal-weight genuine conflict is surfaced/escalated rather than silently resolved; and
4. direct human instruction may override a Standard, but the displaced Requirement/Expectation and
   consequence are surfaced/recorded as appropriate.

Scope determines whether the Standard is applicable before conflict resolution is considered.

## §12 — Ownership boundary

Standards owns Standard meaning, weight structure, canonical Standard production requirements, and
generic usage behaviour.

Peers own:

- Tags — classifications/builders/query;
- Scope — applicability;
- Dependencies — dependency/version state/order;
- Migration — transition semantics/execution;
- Review — independent assessment;
- Build — platform realisation/WorkPackage;
- Deployment — set-aware distribution/publication.

---

**Depends on:** `Capabilities_Design_v6`, `Capabilities_Decisions_v12`.

**References:** `Capabilities_Standards_Brief_v2`, `Capabilities_Tools_Design_v2`,
`AIDE_Scope@v1`, `AIDE_Dependencies@v2`, `AIDE_Migration@v1`, `AIDE_Review@v1`.

**Methodology:** v17
