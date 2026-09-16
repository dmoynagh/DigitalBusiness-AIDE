# AIDE Orchestration — Known Use Cases v1

Purpose: every currently-known consumer of Orchestration, gathered from the scoping
session, the investigation, and other components' completed design passes. For checking
Design v1 against real demand — not a design document itself, and not a complete list
forever, just what's known as of today.

For each: what it needs, who the caller is, what tier/shape it implies, and whether
Design v1's dispatch model covers it as written.

---

## 1. FUP delivery (the validation scenario)

**What it is.** Deploying a File Update Package — currently a fully manual process
(build a zip, write a manifest, hand it to Code, watch it run).

**Caller.** Dave or chat, on behalf of whichever component produced the FUP.

**Shape.** `task_type` not modelled explicitly in Design v1's dispatch (dispatch is
target/workspace/model/payload only) — the FUP instruction is just payload. Target:
`claude-code`. Runs `aide fup` unchanged (D14).

**Checks against Design v1.** Covered directly — this is the scenario the design was
built to prove end-to-end. No gap identified.

---

## 2. Build delegation

**What it is.** "Apply this specification to the codebase" — an intent-level
instruction, agent owns file discovery, edit planning, execution. The core case the
whole Agent SDK investigation was run to prove.

**Caller.** Build component (not yet designed) or chat directly, pending Build's design
pass.

**Shape.** Target: `claude-code`. Payload: whatever Build's eventual package shape is —
opaque to Orchestration per D1/D2. `response_schema` optionally supplied by the caller
if Build wants schema-constrained verification back (D5).

**Checks against Design v1.** Covered in shape. **Open risk:** Build hasn't had its
design pass yet, so nothing has actually exercised this end-to-end with a real Build
payload. The FUP scenario proves transport; it doesn't prove build delegation's specific
payload shape works through the same dispatch. Worth treating as a second validation
scenario once Build exists, not assuming FUP coverage extends to it.

---

## 3. Cross-platform review

**What it is.** Getting a second AI's opinion — code review, design review — via Codex
or another platform, non-interactively. Currently done by hand (compose in chat, run
`codex exec` manually, read the result back in).

**Caller.** Any component whose workflow includes an external-review step — this
already happens today for Standards/Tools/Messaging cross-review, done manually.

**Shape.** Target: `codex` (confirmed working via investigation). `response_schema`
optionally supplied since Codex's `--output-schema` is confirmed to support it.

**Checks against Design v1.** Covered. This is the most immediately useful case to wire
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

**Checks against Design v1.** Covered by composition of use case 3, twice, with no
special Orchestration-side machinery. This is a good sign for D16 — the caller-owned
tier decision genuinely doesn't need Orchestration to know about "heavyweight" as a
concept at all.

---

## 5. Assurance's learning-loop queue writing — RESOLVED 2026-09-15

**What it is.** Assurance's learning loop captures "measurable moments" for later
pattern analysis. Its own design pass (accepted 2026-09-15) originally settled the
boundary as: Infrastructure owns the plumbing, "Orchestration coordinates the
invocation," Assurance decides what to capture (Assurance D14).

**Resolution.** This was flagged as a gap against Design v1's dispatch model — a queue
write isn't cross-platform execution, it doesn't fit "dispatch to an execution target,
get a result back." The resolution dissolves the gap rather than extending Orchestration
to cover it: the framework inbox and Assurance's data logger are **remote-hosted MCP
services** (always-on, cloud-hosted — Supabase/Postgres behind a Cloudflare Workers MCP
layer, ~$25-30/month), reachable directly by any client. Assurance calls the hosted
service the same way it would call any other connected MCP tool. There is nothing for
Orchestration to coordinate.

**Action taken.** Assurance's D14 wording ("Orchestration coordinates invocation") needs
correcting to drop the Orchestration clause — tracked as Orchestration Decisions v1,
D19. The hosted services themselves sit under Infrastructure's "hosted AIDE services"
sub-scope, proposed as one generic service with two logical streams
(`framework-inbox`, `assurance-log`) rather than two bespoke builds.

**Checks against Design v1.** No longer a gap against Orchestration — it was never
Orchestration's use case. Design v1 correctly has nothing to say about it.

---

## 6. Improvement's periodic pattern analysis and scheduling — RESOLVED 2026-09-15

**What it is.** The Improvement component (identified but not designed) analyses the
learnings queue periodically and escalates findings. Its design note originally stated
"Orchestration provides scheduling mechanism," and both Improvement and Assurance's
learning-loop recording were explicitly deferred until Orchestration was "completed and
tested."

**Resolution.** Same family as use case 5, same fix. A recurring/scheduled trigger
querying a data store isn't a dispatch to an execution target either. Once the learnings
queue is a hosted MCP service (see use case 5), Improvement's periodic analysis is a
client querying that service on a schedule — a scheduling concern, not an Orchestration
concern. Orchestration's dispatch model was never the right home for this; the "provides
scheduling mechanism" wording in Improvement's design note needs the same kind of
correction as Assurance's D14.

**Action taken.** Flagged for Improvement's own design pass (not yet run) to correct its
wording and unblock — Improvement no longer needs to wait on Orchestration's completion,
since the actual dependency was the hosted queue service, not Orchestration itself.

**Checks against Design v1.** No longer a gap. Design v1 correctly has nothing to say
about scheduling — that was never its job.

---

## 7. Search/collaboration tasks (open-ended, non-review)

**What it is.** Looser requests to another platform that aren't quite review — "does
this pattern exist elsewhere," "sanity-check this approach." Named in the original
scoping as a `task_type` (`search`, `collaborate`) but not otherwise elaborated.

**Caller.** Chat, ad hoc — this is closer to how the GPT design-shaping handoff itself
was used just now, informally, outside any AIDE mechanism.

**Shape.** Same as use case 3 in dispatch terms — target, workspace, payload, optional
schema. Nothing distinguishes it structurally from cross-platform review; the difference
is purely in what the payload asks for.

**Checks against Design v1.** Covered — and this is a useful confirmation that
`task_type` doesn't need to exist as an Orchestration-level field at all (consistent
with D1/D2: task semantics are the caller's business, not Orchestration's).

---

## Summary — where Design v1 stands against known demand

| Use case | Fit | Notes |
|---|---|---|
| 1. FUP delivery | Covered | The proven scenario |
| 2. Build delegation | Covered in shape, unproven in practice | Needs Build's design pass before it's truly tested |
| 3. Cross-platform review | Covered | Already a real manual task, highest-value first wire-up |
| 4. Risk-flagged review (heavyweight) | Covered by composition | Confirms D16 was the right call |
| 5. Assurance learning-loop queue writing | **Resolved** | Never Orchestration's use case — hosted MCP service, called directly (Decisions v1 D19) |
| 6. Improvement scheduling | **Resolved** | Same family — hosted queue service unblocks Improvement's design pass directly, not via Orchestration |
| 7. Search/collaboration | Covered | Confirms task-type doesn't need to be an Orchestration concept |

**Both original gaps resolved 2026-09-15, by dissolution rather than extension.**
Neither queue-writing nor scheduling turned out to be Orchestration's job — both are
clients of a hosted MCP service that sits under Infrastructure. Design v1 was right not
to address them; the components that originally named Orchestration as responsible
(Assurance's D14, Improvement's design note) need their own wording corrected instead.
That correction is tracked in Orchestration Decisions v1 (D19) for Assurance, and
flagged here for Improvement's own design pass to pick up.

**Net result:** all seven known use cases are now covered by Design v1 as drafted, with
one real open risk remaining — build delegation (use case 2) is covered in shape but
unproven until Build has its own design pass and a real payload can be tested through
the dispatch mechanism.
