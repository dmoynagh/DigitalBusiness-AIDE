# Capabilities Standards — Design

> **Version 7** (2026-09-02). Aligns Standard production with Capability Definition and Element release/checkpoint semantics.

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
Capability Definition + documented production inputs
      ↓
Update Capability Elements
      ↓
canonical Standard Element + evaluated-input checkpoint
```

Update Capability Elements applies `AIDE_StandardsProduction@v3`. If reassessment finds unchanged
meaning, only `LastEvaluated` advances. If meaning changes, the canonical Standard is validated and
the next Element release/history is confirmed. Capability Build/package/Deployment remain later.

## §7a — Capability-reference validation

Canonical production distinguishes saved dependency checkpoints and reader References from current
executable capability instructions. Executable capability references are versionless by default. A
specific release is used only where the instruction deliberately depends on or targets that release;
production validates that the specificity is intentional and correct rather than mechanically
advancing it to the newest available release.

`References:` carries no currency or conformance obligation. Dependency checkpoint advancement
remains owned by `AIDE_Dependencies`/`AIDE_Migration`.

## §8 — Scope, Tags, and Dependencies

Standards consumes `AIDE_Scope`; it does not define another applicability language.

Standards may embed `AIDE_TagBuilder` or `AIDE_DependencyBuilder` blocks where that Standard owns the
semantics from which generated tags/dependencies are derived. Tags/Dependencies own builder
execution/storage/query contracts.

## §9 — Migration and release

Standards may change existing consumers. Each changed Standard Element release follows `AIDE_Migration` and declares Required, OnUpdate, or None. Element release is distinct from source document version, containing Capability release/composition, Package identity and deployment state.

## §10 — Review

Standards uses `AIDE_Review` rather than defining a local review mechanism. Production may select an
appropriate Review Profile for substantive integrity, weight justification, conflict, or other
capability-specific concerns.

Tone/facilitation quality is assessed through Review/judgment, not a mechanical publishing gate.

## §11 — Usage, conflict, and deviation

The Standards Usage outcome defines generic runtime behaviour. Before a Machine Scope result is
relied upon, the consumer honours the current-tag precondition supplied by `AIDE_Scope`/`AIDE_Tags`.
A dependency conformance checkpoint behind the available capability release is expected steady state
and is not by itself stale, missing, or an update trigger; applicable Required Migration remains the
affected-use gate.

The retained resolution principles are:

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


## §13 — Capability Element production

Standards are Capability Elements. Production resolves the current Capability Definition and
Element Production state, separates document revision from semantic Element release, and advances
`LastEvaluated` without a release when reassessment finds unchanged meaning. The current published
contract is `AIDE_StandardsProduction@v3`.

---
Dependencies: !AIDE_DocumentationMethodology@v27, Capabilities_Design_v12, Capabilities_Decisions_v17
References: Capabilities_Standards_Brief, Capabilities_Tools_Design, AIDE_Scope, AIDE_Dependencies, AIDE_Migration, AIDE_Review
