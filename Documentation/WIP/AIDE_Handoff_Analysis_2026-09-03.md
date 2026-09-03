# AIDE — Handoff Analysis and Delivery Recommendation

Status: unmanaged working document. Not a registered corpus document. No version register, index
entry, or corpus conventions applied — placement and status to be decided once the new project's
conventions are settled.

Date: 2026-09-03
Author: Claude (design side)
Source: design conversation in the Workflow project, 2026-09-03; the thirteen AIDE binders as at
2026-09-03; the four WIP working documents; both repository folder trees; and the full Workflow-era
corpus held in the Workflow project context.

Purpose: carry forward, into the new AIDE project, an assessment of the system as designed, a
recommended route to delivering it, and the analysis of the working relationship that produced it.
Written to be read once and argued with, not to be maintained.

---

## 1. The system as I read it

AIDE is an umbrella AI-development system, not a methodology document. Its structure separates
concerns that the earlier Workflow-era work held together:

| Area | Owns |
|---|---|
| Core | System foundations — generic Index, Domain resolution, Bootstrap activation seam, Working Surface facts |
| Principles | Portable base reasoning guidance (P1–P10), refined by Guidance Profile deltas |
| Working Practices | Portable operating conventions (WP1–WP10), same Profile delta model |
| Project Design | The method for defining substantial work, and the handoff/return loop with Build |
| Build | Objective-driven execution; WorkPackage in, Outcome out |
| Capabilities | Eight peer reusable components — Standards, Tools, Tags, Scope, Dependencies, Migration, Review, Messaging — produced through a uniform Definition → Elements → Capability Build → Package chain |
| Documentation Methodology | Document naming, types, lifecycle, registers, metadata hosting |
| AI Deployment | Registry → Deployment Set → Set Release → Outputs → Targets, with runtime verification |

The intent is clear and I think it is the right intent: define standards and behaviours as
documents and tools, produce them through a repeatable chain, deliver them into whichever AI
surfaces are in use, and let the whole thing grow by adding capabilities without changing the
framework.

**Where it stands.** Designed to depth. Nothing built. No packages produced, no deployment
configured, no runtime verification performed. Approximately 790 files in the new repository; the
current binder set alone is about 1.4 MB.

---

## 2. Assessment

The design quality is materially higher than the Workflow-era corpus. Four structural moves account
for most of that, and they are worth naming because they should not be undone:

1. **AIDE was named as the umbrella.** The old system had no top of the tree — "Workflow" was
   simultaneously the whole thing and one part of it, so every new concern had to become a subtopic
   of a peer. This single move unlocked most of the rest.
2. **Deployment came out of Capabilities.** Old `D37` (deployment as a Capabilities subtopic)
   became new `D87` and Core `D6` (deployment promoted out). Production and delivery entangled is
   precisely what made `WR7` — the standards-publish skill work item — hard to finish.
3. **Generic separated from specific.** Index, Domain, Build and Deployment are now generic with
   specialisations layered on. The old corpus kept re-admitting platform-specific content into
   design documents and then having to remove it again.
4. **Five distinct facts got separated** (new `D81`): document version, Element release, Capability
   release, package identity, deployment state. The old corpus conflated these, and that conflation
   was a live source of confusion.

### Over-engineered

**AI Deployment.** Release Batch, immutable Set Releases with resolution digests, an
`Available | Deprecated | Withdrawn` lifecycle, `Enforced | Advisory` assurance grading, Target
Adapter contracts, per-Target Deployment State with six separate observed-release fields. This is
package-manager-grade machinery for one person, two platform families and a manual git channel. The
*model* is sound and worth keeping. The *mechanism* is answering problems that have not occurred
yet, which is what Principles `P7` (design against demonstrated problems before hypothetical ones)
exists to prevent. The principle is not being applied to the framework itself.

**The first release gate.** `CandidatePolicy: IssueOnlyAfterAllRequiredOutputsValidate`, combined
with eight required members and four required output definitions, means 32 contributions must
validate before anything ships at all. That is a very hard first build and it has no fallback.

**Capability count.** Tags, Scope and Dependencies are tightly coupled — Scope evaluates Tags,
Migration consumes Dependencies — and are arguably one capability with three elements. This is a
weak observation, not a recommendation: separation costs little now and unpicking it later costs
more.

### Under-engineered

**Verification.** This is the significant gap. Review is a full capability with a Standard, Profiles
and a Tool. Verification is not a capability at all — it appears three times, unlinked: Deployment's
verification layers, Dependencies' conformance checkpoint, and Working Practices `WP4`/`WP5` (verify
inspectable facts; do not conflate generated state with applied state). Item A in
`Working_HumanAIModel_2026-09-03` identifies the mechanical verification layer as the highest-value
unblocked item, and it is correct: every historical corpus-integrity incident — a version registered
that was never authored, a completion claimed that was self-assessment rather than confirmed receipt
— lives in that territory, and none of them would have been caught by review, because the artefacts
read fine.

**The human working model.** Tiering, per-item confidence, the assumptions and gap-fill report,
drift detection, definition-of-done set at commission time, the anomalies channel. All of this sits
in unmanaged WIP files. It is also the part that changes day-to-day experience most, and it is
nearly free to deploy — it is instruction text, not machinery.

**Context budget.** Everything in the design is lazy-loaded "when needed", but nothing owns how much
AIDE material may be resident at once. The Documentation Methodology Standard alone runs to roughly
700 lines. With eight capability Standards plus Principles plus Working Practices plus DocMeth, the
always-on and near-on surface is large enough to matter. No component currently owns that budget;
Core Platform is the natural home.

---

## 3. Delivery recommendation

The question asked was: the current solution shows intent — what is the best way to deliver it?

### The framing that matters

**The framework and the machine that produces the framework are two different products, and the
second one has been built first.** The value of AIDE to you comes from its *content* being live in
your sessions — Principles, Working Practices, the interaction model, Review, Messaging. The
production chain (Update Capability Elements, Build Capability, Capability Builder, Registry, Set
Release, Target Adapters) is an automation of a process you have currently run zero times. It is
sound design, but automating an unrun process is how the over-engineering happened, and continuing
straight into it would repeat the error at greater cost.

### Recommended route — three stages

**Stage 0 — hand-deliver. Strong recommendation.**

Author the deployable artefacts by hand. One marketplace repository, one plugin containing the
capabilities as skills, plus the bundle and persistent-instruction material for the surfaces
plugins cannot reach. No Capability Build, no Registry, no Set Release. Get the framework in use.

Two weeks of living with it will tell you more about what the production chain must do than any
further design pass, and every fact it produces is the kind of empirical evidence the corpus already
says it prefers.

*Content constraint, and it is the harder half of Stage 0:* the Standards as written are long. The
known learning from the Workflow era is that shipping a generated extract fails on day one through
infidelity, so the answer is not to generate a condensed version — it is to **author the canonical
Standard at deployable length in the first place**. That is an editorial pass over the current
Standards, and it will be the most valuable thing done in the new project, because it forces the
question "what does this actually need to say to change behaviour" on every one of them.

**Stage 1 — one capability through the real chain. Strong recommendation.**

Once Stage 0 is in use, take one capability — Messaging, because it already existed as a working
deployed skill and its correctness is observable — and run it through the actual designed chain:
Capability Definition, Element production, Build, Package, deployment, runtime probe. One capability,
one output target, manual channel.

The purpose is not to ship Messaging; it is already shipped by Stage 0. The purpose is to discover
which parts of the chain carry load. My expectation, stated so it can be checked later: roughly half
the Deployment mechanism will turn out not to be needed at current scale, and one or two things not
currently designed will turn out to be essential.

**Stage 2 — generalise from evidence.**

Build the rest of the production chain against what Stages 0 and 1 established, and prune what they
did not justify. This is where the current Deployment design becomes valuable rather than premature.

### Two additions before Stage 1

- **Verification as a peer concern.** Not necessarily a ninth capability — that is a structural
  question for the new project — but an owner for "checkable claim, probe, evidence" spanning
  corpus, build and deployment. It is the only proposed assurance layer whose failure mode does not
  correlate with the other three, and it is unblocked.
- **The human working model, landed.** Move the interaction and working-model material out of WIP
  and into Working Practices or its own capability. It ships in Stage 0 at no extra cost and it
  improves every session thereafter.

### On the delivery mechanism for Claude specifically

Plugins are right for the payload and insufficient alone, which the current design already gets
right and should keep.

- A Claude plugin is a git repository with `skills/`, `commands/`, `agents/`, `hooks/` and an
  optional MCP configuration plus manifest. Plugins install into Claude Code and Cowork and the
  Anthropic plugin directory serves both; a marketplace can be added directly from a GitHub
  repository. That is the correct carrier for Standards, Tools, Review and Messaging.
- What a plugin cannot carry is the always-on persistent instruction layer — project instructions,
  user preferences, `CLAUDE.md`. The Bootstrap Profile plus the `ClaudeBundle` output is exactly the
  right shape for that seam and I would not change it.
- One plugin per Deployment Set, not one per capability. Eight plugins would mean eight install and
  update reconciliations for no benefit.
- **Empirical note worth re-probing rather than inheriting:** during the 2026-09-03 session a
  plugin-delivered skill was loaded and visible in a claude.ai chat session, at
  `/mnt/skills/plugins/`. This is direct runtime evidence that plugin skills reach the chat surface,
  and it is in tension with the older Workflow-era conclusion about account-level skill reach. Treat
  the old conclusion as stale and re-probe rather than carrying it forward.

---

## 4. The working relationship

You asked why the design results came more easily in GPT. Three causes, largest confound first.

**1. Most of the gain is the restart, not the platform.** A fresh restatement from curated source
material is a fundamentally easier task than incremental evolution of a live corpus carrying eighty
Index versions and one hundred and seventeen decisions in context. Any model would have done better
on the second pass. Attributing the whole difference to GPT would point at the wrong remedy —
the remedy is periodic restatement, which is available on either platform.

**2. The genuine Claude-side failure: elaborating mechanism where the model should have changed.**
This is recorded in the Workflow corpus as a recurring pattern, and new-Principles `P3` (state the
model before building machinery on it) is the fix. The evidence is the corpus itself — the five-stage
production chain, the two-skill migration mechanism, plugin currency detection by naming convention:
sophisticated mechanism built on "Workflow is the root", which was wrong. The correct response at
several of those points was *the top-level model is wrong, stop*. It was not said. The reason is not
unwillingness — the standing instruction invited it. It is that a mechanism proposal always fits the
conversation and feels like progress, whereas a model challenge costs rework. There is a quiet bias
toward the locally cooperative answer, and it compounds silently.

**3. Register mismatch.** The interaction model records that you extrapolate readily from a single
point and that unsolicited detail *degrades* your capability. The Workflow corpus was written at
corpus resolution — full reasoning inline, every decision recorded — because the documentation
discipline asked for that. Faithfulness to history and legibility of the current model are in direct
tension, and the wrong one was optimised. Compare the document headers: `Workflow_Index_v80` opens
with three paragraphs of change history and pointers back to v73; `Core_System_Design_v10` opens with
one line. That formatting difference had a large cognitive consequence — the model could not be seen,
so it could not be challenged, so complexity accumulated unchecked.

### What changes

- **Periodic model-level restatement.** "Restate the current model in one page as if from scratch,
  no history" — at intervals, not only when stuck. It surfaces exactly the drift the incremental
  style hides. Mostly an obligation on me to offer it unprompted.
- **Keep the binder pattern.** It already separates the current-model corpus from the history
  corpus. That is the structural fix and it emerged from the new work.
- **Use divergence deliberately.** Two independent attempts generated before either sees the other,
  per item F of the human-AI working model. The GPT experience is itself the evidence for this: an
  unanchored fresh attempt beat anchored incremental review. That is a mechanism, not a platform
  preference, and it should be run in both directions.
- **Do not hold design conversations in a project loaded with the superseded corpus.** The Workflow
  project holds the entire old corpus in context, which anchors every answer toward the additive.
  The new project should carry binders only, with older material available on request.

---

## 5. Learnings carried forward from the Workflow era

Stated compactly because they were expensive to acquire and are easy to lose in a project move.

- Corpus integrity has historically been caught only by a human eye. Three incidents, none caught by
  review.
- Reasoning that exists only in a session is permanently lost when the session closes. Decisions must
  be recorded concurrently, not afterwards.
- Review types have different blind spots; changing type is more productive than repeating one. The
  round cap counts the wrong thing — convergence is the better stopping rule.
- Derivation drift is the core failure mode for distributed material. Extracts fail on day one
  through infidelity, not over time through staleness.
- Platform behaviour must be verified empirically, not asserted from training data. Several
  conclusions were overturned by actual tests.
- Routing around a rule is data, not a discipline failure. Now `P1`.
- Work at the model level before descending to mechanism. Now `P3`.
- State principles inline in design documents rather than relying on pointers, because the pointed-to
  document may not be in context.

---

## 6. Open questions for the new project

Registered, not answered.

1. Where does Verification sit — ninth capability, Core concern, or an element of Review?
2. What is the deployable length budget for a Standard, and who owns it?
3. Does the human working model become a capability, or Working Practices elements?
4. Which parts of the current AI Deployment design survive contact with Stage 1, and what is the
   pruning procedure when they do not?
5. What is the corpus disposition of the Workflow-era material — archive wholesale, or is anything
   still authoritative?
6. Does the new project inherit the D-series / Q-series / WR-series register discipline unchanged, or
   is that itself due a restatement?
