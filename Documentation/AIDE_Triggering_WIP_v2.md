---
name: triggering
description: How AIDE standards get triggered and applied at the point of action — bootstrap model, multi-pronged enforcement, skill delivery pattern, trigger vocabulary; started 2026-09-23
sources: [chat]
aliases: [triggering, bootstrap, aidebootstrap, enforcement, work-check, OI-3]
---

# AIDE Triggering and Enforcement — Working Document

Status: working capture from the 2026-09-23 session (text then voice). Not yet placed into component documents. Replaces the scope of OI-3 "work-check skill".

Version 2 — added the ab369fa versioning-failure evidence (section 2) and the commit-sequence convention (section 12). Replaces v1.

Marking used below: **Agreed** = Dave stated or accepted it. **Proposed** = Claude's recommendation, not yet confirmed.

## 1. The problem

- Standards deployed as skills often don't load, and when loaded often aren't applied. Worked case: document versioning on save.
- Root causes: trigger descriptions written as purpose statements, not triggers; cross-cutting rules delivered as match-on-trigger skills; rules loaded early don't fire at an action many turns later; work type changes mid-session; the account instructions must stay at one bootstrap line.

## 2. Why loaded is not applied

- Models attend less to material in the middle of a long context than to the start or end ("lost in the middle"), and degrade generally as context grows ("context rot" — every one of 18 tested models degraded).
- A rule loaded at session start is stranded mid-context by the time the save happens. The model isn't ignoring it; it has gone quiet.
- Consequence: better wording alone won't fix it. The obligation has to be reasserted or enforced at the moment of action.
- **Real example (documentation repo, commit ab369fa):** Code made v7 content changes to the Core design but didn't rename the file and overwrote the v6 version note instead of adding one. The file claimed v6 while holding v7 content, and the v6 note was lost until recovered from history (fixed in 160d891, now v8). A git boundary check — content changed on a versioned file with no version bump — would have caught it. Evidence for the boundary-check prong (section 5).

## 3. Research headlines (full report: "Making Guidance Load and Apply at the Right Moment")

- Every platform converges on four loading modes: always-on, path-scoped, description-matched, manual.
- Descriptions are the whole trigger surface; vague descriptions are the top cause of skills not firing.
- The working pattern elsewhere is probabilistic discovery backed by deterministic enforcement.
- Direct precedent: superpowers (session-start meta-skill forcing a skill check before acting).
- Hooks are Claude Code only; tool-level enforcement is the only deterministic lever common to chat, Code and Cowork.

## 4. Bootstrap model — Agreed (from earlier in session)

- One master line in account instructions: load any skill with "aidebootstrap" in its name.
- Per-component bootstrap skills own their own detection condition. No central router.
- Each bootstrap routes to lean reference files; full standards load only when a routing line fires.

## 5. Multi-pronged enforcement policy — Agreed

Apply logic through several overlapping mechanisms; never rely on one prong for anything that matters.

- **Tool** — deterministic where the action passes through it (e.g. document manager on write).
- **Hook** — Code only; watches the action itself (file write), not the tool, so it also catches direct edits.
- **Boundary check** — after the fact at git (Declaration present, version incremented), regardless of how the file got there.
- **Bootstrap and triggers** — probabilistic; raises odds everywhere, guarantees nothing.

Match the prong to two things:
- **The surface** — chat is the primary and hardest case (no hooks, no repo gate in the moment). Solve for chat; Code is easier.
- **The kind of rule** — hard invariants (versioning) earn deterministic prongs; judgement rules (plain English, meaning first) rely on triggers and review.

## 6. Check, not load — Agreed (Dave's proposal)

- Any skill touching a document ends with a lightweight hand-off: confirm the document checks have been applied.
- Reasserting a rule at the point of action moves it from the forgotten middle back to the live edge of context, even if it was loaded earlier.
- Keep the hand-off a pointer, not the standard reloaded — large repeated blocks compete and conflict.

## 7. Delivery pattern — Agreed

- **Standard stays whole** as the authored document; **delivery is split** at build time.
- Three layers:
  - Description — should I care (selection signal only).
  - Skill body — what do I load for this situation (routing table: condition → reference file).
  - Reference files — what do I actually do.
- DocMeth example: one skill, one trigger, a routing table, and a few reference files (versioning, identity, schema, …). Routes may load a subset together (e.g. save → versioning + identity).
- Routing table holds the map, never the rules themselves.
- Build stage enforces this shape on every generated skill: general floor for all, extra specificity designed in where a standard earns it.

## 8. Skill versus reference rule — Agreed

- Make something a new skill only when it needs a distinct trigger surface nothing existing can carry. Everything else is a reference file.
- Reasons: every skill's description loads every session and competes for attention; every skill adds an entry to the slash-command list (real UI clutter). References cost neither.
- Keep descriptions short. Don't relax the limit to fit more words; fill it with the right distinctive trigger terms.

## 9. Trigger vocabulary — Agreed (Dave's proposals)

- Distinctive, rare terms trigger reliably: Declaration, document schema, doctype, block type.
- **Namespace doctypes** by owning component (e.g. project design brief, project design decision). More unique, and carries ownership so routing can follow the prefix.
- **Use the live alias**, not the formal name — if it's always called "document", the types and blocks are "document …", not "document methodology …". Record the alias in the standard; optionally carry the full name as a secondary trigger.
- **One vocabulary, three places**: the standard defines the terms; the header and the skill trigger quote them exactly. Generated at build time so they can't drift.
- Header laid out as labelled fields (schema, doctype, block types): reads as meaningful information that gets acted on, without being an instruction that gets discounted.

## 10. Document manager's role in chat — Agreed

- **Not the read path.** Documents must be in context and searchable in chat; on-demand retrieval defeats the purpose of working there. (Dave, decisive.)
- Documents are worked in context; writing out or updating is an explicit action, usually on instruction. That action is the gateway in chat.
- Open: how much of the write path the document manager owns (see open items).

## 11. Key behaviours walkthrough (chat focus)

Granular behaviours, taken one at a time, to find where each attaches and how to weight its odds.

### Behaviour 1 — on reading a document, detect the Declaration and read the schema

- Where it happens: a document enters the conversation (context, attachment, project knowledge).
- No tool gateway in chat for reads.
- Trigger wording: "when you read a file, run the document check" — reading is Claude's action, so better odds than "when a document is added". Assessed: moderate. (Agreed reframe.)
- Backup: the self-describing header — its distinctive terms fire the declaration and schema skills even when the read-time check doesn't.
- Result: two overlapping moderate prongs; read side accepted as the softer path.

### Behaviour 2 — on saving, increment version and rename

- Write-out/update is a deliberate action — strong trigger odds.
- **Write-time checkpoint** (Dave's proposal, Agreed in principle): a small instruction run on any document write that only names the candidates — Declaration, versioning, schema type, master vs state. If any apply, route from there.
- State documents (WIP, boards) already carry an instruction — natural place to attach the checkpoint.
- Not yet walked through in full.

### Behaviours 3–5 — not yet walked

3. Capture-and-place of brain-dumped fragments (conversational cue, no file event — probabilistic only).
4. At each design decision, ask whether a change in the model would make it better (conversational, decision point).
5. On creating a document, stamp identity — doctype, Declaration, naming (creation-time action).

Second batch of five behaviours still to be identified.

## 12. Open items

- **Commit sequence (convention, Agreed — to place in ways-of-working):** make all changes, rebuild the binder if needed, then commit. The binder builder committing on its own is acceptable when it runs last in that sequence. The binder log is committed as part of that final commit when work is done.

- Walk behaviours 2–5, then the second five.
- Document manager write path: in chat, does it own the save, or are updates written another way? Reads and writes may need different homes.
- Build-stage floor vs design-time specificity: which triggering elements every generated skill gets by default.
- Surface probe: does the master bootstrap line work in Code and Cowork?
- Rewrite existing AIDE skill descriptions as action/trigger-worded (proposed DocMeth line: "Use when creating, updating or saving any document — versioning (_v##, drafts), identity, Declaration, uses, doctypes, blocks.").
- Deployment check rejecting descriptions with no trigger words.
- Decide the namespace convention and alias list for doctypes and block types.

## 13. Proposed, not yet confirmed

- Forced check / commitment step in the master bootstrap (state which conditions apply before acting). Strength: moderate.
- One-line visible trace of which bootstraps fired. Strength: moderate.
- Evals for triggering (10–20 prompts incl. negatives, repeated runs). Strength: moderate.
- Subagent escape hatch and precedence ordering between bootstraps. Strength: moderate.
- Code-side hooks for session-start injection and save-time enforcement. Strength: strong for Code.
