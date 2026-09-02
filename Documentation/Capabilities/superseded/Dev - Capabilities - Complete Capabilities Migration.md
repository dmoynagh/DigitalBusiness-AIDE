## Dev - Capabilities - Complete Capabilities Migration

**Date:** 29 August, 2026

---

> ok

  
  

Good. Migration is now ready to write up; there are no further design questions I think we need to work through first.

When we do the document pass, I’ll update the Migration corpus and also correct the two older conflicting rules we identified so the project has one coherent position.

  
  

> ok&#x20; what else is outstanding in capabilities

  
  

Once Migration is written up, the outstanding Capabilities work is fairly clear.

The current project sequence is:

1.  **Finish Migration (`WR3`)**  
    We have now done the design discussion. What remains is to produce the Migration Brief/Design/Standard/Tool design and reconcile the two older rules that conflict with the decisions we just made.
2.  **Reconcile Standards (`WR1`)**  
    The Standards Brief and Design are explicitly marked as needing revision against the current parent architecture. The main job is to remove stale ownership of Scope/tags/deployment/migration mechanics and make Standards consume the shared components instead.
3.  **Reconcile Tools (`WR2`)**  
    Same issue on the Tools side. Keep the useful generic Tool model—structure, inputs, decisions, reporting, failure handling, idempotency—but remove the old embedded Scope/tag model and old assumptions such as “Tools do not migrate.”
4.  **Finish the shared identity/version contract (`WR8` / `Q7`)**  
    Identity itself is mostly solved. What remains is distinguishing the different version concepts cleanly:
    -   document version;
    -   canonical capability/release version;
    -   package version;
    -   deployment state/version;
    -   transition/version-range semantics.
5.  **Finish Capability Package + Deployment Manifest (`WR9` / `Q8`)**  
    The boundary is settled:
    
    ```
    Capability Package + Deployment Manifest → Deployment
    ```
    
    What remains is the minimal manifest schema actually required by Deployment: identity/version, Deployment Set membership, platform applicability, replacement/removal, integrity/resumption fields where demonstrated, etc.
6.  **Deployment (`WR4`)**  
    This is the largest remaining Capabilities component. It still needs:
    -   Deployment Config;
    -   Deployment Set identity/membership;
    -   composition/assembly;
    -   replacement/removal;
    -   deployment state;
    -   partial failure/resumption/idempotency;
    -   Git/repository publication where relevant;
    -   rejection of defective package/manifest inputs.
7.  **Platform evidence/build/deployment standards (`WR10` / `Q11`)**  
    Claude, Codex and ChatGPT still need empirical platform contracts for:
    -   capability representation;
    -   scope/trigger realization;
    -   bootstrap behavior;
    -   version visibility;
    -   build/package representation;
    -   Deployment Set assembly;
    -   publication/update mechanics.
8.  **Review external environment/communication seam (`WR14`, `Q12`, `Q13`)**  
    Review itself is complete, but two shared mechanisms are intentionally unresolved:
    
    -   where environment-specific reviewer/model/route/default/fallback data lives;
    -   who owns the reusable inter-AI communication capability for direct/indirect send, correlation and failure handling.
    
    This should be coordinated with the future Research work rather than folded back into Review.
9.  **Documentation Methodology review (`WR12`)**  
    This is deliberately later. Capabilities has already accumulated the handoff items—generic metadata containers, Tags, Dependencies, Identity, Migration implications, temporary document state, etc.—but DocMeth should be reviewed as a separate pass rather than edited piecemeal.

There are also two smaller open details:

-   **Build Config inheritance/defaults (`Q9`)** — not currently a blocker.
-   **WorkPackage integration (`WR11/Q10`)** — moved out of Capabilities into AIDE Build, so it is not part of finishing this topic.

So in practical terms, after Migration the remaining **core Capabilities design work** is:

> **Standards → Tools → version/package contracts → Deployment**

Everything after that is mostly platform realization, shared environment/communication infrastructure, and the later DocMeth reconciliation.

  
  

> ok - can you take care of 1-5 - are they straight forward or are there questions you need from me

  
  

Yes. I can take care of **1–5 without needing another design session with you**.

After checking the current open items, I’d classify them like this:

-   **1\. Migration:** straightforward now. We have resolved the substantive model in this session. What remains is consolidation, reconciliation of the older conflicting rules, and producing the Brief/Design/Standard/Tool design.
-   **2\. Standards reconciliation:** straightforward. This is mainly removing stale ownership/mechanics and rewriting the child corpus against the current Tags, Scope, Dependencies, Migration, Review and Build boundaries.
-   **3\. Tools reconciliation:** straightforward for the same reason. The useful Tool structure survives; the obsolete Scope/tag/migration/platform assumptions need replacing.
-   **4\. Identity/version contract:** requires design judgment, but I think I can resolve it from the existing architecture without bothering you.
-   **5\. Package/Manifest:** likewise. It needs careful design, but the parent boundary is already established and the instruction is explicitly to define the _minimum demonstrated contract_, not invent a large packaging system.

For **4**, my working approach will be to keep the different meanings deliberately separate rather than build a universal “version” abstraction:

```
Document version
    → version of the governed source document/output

Capability/release version
    → version of the referenceable canonical capability contract

Dependency conformance version
    → last capability version this consumer has successfully reconciled against

Package version
    → identifies the packaged release of that capability

Deployment state
    → what is actually deployed; not another capability version
```

I will **not** introduce semantic versioning unless an actual need appears, and I will not decide that a Deployment Set needs its own version while doing item 4—that remains a Deployment question. The current open item specifically warns against conflating these concepts.

For **5**, I’ll derive the manifest from what Deployment demonstrably needs. At this stage that looks roughly like:

```
Package/capability identity
Capability/package release version
Deployment Set membership
Platform contribution identification/applicability
Replacement/removal intent
Transition/migration material reference where needed
Integrity information where needed
```

Anything relating to atomic deployment, rollback, detailed resumption state, Deployment Set versioning, etc. stays out until Deployment demonstrates that it needs it. That matches the existing decision to avoid prebuilding a broad manifest schema.

There is **one thing I’ll watch particularly carefully**: whether package version should always equal capability release version or whether a package can be rebuilt without changing the capability contract. I can resolve that from first principles when I get there; I’ll only bring it to you if the answer materially changes the model.

So yes: **I’m confident taking 1–5 through to completion myself.** I’ll surface only significant questions or architectural conflicts, not routine choices. And as agreed, I’ll defer the document-output pass until the substantive work is done so we don't keep paying the document-generation cost.

  
  

> ok the 6- are deployment related and we havent covered this fully yet. are there any items you can do without me?

  
  

Yes. Of the remaining items, there are parts I can advance without you, but I would not try to “complete Deployment” yet because the deployment model still needs a proper design pass with you.

What I can do independently now is:

-   **Platform evidence gathering prep**: define exactly what facts we need to establish for Claude, Codex and ChatGPT—capability representation, package shape, install/update mechanics, version visibility, deployment-set composition, failure/resume behaviour. This is mostly a research checklist and acceptance criteria, not architecture.
-   **Review the current Deployment assumptions for contradictions/gaps** against the parent model, Package/Manifest boundary and Build Config. I can cleanly identify what is already fixed versus genuinely open.
-   **Draft the Deployment problem statement / design questions** so when we do that session we are solving the real choices rather than rediscovering the territory.
-   **Work on the environment/communication seam analysis** at a conceptual level—identify what data Review/Research need from Environment and what a shared inter-AI communication capability must provide. I can probably get that to a strong proposed model, but I would still bring you in before locking ownership/storage decisions.
-   **Prepare the DocMeth handoff additions** from this Migration session: temporary document state container, compact metadata principle, dependency-order precedence, migration-related consequences. I would not modify DocMeth itself yet.

What I would _not_ lock without you is:

-   Deployment Set semantics
-   Deployment Config ownership/shape
-   full vs incremental assembly
-   atomicity/partial failure/rollback
-   publication model
-   environment settings home
-   permanent owner of the shared communication capability

So once I finish 1–5, the useful independent work is mostly **preparing 6–8 so the next design sessions are shorter and focused**, rather than pretending those architecture choices are already settled.

  
  

> proceed

  
  

Done. I have **not created or updated any documents yet**, per your instruction to leave the document pass until the end.

The independent work beyond items 1–5 has produced three useful things.

### 1\. Deployment: fixed boundary vs genuine design questions

A surprising amount of Deployment is already fixed.

The following should **not** be reopened in the Deployment session:

-   Build is **capability-local**; Deployment is **set-aware**.
-   Deployment begins only at `Capability Package + Deployment Manifest`.
-   Deployment must not reopen Capability Design or infer intent from package structure.
-   `Deployment Set` is a logical name/grouping; capability Build Config names it.
-   `Deployment Config` maps that logical name to physical platform destinations.
-   Deployment may compose several capability contributions into one output—for example a ChatGPT bundle.
-   Deployment owns validation, set resolution, composition, replacement/removal, publication, resumption/idempotency and rejection of defective inputs.
-   Host-side pickup/synchronisation stays outside Deployment unless a platform contract explicitly brings it in.

So when we eventually design Deployment, the actual questions requiring you are narrower:

**Deployment Set**

-   Is membership declarative only, or does a set have lifecycle/state of its own?
-   Can one capability belong to multiple sets?
-   What does removing a capability from a set mean operationally?

**Deployment Config**

-   Where does it live?
-   Environment-wide vs repo/project-specific overrides.
-   How logical set/platform maps resolve to paths/repos/plugins/bundles.

**Assembly**

-   Full rebuild versus incremental assembly.
-   Whether different platforms choose differently.
-   How conflicting package contributions are handled.

**State/failure**

-   What counts as successfully deployed.
-   Atomicity expectations.
-   Partial deployment across platforms/targets.
-   Resume versus rollback.

**Publication**

-   Whether Deployment itself commits/pushes Git or hands completed artefacts to another publication mechanism.

Those are real architecture choices; I would not decide them silently. The corpus already marks these as deliberately unresolved.

---

### 2\. Platform evidence: I can prepare this completely before Deployment

For **Claude, Codex and ChatGPT**, the evidence pass should answer the same questions for each platform:

```
Capability representation
→ What is the deployable thing?
  skill/plugin/bundle/instructions/commands/etc.

Build adaptation
→ How does canonical Standard/Tool become that representation?

Identity/version visibility
→ What metadata is eagerly visible?
→ Can MigrationSummary be exposed cheaply?

Scope/trigger realization
→ What can be mechanically scoped?
→ What is description/discovery/context-only?

Bootstrap
→ What actually executes or becomes visible at session start?
→ Best effort vs reliable.

Composition
→ Can several capabilities be assembled into one deployed unit?
→ What are naming/conflict rules?

Install/update/remove
→ How is a deployment created?
→ How is an existing one replaced?
→ How is removed content actually removed?

Publication/pickup
→ What API/file/Git/account action makes the new artefact live?
→ Does the host notice changes automatically?

Failure/state
→ What can we verify after deployment?
→ What information exists for resumption/idempotency?
```

That is exactly the empirical work currently required by `WR10/Q11`; it is not another conceptual architecture exercise.

Once items 1–5 are written, I can do that research independently and bring you the evidence before we make Deployment choices.

---

### 3\. Environment / inter-AI communication: proposed boundaries

I can also narrow `WR14` substantially without choosing its final architecture.

#### Environment resolver

The thing Review needs is simply a factual query service such as:

```
Current environment/surface
    ↓
available AI families/models
capability levels
routes
independence characteristics
access/usage/cost constraints
preferences
fallbacks
    ↓
resolved candidates
```

It should **not** contain Review policy. Review asks for capabilities; Environment reports facts.

The open architecture question is principally **where this environment configuration belongs and how it inherits/overrides**, not what Review needs from it. The current documents already deliberately leave this outside Review.

#### Shared inter-AI communication

Similarly, Review and future Research appear to need one generic transport layer:

```
Send:
destination/reviewer
payload
correlation identity
delivery requirements

Return:
correlation identity
response
actual source/model
delivery status

Transport owns:
route
packaging
send/receive
correlation
retry/failure
manual AI Message relay
```

Review owns **why it is communicating and what the payload means**.

Research will own its own research lifecycle.

Communication should know neither.

That means when we address Research later, we should not create another Claude↔GPT messaging system—the shared communication seam is deliberately reusable. This is exactly how Review currently defines the boundary.

I would still bring you in before deciding whether this becomes an AIDE top-level component, part of Environment, a generic Tool/capability, or something else.

---

### 4\. New DocMeth handoff items from this Migration session

There are three additions we should eventually put into `Capabilities_DocMethReviewItems`.

**Generic temporary document state**

DocMeth should provide a general compact location/format for temporary operational document state, without knowing what Migration, Validation, Concurrency, etc. mean.

Recommended human-readable rendering:

```
Title [Owner]
Message
```

Owner controls creation/update/removal; DocMeth controls placement/rendering.

**Compact machine content principle**

For documents potentially read by humans:

> Metadata, derived state and other machine-generated content should be as compact as practicable while remaining unambiguous and machine-usable.

This generalises beyond Migration to Tags, Dependencies, Identity and future generated state.

**Update/Migration interaction**

Existing `DR7` currently says `/update-doc` stops on Required Migration.

Our new Migration position supersedes that: if the document is being updated and a Required migration is outstanding, the update performs the Required migration as part of bringing the document forward; pending On-Update transitions come along in the same save.

That needs to be corrected during the eventual DocMeth review.

---

### One other cross-component change

Our Migration work produced one addition to **Dependencies**:

> Dependency declaration order is significant. Earlier dependencies have higher default processing precedence where an operation requires deterministic ordering, unless a more specific rule overrides it.

Migration will consume that for multi-dependency processing. This belongs in Dependencies rather than being repeated as a Migration-only ordering convention.

So there is useful progress we can make without touching the still-open Deployment choices.

The logical next move is for me to **complete items 1–5 in working form**, including these consequential cross-component changes, while still holding all actual document generation until we decide the session is ready for the final output pass.

  
  

> with deployment we may be able to use plugins and skills for gpt as well
> 
> Yes. You’re right: **skills can run in ChatGPT web, and a plugin is the proper way to deploy them there.**
> 
> A plugin can be completely **skills-only**—it does not require an MCP server. It can contain one or several related skills, supporting files, templates, examples, and scripts:
> 
> ```
> workflow-core/
> ├── .codex-plugin/
> │   └── plugin.json
> └── skills/
>     ├── documentation-methodology/
>     │   └── SKILL.md
>     ├── review/
>     │   └── SKILL.md
>     └── aimessage/
>         └── SKILL.md
> ```
> 
> ```
> {
>   "name": "workflow-core",
>   "version": "1.0.0",
>   "description": "Core Workflow standards and tools",
>   "skills": "./skills/"
> }
> ```
> 
> OpenAI explicitly states that skills bundled in plugins work in **Chat and Work across ChatGPT web, desktop, and mobile**, as well as Codex. OpenAI: Build skills
> 
> For deployment:
> 
> -   **Private development:** expose the plugin through a personal or repository marketplace and install it for testing. Local marketplace setup is primarily managed through the desktop app or Codex.
> -   **ChatGPT workspace:** a workspace administrator can publish the plugin privately and assign access by role.
> -   **General web availability:** submit the skills-only plugin to OpenAI’s universal plugin directory.
> -   **Updates:** publish/install a new plugin version; the plugin is a deployed snapshot rather than ChatGPT reading the latest skill files directly from Git at runtime.
> 
> OpenAI documents skills-only plugins as a supported submission type. OpenAI: Submit plugins The package and private-marketplace structure are described here: OpenAI: Package your plugin.
> 
> So our Capabilities platform model should change to:
> 
> | SurfaceDeployment artefact |  |
> | --- | --- |
> | Claude Chat / Claude Code | Claude plugin |
> | ChatGPT Chat / Work | OpenAI plugin containing skills |
> | Codex desktop / CLI | The same OpenAI plugin |
> | ChatGPT Project bundle | Optional compatibility/bootstrap artefact, not the primary deployment mechanism |
> 
> That is materially better than the earlier assumption that web ChatGPT required a concatenated Markdown bundle. The **OpenAI plugin can now be the common deployment unit for both ChatGPT and Codex**, while the bundle remains useful only where skills/plugins are unavailable or where project-level always-present context is specifically required.

  
  

Yes — that materially changes the Deployment assumptions, and it is a better model.

The earlier architecture treated ChatGPT web as needing a merged Markdown bundle because skills/plugins were assumed unavailable there. Based on the OpenAI material you’ve brought in, that assumption should now be treated as outdated. OpenAI’s current platform supports skills as deployable resources, and the direction is clearly toward skills/plugins as first-class capability packaging rather than treating ChatGPT chat as a bundle-only surface. OpenAI Developers

So I would revise the platform model to this:

| Surface | Primary deployment artefact |
| --- | --- |
| Claude Chat / Claude Code | Claude plugin |
| ChatGPT Chat / Work | OpenAI plugin containing skills |
| Codex desktop / CLI | Same OpenAI plugin / shared skills package |
| ChatGPT Project bundle | Compatibility or bootstrap fallback, not primary |

Architecturally, that is much cleaner because it gives us:

```
Canonical capability
    ↓
Build platform contribution
    ↓
Capability Package
    ↓
Deployment Set: workflow-core
    ├── Claude plugin
    └── OpenAI plugin
         ├── ChatGPT
         └── Codex
```

rather than treating ChatGPT and Codex as unrelated deployment targets.

It also strengthens the MigrationSummary idea we just designed. If skill headers/metadata are eagerly discoverable in ChatGPT and Codex, the OpenAI plugin can expose:

```yaml
MigrationSummary:
  LatestRequiredVersion: v18
  LatestOnUpdateVersion: v19
```

without loading full migration content. That becomes a real platform implementation pattern, not merely a hypothetical optimisation.

I would therefore change the earlier Deployment work in three ways:

-   **OpenAI becomes one platform family with multiple surfaces**, rather than separate “ChatGPT bundle” and “Codex collection” assumptions.
-   **Deployment Set resolution can map one logical set to one OpenAI plugin** that is consumed by ChatGPT and Codex.
-   The **bundle remains supported as an alternate representation**, for environments/projects where always-present context is useful or plugin/skill installation is unavailable, but it is no longer the default OpenAI deployment architecture.

One thing I would not lock yet is whether ChatGPT and Codex should _always_ consume the exact same plugin artefact. They may share the plugin package while still needing different skill content, manifests, triggers, or surface-specific adaptations inside it. That is exactly what the platform evidence pass should establish rather than assuming identical runtime behaviour.

So yes: this should be incorporated into the Deployment design before we do the detailed Deployment session. It removes one of the biggest awkward parts of the previous model.

  
  

> we will need to test with a standard.

  
  

Yes. Before we treat the OpenAI plugin/skills route as the primary Deployment path, we should prove it with a real Standard end to end.

The right test is a **small but representative Standard**, not Review or DocMeth first. I’d use something like **AIDE\_Tags** because it is compact but still tests the things we care about:

-   packaging a Standard as a skill inside a plugin;
-   whether ChatGPT web actually discovers/uses it;
-   whether Codex sees the same deployed skill;
-   whether the skill header/metadata is eagerly visible;
-   whether `MigrationSummary` can sit there without loading the full body;
-   whether Scope/trigger wording works in practice;
-   install/update/version behaviour;
-   whether one OpenAI plugin can serve both ChatGPT and Codex cleanly.

The test sequence should be:

```
AIDE_Tags canonical Standard
        ↓
build OpenAI skill
        ↓
package in test plugin
        ↓
install/deploy
        ↓
test in ChatGPT web
        ↓
test in Codex
        ↓
update plugin version
        ↓
verify replacement/version visibility
        ↓
record platform evidence
```

I would also deliberately include a tiny migration header in the test even if there is no real migration yet, for example:

```yaml
MigrationSummary:
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none
```

That lets us test the performance/discovery mechanism now rather than later.

So yes: **we should treat the OpenAI deployment model as provisional until one Standard successfully survives that full path.** After that, we can use the evidence to shape the actual Deployment Standard instead of designing from documentation alone.

  
  

> ok - before we continue to that we should update pending files. is there anything else we need to do before we output

  
  

Yes. I think we are ready for the output pass, but there are a few bookkeeping/cross-document items we should make sure are included so nothing from this session gets lost.

Before output, I would treat these as the complete pending changes:

-   **Migration corpus** — create the Migration Brief, Design, Standard and Tool Design from the decisions we made, including Required-on-use, On-Update-on-save, version-level posture, MigrationSummary fast-path, partial-success/failure state, exact-version handling, supported baseline, and skill-header guidance.
-   **Dependencies** — add the confirmed rule that declaration order is significant and provides default processing precedence.
-   **DocMeth review handoff** — add the generic temporary document-state mechanism (`Title [Owner] / Message`) and the broader principle that metadata/machine-generated content should stay compact in human-readable documents. Also record the revised update/migration interaction.
-   **Standards reconciliation** — rewrite the stale Standards Brief/Design against the current Tags/Scope/Dependencies/Migration/Review/Build boundaries.
-   **Tools reconciliation** — same for Tools, including removal of the old “Tools do not migrate” assumption.
-   **Identity/version contract** — complete the distinctions between document version, capability/release version, dependency conformance version, package version and deployment state.
-   **Package/Manifest contract** — define the smallest schema needed by Deployment, without pre-solving Deployment itself.
-   **Parent Capabilities docs** — update Decisions, Design, OpenItems, WorkRegister, Overview and Index so the new child work and superseded assumptions are reflected consistently.

One additional item from the last few turns should be captured, but as **provisional evidence/work to test**, not as a locked architecture decision:

> OpenAI plugins/skills may become the primary deployment mechanism for both ChatGPT and Codex, with the ChatGPT bundle becoming fallback/compatibility rather than primary. This must be validated with a real Standard before Deployment is designed around it.

That should go into the platform-evidence/open-work material, not into the final Deployment model yet.

I don't see another substantive design question we need to answer before output. The important thing now is a **single coordinated document pass** so the cross-component changes land together and we don't leave stale contradictory rules behind.

  
  

> ok - proceed

  
  

Completed. I updated the full pending Capabilities checkpoint and ran a consistency check across the new files. The OpenAI plugin/skills route is recorded as **provisional platform evidence to test**, not a Deployment decision.

The 18 updated/new files are:

-   **Migration:** · · ·
-   **Dependencies:** ·
-   **Standards:** ·
-   **Tools:** ·
-   **Parent checkpoint:** · · · · · ·
-   **DocMeth handoff:**

Items **1–5 are now marked complete**. The next substantive work is the representative Standard test of the OpenAI skill/plugin route, followed by the Deployment design pass.

  
  

> ok we now have 29 items in capabilities master folder and you can only add 25 to a gpt project sources. how to manage this

  
  

This is exactly the point where I would **stop treating the GPT Project source list as a mirror of the master folder**.

The 29 files in the Capabilities master folder are the **authoritative design corpus**. The GPT Project should receive a **deployment representation** of that corpus.

I’d use generated bundles.

For Capabilities, I would probably create around **4–6 project-source files**, for example:

```
Capabilities_Project_Core.md
  Brief
  Design
  Decisions
  Overview
  Index

Capabilities_Project_Work.md
  WorkRegister
  OpenItems
  DocMethReviewItems

Capabilities_Project_StandardsTools.md
  Standards Brief/Design
  Tools Brief/Design

Capabilities_Project_Runtime.md
  Tags Design/Standard
  Scope Design/Standard
  Dependencies Design/Standard
  Migration Brief/Design/Standard/Tool Design

Capabilities_Project_Review.md
  Review Design
  Review Decisions
  Review Standard
  Review Profiles Standard
  Review Tool Design
```

That reduces ~29 source files to about **5 sources** while keeping useful semantic boundaries.

Each generated bundle should retain very clear document boundaries:

```markdown
# SOURCE: Capabilities_Design_v6.md

<complete document>

---

# SOURCE: Capabilities_Decisions_v12.md

<complete document>
```

and ideally a short generated manifest at the top:

```
Bundle: Capabilities_Project_Core
Generated from:
- Capabilities_Brief_v5
- Capabilities_Design_v6
- Capabilities_Decisions_v12
...
```

### I would not make one giant 29-document bundle

It would technically solve the file-count problem, but I prefer several coherent bundles because:

-   retrieval has better semantic boundaries;
-   changing one area does not require rebuilding one enormous source;
-   a chat can more easily locate the relevant material;
-   we can eventually deploy different subsets where appropriate;
-   it remains understandable to us when debugging why an AI saw something.

Five-ish bundles gives us plenty of headroom under 25.

### Most important architectural rule

The bundles are **not another source of truth**.

```
Capabilities master folder
        ↓
authoritative 29 individual documents
        ↓
generated GPT Project bundles
        ↓
ChatGPT Project Sources
```

Never edit a bundle manually. Change the master document and regenerate.

That is actually consistent with the Deployment architecture we have been building: **Build/Deployment can compose multiple capability-local artefacts into a platform-specific Deployment Set output.** For ChatGPT Projects, these bundle files are exactly that sort of composed deployment artefact.

### There are really two different needs

For a **Capabilities design project**, we may want nearly the whole current corpus available, so the 5-bundle approach works well.

For a **consumer project**, we should not deploy the Capabilities internal Design/Decisions/WorkRegister at all. It should receive only the published Standards/Tools it needs — increasingly probably through skills/plugins, with a bundle only where required.

So I would adopt:

> **Master folder stays document-granular. GPT Project Sources are generated, logically grouped bundles.**

And I think we should add this as a concrete ChatGPT Project deployment pattern when we get to Deployment. It solves the 25-source limit without compromising the document methodology.

  
  

> ok if you are making bundles we should name them as such so there is not file confusion. project isnt clear, bundle is name might use elsewhere - maybe we use binder

  
  

Yes — **Binder** is better.

It clearly signals:

> “This is a generated collection of authoritative documents for a particular consumption context.”

That distinguishes it from:

-   the individual master documents;
-   capability packages;
-   Deployment Sets;
-   generic “bundles” that may be used elsewhere.

I’d use names like:

```
Capabilities_Core_Binder.md
Capabilities_Work_Binder.md
Capabilities_StandardsTools_Binder.md
Capabilities_Runtime_Binder.md
Capabilities_Review_Binder.md
```

And put a compact generated header in each:

```
Binder: Capabilities_Core
Generated from:
- Capabilities_Brief_v5
- Capabilities_Design_v6
- Capabilities_Decisions_v12
- Capabilities_Overview_v11
- Capabilities_Index_v12

Generated artefact. Do not edit directly.
```

I’d also define **Binder** as a deployment/build artefact, not a new authoritative document type. Its job is composition for source-count/context constraints.

So the model becomes:

```
Master documents
    ↓
Binder builder
    ↓
one or more Binders
    ↓
ChatGPT Project Sources
```

That naming is much less likely to get confused with the source corpus.

  
  

> ok can you build these - how can i give you the source files?

  
  

Yes. The easiest and cleanest way is to **ZIP the entire current Capabilities master folder and upload that single ZIP here**.

You do **not** need to add the 29 individual files to the GPT Project first. I can extract the ZIP, determine the current versions from the filenames/Index, and build the Binders from the authoritative files.

I’d produce these initially:

```
Capabilities_Core_Binder.md
Capabilities_Work_Binder.md
Capabilities_StandardsTools_Binder.md
Capabilities_Runtime_Binder.md
Capabilities_Review_Binder.md
```

Each Binder will:

-   contain the complete source documents, not summaries;
-   preserve each source document unchanged inside clear boundaries;
-   include a compact manifest of included filenames/versions;
-   say clearly that it is generated and must not be edited directly;
-   use deterministic ordering so rebuilding doesn't cause needless churn;
-   avoid including superseded versions where the current Index identifies the current one.

If, once I inspect the actual 29 files, a slightly different grouping gives substantially better retrieval or balance, I can adjust the Binder boundaries while keeping the naming obvious.

So: **ZIP `AIDE/Capabilities/` as it currently stands and upload the ZIP here.** That gives me the best source for building them.

  
  

  
  

Built and validated.

Your ZIP contained **28 files**: **27 current Capabilities documents registered in `Capabilities_Index_v12`**, plus `DocumentationMethodology_Guide_v17.md`. All 27 Capabilities documents are included **exactly once and byte-for-byte unchanged** across five Binders.

For the GPT Project, use these **6 sources total**:

-   — Index, Brief, Overview, Design, Decisions
-   — Work Register, Open Items, DocMeth review handoff
-   — Standards + Tools Briefs/Designs
-   — Tags, Scope, Dependencies, Migration
-   — Review Design, Decisions, Standards and Tool Design
-   — unchanged

I also packaged everything here:

The Binders are explicitly labelled **generated artefacts — do not edit directly** and contain a manifest plus clear `BEGIN SOURCE` / `END SOURCE` boundaries. Your individual master documents remain the source of truth.