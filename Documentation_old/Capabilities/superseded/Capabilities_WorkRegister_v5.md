# Capabilities — Work Register

> **Version 5** (2026-08-28). **Production chain and deployment work items.** `WR11` (DocMeth
> work item: package manifest document type), `WR12` (DocMeth work item: build record document
> type), `WR13` (Deployment subtopic design). WR1–WR10 unchanged from v4.
>
> Created: 2026-08-27 | Last modified: 2026-08-28

---

## WR1 — Message to DocMeth: Overview type and metadata standard

**Status:** Open
**Raised:** 2026-08-27

Two items for DocMeth via cross-project message:
1. **Overview document type** — define and record per `D5` (the Overview type decision).
   Carry the type's purpose, content rules, scoping/delegation behaviour, and working-surface
   rule.
2. **Document metadata standard** — created and last-modified dates on all governed documents
   per `D6` (the metadata standard decision).

---

## WR2 — Continue baseline re-admission

**Status:** Open
**Raised:** 2026-08-27

Work through remaining Workflow corpus elements block by block, confirming or discarding each
against the capability model. Nothing is re-admitted without explicit decision.

---

## WR3 — Principles topic: produce a standard

**Status:** Open
**Raised:** 2026-08-27

Principles is confirmed as a top-level topic (`D8`, Principles separation). It will produce
a published standard as an outcome. Scope, content and structure to be worked through.

---

## WR4 — Standards Standard: produce first draft

**Status:** Open
**Raised:** 2026-08-27

Design the Standards Standard itself — the standard governing how standards and tools are
authored, weighted, structured, and published. This is the primary output of the Standards
subtopic.

**Depends on:** completing the remaining design areas in `Capabilities_Standards_Design` v2
§10 (the deliberately open items) — versioning, publishing, and currency (`Q7`, now resolved).

---

## WR5 — AIDE-scoped standard: contribute runtime rules

**Status:** Open (revised)
**Raised:** 2026-08-27
**Revised:** 2026-08-27

Produce a separately published standard, scoped to AIDE contexts, containing the runtime
conflict hierarchy, deviation handling, and weight-honouring rules. The content is defined in
`Capabilities_Standards_Design` v2 §8 (conflict handling). Deploys alongside the Standards
Standard (same plugin, same package) but is its own artefact.

**Previously** this was a standard block for inclusion in the AIDE standard. Revised following
`D26` (standard blocks removed) and `D27` (AIDE standard delivery revised).

**Depends on:** `WR4` (Standards Standard first draft) and the AIDE standard design being ready
to coordinate scope.

---

## WR6 — Tools Standard: assess whether a standalone standard is needed

**Status:** Open
**Raised:** 2026-08-27

The tools design (`Capabilities_Tools_Design` v1) defines tool structure, interaction model,
and boundary with standards. Assess whether this warrants a standalone published Tools Standard
or whether the content folds into the Standards Standard (`WR4`). The answer depends on whether
tool authors need a separate artefact or whether one standard governing both kinds is cleaner.

---

## WR7 — Migrations standard: govern how migration files are written

**Status:** Open
**Raised:** 2026-08-28

Produce the standard governing how standard owners write migration files. Covers: structure
of `migrations.md`, per-version-transition format, required versus lazy classification per
change, sequential application requirement, what a migration instruction must contain for
`/migrations-apply` to execute it without judgement.

**Quality is load-bearing.** The migration mechanism (`D31`, two-skill mechanism) is a dumb
executor. A badly written migration file applied faithfully produces a confidently wrong
artefact. The standard must make the right thing easy and the wrong thing visible — the failure
mode should be "author couldn't publish" rather than "author published something ambiguous."

**Depends on:** `D28`–`D34` (the migration decisions). Independent of `WR4` (the Standards
Standard) — can proceed in parallel.

---

## WR8 — Build `/migrations-check` skill

**Status:** Open
**Raised:** 2026-08-28

Build the diagnostic skill that reports pending migrations. Enumerates available skills matching
the `{key}_pendingmigrations` naming convention, reads version from YAML frontmatter, compares
against the `AppliedMigrations` section in the domain's context file. Reports required and lazy
changes pending. Does not act.

**Trigger inventory** (`Q10`) feeds the skill's description and the always-on instruction line
that points to it.

**Depends on:** `WR7` (migrations standard — needed to know what the skill is checking against)
and `Q9` (probe results may refine the enumeration mechanism).

---

## WR9 — Build `/migrations-apply` skill

**Status:** Open
**Raised:** 2026-08-28

Build the execution skill that applies pending migrations. Reads the pending list, reads
`migrations.md` files stored with each standard skill, applies changes in version order, outputs
updated files for download. Updates the `AppliedMigrations` record.

**Execution surface is the user's choice** (`D31`). The skill works in chat, Cowork, or Code
without a separate handoff prompt.

**Depends on:** `WR7` (migrations standard) and `WR8` (`/migrations-check`).

---

## WR10 — Probe: chat-side plugin metadata visibility

**Status:** Open — empirical test
**Raised:** 2026-08-28

Run a probe to determine whether a chat-side skill can programmatically enumerate installed
plugins and their version numbers. Results feed `Q9` (the open question) and may refine `D32`
(plugin currency detection via naming convention).

A parallel GPT search has been prompted to cover the same ground independently. Compare results
before running the probe.

---

## WR11 — DocMeth work item: package manifest document type

**Status:** Open — for DocMeth batch
**Raised:** 2026-08-28

A new document type is needed: **package manifest**. This is the contract between
capability-specific production and generic deployment (`D35`, five-stage production chain). The
manifest carries: required-migration flags, the standard version each migration attaches to,
platform applicability per file, and a removal list for deprecated skills.

**Not a message to DocMeth** — noted as a work item to be included in the DocMeth batch when
that topic is next worked. The manifest type definition, along with `WR12` (build record type),
will go across in one pass.

---

## WR12 — DocMeth work item: build record document type

**Status:** Open — for DocMeth batch
**Raised:** 2026-08-28

A new document type is needed: **build record** (or output record). Machine-maintained, never
hand-edited. Holds: what was built, what version, what's deployed, and when. Serves as the
resumption point for re-running any stage of the production chain (`D35`), and prevents build
state from polluting the design file (`D36`, capability versioning).

**Generalises.** Anything that produces versioned outputs from a source document can use this
type — not limited to capability artefacts.

**Not a message to DocMeth** — noted as a work item for the DocMeth batch alongside `WR11`
(package manifest type).

---

## WR13 — Deployment subtopic: design

**Status:** Open
**Raised:** 2026-08-28

Design the Deployment subtopic (`D37`, Deployment as a subtopic). Covers: platform deployment
package production, publish-to-plugin mechanism, manifest consumption, platform-specific
variance (git-hosted for Claude, potentially different for OpenAI), skill removal handling,
and the `{key}_pendingmigrations` version bump on required migration.

**Generic service.** Deployment is platform-agnostic at its interface. It takes a deployment
package and manifest, does not know or care what produced them.

**Depends on:** `D35` (five-stage chain), `D37` (Deployment subtopic), and `Q11` (re-runnability
design).

---

**Depends on:** `Capabilities_Decisions` v5.

**Methodology:** v17
