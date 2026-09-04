# Documentation Methodology — Decisions

> **Version 17** (2026-08-31). Preserves the existing history and records the Decisions-model
> completeness correction, proportionality clarifications, and v19 release treatment.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

## D1 — Metadata containers are generic hosts

**Decision.** DocMeth owns placement/coexistence/compact rendering for header metadata, temporary
state and footer metadata. Contributing owners retain semantics.

## D2 — Documentation Methodology conformance is a Dependency

**Decision.** Retire the special `Methodology: vN` footer from v18. A document records its
saved/proven DocMeth conformance through `AIDE_Dependencies`.

**Reason.** This removes a duplicate version-gap/checkpoint mechanism and lets Migration govern
Required/OnUpdate/None transitions consistently.

## D3 — v18 migration posture is OnUpdate

**Decision.** v18 is `OnUpdate`.

**Reason.** v17 documents remain safely readable. The metadata/conformance model should be applied
when a document is next changed rather than forcing a corpus-wide rewrite merely to refresh
metadata. An operation that explicitly requires v18-only semantics can require migration first.

## D4 — Tags and Dependencies are hosted, not redefined

**Decision.** `Tags:` and `Dependencies:` are footer properties hosted by DocMeth. Their internal
grammar/build/query/conformance semantics remain with `AIDE_Tags` and `AIDE_Dependencies`.

## D5 — Identity is header metadata

**Decision.** Formal Core `Identity:` metadata is hosted in the header container where a governed
document exposes a referenceable identity. Filename and formal identity remain distinct.

## D6 — Temporary state is compact and owner-labelled

**Decision.** An optional temporary state container is placed near the top of the document.
Entries require stable owner identity plus concise human-readable title/message. The owner alone
defines lifecycle/content.

## D7 — WorkPackage execution semantics move to Build

**Decision.** DocMeth retains WorkPackage/Outcome document naming and archive integration but
delegates generic WorkPackage contract/execution/validation/return semantics to
`AIDE_WorkPackage@v1` and `AIDE_Build@v1`.

## D8 — Machine content remains compact

**Decision.** Metadata, derived state and generated operational content should be as compact as
practicable in human-readable documents.

## D9 — Re-establish a current Documentation Methodology Design

**Decision.** `DocumentationMethodology_Design_v15` is the confirmed internal model from which
the current published outcomes are produced.

**Reason.** A distributable outcome should have an authoritative defining source. The v18 Guide
already describes Design as the confirmed internal position; the operational closure package had
not included the older Design master.

## D10 — Publish a canonical Documentation Methodology Standard

**Decision.** Produce `AIDE_DocumentationMethodology_Standard_v1` with formal capability identity
`AIDE_DocumentationMethodology@v18`.

**Reason.** Documentation Methodology is reusable AI-facing behavioural infrastructure and should
use the same Design → canonical Standard → Build/Deployment path as other AIDE capabilities.

## D11 — Retain the Guide as a human companion

**Decision.** `DocumentationMethodology_Guide_v18` remains the human-readable explanatory outcome.
It is not replaced by the Standard.

**Reason.** The Standard is the concise AI operating contract; the Guide carries richer examples,
rationale and detailed explanatory material. Both derive from the same Design.

## D12 — Documentation Methodology Standard version follows the established methodology release

**Decision.** The canonical Standard for the current methodology release is
`AIDE_DocumentationMethodology_Standard_v18.md` with formal identity
`AIDE_DocumentationMethodology@v18`.

**Reason.** Documentation Methodology already has an established release lineage through v18.
Using `_v1` for the first Standard representation creates an unnecessary second visible version
number for the same methodology state. Aligning the Standard filename with the methodology
release preserves continuity and makes the Standard/Guide pair visibly one release.

**Scope.** This does not collapse the general distinction between document version, capability
release version, package identity, and deployment state. It is a deliberate alignment for this
existing methodology lineage.

## D13 — Legacy `Methodology: v17` supplies the migration starting checkpoint

**Decision.** For the v17→v18 transition only, where no Documentation Methodology dependency
checkpoint exists, an unambiguous legacy `Methodology: v17` declaration is interpreted by
Migration as proven conformance through `AIDE_DocumentationMethodology@v17`.

The interpretation is read-only until a qualifying update/save. Successful migration writes the
v18 dependency checkpoint and removes the legacy line.

**Reason.** v17 predates the generic Dependencies checkpoint. Without this bridge the v18
transition describes the target change but does not mechanically define where Migration obtains
the old conformance checkpoint.

## D14 — No dedicated Documentation Methodology Tool yet

**Decision.** Do not create a DocMeth-specific Tool at this stage.

**Reason.** The demonstrated actions are already owned by generic capabilities such as Migration,
Build Capability and Review. A new Tool without a distinct repeated action contract would add
machinery rather than capability.

## D15 — The common Bundle becomes the normal operational distribution

**Decision.** Include the Documentation Methodology Standard in the common AIDE Standards/Tools
Bundle. Once a project has that Bundle, the Guide is not separately required merely to obtain
operational DocMeth behaviour.

**Reason.** This makes the methodology deployable through the same common operating environment
as the other AIDE Standards/Tools while preserving the Guide as the richer human companion.


## D16 — Restore the full Decisions contract to the canonical Design and Standard

**Trigger / problem.** Review of current project use found that the v18 Guide still carries the
established substantive Decisions model, while the re-established Design and canonical Standard
compress it to a much weaker rule. The current Standard therefore does not reliably reproduce the
behaviour expected when it is the only runtime representation available to an AI.

The production path makes this a source-completeness problem as well as an output-completeness
problem: canonical Standards are produced from confirmed Design and production is not authorised
to recover missing capability meaning from Decisions history or invent it during compression.

**Alternatives considered.**

- Leave the Standard concise and rely on the Guide when richer behaviour matters. Rejected because
  the Standard is explicitly the normal deployable/runtime representation and the Guide is not
  expected in every consuming project.
- Expand only the Standard by copying behaviour from the Guide. Rejected because that would repair
  the outcome from a source the production contract does not treat as the authoritative capability
  definition, leaving the Design under-specified.
- Weaken the Guide to match the Standard. Rejected because the stronger model addresses the real
  cost of repeated re-derivation and already contains proportionality safeguards.

**Decision.** Retain the established Decisions model and make it explicit in the confirmed Design,
then produce the canonical Standard from that Design. Decisions records synthesized substantive
reasoning for a future Design reader: the trigger/requirement, problem, genuine alternatives, key
reasoning/distinctions, decision, and important consequences/trade-offs as applicable and
proportionate. Non-trivial rejected alternatives remain visible. Existing historical entries are
not rewritten.

**Consequences.** The canonical AI-facing contract becomes sufficient to reproduce the intended
behaviour without requiring the Guide. The Guide remains the richer explanation, not an alternate
source of missing semantics. Existing short historical entries remain valid history; the stronger
recording discipline applies prospectively.

## D17 — Make the event trigger objective and the record synthetic, not transcript-like

**Trigger / problem.** The phrase “when the reasoning is material” in the v18 Standard allows a
substantive Design change to escape the Decisions record based on a subjective judgment that its
reasoning was not important enough. At the same time, strengthening the rule without a boundary
could turn editorial maintenance or ordinary conversation into documentation ceremony.

**Alternatives considered.**

- Keep “material reasoning” as the only trigger. Rejected because it weakens the knowledge-
  preservation rule precisely when the author underestimates future re-derivation risk.
- Record every textual Design edit and every discussion branch. Rejected because this confuses
  document maintenance with design decisions and would create disproportionate burden.

**Decision.** A Decisions event is triggered by a change to the **confirmed substantive Design
position**, a requirement established or materially revised, or a rejected alternative a future
reader could reasonably re-derive. Purely editorial, formatting, metadata, migration, mechanical
maintenance, or application of an already-recorded decision is not by itself a new design
decision.

Preserve the reasoning necessary to reconstruct why the decision was reached; do not preserve
discussion merely because it occurred. Proportionality controls depth. A genuinely trivial
alternative may be omitted.

**Consequences.** The trigger is objective enough to protect knowledge while the depth rule remains
lightweight. `Decision + Reason` remains acceptable for genuinely simple decisions, but it is not a
sufficient template for work that actually involved meaningful alternatives, distinctions or
trade-offs.

## D18 — Keep Decisions at Design granularity and preserve the downstream boundary

**Trigger / problem.** Current project practice has sometimes expanded child Designs while leaving
their substantive reasoning permanently in a parent Decisions register. The v18 Guide already says
Decisions follows Design granularity. A separate inconsistency in the Guide also says in one place
that Decisions may feed a Guide, contradicting the core rule that Decisions informs Design and
nothing downstream.

**Decision.** Retain same-granularity recording: an independently expanded child Design normally
keeps its substantive reasoning in a Decisions record at that same scope; condensed topics may use
a Decisions section. Parent Decisions remains the correct home for parent-level architecture.
Apply this prospectively rather than relocating or rewriting historical entries.

Decisions remains outside downstream outcome production. If reasoning is necessary for correct
implementation or use, that meaning must be represented in the current Design and may then be
expressed in the downstream outcome. Outcomes do not reach back to Decisions as an input.

**Consequences.** Future retrieval aligns the “what” and “why” at the same scope without disturbing
history. Existing parent-level records may be cited from new child Decisions entries where useful.
The contradictory Guide sentence is corrected in the next Guide issue.

## D19 — Issue the correction as v19 with no artefact migration requirement

**Trigger / problem.** v18 has already been issued. Replacing its bytes in place would violate the
issued-output version rule, while issuing a Standard file version different from the methodology
release would undo the deliberate version alignment recorded in D12.

**Decision.** Issue the corrected methodology as `AIDE_DocumentationMethodology@v19`, with
`AIDE_DocumentationMethodology_Standard_v19.md` and `DocumentationMethodology_Guide_v19.md`.
Declare the v19 transition `None` and retain the v18 `OnUpdate` transition history.

**Reasoning.** v19 corrects the canonical behavioural contract and clarifies existing methodology
meaning; it does not require existing governed documents to be structurally or textually rewritten.
A document at the v18 checkpoint can traverse v19 without content migration and persist the v19
checkpoint on its next qualifying save under normal Dependencies/Migration behaviour.

**Consequences.** No mass migration or retrospective Decisions rewrite is required. The common
Standards/Tools Bundle and other runtime distributions should replace the v18 Standard with v19 on
their next regeneration/deployment.

---
Dependencies: !AIDE_DocumentationMethodology@v19, DocumentationMethodology_Design_v16
References: DocumentationMethodology_Guide_v19, AIDE_Dependencies@v2, AIDE_Migration@v1, AIDE_StandardsProduction@v1
