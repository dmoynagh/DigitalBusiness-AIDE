# AIDE Rebuild — WIP v9 Delta

> Changes to apply to WIP v8 to produce v9. Three parts: version-note update,
> line-level edits to existing sections, and a new section (§15a) recording
> item 7 progress.

---

## Version note (line 3)

Replace with:

> **Version 9** (2026-09-07). Item 7 progress: component naming pass —
> standing rules, purpose lines for twelve components, three new multi-AI
> components surfaced, Core deferred by design. Fixes stale §11a status line
> and downgrades four missing Contents entries to documentation debt.

---

## Edit 1 — Contents entries (lines 19–22)

The four entries for the lifecycle model, the design half, AIDE scope and
containers, and structure vs transport currently promise sections whose body
is missing. Downgrade each. Replace:

```
- **The lifecycle model** — four modes, cross-cutting threads.
- **The design half** — brief, design, decisions; universal across project types.
- **AIDE scope and containers** — what AIDE is, the root, how containers earn their place.
- **Structure vs transport** — meaning drives the tree; binders carry documents into context.
```

With:

```
- **The lifecycle model** — unchanged from v2, not yet written up.
- **The design half** — unchanged from v2, not yet written up.
- **AIDE scope and containers** — open; depends on Q8 (which containers earn their place). Not written.
- **Structure vs transport** — unchanged from v2, not yet written up.
```

Add after the "Next actions" Contents entry:

```
- **Item 7 progress** — component naming: standing rules, purpose lines, new components, open items.
```

---

## Edit 2 — Stale §11a status line (line 399)

Replace:

```
tractable. **A is settled. B is largely settled. C is not started.**
```

With:

```
tractable. **All three are now settled** (see the SETTLED headers below).
```

---

## Edit 3 — §14 open questions: add item-7 consequences

After the current §14 "Added this session" block, add:

```
Added v9 (item 7 naming pass):
- A3 (AIDE scope and containers) is not a blocker for item 7; it depends on Q8
  which item 7 helps discharge rather than waiting on. Downgraded to
  documentation debt.
- A1, A2, A4 similarly not blockers — documentation debt.
- "Component" confirmed as the single word for the ownership unit. The old
  Capabilities-internal usage (D43, D60, D92) is subsumed.
- Capabilities is a grouping label for now, not a component — revisited if it
  earns a purpose.
- Q8 (Deployment and Principles container survival) is partly addressed:
  Deployment is parked with a purpose line but deferred mechanism; Principles
  has a settled purpose line. Neither is closed — survival as containers
  depends on the full picture.
```

---

## Edit 4 — §15 next actions: update item 7

Replace item 7:

```
7. Name the one-line task for each remaining component, then filter its contents against it.
```

With:

```
7. Name the one-line task for each remaining component, then filter its contents
   against it. **In progress — see §15a.** Twelve components have purpose lines;
   five Capabilities peers remain (Tools, Tags, Scope, Dependencies, plus the
   Capabilities grouping itself). Core is deferred by design. Consultation
   (multi-AI) sent for external review.
```

---

## New section — §15a. Item 7 progress — component naming

Insert after §15 (before end of file).

```markdown
---

## 15a. Item 7 progress — component naming

Working section. Records the standing rules, settled purpose lines, new
components surfaced, and open items from the item 7 naming pass (v9, voice
sessions 2026-09-07).

### Unit and terminology

**Component** is the single word for the ownership unit — any unit that adds
or extends functionality. It applies at every level. The old
Capabilities-internal usage (D43 "seven top-level Capabilities components,"
D60, D92) is subsumed; the word now means the same thing everywhere.

**Capabilities** is an organisational grouping — a wrapper for components
that extend the development environment (standards, tools, etc.). It is not
itself a component unless it earns a purpose. Components inside the
Capabilities grouping are components in their own right; the grouping is
just filing.

### Standing rules

These govern the whole naming pass and downstream filter work.

1. **Owner is whoever knows the most about it.** Ownership goes to the
   component with the deepest knowledge of the thing. Applies to block types,
   document types, workflow artefacts, and boundary disputes.

2. **Documentation methodology owns structure and mechanics, not content
   definitions.** It defines how documents are built and how the document
   workflow runs. It does not hold a registry of document types belonging to
   other components. The only things that live in methodology are genuinely
   global — a type used across many components where no single component knows
   the most about it.

3. **Each component defines its own block types and document types.** Project
   Design defines objectives, requirements, considerations. Working Practices
   defines work-in-progress, work register. Standards defines what a standard
   is (provisionally in methodology — see open items). Being written down as a
   document does not make something methodology's business.

4. **A purpose line is a filter criterion, not a description.** Its job is to
   reject content. A good line carries an outcome, a consumer, and a visible
   edge. If it rejects nothing from the component's own current documents, it
   was written from the corpus rather than from need.

5. **Mode and interaction pattern are separate axes.** Mode is the
   contract — what role an external AI plays. Interaction pattern (one-shot,
   multi-round, conversational) is how many rounds it takes. Any mode can use
   any pattern. Adversarial/challenge is an approach or style applied to a
   mode, not a separate mode. Adjudication (resolving competing outputs) is a
   role within a workflow, not a separate mode.

### Settled purpose lines

| # | Component | Purpose line | Key boundaries / reject-test notes |
|---|---|---|---|
| 1 | Documentation methodology | Define how documents are structured and created — the generic mechanics. | Not a registry of doc types. Specific types live with whoever knows the most. Provisionally holds the definition of what a standard *is* (see open items). |
| 2 | Standards | Make sure standards are applied, honoured, and kept current across the environment. | Owns use, application, and migration of standards. Does NOT own the document-shape definition of a standard (provisionally methodology). |
| 3 | Migration | Bring a document into line with the current version of every standard it depends on, before it is used. | Rejects: Migration Tool content (migration is an AI task, not a script), wide corpus scan material, presence levels and exact pins. |
| 4 | Review | Give work an independent check by a separate reasoning path, so problems are caught before the work is trusted. | Doesn't own fixing or quality rules. Already has five Types (Check, Inspect, Evaluate, Robust, Stress Test) — the challenge/adversarial concept is covered by Robust and Stress Test as approach, not a separate mode. |
| 5 | Research | Get an answer to an open question by putting more than one AI on it and pooling what comes back, so the result is stronger than any single pass. | Convergent — pools toward one answer. Distinguished from parallel solutioning (which keeps answers apart). NEW component. |
| 6 | Parallel solutioning | Get two or more AIs to each produce their own design from the same brief, independently, so different approaches can be compared before committing. | Divergent — deliberately keeps approaches independent. Resolution (picking the winner) is a separate flexible role: human, lead AI, or both depending on automation level. NEW component. |
| 7 | Consultation | Bring an external AI in to discuss something you're working through — a single question or an evolving thread — so its input shapes your thinking. | Defined by the ownership test: primary actor retains ownership of the work; external AI advises without owning the outcome. Renamed from "contributory input." Sent for external review. NEW component. |
| 8 | Messaging | Carry a message between AIs reliably — across sessions, platforms, or models — with a known envelope and confirmed receipt. | Owns the envelope and receipt. Does not own message content (sender's job) or route selection (platform transport). |
| 9 | Principles | Give any AI the durable, portable reasoning and interaction premises to think and act well — independent of platform or methodology. | Portability is the defining test. If a candidate principle only makes sense inside AIDE, it's not a principle — it's methodology or working practices. |
| 10 | Working practices | Own the workflows and behaviours for getting work done — including work-in-progress, work registers, and how design and build hand over — whatever the task. | Owns workflow artefacts end to end, definitions included. WIP and work register are NOT methodology's business. Divisional boundaries with project design and build to be resolved by "knows the most." |
| 11 | Project design | Produce a coherent specification for work of any size — one scalable architecture from simple single-document to complex multi-document structures. | Defines its own block types (objectives, requirements, considerations) and document types. Does not need to know about build. Handover mechanics belong to working practices. |
| 12 | Build | Take defined work and execute it — produce the outcome, report what was done. | Generic core plus specialised paths by work type. Core-vs-path ownership boundary deferred for "knows the most." Handover loop goes to working practices. |

### Deferred

| Component | Reason | Trigger |
|---|---|---|
| Core | Cannot be judged until everything else has declared what it needs. Core is defined by leftover shared requirements that have no natural home elsewhere. | Resolve last, after all other component purpose lines are settled. |
| AI Deployment | Parked (§6b). Purpose line settled: "Get the finished standards and behaviours live in a session, on whatever surface is in use." Mechanism deferred — will be hand-written, single-instance. | Revisit when mechanism is designed. |

### Not yet named

Five Capabilities peers have not been through the naming pass:

- **Tools** — not yet discussed.
- **Tags** — consumer is Scope; §9 already parks the Tags block; line may not be writable yet.
- **Scope** — CM-Q1 removed one of its two demonstrated consumers; check before writing.
- **Dependencies** — substance reduced by §11a; may no longer be a component (flagged moderate-to-strong, not yet decided).
- **Capabilities grouping** — organisational wrapper for now; revisited if it earns a purpose.

### New component candidates — parked

| Candidate | Description | Status |
|---|---|---|
| Decomposed collaboration | Different AIs solve different parts of a larger problem, then results are assembled. | Real pattern. Parked — no demonstrated need for a solo developer. |

### Open items from this pass

1. **Standards definition placement.** Where the concept of a standard, and its
   document type, is defined — methodology or the standards component.
   Provisionally in methodology (it's a document-shape question; sits naturally
   beside other doc-type definitions). Leaning toward capabilities. Review once
   the full standards side is worked through.

2. **Divisional boundaries: project design / build / working practices.** The
   handover between these three has plausible ownership claims from each side.
   Parked for "knows the most" once all three are named and side by side.

3. **Build specialisation paths.** Where the boundary sits between build's
   generic core and each specialised path, and whether a given path is owned
   inside build or by the component that knows that output type.

4. **Consultation external review.** A prompt was sent to an external AI asking
   whether consultation is a coherent distinct mode or collapses into another.
   Response received and triaged:
   - **Accepted:** the ownership test (who owns the outcome) as the defining
     boundary; separating mode from interaction pattern.
   - **Accepted with caution:** three proposed new modes (decomposed
     collaboration, adversarial challenge, adjudication). Challenge is already
     covered by Review's Robust and Stress Test types. Adjudication is the
     resolution role already noted in parallel solutioning. Decomposed
     collaboration is parked as a genuine pattern without demonstrated need.
   - **Rejected:** the four-axis model (mode, topology, lifecycle, integration)
     — over-engineering.
   - **Accepted:** rename from "contributory input" to "consultation."

5. **Core's eventual scope.** The previous Core design material (index, domain
   resolution, bootstrap, platform) is held as reference, not commitment. When
   another component surfaces a shared requirement with no natural home, check
   it against what Core originally proposed. Consideration only.
```

---

## Summary of changes

- Version note updated to v9.
- Four missing Contents entries downgraded to documentation debt.
- §11a stale status line corrected.
- §14 open questions updated with item 7 consequences.
- §15 item 7 updated to reflect in-progress state.
- New §15a added: twelve settled purpose lines, standing rules, deferred and
  parked components, five open items.
