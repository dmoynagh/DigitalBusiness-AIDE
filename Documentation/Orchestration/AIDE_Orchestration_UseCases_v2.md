# AIDE Orchestration — Known Use Cases v2

> identity: Orchestration_UseCases@v2 | doctype: working | updated: 2026-09-17

v2 change: use cases 5 and 6 reworded per cross-review finding F12 (D31). Orchestration
responsibility dissolution settled; replacement architecture removed — that belongs to
the owning components' design passes.

Purpose: every currently-known consumer of Orchestration, gathered from the scoping
session, the investigation, and other components' completed design passes. For checking
Design v2 against real demand — not a design document itself, and not a complete list
forever, just what's known as of today.

For each: what it needs, who the caller is, what tier/shape it implies, and whether
Design v2's dispatch model covers it as written.

---

## 1. FUP delivery (the validation scenario)

**What it is.** Deploying a File Update Package — currently a fully manual process
(build a zip, write a manifest, hand it to Code, watch it run).

**Caller.** Dave or chat, on behalf of whichever component produced the FUP.

**Shape.** Target: `claude-code`. The FUP instruction is payload (UTF-8 text). Runs
`aide fup` unchanged (D14).

**Checks against Design v2.** Covered directly — this is the scenario the design was
built to prove end-to-end. No gap identified.

---

## 2. Build delegation

**What it is.** "Apply this specification to the codebase" — an intent-level
instruction, agent owns file discovery, edit planning, execution.

**Caller.** Build component (Design v3 deployed) or chat directly.

**Shape.** Target: `claude-code`. Payload: whatever Build's package shape is — opaque to
Orchestration per D1/D2. `response_schema` optionally supplied by the caller if Build
wants schema-constrained verification back (D5/D20).

**Checks against Design v2.** Covered in shape. Build's design pass is now complete
(v3 deployed), so testing with a real Build payload through the dispatch mechanism is
the next validation milestone.

---

## 3. Cross-platform review

**What it is.** Getting a second AI's opinion — code review, design review — via Codex
or another platform, non-interactively. Currently done by hand (compose in chat, run
`codex exec` manually, read the result back in).

**Caller.** Any component whose workflow includes an external-review step — this
already happens today for cross-review, done manually.

**Shape.** Target: `codex` (confirmed working via investigation). `response_schema`
optionally supplied since Codex's `--output-schema` is confirmed to support it.

**Checks against Design v2.** Covered. This is the most immediately useful case to wire
up first after FUP, since it's already a real, frequent, manual task.

---

## 4. Risk-flagged external review (heavyweight tier)

**What it is.** For heavyweight work: plan reviewed by an external AI, build reviewed
by an external AI, completion document written. Two review dispatches around one piece
of Dave-driven interactive work.

**Caller.** Whatever component defines the heavyweight workflow (Working Practices, most
likely, per its ownership of working state and lifecycle).

**Shape.** Two separate dispatches, target `codex` (or whichever platform), same shape
as use case 3. Tier itself lives with the caller, not Orchestration (D16) — Orchestration
just executes two ordinary review dispatches at points the caller's workflow decides.

**Checks against Design v2.** Covered by composition of use case 3, twice, with no
special Orchestration-side machinery. Confirms D16 — the caller-owned tier decision
genuinely doesn't need Orchestration to know about "heavyweight" at all.

---

## 5. Assurance's learning-loop queue writing — NOT AN ORCHESTRATION RESPONSIBILITY

**What it is.** Assurance's learning loop captures "measurable moments" for later
pattern analysis. Its own design pass (accepted 2026-09-15) originally settled the
boundary as: Infrastructure owns the plumbing, "Orchestration coordinates the
invocation," Assurance decides what to capture (Assurance D14).

**Resolution.** A queue write is not cross-platform execution — it doesn't fit
"dispatch to an execution target, get a result back." The framework inbox and
Assurance's data logger are services called directly by any client, the same way any
connected tool is called. There is nothing for Orchestration to coordinate.

**Downstream action required.** Assurance's D14 wording ("Orchestration coordinates
invocation") needs correcting to drop the Orchestration clause — tracked in
Orchestration D19. The service architecture and hosting belong to Infrastructure's
design pass. Orchestration's review established only that this is outside its boundary.

**Checks against Design v2.** Not a gap against Orchestration — it was never
Orchestration's use case.

---

## 6. Improvement's periodic pattern analysis and scheduling — NOT AN ORCHESTRATION RESPONSIBILITY

**What it is.** The Improvement component (identified but not designed) analyses the
learnings queue periodically and escalates findings. Its design note originally stated
"Orchestration provides scheduling mechanism."

**Resolution.** Same family as use case 5. A recurring/scheduled trigger querying a data
store isn't a dispatch to an execution target. The scheduling concern and the service it
queries are not Orchestration's to own or design.

**Downstream action required.** Improvement's design pass (not yet run) needs to
identify the actual owner and mechanism for scheduling, and correct its wording. The
service that Improvement queries is the same service Assurance writes to — both depend
on Infrastructure's hosted-services design, not on Orchestration.

**Checks against Design v2.** Not a gap. Design v2 correctly has nothing to say about
scheduling.

---

## 7. Search/collaboration tasks (open-ended, non-review)

**What it is.** Looser requests to another platform that aren't quite review — "does
this pattern exist elsewhere," "sanity-check this approach."

**Caller.** Chat, ad hoc.

**Shape.** Same as use case 3 in dispatch terms — target, payload, optional workspace,
optional schema. Nothing distinguishes it structurally from cross-platform review; the
difference is purely in what the payload asks for.

**Checks against Design v2.** Covered — and confirms that `task_type` doesn't need to
exist as an Orchestration-level field at all (consistent with D1/D2: task semantics are
the caller's business, not Orchestration's).

---

## Summary — where Design v2 stands against known demand

| Use case | Fit | Notes |
|---|---|---|
| 1. FUP delivery | Covered | The proven scenario |
| 2. Build delegation | Covered in shape | Build v3 deployed — real payload test is next milestone |
| 3. Cross-platform review | Covered | Already a real manual task, highest-value first wire-up |
| 4. Risk-flagged review (heavyweight) | Covered by composition | Confirms D16 |
| 5. Assurance queue writing | **Not Orchestration's responsibility** | Downstream: Assurance D14 correction, Infrastructure hosted-services design |
| 6. Improvement scheduling | **Not Orchestration's responsibility** | Downstream: Improvement design pass, Infrastructure hosted-services design |
| 7. Search/collaboration | Covered | Confirms task-type is not an Orchestration concept |

Both non-Orchestration items were correctly excluded by the design. The components that
originally named Orchestration as responsible need their own wording corrected — tracked
in Orchestration D19 for Assurance; flagged for Improvement's own design pass.
