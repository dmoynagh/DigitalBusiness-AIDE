# Workflow — Platform — Working — Extensibility and deployment mechanisms

**Version 1 · 2026-09-02 · handoff brief, design-side authored**

> **Purpose.** A single consolidated statement of what this corpus knows, and what it has
> documented, about the mechanisms available for extending and governing AI behaviour across
> Claude's surfaces and adjacent platforms — plugins, skills, hooks, MCP servers, slash commands,
> settings, and passive context. Written to be handed to a session that does not have the corpus
> loaded, or that needs the whole picture in one place rather than across eight documents.
>
> **This is a Working document (design in progress), not a Reference.** It restates content that
> lives canonically elsewhere. Where it disagrees with a source document, the source wins. It is
> expected to be disposed of after use — archived if anything in it proves worth keeping,
> otherwise dropped — rather than maintained.
>
> **Evidence status is marked throughout** and is the most important thing in this document.
> Three levels are used:
> - **[TESTED]** — observed by running an instrument, with the observation recorded.
> - **[RESEARCHED]** — read from vendor documentation, not run.
> - **[ASSUMED]** — believed, not established. Treat as a hypothesis.
>
> **Staleness warning.** The bulk of the tested findings date from 2026-08-26. This platform
> changes fast. A receiving session should re-verify anything load-bearing against current
> vendor documentation before designing on it.

---

## 1. The mechanisms, at a glance

Seven distinct ways to extend or govern behaviour exist across the surfaces this project uses.
They differ in where the artefact lives, which surfaces see it, how it fires, and whether it is
enforced by the platform or depends on the model choosing to comply.

| Mechanism | What it is | Fires by | Enforcement class |
|---|---|---|---|
| **Plugin** | Git repository with manifests, carrying skills (and potentially commands, settings, MCP references) | Installed once; contents then fire by their own mechanisms | Delivery channel, not enforcement |
| **Skill** | A named markdown body with a description, loaded on match | Model selecting it against its description | Advisory — model compliance |
| **Slash command** | A command file invoked by typing `/{name}` | User typing it | Deterministic invocation of non-deterministic behaviour |
| **Hook** | Lifecycle shell command in the agentic CLI environment | Platform, at a lifecycle event | **Enforced** — outside the model |
| **MCP server** | External tool server, local process or remote URL | Tool call | Enforced at the tool boundary; expensive |
| **Settings / permission rules** | `allow` / `deny` / `ask` rules in a settings file | Platform, on tool use | **Enforced** — a `deny` cannot be cancelled by an `allow` at any scope |
| **Passive context** | Project knowledge, `CLAUDE.md`, `AGENTS.md`, the always-on instructions field | Present in context, or retrieved | Advisory — weakest, and silently degrades |

**The governing distinction is enforcement class, not mechanism.** Two named assurance levels
were recommended by independent review and accepted: **enforced** (checked outside the model) and
**advisory / self-attested** (checked by the model choosing to). The stronger corollary from that
review — *an advisory environment should not be allowed to mint authoritative migration success* —
is the sharpest single line in this whole area.

---

## 2. Surface matrix — what reaches where

**Six clients, two installs.** [TESTED 2026-08-26]

| Client | Plugin path observed | Notes |
|---|---|---|
| claude.ai web chat | `/mnt/skills/plugins/{plugin}:{skill}/` | No version segment in the path |
| Desktop chat | as above | |
| Mobile app | not inspectable | Appeared with no separate install act — was not anticipated |
| Cowork | `/root/.claude/plugins/synced/{plugin}/skills/{skill}` | |
| Desktop Code tab | `AppData\Roaming\Claude\local-agent-mode-sessions\{session-guid}\rpm\{plugin-id}\skills\{skill}` | Materialised per session |
| Terminal CLI | `~\.claude\plugins\cache\{marketplace}\{plugin}\{version}\skills\` | **Separate install** |

**The differing paths are views, not copies.** The Code tab's per-session path suggested an
independent resolution; it is not one. It unpacks whatever the account install currently holds and
reported the same release as chat throughout.

**There are two installs, not six:**

- **Account install** — Customize → Plugins → Personal plugins. Covers the five clients above.
  Tracks the marketplace by commit; the panel shows the synced commit hash. The five clients
  behind it **cannot drift from each other**, because there is one copy.
- **Machine install** — its own marketplace add *and* its own install, recorded in
  `~/.claude/plugins/installed_plugins.json` with a pinned commit. Terminal CLI only.

**Nothing keeps the two installs in step.** This is the residual defect of the plugin channel and
it is accepted, not solved. Any currency report must name which install it describes.

**Live corroboration, this session (2026-09-02, claude.ai web chat).** [TESTED] The plugin path
form holds: `/mnt/skills/plugins/currency-probe:currency-probe/SKILL.md` is present, carrying
`metadata.release: "3"` in its YAML frontmatter, alongside a user-scope skill at
`/mnt/skills/user/workflow-messaging/`. The August path finding is still accurate a week later.

---

## 3. Skills — three delivery channels and three scopes

### 3a. Delivery channels

| Channel | Where it lives | Reaches | Currency |
|---|---|---|---|
| **Account skill** | Cloud, account-level (Customize → Skills). No local file exists | Chat, Cowork, Code tab; terminal CLI only after explicit sync | Manual upload, **replaces destructively, no restore** |
| **Machine skill** | `~/.claude/skills/<name>/` on disk | Terminal CLI and Code tab on that machine | Manual file edit |
| **Plugin** | Git marketplace, installed per environment | All surfaces, via the two installs above | Automatic on the account side, commit-tracked |

**Account skills sync down to the terminal CLI only on demand.** [TESTED] Landing zone is
`~/.claude/skills/synced/`. Nothing arrives in an ordinary interactive session; the download
happens only in a non-interactive run with the sync environment variable set. Consequence: a skill
*removed* from the account **stays live in the CLI** until the next such run, and keeps winning
description matches meanwhile. A stale capability that still fires is worse than an absent one,
because it produces plausible output under a name you believe is gone.

### 3b. Scopes (the filesystem view)

| Scope | Location | Enumerated by `/skills` and `/context` | Reachable from Claude Code | Reachable from Claude chat |
|---|---|---|---|---|
| Project | `.claude\skills\` in the repo | yes | yes | **no** |
| User (machine) | `%USERPROFILE%\.claude\skills\` | yes | yes | **no** |
| Account | Settings → Customize → Skills; cloud-persisted, **no file exists** | **no** | **no** | yes |

**A complete-looking enumeration is not complete.** The CLI panel reported 32 skills mid-migration
— sixteen project plus sixteen user — with no indication that a third tier existed. An absent
skill read as a missing skill rather than an unlisted one.

**Account scope cannot be depended on from a repo session.** A deployed skill body that instructs
Claude Code to follow an account-level skill's procedure is instructing it to follow something it
cannot load.

### 3c. Skills are trigger-based, and there is no always-on skill

**There is no `alwaysApply` frontmatter field or equivalent.** [RESEARCHED] Claude reads every
skill's name and description at session start, but the body loads only when the description
matches. The only genuinely always-on channels — the chat-side instructions field, project
instructions, `CLAUDE.md` on the build side — are hand-maintained, outside any adapter chain, and
none is plugin-deployable.

**The bootstrap pattern is the answer, and it is a path, not a guarantee.** Two artefacts: a skill
carrying the actual rules, versioned and plugin-deployed, with a description engineered for
near-certain selection on every turn; plus a one-line always-on instruction, hand-placed, that
does nothing but point at the skill. The always-on channel carries a pointer; the content stays
versioned and deployable. The residual is that skill selection remains dynamic model behaviour —
a future model, a reworded description, or a competing skill could silently reduce invocation
reliability and nothing would report it. Reliability should be established by testing a
representative prompt set and inspecting the tool trace, never assumed from the wording.

### 3d. Skill frontmatter version is display-only

The frontmatter supports a `version` field and an arbitrary `metadata` block, but **the platform
does not enforce or compare it.** Plugin-level version (what the UI shows) is *not* exposed to a
running skill. Any version mechanism therefore has to work at skill level using a naming
convention, not at plugin level using platform metadata.

---

## 4. Plugins — shape, publishing, and currency

**Shape.** A Git repository carrying `.claude-plugin/marketplace.json` at its root and one or more
plugin directories, each with `.claude-plugin/plugin.json` and a `skills/` subdirectory.

**Publishing is a commit and a push.** [TESTED] A private repository works; no public hosting is
required.

**A release-tag gate is available and free.** The CLI supplies a tag command that **refuses to cut
a release tag when the plugin manifest and the marketplace entry disagree on version.** That is a
machine check on exactly the drift class this corpus has otherwise caught only by human reading.

### 4a. Currency — the refresh is an account event

[TESTED, and it is the finding that shapes the design]

- A push does **not** propagate on its own within any observed window.
- Restarting the desktop app does **not** refresh. Rebooting the machine does **not** refresh.
  There is no client-side cache to clear, so client-level acts have nothing to act on.
- **Forcing an update in one client moved every client**, including mobile. The act is not "update
  this client"; it is "tell the account to re-resolve against the marketplace."

So the cost of a release is **one act propagating to five clients.**

The machine install is separate: `claude plugin update <name>` then `/reload-plugins`, or a
per-marketplace auto-update setting that is **off by default**.

**Marketplace update and plugin update are different acts.** Refreshing the marketplace updates
the catalogue of what is *available to install*; it does not advance an *installed* plugin, which
stays pinned to its install-time commit. Conflating them is the common failure and was reproduced
during the test — an update reported as applied while the running session still resolved the
previous release.

### 4b. Install shape differs by side, which constrains the architecture

- **Machine side installs alongside.** `1.0.0` and `2.0.0` exist as sibling directories; the
  reload selects which resolves. Releases genuinely coexist, so a **pinned-release model is
  available**.
- **Account side replaces in place.** No version segment in the path. **Pinning is not available.**

This is why "root pins its version, with multiple releases coexisting in a local store" works on
the repository side and cannot work on the chat side. The chat side pins and checks but can hold
only one release. Stated, not smoothed over.

### 4c. The packaging is portable; the runtime is not

[TESTED against a non-Anthropic client] It parsed the marketplace, read the plugin manifest,
displayed the correct version, and offered the skill for selection — then **could not dispatch
it**, and answered by guessing from the skill's *name* rather than its body.

Two consequences. The format is inert data — a Git repository with JSON manifests and markdown —
readable anywhere, which limits vendor lock-in more than expected. And the failure mode is the
silent-fallback class in its strongest form: not a wrong answer from a stale capability, but a
confident answer derived from a name.

### 4d. An operational trap

Closing the desktop window does not quit the application; processes persist. Any procedure saying
"restart the app" must specify a genuine quit and a check for surviving processes, or "I restarted
it" and "it restarted" are different claims.

---

## 5. Hooks — the enforcement mechanism, and it is one-sided

[RESEARCHED, checked against current vendor documentation 2026-08-26 rather than recalled]

- The agentic CLI environment supports **lifecycle hooks** — deterministic shell commands, not
  model-invoked. This moves enforcement out of the model-compliance class entirely for that
  surface.
- A **session-start hook can inject context but cannot block.**
- A **pre-tool-use hook can deny**, and that denial holds **regardless of the user's permission
  mode**.
- A **prompt-submit hook is a cheaper and earlier gate** than a pre-tool-use hook on every write —
  independent review's recommendation, not yet designed against.
- The **chat environment has no hook mechanism**, and installed extensions cannot enumerate each
  other. Any check there depends on the model choosing to run it.
- **Hook configuration lives in a per-user file on the machine, covering every repository.** This
  is what answers the "you'd need a registry per repo" objection.

**The asymmetry is the design constraint.** Enforcement is possible on the build side and not the
chat side. That should be recorded and designed around, never hidden behind language that implies
symmetric assurance.

**Untested:** whether a session-start hook running an update affects that same session or only the
next.

---

## 6. MCP servers

[RESEARCHED — corrects a standing corpus assumption]

- **A plugin can reference a remote MCP server by URL**, and the marketplace is surfaced in both
  Claude Code and claude.ai settings. Constraint: **remote server by URL, not a local process.**
- This means genuine executable enforcement is **possible chat-side** but expensive — hosting,
  availability, auth. The earlier corpus claim that enforcement is unavailable in chat is wrong;
  it should read "available and expensive." This changes what is *possible*, not what is
  *sensible now*.
- **MCP as the delivery vehicle for capabilities was considered and rejected.** A connected
  server's tool list is present by construction, which would make enumeration free — but it needs
  hosting and an endpoint, and the plugin channel answers the currency question without either.
- On the OpenAI side, the MCP JavaScript runtime is a known **silent-fallback source**: a review
  invocation fell back to it, produced a correct-looking repository listing, and reported success.
  Verification looks for `mcp:` markers and the absence of a `succeeded in` line in the transcript.

---

## 7. Settings and permission rules

[RESEARCHED]

- **Strict override for ordinary keys:** managed > CLI flags > local > project > user.
- **Combine-and-deduplicate for list keys:** `permissions.allow` / `deny` / `ask`, hooks, and
  `enabledMcpjsonServers`.
- **A `deny` can never be cancelled by an `allow` at any scope.**
- **Where plugin-supplied settings sit in that chain was not found in any source consulted.**
  Probably at or below user level. **Test, do not assume** — the distinction matters if a
  protection block ships as plugin settings rather than a repo-deployed `.claude/settings.json`.

**Local-override drift is the quiet risk on the repo side.** `.claude\settings.json` is committed
and so its changes are visible in version control; `.claude\settings.local.json` overrides it
silently and is not committed. Keep it minimal or empty.

---

## 8. Passive context — the weakest channel, and it degrades silently

- **Chat-side slash commands are convention, not mechanism.** They work because a guide document
  is in project knowledge and the model reads it. There is no deterministic invocation layer in
  chat: no autocomplete, no guarantee. If a command misbehaves, the first check is whether the
  guide is actually in project knowledge and current.
- **Claude Code slash commands are deterministic.** Typing `/{name}` invokes that command file's
  content exactly, with real autocomplete.
- **Project knowledge silently switches to RAG retrieval** past the context limit (cited as ~200K
  tokens). [RESEARCHED] Retrieval expands capacity roughly tenfold but trades determinism for
  retrieval accuracy. **This mechanically explains the observed failure of standards being ignored
  in large projects.**
- **Git-backed project sources were tried and rejected.** [TESTED] Retrieval quality collapsed to
  an estimated twenty percent of what the same documents produced when uploaded natively,
  recovering fully on reverting with no other variable changed. Manual upload is a cost to
  convenience accepted in place of a cost to output.

---

## 9. The Claude Code / Code tab / CLI relationship

[RESEARCHED — corrects an earlier two-install picture]

**The desktop Code tab and the terminal CLI run the same engine and share configuration:** project
memory, settings, MCP servers, hooks, skills, plugins, permission rules. *Sessions* differ;
*config* does not. So the real split is: the account install serves the chat surfaces; Claude Code
(terminal or desktop tab) is the other install.

**Caveat:** plugins do not work in remote/cloud sessions, only local.

**Operating constraints, both hard-won:** launch at the repo root (the folder containing `.git`),
never a project subfolder and never a parent of several repos. One `CLAUDE.md`, at repo root — a
second copy in a subfolder is a bug, not a local override, because the session always launches at
root.

---

## 10. The production and deployment chain

The five-stage chain for getting a capability from design to a running session:

1. **Build** — takes a design document, produces the artefacts it declares (tool documents,
   standard documents, migration files) and applies platform design for platform variants.
   Capability-specific. Command is `build-capability`, not bare `build`, because build is a family
   of commands and a scoped noun prevents collision.
2. **Package** — assembles build outputs into a capability package with a **package manifest**.
   The manifest is the contract between capability-specific production and generic deployment:
   required-migration flags, the standard version each migration attaches to, platform
   applicability per file, and a removal list for deprecated skills. Capability-specific.
3. **Platform deployment package** — filters the capability package by target platform and
   produces a platform-specific package. Generic. Claude = git-hosted plugin; other platforms may
   differ.
4. **Publish** — pushes to the plugin repository. **The only stage that touches a live plugin.**
   Needs git access, reads the manifest, bumps the pending-migrations skill version only if a
   required migration is declared, and handles skill removals.
5. **Plugin update** — the host platform picks up the change. **A platform responsibility, not an
   AI-workflow one.**

**Versioning:** capability version is a *deployment* version, distinct from document version. It
increments **on publish, not on build** — build regenerates freely at the same number. Per-artefact,
not per-design: if a design emits two standards and one changed, only that one increments. Build
and deployment state live in a machine-maintained **build record**, never in the design file and
never hand-edited.

**Atomic deployment:** one commit carries the whole capability. A stub and its target cannot be at
different versions, so partial deployment — the failure mode of the destructive-upload model —
cannot occur within a single install.

**Plugin boundaries buy almost nothing.** One plugin, one marketplace repo. The account install
applies a plugin across all five chat clients with no per-client control; the only real switch is
account versus CLI. Skills carry their own scope and version and decide applicability at runtime.
Split later if a genuinely install-specific capability appears.

---

## 11. Repo-side deployment (the separate, older mechanism)

Distinct from plugin distribution and still live: a **deployment manifest** governs which artefacts
are copied into the repository, where, and how staleness is caught. The test for inclusion:

> Does a tool read this from the repo during normal work, and would a stale copy change what that
> tool does?

Everything else — Working documents, Decisions, Briefs, Open Items, Index — stays design-side.
Copying them into the repo multiplies drift surface for no operational gain.

There is a parallel local-filesystem convention: repo-only artefacts sit in a `deploy\` subfolder
of the master documentation folder, which works as a zero-cost exclusion mechanism because the
project-knowledge dropzone does not walk into subfolders. The governing rule: **if it needs to be
in context, it stays in the folder root.**

---

## 12. Non-Claude platforms

- **ChatGPT (design-side reviewer)** — reached by manual copy-paste relay. No skill or plugin
  mechanism is used or assumed. The envelope convention used for cross-AI messages is plain text
  and needs no tooling to read, which is deliberate.
- **Codex CLI (dev-side reviewer)** — invoked as a standalone executable by full path, not via the
  PATH shim. Read-only sandbox mode is required by role, not optional; the CLI's own default is
  workspace-write.
- **Known but not in the corpus** [ASSUMED — recorded from session recollection, unverified]:
  on the ChatGPT side, personal standalone skills execute on Work surfaces but are unavailable in
  ordinary Chat; account-level skills persisted via Settings have no reach into Claude Code. A
  receiving session should verify this before relying on it.

---

## 13. What is decided

Glossed, with identifiers so the receiving session can find the full entries.

| Ref | What it settles |
|---|---|
| `Workflow_SD22` (standards distributed as Git-marketplace plugins) | The distribution channel. Adopted **after** testing, not before — and two claims that looked settled from documentation alone turned out false |
| `Workflow_D114` (the currency model) | Three separate questions — *can I run this / is anything newer / should I migrate* — root-pinned local store, digest alongside version number, migration declared positively, partial migration as a state plus journal rather than a version number |
| `Workflow_D115` (bootstrap pattern) | How always-on session-conduct rules get deployed: versioned skill plus a hand-placed one-line pointer |
| `Workflow_D116` (validity horizon narrowed) | The time-based fallback is retained only for surfaces where a real check cannot run, and never overrides a real check where one is available |
| `Capabilities_D31`–`D38` (the capability production model) | Five-stage chain, deployment versioning, migration content owner-authored, multiple independent triggers, currency delegated to the host platform |
| `Workflow_D43` (corpus stays in native project knowledge) | Git-sync rejected on measured retrieval quality |
| `Workflow_D49`, `D53` (command layer at machine scope; three skill scopes) | Where commands and skills live, and which surfaces can reach each |

**On reliability where no hook exists:** the chat side gets reliability from **multiple
independent triggers**, not one guaranteed one. Independence is the load-bearing word — three
skills all depending on the same retrieval mechanism are one trigger wearing three hats.
Independence comes from spreading across *mechanisms*: an always-resident instruction, a skill
body, a step inside an already-invoked procedure. A planned trigger inventory makes the
independence claim inspectable rather than assumed.

---

## 14. What is open — hand this list over intact

| Ref | Open question |
|---|---|
| `Workflow_Q96` | **Where plugin-supplied settings sit in the precedence chain.** Not found in any source. Candidate test: enable a plugin with a deny rule, check whether a project-level allow overrides it |
| `Workflow_Q99` | **Three untested distribution surfaces** under the plugin mechanism: Cowork; Claude Code dispatch (including whether the skill-sync environment variable applies to plugin-delivered skills or only account-level ones); and republication visibility — whether a plugin update reaches an already-open session or only a fresh one, and whether staleness is visible |
| `Workflow_Q102` | **The currency model needs one consolidated review pass** — a per-surface statement of how "am I current" is answered on each surface, folding in five older residuals: change notification, provenance, preflight reach, account/CLI drift, and sync cadence |
| `Workflow_Q106` | **Some deployed skills are directly writable from a chat session, and the extent is unknown.** In tension with the whole premise of a publish mechanism. See §15 — this brief carries new evidence on it |
| `Workflow_Q82` | **The residual compliance class**: any rule resting on the model choosing to run a check, rather than on platform enforcement |
| `Workflow_Q100` | Whether `Platforms` should become a sub-topic under a promoted `Capabilities` topic, absorbing the per-platform documents |
| Unmeasured | Whether the account's "Sync automatically" toggle ever fires on its own. It was on throughout the test; a push, a restart and a reboot all passed without a sync. Three live explanations: a long cadence, a toggle governing something narrower, or no passive sync at all |
| Unmeasured | Whether editing a capability in place under an unchanged version number propagates, or whether resolution is keyed on the version number |
| Unmeasured | Whether a session-start hook running an update affects that same session or only the next |
| `Workflow_WR12` | Three corpus corrections identified but not yet applied to the documents that carry the wrong claims: the Code-tab/CLI shared-config finding, the MCP-via-plugin-URL finding, and the project-knowledge RAG finding |

---

## 15. New evidence in this session, not yet in the corpus

**[TESTED, 2026-09-02, claude.ai web chat.]** Both a user-scope skill directory
(`/mnt/skills/user/workflow-messaging/`) and a **plugin-delivered** skill directory
(`/mnt/skills/plugins/currency-probe:currency-probe/`) are **writable from the chat session's
container.** A create-and-delete test succeeded in both. The read-only mounts in this environment
are `/mnt/skills/public`, `/mnt/skills/private`, `/mnt/skills/examples` and the uploads folder —
the user and plugin skill trees are not among them.

**Why this matters, and the reading it suggests.** `Workflow_Q106` records writability as a
finding in tension with the premise that a chat session has no reach into deployed artefacts. This
session extends that finding to plugin-delivered skills as well as user-scope ones — but it also
suggests the resolution. **The container is per-session and ephemeral.** A write that succeeds
inside it is not evidence that the deployed artefact changed; it is evidence that the *materialised
view* of it changed for the remainder of that session. The August observation established that a
write *succeeded*; it did not establish that the write *persisted*.

**The test that would settle it** is cheap and mechanical: edit a marker string into a deployed
skill body from one chat session, then open a fresh session on the same surface and read the same
file. If the marker is absent, the publish-mechanism premise stands intact and `Q106` closes as a
misreading of an ephemeral filesystem. If it is present, the premise needs revisiting for that
class of artefact. Worth doing before the publish work goes further, because it is the difference
between an assumption confirmed and an architecture built on a wrong one.

**Stated as a hypothesis, not a finding.** Persistence has not been tested here.

---

## 16. Source documents

Version suffixes omitted; the receiving session should read the current version of each.

| Document | Carries |
|---|---|
| `Workflow_Platform_Claude_Reference` §5, §5a | Skill delivery channels, and the full tested plugin-distribution findings |
| `Workflow_Capabilities_Design` §10, §11 | Plugin architecture on the Claude platform, and the three platform corrections |
| `Workflow_Standards_Decisions` `SD22` | Why the plugin channel was adopted, what was rejected and why, including MCP-as-delivery |
| `Workflow_Decisions` `D114`, `D115`, `D116` | Currency model, bootstrap pattern, validity-horizon narrowing |
| `Workflow_Deployment_Reference` §2, §2b, §2c | Repo and machine destinations, and the three skill scopes |
| `Workflow_SessionReview_2026-08-26` §3, §6 | The review record behind the currency model, including the hook findings and the reviewer's eight points |
| `claude_Capabilities_Decisions` `D31`–`D38` | The production chain, versioning, triggers, migration authorship |
| `Workflow_DistributionArchitecture_TestPackage` | The instrument design — how the elimination gate was built and why compliance needs a no-rule control |
| `Workflow_Platform_OpenAI_Reference` | ChatGPT relay and Codex CLI invocation |
| `Workflow_OpenItems` | Full text of every `Q` reference in §14 |

---

**Depends on:** none — this is a derived consolidation.

**References:** `Workflow_Platform_Claude_Reference`, `Workflow_Capabilities_Design`,
`Workflow_Standards_Decisions`, `Workflow_Decisions`, `Workflow_Deployment_Reference`,
`Workflow_SessionReview_2026-08-26`, `claude_Capabilities_Decisions`,
`Workflow_DistributionArchitecture_TestPackage`, `Workflow_Platform_OpenAI_Reference`,
`Workflow_OpenItems`.

**Methodology:** v17
