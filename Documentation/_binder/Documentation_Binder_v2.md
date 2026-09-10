# Documentation Binder

> **Generated Binder - do not edit directly.** Edit the individual master documents
> and regenerate the Binder.
> **Binder Version 2** (2026-09-10).

This Binder is a current-context consumption artefact; authoritative masters remain
individual files.

## Binder manifest

- `Core/_index.md` - sha256 `8e58c5e0026b`
- `Core/Core_AIDEMap.md` - sha256 `e3b0c44298fc`
- `Core/Core_AIDEMap.yaml` - sha256 `a3f651bdb590`
- `Core/Core_AIDEPrinciples_Decisions_v1.md` - sha256 `655de3e64709`
- `Core/Core_AIDEPrinciples_Design_v1.md` - sha256 `60e20e8d0b9d`
- `Core/Core_Brief_v1.md` - sha256 `6c2e6280ea89`
- `Core/Core_Design_Documentation_Working_v1.md` - sha256 `b2999c523397`
- `Core/Core_Structure_Decisions_v1.md` - sha256 `2217f6768b89`
- `Core/Core_Structure_Design_v1.md` - sha256 `f464dc43de50`
- `Core/Core_Tags_Working_v1.md` - sha256 `ae6557378adf`
- `Core/Core_Working_v1.md` - sha256 `9808a331b339`
- `Documentation Methodology/_index.md` - sha256 `dd54608243d5`
- `Documentation Methodology/DocMeth_Decisions_v1.md` - sha256 `b349e5ec403e`
- `Documentation Methodology/DocMeth_Design_v1.md` - sha256 `e747f8b0f5e2`
- `Documentation Methodology/DocMeth_Working_v1.md` - sha256 `1af58d615fd8`
- `Infrastructure/_index.md` - sha256 `fb736219786c`
- `Infrastructure/binder-builder/binder_builder.py` - sha256 `0e833e66f750`
- `Infrastructure/binder-builder/binder_builder_Documentation_settings.json` - sha256 `b9b89306305b`
- `Infrastructure/binder-builder/BinderBuilder_Design_v10.md` - sha256 `e6573d80384e`
- `Infrastructure/binder-builder/README.md` - sha256 `3ec5dab12e67`
- `Infrastructure/file-update-package/file_update_package.py` - sha256 `b8ed8dd55035`
- `Infrastructure/file-update-package/file_update_package_settings.json` - sha256 `fce12837157e`
- `Infrastructure/file-update-package/FileUpdatePackage_Design_v1.md` - sha256 `11ad3a9f4c94`
- `Infrastructure/file-update-package/README.md` - sha256 `203b6f20f7ce`
- `Infrastructure/Infrastructure_CLI_Decisions_v1.md` - sha256 `d6e28bcbd3c3`
- `Infrastructure/Infrastructure_CLI_Design_v1.md` - sha256 `6ca6dc31f006`
- `Infrastructure/Infrastructure_Working_v1.md` - sha256 `1d7a11e25a57`
- `Infrastructure/version-cleanup/README.md` - sha256 `a978d666e85a`
- `Infrastructure/version-cleanup/version_cleanup.py` - sha256 `e5b1a470b662`
- `Infrastructure/version-cleanup/version_cleanup_settings.json` - sha256 `c17e9142e485`
- `Infrastructure/version-cleanup/VersionCleanup_Design_v3.md` - sha256 `e6d1eb38aba5`
- `Principles/Principles_Decisions_v4.md` - sha256 `2c31c26b5c66`
- `Principles/Principles_Design_v4.md` - sha256 `4bd5797d3d2e`
- `Standards/_index.md` - sha256 `3bd4678a60c0`
- `Standards/Standards_Working_v1.md` - sha256 `9677537477ab`
- `Working Practices/_index.md` - sha256 `f1d40d14c547`
- `Working Practices/FileOps/WP_FileOps_Working_v1.md` - sha256 `f2ffcdd7c76f`
- `Working Practices/WP_Capture_Working_v1.md` - sha256 `54171d4dea8b`
- `Working Practices/WP_ContentDelivery_Working_v1.md` - sha256 `6b858ff04f50`
- `Working Practices/WP_WorkManagement_Working_v1.md` - sha256 `59a0bba2401c`

---

<!-- BEGIN SOURCE: Core/_index.md -->
# Core

Role: component design

Core is the root entry to AIDE — the framework's self-description, component model, framework-wide requirements, and the map to all components. A reader arriving at AIDE reads Core to understand what AIDE is, what a component is, what the framework expects, and where to find any specific component's design.

## Key definitions at this level

**Component.** A defined area of functionality with a declared purpose, scope, and ownership. It owns its own documents and decisions. It may produce capabilities but need not. It is the functional unit independent of where it lives.

**Capabilities.** A term covering output definitions — Standards, Tools, Utilities. Components that define things delivering and adding functionality.

## Parts

**Structure** (prefix `Core_Structure_`)
How AIDE documentation is physically and logically organised — folder conventions, container labels, the AIDE document concept, path authority, and naming.

**AIDEPrinciples** (prefix `Core_AIDEPrinciples_`)
The operating principles specific to AIDE as a framework — facilitate not constrain, opt-in behaviour, strength model, aliases. Produces a standard for deployment. Distinct from the Principles component, which owns universal, portable premises.
<!-- END SOURCE: Core/_index.md -->

---

<!-- BEGIN SOURCE: Core/Core_AIDEMap.md -->
<!-- END SOURCE: Core/Core_AIDEMap.md -->

---

<!-- BEGIN SOURCE: Core/Core_AIDEMap.yaml -->
AIDEBrowser:
- name: Core
  type: Component
  description: ""
  folder: "~\Core"
  items: 
    - name: ""
      version: 1
      type: "file"
      filename: ""      
      doctype: ""
      description: ""
    
- name: Document Methodology
  type: Component
  description: 
  folder:"~\Document Methodology"  
- name: Workflow
  type: Component
  description: 
  folder:"~\Workflow"
- name: Capabilities
  type: Container
  description: 
  folder:"~\Core"
<!-- END SOURCE: Core/Core_AIDEMap.yaml -->

---

<!-- BEGIN SOURCE: Core/Core_AIDEPrinciples_Decisions_v1.md -->
Core AIDEPrinciples | decisions | Core_AIDEPrinciples_Decisions@v1 | 2026-09-10

## Summary

Reasoning behind the AIDE-specific principles, the strength model, and the aliases mechanism.

## Facilitate not constrain — placement

"Facilitate not constrain" was deferred during the Core brief (2026-09-08) pending a home. It was tested against the Principles component and failed the portability test — it is about AIDE specifically, not about all AI work. Placed in Core as an AIDE-specific operating principle.

The principle was then reworded to "facilitate and extend, not create friction or restrict" during the voice session (2026-09-09) to better express the active posture — AIDE does not just avoid constraining, it actively empowers.

## The design pattern it produces

Dave articulated the principle's mechanical consequence: functionality is attached to the structure and data it needs. The framework does not gate features behind compliance — it looks for the data a feature needs and applies the feature when that data is present. This is the "define it and you get functionality" incentive model operating at the principle level.

Examples: add a version tag to a document's identity and versioning applies. Add a doctype declaration and doctype logic fires. Add a dependency block and change management tracks it. Each feature activates from its own trigger data, not from a global compliance flag.

## Strength model — the fourth level

The original model had three levels (must/should/could, or required/recommended/optional). The fourth level — information — was added during the voice session (2026-09-09) when the reference document type was discussed.

The case: reference knowledge sometimes needs to reach the AI platform but carries no compliance expectation. A reference document is authored into a standard for delivery, not for governance. Without a fourth level, reference-origin content would carry "optional" strength, implying it is a choice to be made. "Information" correctly signals that the content is there to inform, with no decision or compliance attached.

## Aliases — why they matter

Arose during the session (2026-09-10) from the practical problem of referring to Documentation Methodology repeatedly in conversation and documents. The full name is precise but costly to type and read. Dave already uses "DocMeth" and "WP" (for Working Practices) naturally.

Rather than treating this as informal shorthand, aliases are declared alongside the thing they name. This makes them discoverable, unambiguous, and usable by both humans and AI — an AI seeing "DocMeth" can resolve it to Documentation Methodology because the alias is recorded.

Aliases are placed in the `_index.md` for the thing they name. This keeps them with the authoritative description rather than in a central registry.

---

Version note: v1 — initial decisions from sessions 2026-09-09 and 2026-09-10.
<!-- END SOURCE: Core/Core_AIDEPrinciples_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: Core/Core_AIDEPrinciples_Design_v1.md -->
Core AIDEPrinciples | design | Core_AIDEPrinciples_Design@v1 | 2026-09-10

## Brief

**Purpose.** Produce a standard that delivers the operating principles specific to AIDE as a framework.

**Scope.** AIDE-specific tenets that shape how the framework behaves and how its features are adopted. Distinct from the Principles component, which owns universal, portable premises governed by the portability test. Content that fails the portability test — it is about AIDE, not about all AI work — lives here.

**Target outcome.** A deployed standard carrying these principles, the strength model, and the aliases mechanism, so that any AIDE-governed session applies them.

## Facilitate and extend, not create friction or restrict

AIDE empowers. It adds functionality where needed but does not do so from a position of control or dictation. If a user wants to add AIDE's features to a document or project, in full or in part, AIDE applies them where it can. If the user chooses not to, they manage those items on their own.

This leads to a design pattern: functionality is attached to the structure and data it needs to function. Add a particular block type to a document which has the data needed for a component feature to function, and it will be applied.

## Opt-in for benefit, opt-out loses the benefit only

Adopting an AIDE convention activates the functionality it provides. Not adopting it means managing that concern yourself — nothing breaks, nothing is imposed. The cost of opting out is losing the benefit, not gaining a penalty.

AIDE is ambient until something triggers its behaviour. The presence of declarations in the header — the doc type above all — is what brings AIDE into play. This is opt-in by self-description.

## Strength model

Items in standards carry strength — four levels defining how strongly they apply:

- **Required** — must be followed
- **Recommended** — should be followed; deviation needs a reason
- **Optional** — available for use; adoption is a choice
- **Information** — reference-origin content provided for awareness; no compliance expectation

The fourth level (information) exists for content that originated as reference knowledge and was authored into a standard for delivery to the platform. It carries no compliance weight — it informs, it does not direct.

## Aliases

Named things in AIDE — components, areas, parts — may have aliases: shorter or alternative names used for convenience. An alias is an equivalent reference to the same thing.

Aliases are declared where the named thing is described. For a component, that is the `_index.md` in its folder. For example, Documentation Methodology carries the aliases DocMeth and DM.

The purpose is practical — reducing typing and making conversation easier without losing precision. An alias resolves to exactly one thing; where ambiguity exists, the full name is used.

---

Version note: v1 — initial design. Principles from voice session 2026-09-09; aliases from session 2026-09-10.
<!-- END SOURCE: Core/Core_AIDEPrinciples_Design_v1.md -->

---

<!-- BEGIN SOURCE: Core/Core_Brief_v1.md -->
# Core — Brief

Version 1. 2026-09-08.

---

## Purpose

Core is the root entry to AIDE. It describes what AIDE is, how it is structured, and the framework-wide requirements and concepts that govern all components. A reader starting here should be able to understand AIDE's shape and navigate to any component from it.

---

## What AIDE is

AIDE makes the standards and behaviours that shape how AI works with you live in your sessions, on whatever surface is in use. Everything else in AIDE exists to produce, deliver and keep that content current.

It is a methodology-driven framework for a solo developer working with AI. It gives AI sessions consistent behaviour, accumulated knowledge, and standards defined by the owner — not by platform defaults.

---

## Objectives

O1. Provide a single, maintained description of what AIDE is and how it works — the framework's own self-description.

O2. Define the component model: what a component is, what a capability is, and how components relate to each other.

O3. Hold the framework-wide requirements that govern all components and cannot be owned by any single one.

O4. Serve as the entry point — a reader (human or AI) arriving at AIDE for the first time navigates from here.

---

## Requirements

R1. **Facilitate, not constrain.** AIDE exists to facilitate and empower, not to constrain or be a source of friction. This is AIDE's own character — distinct from the universal principles, which hold outside AIDE. Every framework-wide decision is tested against it.

R2. **Component model.** Every component has a declared purpose, scope and ownership. A component owns its own documents and decisions. The component definition, the capability definition (standards and tools), and the utility definition all live here.

R3. **Platform neutrality.** Capabilities are defined platform-neutral — the what — and transformed into platform-specific delivery. On Claude, that means skills in a plugin.

R4. **Leanness.** What loads into a session must justify its weight. Leanness is a governing principle at the framework level; the Standards component owns the authoring guidance that enforces it.

R5. **Design is the default.** A design almost always exists behind a standard. Authoring straight to standard is the exception, not the rule.

R6. **No knowledge lost.** The framework captures and places everything of value. This is the fundamental rule.

R7. **Entry-point completeness.** Core's design document must contain a summary of every active component — its purpose and key boundaries — sufficient for navigation. The design specification of each component lives in its own folder.

---

## Considerations

C1. Core absorbs the "facilitate not constrain" position that was deferred pending a home. It is now settled here.

C2. Core replaces the previous definition ("hold whatever shared requirements have no natural home elsewhere"). The new purpose is deliberate and first-class, not residual.

C3. The relationship between Core and Principles needs to stay clean. Principles owns universal premises (portability test). Core owns AIDE-specific character and governance. "Facilitate not constrain" fails the portability test — it is about AIDE, not about all AI work — and therefore lives here, not in Principles.

C4. Some requirements above (leanness, design-is-the-default, no-knowledge-lost) are also expressed or implied elsewhere. Core holds the framework-wide statement; the owning component holds the mechanism. No duplication of mechanism.

C5. The three held candidates (Tags, Scope, Dependencies) and the deferred concerns (environment, platform, domains) remain open and are not resolved by this brief.

---

## Scope and boundaries

**In scope:**
- The framework's self-description and conceptual model
- Framework-wide requirements and considerations
- The component, capability and utility definitions
- The component map — purpose lines and navigation to each component's own material
- AIDE's character statement (facilitate not constrain)

**Out of scope:**
- Individual component designs — each component owns its own folder
- Principles — universal premises live there, governed by the portability test
- Documentation Methodology — the grammar of how documents are written
- The rebuild process itself — that is a project, not a permanent part of the framework

---

## Target outcome

A reader arriving at AIDE — whether a new AI session, a reviewing AI, or the human owner returning after time away — can read Core and understand: what AIDE is, what a component is, what the framework expects of every component, and where to find any specific component's design. Core is the map and the constitution.

---

## Definition of done

1. Core's design document describes the component model, capability and utility definitions, and framework-wide requirements
2. Core's design document contains a current summary of every active component with purpose and key boundaries
3. "Facilitate not constrain" is placed and stated with its rationale
4. The distinction from Principles (portability test) is explicit
5. A reader unfamiliar with AIDE can navigate from Core to any component
<!-- END SOURCE: Core/Core_Brief_v1.md -->

---

<!-- BEGIN SOURCE: Core/Core_Design_Documentation_Working_v1.md -->
# Core — Design Documentation Working

Version 1. 2026-09-08. Working document — concept and principle, not placed.

---

## Status

Exploratory shaping session. Recording thoughts, knowledge, ideas and decisions as concept and principle. Residence of each piece not yet decided. When complete, consolidate and work out where each item belongs.

---

## The anchor — what AIDE is for

Core states AIDE's outcomes; components deliver them. The design use case is the lead outcome, delivered by the Project Design component.

AIDE is ambient until triggered by self-declaration. A document opts into AIDE's capabilities by carrying the information that maps it into scope. No declaration, no imposition — it is just a document. This is facilitate-not-constrain expressed as a mechanical principle.

---

## Forks abandoned

An earlier proposal split AIDE into two forks — Development (building the framework) and Framework (using it). Abandoned because it duplicates: every component would be described twice with most of the substance shared.

Instead, one project per component carries both concerns. The applied-behaviour lens — how the component operates once the framework is live — is included in each component's design where relevant, not as a fixed required element on every design.

---

## Structure — design projects and design areas

### Design project

A container grouping all design material for an area of work. "Project" is the term despite collision with Claude/chat projects — it is the natural word, and the collision is handled by context. "Design project" disambiguates when needed.

### Design area

A bounded part of the thing being designed. Areas are the groupings within a project — each is a section of the overall design. Terminology settled: **project** as the container, **area** as the grouping.

CMS is the reference example: areas include query, views, relationships, dependency system, keys, change log, localisation, pipeline, predicate engine, schema, tags, values — each a different part of the overall design.

### Folder structure

Folders are free organisation only. They carry no meaning the system depends on. A folder might hold one area, several areas, or areas might sit loose with no subfolders. Binders retire the old flatness constraint — a binder can carry a whole project or a segment, so subfolder hierarchies are now practical without paying a sync cost.

### Area identity and hierarchy

Areas are declared on the document, not by folder position. Expressed as a delimited **path** relative to a context-defined root. The path encodes the hierarchy — each segment is a level, shared prefixes show what is related.

Example: CMS / query / SQL — CMS is the project, query is the area, SQL is the sub-area.

Areas can be hierarchical. A sub-brief either opens a new area or sections an existing one — the brief itself declares which by carrying a different or the same area identity.

### Path — the general property

The property is **path**, not "design path." It is a general locating mechanism, not design-specific. Build documentation or anything else uses the same concept. The path is relative to a context-defined root; what the root represents depends on the domain. In a design project, the root is the project.

---

## Expand and collapse

The brief is always conceptually present. Big areas earn a separate brief and separate design documents. Small areas collapse the brief inline into the design document. Same methodology, scaled to the weight of the area.

A brief can branch to sub-briefs, to design documents, or both. The author decides per case and records it — flexible where it should be, explicit so the system knows.

---

## Document handling model

Three self-declared properties compose to give a document its behaviour:

1. **Path** — where it sits in the design structure, relative to a root.
2. **Doc type** — what it is. A known doc type inherits functionality and behaviour automatically. Declare the type and the behaviour comes with it.
3. **Blocks** — the granular unit of functionality. Known defined blocks bring their own logic whether or not the document has a doc type. Include a versioning block and versioning applies. Declare a dependency and the system knows what to do when that standard changes.

Path and doc type are independent and compose. Path is location, doc type is nature. Neither depends on the other.

### Partial application

Blocks work independently of doc type. A freeform document with no doc type can include known blocks, and each block gains its functionality — production guidance, navigation, extraction, and migration scope. Known parts get full support; the rest is carried inert. Functionality degrades gracefully, not all-or-nothing.

### The incentive model

"Define it and you get functionality; don't and it's inert." This is the design principle that lets AIDE be permissive without becoming chaos. You can extend freely — new doc types, modified structures — but you define what you create so the system knows how to handle it. Stay within known structures and you get support for free. Go your own way and you document your own information locally.

---

## Header and footer convention

### Header — triggers and identifies

The header holds what must be seen first because it switches on logic. A machine reading a document starts at the header, sees a doc type, and that fires the doc type skill, loads the rules and functionality, and loads the standard containing that type.

Header carries:
- Path
- Document identity
- Dependencies (change tracking / change management)
- Doc type
- Custom block types (delimited list, if the document includes blocks beyond what the doc type implies)

### Footer — elaborates

The footer holds structural detail needed only after the header has established what the document is. Accessed by jumping to the end, which is fast for both humans and machines.

Footer carries:
- Custom layout and block positioning within the document flow
- Document spec or structure definition for custom documents
- Custom doc type definition, if this document defines its own

### Principle

Header triggers, footer elaborates. Anything that must fire functionality goes up top and stays lean. Structural elaboration goes to the bottom, out of the way but findable. Metadata placement serves both machine navigation and human readability.

---

## AIDE activation model

AIDE is ambient until something triggers its behaviour. The presence of declarations in the header — the doc type above all — is what brings AIDE into play against a document. The header is not just describing the document, it is activating AIDE.

This is opt-in by self-description. No declaration, no imposition. The trigger model is the facilitate-not-constrain principle operating at the mechanical level.

---

## Stable triad

Most designs vary in their stages, but nearly all land on three document types: **brief** (the what — purpose, objectives, requirements, considerations, scope), **design** (the how — the confirmed model and approach), and **decisions** (the knowledge capital — how decisions were made, what was learned along the journey).

---

## Rapid evolution cycle

AIDE is a living, evolving system. Learn something while working, stop, design the component or standard or doc type needed, build it, deploy it — and use it almost immediately. This rapid application development cycle is why migration and change management are fundamental infrastructure, not bolted on.

---

## Open items

1. **Working document** — needs a proper definition as a concept. Flagged, not solved.
2. **Header/footer detail** — which exact properties at which end; the rule is clear but the full list needs pinning.
3. **Residence** — where each piece in this document eventually belongs across the AIDE components. To be consolidated when the shaping is complete.
4. **Path delimiter** — settled as a concept; the exact delimiter and any naming rules are design detail.
5. **Area boundary mechanism** — area boundaries are declared in documents, not by folders. The precise mechanism (property, marker block, doc type implication) is for the design.
6. **Core Brief v2** — drafted but needs rework to reflect this session. The fork structure is abandoned; Core's objectives now include stating AIDE's outcomes with components delivering them.
<!-- END SOURCE: Core/Core_Design_Documentation_Working_v1.md -->

---

<!-- BEGIN SOURCE: Core/Core_Structure_Decisions_v1.md -->
Core Structure | decisions | Core_Structure_Decisions@v1 | 2026-09-10

## Summary

Reasoning and alternatives considered for the structural design decisions in the core structure design.

## Physical folders over logical overlays

Explored whether documents needed a logical path structure separate from the physical folder tree. The case for logical paths: documents loaded into flat AI context lose their folder position, so something must carry "where do I sit." Two mechanisms already solve this — the binder manifest carries relative paths for bulk loading, and the document header carries its own path for individual files. A logical overlay on top of the physical structure would duplicate what both already do.

Also explored whether multiple root scopes could share a folder, with documents associating to a specific root by reference. This was the logical-vs-physical separation at its most complex. Dave's direction: drop logical overlays entirely, keep it physical. If two areas need separation, make two folders.

## Root scope parked

Root scope was designed as a block type declaring a folder as a root of a particular kind — design project, component design, etc. The concept went through several iterations: separate block types per root scope kind, then a single block with a type name pointing at a standard.

Parked because no consumer could be identified. Every purpose root scope was supposed to serve is already handled:
- Path anchoring → physical folders plus header paths
- Structure preservation in context → binder manifest
- Container description → the AIDE document
- Classification ("this is a design project") → the role field in the AIDE document

Root scope was compensating for a problem (context flattening) that binders already solve. Identified during discussion as the likely origin of the concept — when files were in flat folders for context loading, logical structure needed to be declared. With binders carrying relative paths, the need disappeared.

## Container labels — vocabulary not types

Considered whether folder roles should be a formal type system with defined nesting rules (solution design contains project designs, project designs contain component designs, etc). Decided against: the labels describe what something is, not what it is allowed to contain. Nesting rules would impose structure the facilitate-not-constrain principle argues against, and no current functionality depends on knowing what's inside what.

Four labels chosen from existing vocabulary Dave already uses:
- Solution design — mirrors .NET solution concept
- Project design — mirrors .NET project concept, aligns with the Project Design component name
- Component design — matches the component definition
- Area / part — both used naturally, synonyms until a distinction is demonstrated

## AIDE document naming

Explored several options for the file name:
- `_AIDE.md` — sorts to top but brands every folder with the framework name
- Named after the container (e.g. `Principles_AIDE.md`) — self-describing but doesn't stand out
- `_folder.md` — generic but describes the container, not the function
- `_index.md` — generic, familiar concept, describes the function (indexing), room to grow

Chose `_index.md`. The underscore sorts it to the top. "Index" describes what it does rather than what it is about. The name is generic enough to work for any project whether using AIDE fully or partially. The concept retains the name "AIDE document" within framework terminology; the file on disk uses a name that doesn't advertise.

## Path authority chain

Applied the same pattern as identity and filename: header is authoritative, file system mirrors. This was a deliberate alignment — both follow the principle that a document should be self-describing and survive being detached from its context. A file pasted without its folder still states where it belongs.

Considered whether the physical-folders-as-structure decision created tension with header-as-authority. It does not — the physical structure is the expected organisation, the header is what the document says about itself. They agree in the normal case; the header wins on conflict.

## Three-tier file model

Arose from the question of what the binder should include. Initially framed as "governed documents only" versus "everything." Dave's test was sharper: does it need to be there for thinking and reasoning? A utility script that is the project's deliverable needs to be in context when working on that utility. A log file never does.

The three tiers:
1. In the binder — needed for thinking and reasoning in the AI session
2. Known to the framework — listed in the `_index`, not loaded into context. The framework knows it exists
3. Just present — incidental files AIDE has no opinion about

This is recorded as a decisions entry because it affects binder design (owned by Working Practices / Content Delivery) and will be referenced from there. The structural implication — the `_index` as the awareness mechanism for tier 2 — belongs here.

## Design and output separation

Design documents and the outputs they produce are separate. The design folder holds the specification; what gets built from it lives where it is consumed. This arose from Infrastructure where utility design docs sat alongside the Python scripts they specified. The scripts are outputs, not design — they belong where they run (_utilities), not where they were designed.

The principle applies broadly: utilities to _utilities, skills to the skills deployment location, standards to capabilities, plugins to the marketplace. The design folder is always "why and how"; the output is always elsewhere.

---

Version note: v1 — initial decisions from session 2026-09-10.
<!-- END SOURCE: Core/Core_Structure_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: Core/Core_Structure_Design_v1.md -->
Core Structure | design | Core_Structure_Design@v1 | 2026-09-10

## Summary

Defines how AIDE documentation is physically organised and navigated. Physical folders are the structure. Documents self-declare their identity and path in their headers, which is authoritative — the file system mirrors it. An optional file named `_index.md` describes a folder and indexes its contents for both human and AI readers. Four container labels provide shared vocabulary for describing what a folder holds. There is no logical overlay, no root scope mechanism, and no formal folder-type system — the conventions empower organisation without imposing it.

## Physical folders are the structure

Folder hierarchy on disk is the organisational structure. There is no separate logical layer. Documents live where the folders put them, and paths resolve from the physical tree.

This decision followed from the removal of root scope (see below) and the recognition that the binder manifest preserves relative paths when documents are loaded into flat AI context. The need to reconstruct structure from declarations disappears when the binder already carries it.

## Path authority

The path declared in a document's header is authoritative. The file's position on disk mirrors it. If they disagree, the header is what the document says it is and the file is in the wrong place. This is the same relationship as identity and filename — header wins, filename mirrors.

A mismatch between header path and physical location is a detectable signal AIDE can flag.

### Path maintenance

To change a document's path: update the path in the header. The FileUpdatePackage carries the move to the file system via a move action. For files updated outside an update package in chat, instruct the user where to save based on the header path. For Code or Cowork working directly on files, check the file's physical location against the header path and move if they disagree.

## Container labels

Four labels provide shared vocabulary for describing what a folder contains. Declared in the `_index.md` file via a `role` field. Plain string value.

Known labels:

- **solution design** — umbrella container; holds component designs, project designs, and areas
- **project design** — contains the design docs for a project
- **component design** — contains the design for a component
- **area / part** — a segment or grouping within a design; two labels for the same concept

Using a known label gives AIDE inference — it recognises what the folder is for. Using a custom label works, it just is not one AIDE knows about. The list grows as new kinds demonstrate the need. No nesting rules are defined — the labels describe what something is, not what it is allowed to contain.

## The AIDE document — `_index.md`

A file named `_index.md` placed in a folder serves as the container's description and index. The concept is called the AIDE document within the framework; the file on disk uses a generic name with no framework branding.

The underscore prefix sorts it to the top of any folder listing. The name "index" describes its function and has scope for including additional logic in future.

### Purpose

Describes what this folder is (via the role field) and indexes what it contains. In a mixed folder holding multiple parts, the body carries a parts list. Each entry in the parts list has a name, a short description, and optionally an entry point file. The parts list also records the file prefix associated with each part.

### When it earns its place

The AIDE document is optional. It earns its place when a folder's contents are not obvious from the files alone — typically when a folder holds multiple parts or when a reader needs orientation. Single-part folders with a handful of clearly-named files do not need one.

### Format

Markdown is the natural choice when the content mixes structured fields (role, parts list) and descriptive prose. If a future `_index` is primarily machine-consumed structured data, yaml or json would be the right format. Format fits the job.

## Root scope — parked

Root scope was explored as a mechanism for declaring a folder as a root of a design project, component design, or similar container. It was parked: no consumer exists. Physical folder structure provides organisation, the binder manifest preserves paths for context loading, and the path in document headers provides self-description. Root scope was compensating for context flattening, which the binder already solves.

Root scope returns if a feature demonstrates it needs a formal root declaration.

## Binder as structure preservation

The binder manifest records relative paths for every document it includes. When documents leave the file system and enter flat AI context, the manifest is what preserves their structural relationships. This is not a new mechanism — binders already do this. It is documented here because it is the reason root scope is unnecessary and physical folders are sufficient.

---

Version note: v1 — initial design from session 2026-09-10.
<!-- END SOURCE: Core/Core_Structure_Design_v1.md -->

---

<!-- BEGIN SOURCE: Core/Core_Tags_Working_v1.md -->
Core — Tags | working | Core_Tags_Working@v1 | 2026-09-10

## Status

Tags resurrected from the held candidates list during the 2026-09-09 voice session. Confirmed as a Core capability with its own area (prefix Core_Tags). Four items identified for design; standard as output, tools deferred.

## Confirmed design (2026-09-09)

### What tags are

A flat list of string keys placed in a document's header. Tags label a document for classification, discovery, and feature activation. They are a Core capability because they serve any component — not owned by a single consumer.

### Named groups

Tags may be organised into named groups for ownership purposes. A group declares which component or area owns a set of tag definitions. Groups are an authoring-time concept only — they are invisible to consumers.

**Collapse behaviour.** When tags are consumed (by search, by a tool, by any logic reading a document), groups collapse to a single flat list of distinct keys. A consumer never sees group boundaries. This keeps the consumer interface simple regardless of how many groups or owners contribute tags.

### Producer/consumer model

Any component can define tags (producer). Any logic can read tags (consumer). The openness is deliberate — tags are a shared vocabulary, not a controlled namespace. Collision between independently-defined tags sharing a key is possible and is resolved by the tag definition, not by the framework.

## Items for design

1. **Tag definition** — what a tag definition looks like, where it lives, what it must state
2. **Group-ownership model** — how groups are declared, how ownership is expressed
3. **Collapse behaviour** — the precise rule for flattening groups to a distinct list
4. **Producer/consumer openness** — any constraints on who can define or read tags, or fully open

## Output

A standard. Tools deferred — no demonstrated need for tag-manipulation tooling yet.

---

Version note: v1 — initial working document from session 2026-09-09.
<!-- END SOURCE: Core/Core_Tags_Working_v1.md -->

---

<!-- BEGIN SOURCE: Core/Core_Working_v1.md -->
Core | working | Core_Working@v1 | 2026-09-10

## Three pillars (confirmed 2026-09-09)

AIDE's components organise around three pillars — three kinds of thing that together make the framework work:

- **Building blocks** — the structural primitives. How documents are shaped (doctypes, block types, the declaration), how they identify themselves (identity, versioning), how they are organised (folders, paths, the AIDE document). Documentation Methodology owns this pillar.

- **Workflows** — the behavioural patterns. How a person works with AI across sessions and surfaces: the development lifecycle, capture-and-place, handoffs, work management, file operations. Working Practices owns this pillar, with Project Design and Build owning the design-and-build path within it.

- **Standards** — the guidance layer. Rules, expectations, and context that shape decisions and behaviour while work is being done. The Standards component owns what a standard is and how one is authored; individual standards are owned by the component that knows the most about their subject.

The overview sits in Core because it is a framework-level concept — it describes how AIDE's parts relate to each other. The individual pillars are owned by their respective components.

This is a framing concept, not a hierarchy. Components do not belong to pillars; they contribute to them. A component like Migration contributes to both workflows (how change actions are executed) and standards (what a migration record looks like).

---

Version note: v1 — initial working document from session 2026-09-09.
<!-- END SOURCE: Core/Core_Working_v1.md -->

---

<!-- BEGIN SOURCE: Documentation Methodology/_index.md -->
# Documentation Methodology

Role: component design
Aliases: DocMeth, DM

Documentation Methodology defines how documents are structured and created — the generic mechanics. It owns the grammar of documents: doctypes, block types, the declaration, rendering rules, and the structural conventions that make documents portable and machine-readable. It is not a registry of types belonging to other components — specific doctypes and block types live with whoever knows the most about them.
<!-- END SOURCE: Documentation Methodology/_index.md -->

---

<!-- BEGIN SOURCE: Documentation Methodology/DocMeth_Decisions_v1.md -->
Documentation Methodology | decisions | DocMeth_Decisions@v1 | 2026-09-10

## Status

Awaiting the full design pass. Reasoning from the rebuild sessions covering doctypes, block types, versioning, and format rules will be consolidated here from the settled rebuild decisions and session transcripts.
<!-- END SOURCE: Documentation Methodology/DocMeth_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: Documentation Methodology/DocMeth_Design_v1.md -->
Documentation Methodology | design | DocMeth_Design@v1 | 2026-09-10

## Status

Awaiting the full design pass. Substantial content exists in the settled rebuild decisions (extracted from WIP v22) covering the doctype/block-type model, the block catalogue, the versioning model, format rules, and the decisions doctype. This document will be populated when that material is worked through.
<!-- END SOURCE: Documentation Methodology/DocMeth_Design_v1.md -->

---

<!-- BEGIN SOURCE: Documentation Methodology/DocMeth_Working_v1.md -->
Documentation Methodology | working | DocMeth_Working@v1 | 2026-09-10

## Confirmed items — session 2026-09-10

### File naming convention

Recommended pattern: `{Prefix}_{DocType}_v{N}.md`. Applied by default, not enforced. Deviate and you manage your own file identification. The header is authoritative for identity, doctype, and path; the filename mirrors for human readability.

### Format fits the job

Choose the format that best serves the document's primary consumer and content shape. Markdown for prose-heavy documents. Yaml or json for structured data. Html where appropriate. The declaration header and block model work across formats — this is already settled in the block catalogue rendering rules. Format is a considered choice, not a default.

### Prefix convention

File prefixes identify the subject — typically the area, part, or component name. Recommended and applied by default. A prefix makes a file distinguishable in search results, open-file lists, and folder listings regardless of whether it sits in its own subfolder or flat alongside other files.

### Binder as a doctype

The binder is owned as a doctype definition by Documentation Methodology — its structure as a document, how to read it, what a binder contains. The concept of the binder — why it exists, how it is built, inclusion rules, how it delivers content to the platform — is owned by Working Practices / Content Delivery.

---

Version note: v1 — initial working document from session 2026-09-10.
<!-- END SOURCE: Documentation Methodology/DocMeth_Working_v1.md -->

---

<!-- BEGIN SOURCE: Infrastructure/_index.md -->
# Infrastructure

Role: component design

Infrastructure defines how to build and deploy utilities, and owns the design of the delivery mechanism (the `aide` dispatcher). It is a methodological component — it does not hold all utility designs. Individual utility designs live with the component or area that knows the most about them, under the what-knows-most-about-it principle.

Infrastructure is machinery that acts on the corpus and environment from outside the AI session. It is never loaded into session context and does not shape in-session decisions.

## Key distinction

Infrastructure utilities are not capability Tools. Capabilities (Standards, Tools) are loaded into the AI session to shape behaviour. Utilities run outside the session, acting on files, folders, and the environment.
<!-- END SOURCE: Infrastructure/_index.md -->

---

<!-- BEGIN SOURCE: Infrastructure/binder-builder/binder_builder.py -->
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
binder builder - gather the documents of a defined scope into one file.

WHAT IT DOES
    Walks a folder tree, collects every in-scope file, and writes them into a
    single Markdown "binder" that can be dropped into an AI session's context,
    so a whole topic loads as one artefact rather than as many files.

    The binder carries a header, a manifest of what it contains with a sha256
    digest per file, and then each source file verbatim between comment
    delimiters.

WHAT IT DOES NOT DO
    It does not resolve versions - that is version cleanup's job, run first -
    and it does not deploy. It collects and assembles, nothing else.

    Source content is copied UNMODIFIED. No reformatting, no heading demotion,
    no normalisation. A binder that alters its sources would be worse than no
    binder at all.

HOW IT IS RUN
    Live by default. Pass --dry-run to see the report without writing
    anything. It reads its settings from a JSON file sitting beside this
    script, so it can simply be double-clicked on Windows.

    A settings file IS a binder definition - it declares the scope. Several
    definitions can sit in one folder, as binder_builder_settings.json plus any
    number of binder_builder_settings_<something>.json beside it. One run keeps
    all of them current; name one or more binders on the command line to run
    only those.

    A rebuild is skipped when nothing in scope has changed since the last
    binder was written: the manifest inside that binder carries a digest per
    file, and comparing it against this run's digests answers the question
    without keeping any state of its own. Pass --force to rebuild anyway.

DESIGN NOTE
    This is one tool that does one thing, and a sibling to version cleanup.
    The path logic, settings loader and plan/apply split below are deliberately
    the same shape as that tool's, copied rather than imported: there is no
    shared module, no plugin system and no base class between them.

Python 3.8 or newer. Standard library only.
"""

import argparse
import datetime
import fnmatch
import hashlib
import json
import os
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
# Path(__file__) is this script's own file. .resolve() turns it into a full,
# unambiguous path, and .parent gives the folder holding it. Everything the
# tool reads or writes hangs off this folder rather than off the "current
# working directory", because the working directory depends on *how* the script
# was launched (double-click, terminal, scheduler) and is therefore unreliable.
# It also means each copy of the tool uses its own settings and its own log.
SCRIPT_DIR = Path(__file__).resolve().parent

# A settings file is named for the binder it defines, so a folder holding four
# of them can be read without opening any of them:
#
#   binder_builder_AIDE_Documentation_settings.json
#   binder_builder_ProjectDesign_settings.json
#
# The name in the filename is not what the tool reads - the "name" setting
# inside the file is - so the two can in principle disagree. --list prints them
# side by side, which is where a disagreement shows up.
SETTINGS_FILENAME_FORMAT = "binder_builder_{name}_settings.json"

# What a fresh copy of the tool writes for itself, before anyone has told it
# what the binder is called.
DEFAULT_BINDER_NAME = "Documentation"

# The name this tool used before definitions were named, kept working because
# settings files carrying it exist. It sorts first when present.
LEGACY_SETTINGS_FILENAME = "binder_builder_settings.json"

# Deliberately wider than the format above. It matches the named form, the
# legacy plain name, and the "binder_builder_settings_<x>.json" spelling
# documented between v5 and v8 - none of which should stop working because the
# convention was tidied.
SETTINGS_GLOB = "binder_builder*settings*.json"

# A log is named for its binder too, so four definitions in one folder do not
# interleave four runs in one file. A definition can still point several
# binders at one log by setting log_file explicitly.
LOG_FILENAME_FORMAT = "binder_builder_{name}.log"
SUPERSEDED_FOLDER_NAME = "_superseded"

# Folders skipped unless the settings explicitly include them. The leading
# underscore rule is the important one: it keeps the walk out of _superseded
# and out of the tool's own _binder output, which is what makes it impossible
# for a binder to contain a previous binder.
ASSET_FOLDER_NAMES = ("assets", "images", "img", "media")

DEFAULT_FILE_TYPES = ("md", "yaml", "yml", "json", "txt", "py")

# Matches "<Name>_Binder_v<number>.md" so the output folder can be scanned for
# the highest version already written. The name is substituted in escaped, and
# matching is done against a case-folded filename, so the pattern itself does
# not need to worry about case.
BINDER_FILENAME = "{name}_Binder_v{number}.md"

# Spots "C:" or "D:" at the start of a settings path, so a Windows path in a
# settings file being run on Mac or Linux fails loudly rather than being
# mistaken for a relative pattern that then silently never matches anything.
WINDOWS_DRIVE = re.compile(r"^[A-Za-z]:")

# Digests are truncated sha256. Twelve hex characters is plenty to answer
# "is this binder still in step with the masters" without filling the manifest
# with noise.
DIGEST_LENGTH = 12

# Change detection reads the manifest back out of the previous binder, so these
# three constants describe the header that build_binder_text writes. They are
# not a second definition of the format - they are a reader for it, and the two
# have to be changed together.
MANIFEST_HEADING = "## Binder manifest"

# "- `<label>` - sha256 `<digest>`". The separator between the two is matched
# loosely, so a manifest written with an en dash - or tidied by hand - still
# parses. A line that does not match at all makes the whole manifest
# unreadable, and an unreadable manifest means rebuild.
MANIFEST_ENTRY = re.compile(
    r"^-\s+`(?P<label>[^`]+)`.*?sha256\s+`(?P<digest>[0-9a-fA-F]+)`\s*$"
)

# A binder that announced itself as incomplete is never used as a comparison
# baseline. It is missing files by definition, so "nothing changed" measured
# against it would hold the hole open indefinitely.
INCOMPLETE_MARKER = "INCOMPLETE BINDER"

# The settings file is shipped with the tool, but if someone deletes it - or
# copies just the .py file to a new location - we write this back out rather
# than failing. Keeping the defaults as *text* (not as a Python dictionary that
# gets dumped to JSON) means the file we create is byte-for-byte the file we
# ship, comments and ordering included.
#
# JSON has no comment syntax, so the explanatory lines are carried as ordinary
# keys beginning with "_comment". The loader ignores them. That keeps the file
# valid JSON, readable by any editor and parseable by the standard library.
DEFAULT_SETTINGS_JSON = """{
  "_comment": "Settings for the binder builder. This file IS the binder definition - it declares what the binder contains. One binder per copy of the tool: a second binder means a second folder with its own copy of the script and its own settings, not a second entry here. Any key starting with _comment is ignored by the tool - JSON has no comment syntax, so notes live in keys like this one.",

  "_comment_name": "The binder's name. Used in the heading (\\"<name> Binder\\"), in the binder filename (\\"<name>_Binder_v<number>.md\\"), and in this settings file's own name (\\"binder_builder_<name>_settings.json\\") and log (\\"binder_builder_<name>.log\\"). It also identifies this binder on the command line, and no two definitions in one folder may share it.",
  "name": "Documentation",

  "_comment_root": "The folder the binder is built from, including everything beneath it unless subfolders is false. A relative path is resolved against the folder this script lives in, so \\"..\\" means the parent folder. Give a full path such as \\"C:/Users/you/Documents\\" to point somewhere else. Forward slashes are safe on Windows.",
  "root": "..",

  "_comment_subfolders": "true walks the whole tree from root. false collects from root only.",
  "subfolders": true,

  "_comment_paths": "include and exclude accept three kinds of path. ABSOLUTE - \\"C:/Docs/_binder\\" - names one exact folder. ROOT-ANCHORED - \\"~/_binder\\" - names one exact folder, measured from the root above. RELATIVE - \\"_binder\\" - is a pattern rather than a place: it matches every folder in the tree whose path ends with those segments, so one entry covers a _binder subfolder wherever it appears. Note that ~ means the root of the tree here, never your home folder.",

  "_comment_defaults": "The tool skips two kinds of folder by default, without any entry in exclude. (1) Any folder whose name starts with an underscore. (2) The asset folders: assets, images, img and media. Use include to override a default skip for a specific folder. include does not include a default-skipped folder's own default-skipped children, so including _rebuild does not include _rebuild/_superseded.",

  "_comment_include": "Folders skipped by default that should be collected from anyway. See _comment_defaults above for what is skipped, and why including one folder does not include its underscore-prefixed children.",
  "include": [],

  "_comment_exclude": "Folders to skip entirely, along with everything inside them. Exclude always wins over include. A relative entry here is powerful: \\"_superseded\\" would skip every _superseded folder in the tree.",
  "exclude": [],

  "_comment_file_types": "File extensions to collect, without the dot.",
  "file_types": ["md", "yaml", "yml", "json", "txt", "py"],

  "_comment_exclude_files": "Files to skip. Applied AFTER file_types has chosen what to collect, so this setting only ever removes, and it is the last word. Three forms, the same convention include and exclude use for folders. FILENAME - \\"*_WIP_*\\" - matched against the name wherever the file appears. ROOT-ANCHORED - \\"~/_rebuild/*.json\\" - one exact path, measured from the root. TRAILING - \\"_rebuild/*.json\\" - a pattern rather than a place: any file whose path ends with those segments, so one entry covers a _rebuild folder wherever it appears.",

  "_comment_exclude_files_wildcards": "? matches one character. In the two path forms * stops at a folder separator and ** crosses them: \\"~/_rebuild/*.json\\" is JSON directly in _rebuild, while \\"~/_rebuild/**/*.json\\" is JSON in _rebuild and everything beneath it. The filename form has no separators to stop at.",

  "_comment_exclude_files_convention": "The working document - work in progress, working notes - is what belongs here: it is loaded separately when active state is needed. The test is durability, not cadence. Work registers and open-items documents outlive the session and belong IN the binder, so never exclude them here. Example: [\\"*_WIP_*\\", \\"*_WIP.*\\"]",
  "exclude_files": [],

  "_comment_order": "Optional. Filenames pulled to the front of the binder, in the order listed. Everything not named here follows, sorted by path. A name that matches nothing in scope is reported, not silently ignored.",
  "order": [],

  "_comment_output": "The folder the binder is written to. Absolute, or \\"~/\\" for root-anchored, or relative to the script folder. The default \\"~/_binder\\" is an underscore folder inside the root, so it is skipped by the walk and a binder can never contain itself.",
  "output": "~/_binder",

  "_comment_log_file": "Where the run log is appended. One entry per run, never overwritten. Absolute, or \\"~/\\" for root-anchored, or relative to the script folder. Leave this out entirely and the log is named for the binder - binder_builder_<name>.log - which is what keeps four definitions in one folder from interleaving four runs in one file. Set it explicitly to point several binders at one log on purpose.",
  "log_file": "binder_builder_Documentation.log"
}
"""


# ---------------------------------------------------------------------------
# Small record types
# ---------------------------------------------------------------------------
# A dataclass is Python shorthand for "a class that just holds these fields".
# The lines below generate the constructor for us. Used here instead of loose
# tuples so that report code can say event.kind rather than event[0].

@dataclass
class Event:
    """One line of the report: something that happened, or failed to."""
    kind: str      # see REPORT_KINDS
    folder: Path   # the folder it concerns
    detail: str    # human-readable description


# The vocabulary, in the order a summary line lists it. INCLUDED/WOULD INCLUDE
# and WRITTEN/WOULD WRITE are the same event seen live and in a dry run, which
# is the same shape version cleanup uses for MOVED/WOULD MOVE. CONFLICT and
# ERROR mean exactly what they mean there.
REPORT_KINDS = (
    "INCLUDED",      # file placed in the binder
    "WOULD INCLUDE", # dry run: the same file, nothing written
    "SKIPPED",       # in a collected folder, deliberately left out
    "UNMATCHED",     # an "order" entry naming a file that is not in scope
    "NO CHANGES",    # nothing in scope has changed; the binder was not rebuilt
    "WOULD CHECK",   # dry run: the same comparison, reported not acted on
    "WRITTEN",       # the binder file itself
    "WOULD WRITE",   # dry run equivalent
    "SUPERSEDED",    # the previous binder moved into _superseded
    "WOULD SUPERSEDE",
    "CONFLICT",      # a destination name is already taken; nothing overwritten
    "EMPTY",         # nothing in scope; no binder written, previous left alone
    "INCOMPLETE",    # a source could not be read; the binder has a hole in it
    "ERROR",         # filesystem refusal
)


@dataclass
class FilePattern:
    """One compiled exclude_files entry."""
    text: str          # exactly as written in the settings, for the report
    kind: str          # "name", "path" or "trailing"
    regex: object      # compiled regex for path/trailing; None for name


@dataclass
class SourceFile:
    """One file selected for the binder, with its place in the order."""
    path: Path
    sort_key: tuple


@dataclass
class BinderPart:
    """One assembled section of the binder body, and its digest."""
    path: Path
    label: str      # how the file is named in the manifest and delimiters
    text: str       # the section as it will appear, delimiters included
    digest: str     # sha256 of the source bytes written, truncated


# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------

def create_default_settings(settings_path):
    """
    Write the shipped defaults out. Used when a folder holds no definition at
    all, so a bare copy of the script explains itself rather than failing.
    """
    print("No settings file found. Creating one with default values:")
    print("  {}".format(settings_path))
    print("This file is a binder definition, so it almost certainly needs "
          "editing.")
    print("Review it, then run the tool again.")
    print("")
    settings_path.write_text(DEFAULT_SETTINGS_JSON, encoding="utf-8")


def load_settings(settings_path):
    """
    Read one settings file.

    Returns a plain dictionary. Raises ValueError with a readable message if
    the file is not valid JSON - a mistyped settings file should stop that
    binder with an explanation, not with a stack trace.
    """
    text = settings_path.read_text(encoding="utf-8")
    try:
        settings = json.loads(text)
    except json.JSONDecodeError as error:
        # The exception carries the line and column of the problem, which is
        # the single most useful thing to show someone fixing the file.
        raise ValueError(
            "The settings file is not valid JSON.\n"
            "  file: {}\n"
            "  problem: {} (line {}, column {})\n"
            "Common causes: a missing comma, a trailing comma after the last "
            "item, or a single backslash inside a path (write \\\\ or use /)."
            .format(settings_path, error.msg, error.lineno, error.colno)
        )


    if not isinstance(settings, dict):
        raise ValueError(
            "The settings file must contain a JSON object (a {{ ... }} block), "
            "but it contains {}.".format(type(settings).__name__)
        )

    return settings


def read_string_list(settings, key):
    """Read a settings value that must be a list of strings, or absent."""
    values = settings.get(key)
    if values is None:
        return []
    if not isinstance(values, list):
        raise ValueError(
            'Setting "{}" must be a list, written in square brackets, for '
            'example ["one", "two"].'.format(key)
        )
    return [str(value).strip() for value in values if str(value).strip()]


def read_flag(settings, key, default):
    """Read a true/false setting, rejecting the string "true" politely."""
    value = settings.get(key, default)
    if isinstance(value, bool):
        return value
    raise ValueError(
        'Setting "{}" must be true or false, without quotes around it.'
        .format(key)
    )


# ---------------------------------------------------------------------------
# Path forms
# ---------------------------------------------------------------------------
# Three spellings are accepted, because the tree needs two different kinds of
# statement: "this exact folder" and "any folder shaped like this".
#
#   absolute        "C:/Docs/_binder"   one exact folder
#   root-anchored   "~/_binder"         one exact folder, measured from root
#   relative        "_binder"           a PATTERN: every folder whose path
#                                       ends with those segments
#
# The relative form is the interesting one. It is not resolved once at startup;
# it is a shape the walk tests every folder against, so a single "_binder"
# entry covers a _binder subfolder wherever one turns up in the tree. Several
# segments work too: "_binder/current" matches any .../_binder/current.
#
# Note that "~" does NOT mean the home folder here. Python's expanduser is
# deliberately never called on these settings, so "~/" always means the root of
# the tree being collected from and can never quietly resolve to
# C:\\Users\\someone.
#
# This is the same model as version cleanup, ratified as the Infrastructure-wide
# convention. Two sibling tools with different path semantics would be a trap.

def tidy_setting_text(value, label):
    """Trim a settings value and normalise its separators to forward slashes."""
    text = str(value).strip().replace("\\", "/")
    if not text:
        raise ValueError('Setting "{}" contains an empty path.'.format(label))
    return text


def resolve_one_folder(text, label, root=None):
    """
    Resolve a settings value that names ONE place: absolute, "~/" measured from
    the root, or relative to the script's own folder.

    Used for the root, the output folder and the log file. Include and exclude
    go through parse_scope_entry instead, because they also accept patterns.
    """
    if text.startswith("~"):
        if root is None:
            raise ValueError(
                'Setting "{}" cannot use "~/", because "~/" means "measured '
                'from the root" and this setting is what defines the root. '
                'Use a full path, or a path relative to the script folder.'
                .format(label)
            )
        if not text.startswith("~/"):
            raise ValueError(
                'Setting "{}": "~" means the root folder, so it has to be '
                'written as "~/something".'.format(label)
            )
        return (root / text[2:]).resolve()

    path = Path(text)
    if not path.is_absolute():
        if WINDOWS_DRIVE.match(text):
            raise ValueError(
                'Setting "{}" is "{}", which looks like a Windows path, but '
                "this is not Windows.".format(label, text)
            )
        # resolve() also removes any ".." segments, so two spellings of the
        # same folder compare equal later on.
        path = SCRIPT_DIR / path
    return path.resolve()


def parse_scope_entry(text, label, root):
    """
    Classify one include or exclude entry.

    Returns ("folder", Path) for the absolute and "~/" forms, or
    ("pattern", (segments...)) for the relative form.
    """
    if text.startswith("~"):
        return ("folder", resolve_one_folder(text, label, root))

    path = Path(text)
    if path.is_absolute():
        return ("folder", path.resolve())
    if WINDOWS_DRIVE.match(text):
        raise ValueError(
            'Setting "{}" contains "{}", which looks like a Windows path, but '
            "this is not Windows.".format(label, text)
        )

    # Anything else is a pattern. Splitting on "/" and dropping empty pieces
    # tolerates a stray leading or trailing slash.
    segments = tuple(part for part in text.split("/") if part)
    if not segments or "." in segments:
        raise ValueError(
            'Setting "{}" contains "{}", which does not name anything.'
            .format(label, text)
        )
    if ".." in segments:
        raise ValueError(
            'Setting "{}" contains "{}". A relative entry is a pattern tested '
            'against every folder in the tree, so ".." has no meaning in one. '
            'Write "~/..." to anchor at the root, or give a full path.'
            .format(label, text)
        )
    return ("pattern", segments)


def normalise(path):
    """
    Case-fold a path the way the local filesystem does.

    os.path.normcase lowercases on Windows, where FOO and foo are the same
    folder, and changes nothing on Mac or Linux. Comparing paths through it
    avoids both false misses on Windows and false matches elsewhere.
    """
    return Path(os.path.normcase(str(path)))


# ---------------------------------------------------------------------------
# Folder scope
# ---------------------------------------------------------------------------

def is_inside(path, folder):
    """True if `path` is `folder` itself, or anywhere beneath it."""
    try:
        normalise(path).relative_to(normalise(folder))
        return True
    except ValueError:
        # relative_to raises when path is not under folder. Catching that is
        # the standard pathlib way of asking this question.
        return False


@dataclass
class Scope:
    """
    Everything the walk needs in order to decide which folders are in play.

    Entries arrive already sorted into exact folders and patterns, so the walk
    itself stays readable: it asks questions, it does not parse settings.
    """
    root: Path
    subfolders: bool = True
    include_folders: list = field(default_factory=list)
    include_patterns: list = field(default_factory=list)
    exclude_folders: list = field(default_factory=list)
    exclude_patterns: list = field(default_factory=list)
    include_text: list = field(default_factory=list)   # as typed, for the report
    exclude_text: list = field(default_factory=list)

    def parts_below_root(self, path):
        """The folder's path as case-folded segments measured from the root."""
        try:
            relative = path.relative_to(self.root)
        except ValueError:
            return None
        return tuple(os.path.normcase(part) for part in relative.parts)

    def matches_pattern(self, path, patterns):
        """
        True if the folder's path ENDS WITH one of the patterns.

        This trailing-segment test is what makes "_binder" mean "any _binder
        folder, wherever it appears". Because the comparison is made against
        the path measured from the root, a pattern can never reach above the
        root, and the root itself is never matched: it has no segments to
        compare.
        """
        parts = self.parts_below_root(path)
        if parts is None:
            return False
        for pattern in patterns:
            length = len(pattern)
            if length > len(parts):
                continue
            wanted = tuple(os.path.normcase(part) for part in pattern)
            if parts[-length:] == wanted:
                return True
        return False

    def leads_to_include_pattern(self, path):
        """
        True if something deeper down could still match a multi-segment
        include pattern.

        For "_binder/current", a folder ending in "_binder" is not itself
        included, but the walk has to pass through it to reach "current".
        Testing every *proper* prefix of every pattern is exactly that
        lookahead. Single-segment patterns have no proper prefix and contribute
        nothing here, which is right: they match the folder itself or not at
        all.
        """
        parts = self.parts_below_root(path)
        if parts is None:
            return False
        for pattern in self.include_patterns:
            for length in range(1, len(pattern)):
                if length > len(parts):
                    continue
                wanted = tuple(os.path.normcase(part)
                               for part in pattern[:length])
                if parts[-length:] == wanted:
                    return True
        return False

    def is_excluded(self, path):
        """Excluded folders, and everything inside them, are never touched."""
        if any(is_inside(path, folder) for folder in self.exclude_folders):
            return True
        return self.matches_pattern(path, self.exclude_patterns)

    def is_included(self, path):
        """True if this exact folder was named, or it matches a pattern."""
        if any(normalise(path) == normalise(folder)
               for folder in self.include_folders):
            return True
        return self.matches_pattern(path, self.include_patterns)

    def is_skipped_by_default(self, path):
        """
        Folders left out unless the settings ask for them.

        The underscore rule is the load-bearing one: it keeps the walk out of
        _superseded and out of the tool's own _binder output folder, which is
        what makes it structurally impossible for a binder to include a binder.
        Asset folders are excluded by name because their contents are not
        documents.
        """
        name = path.name
        if name.startswith("_"):
            return True
        return os.path.normcase(name) in ASSET_FOLDER_NAMES

    def should_descend(self, path):
        """
        Should the walk go *into* this folder?

        Note the difference between descending and collecting. A folder that is
        not itself collected from may still need to be walked through, because
        something deeper down is on the include list. It is traversed, but its
        own files are left alone.
        """
        if self.is_excluded(path):
            return False
        if not self.is_skipped_by_default(path):
            return True
        if self.is_included(path):
            return True
        # Is this folder on the way to an exactly-named include?
        if any(is_inside(folder, path) for folder in self.include_folders):
            return True
        return self.leads_to_include_pattern(path)

    def should_collect(self, path):
        """Should this folder's own files go into the binder?"""
        if self.is_excluded(path):
            return False
        if not self.is_skipped_by_default(path):
            return True
        # Only an explicit include overrides the default skip. Note that
        # including a folder does not include its underscore-prefixed children:
        # each folder is asked this question in its own right.
        return self.is_included(path)


def build_scope(root, subfolders, include_values, exclude_values):
    """Turn the raw include and exclude settings into a Scope."""
    scope = Scope(root=root, subfolders=subfolders)

    for label, values in (("include", include_values),
                          ("exclude", exclude_values)):
        for value in values:
            text = tidy_setting_text(value, label)
            kind, resolved = parse_scope_entry(text, label, root)
            if label == "include":
                scope.include_text.append(text)
                target = (scope.include_folders if kind == "folder"
                          else scope.include_patterns)
            else:
                scope.exclude_text.append(text)
                target = (scope.exclude_folders if kind == "folder"
                          else scope.exclude_patterns)
            target.append(resolved)

    return scope


def folders_to_collect(scope):
    """
    Walk the tree from the root and return the folders whose files belong in
    the binder, in a stable, predictable order.
    """
    root = scope.root

    if not scope.subfolders:
        # "subfolders": false means the root and nothing else. An explicit
        # exclude of the root still wins.
        return [] if scope.is_excluded(root) else [root]

    found = []

    # os.walk visits every folder beneath root. With topdown=True (the default)
    # it hands us the list of subfolder names *before* descending, and editing
    # that list in place prunes the walk - the standard way to skip whole
    # branches cheaply. Pruning is also what makes exclusion inherited: once a
    # folder is skipped, nothing inside it is ever looked at, so there is no
    # need to ask again further down. Symbolic links to folders are not
    # followed by default, which is what we want: a link should not cause the
    # same documents to appear in the binder twice.
    for dirpath, dirnames, _filenames in os.walk(root):
        current = Path(dirpath)

        # dirnames[:] = ... replaces the contents of the existing list rather
        # than rebinding the name. os.walk only notices the former.
        dirnames[:] = sorted(
            name for name in dirnames if scope.should_descend(current / name)
        )

        if current == root:
            # The root was chosen deliberately by whoever edited the settings,
            # so the default skips do not apply to it. An explicit exclude
            # still does.
            collect = not scope.is_excluded(current)
        else:
            collect = scope.should_collect(current)

        if collect:
            found.append(current)

    return found


# ---------------------------------------------------------------------------
# File selection
# ---------------------------------------------------------------------------

# exclude_files takes the same three path forms as include and exclude, which
# is the Infrastructure-wide convention (D6). Applied to files rather than
# folders they read as:
#
#   name         "*_WIP_*"             a filename, matched wherever it appears
#   root-anchored "~/_rebuild/*.json"  one exact path, measured from the root
#   trailing     "_rebuild/*.json"     a PATTERN: any file whose path ends
#                                      with those segments, so one entry
#                                      covers a _rebuild folder at any depth
#
# An entry with no "/" in it is the first form and behaves exactly as it always
# did. That is what keeps every existing settings file working unchanged.
#
# The wildcards are glob's, NOT fnmatch's, and the difference is the whole
# point: fnmatch's "*" matches "/" as well, so "~/_rebuild/*.json" under
# fnmatch would also match _rebuild/anything/deep/x.json and the qualification
# would mean nothing. Here "*" stops at a separator and "**" is the segment
# that crosses them.

def fold_path(text):
    """
    Case-fold a relative path the way the local filesystem does, keeping "/"
    as the separator.

    os.path.normcase cannot be used alone here: on Windows it rewrites "/" as
    "\\" as well as lowercasing, which would compile a pattern over
    backslashes and then match it against a forward-slash path. Folding and
    then restoring the separator keeps the platform's case rule and the
    tool's one spelling of a path.
    """
    return os.path.normcase(text.replace("\\", "/")).replace("\\", "/")


def translate_segment(segment):
    """Turn one glob segment into regex source. "*" does not cross "/"."""
    out = []
    for character in segment:
        if character == "*":
            out.append("[^/]*")
        elif character == "?":
            out.append("[^/]")
        else:
            out.append(re.escape(character))
    return "".join(out)


def glob_to_regex(pattern, trailing=False):
    """
    Compile a "/"-separated glob into a regex over a forward-slash path.

        _rebuild/*.json      _rebuild/notes.json          yes
                             _rebuild/sub/notes.json      no
        _rebuild/**/*.json   _rebuild/notes.json          yes
                             _rebuild/sub/deep/notes.json yes

    "**" is zero or more whole path segments, so it covers the folder itself
    as well as everything under it. `trailing` anchors the pattern at the end
    of the path rather than at the root, which is the third form above.
    """
    segments = [part for part in pattern.split("/") if part]
    pieces = []
    for index, segment in enumerate(segments):
        last = index == len(segments) - 1
        if segment == "**":
            # As the final segment "**" means "everything from here down";
            # anywhere else it means "any number of intervening folders",
            # including none, so it carries its own separator.
            pieces.append(".+" if last else "(?:[^/]+/)*")
        else:
            pieces.append(translate_segment(segment) + ("" if last else "/"))
    prefix = "(?:.*/)?" if trailing else ""
    return re.compile("^" + prefix + "".join(pieces) + "$")


def compile_exclude_files(values, label="exclude_files"):
    """
    Sort the exclude_files entries into the three forms and compile them.

    Raises ValueError for an entry that cannot mean anything, rather than
    letting it sit in the settings quietly matching nothing.
    """
    compiled = []
    for value in values:
        original = str(value).strip()
        tidied = original.replace("\\", "/")
        if not tidied:
            continue

        if tidied.startswith("~"):
            if not tidied.startswith("~/"):
                raise ValueError(
                    'Setting "{}" contains "{}": "~" means the root folder, '
                    'so it has to be written as "~/something".'
                    .format(label, original)
                )
            body = tidied[2:]
            kind = "path"
        elif "/" in tidied:
            body = tidied
            kind = "trailing"
        else:
            compiled.append(FilePattern(original, "name", None))
            continue

        segments = [part for part in body.split("/") if part]
        if not segments:
            raise ValueError(
                'Setting "{}" contains "{}", which does not name anything.'
                .format(label, original)
            )
        if ".." in segments:
            raise ValueError(
                'Setting "{}" contains "{}". A file pattern is matched '
                'against a path measured from the root, so ".." has no '
                'meaning in one.'.format(label, original)
            )
        compiled.append(FilePattern(
            original, kind,
            glob_to_regex(fold_path("/".join(segments)),
                          trailing=(kind == "trailing")),
        ))
    return compiled


def excluded_by(entry, relative_path, patterns):
    """
    The first exclude_files pattern that drops this file, or None.

    Returning the pattern rather than a boolean is what lets the report name
    which entry did it - the question anyone with four patterns in a settings
    file actually has.
    """
    for pattern in patterns:
        if pattern.kind == "name":
            # fnmatch case-folds through os.path.normcase, so a filename
            # pattern follows the local filesystem exactly as folder
            # comparison does.
            if fnmatch.fnmatch(entry.name, pattern.text):
                return pattern
        elif pattern.regex.match(relative_path):
            return pattern
    return None


def binder_name_pattern(name):
    """
    Matches any binder belonging to this definition: "<Name>_Binder_v<N>.md".

    Used twice, for two different reasons: to find the highest version already
    written, and to keep the tool's own output out of its own input.
    """
    return re.compile(
        r"^" + re.escape(os.path.normcase(name)) + r"_binder_v(\d+)\.md$"
    )


def collect_files(scope, folders, file_types, exclude_files, order,
                  output_folder, output_path, name):
    """
    Choose the files that go into the binder, in binder order. Nothing is read
    here beyond the directory listings.

    Returns (sources, events). Splitting selection from assembly - and both
    from writing - is what makes --dry-run trustworthy: the dry run takes
    exactly the same decisions as a live run, and only the last step differs.
    """
    sources = []
    events = []

    # Order entries are matched on filename, case-folded the way the local
    # filesystem folds names. The dictionary maps a folded filename to its
    # position in the list, which becomes the primary sort key.
    order_rank = {}
    for position, name in enumerate(order):
        order_rank.setdefault(os.path.normcase(name), position)
    order_seen = set()

    wanted_extensions = {"." + extension.lstrip(".").lower()
                         for extension in file_types}

    own_binder = binder_name_pattern(name)

    for folder in folders:
        try:
            entries = sorted(folder.iterdir())
        except OSError as error:
            events.append(Event("ERROR", folder,
                                "cannot read folder: {}".format(error)))
            continue

        for entry in entries:
            if not entry.is_file():
                continue  # subfolders are visited in their own right

            # The defensive self-inclusion check. The output folder is normally
            # underscore-prefixed and therefore already outside the walk, but
            # if someone points "output" at a collected folder, the binder must
            # not swallow itself. Two things are refused: the file this run is
            # about to write, and any earlier binder of this same definition
            # sitting in the output folder. The second is the one that actually
            # bites - this run's own output does not exist yet, but last run's
            # does, and including it would nest a binder inside a binder and
            # double the corpus on every build.
            if normalise(entry) == normalise(output_path):
                events.append(Event(
                    "SKIPPED", folder,
                    "{}: this is the binder's own output file".format(entry.name)
                ))
                continue
            if normalise(entry.parent) == normalise(output_folder) and \
                    own_binder.match(os.path.normcase(entry.name)):
                events.append(Event(
                    "SKIPPED", folder,
                    "{}: this is an earlier version of this binder"
                    .format(entry.name)
                ))
                continue

            if entry.suffix.lower() not in wanted_extensions:
                # Not reported. A document tree is full of files of other
                # types and listing every one of them would bury the report.
                continue

            # The path a pattern is matched against is measured from the
            # root and spelled with forward slashes, so one settings file
            # behaves the same on every platform.
            relative_path = fold_path(relative_to(entry, scope.root))
            excluding = excluded_by(entry, relative_path, exclude_files)
            if excluding is not None:
                events.append(Event(
                    "SKIPPED", folder,
                    '{}: matches exclude_files pattern "{}"'
                    .format(entry.name, excluding.text)
                ))
                continue

            folded = os.path.normcase(entry.name)
            if folded in order_rank:
                rank = order_rank[folded]
                order_seen.add(folded)
            else:
                # Everything not named in "order" sorts after everything that
                # is. len(order_rank) is one past the last explicit position.
                rank = len(order_rank)

            # Within a rank, sort by path so the binder is reproducible.
            # normcase keeps the ordering consistent with how the filesystem
            # itself compares names.
            sources.append(SourceFile(
                path=entry,
                sort_key=(rank, os.path.normcase(str(entry))),
            ))

    sources.sort(key=lambda source: source.sort_key)

    # An "order" entry that matched nothing is a quiet defect: the binder is
    # assembled in an order its author did not get. Say so.
    for name in order:
        if os.path.normcase(name) not in order_seen:
            events.append(Event(
                "UNMATCHED", scope.root,
                'order entry "{}" matched no file in scope'.format(name)
            ))

    return sources, events


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------
# Encoding, stated rather than inherited from the platform:
#
#   READ   the file's bytes, then decode as UTF-8. The "utf-8-sig" codec is
#          used, which is plain UTF-8 except that it removes a byte-order mark
#          if one is present. This is the single deviation from byte-for-byte
#          copying, and it is deliberate: a BOM is a start-of-file marker, and
#          leaving one embedded halfway down a binder produces a stray U+FEFF
#          in the middle of the text.
#   WRITE  UTF-8, no BOM, opened in BINARY mode so that no line-ending
#          translation can happen. Line endings therefore pass through exactly
#          as they were in the source.
#
# Nothing else is altered: no reformatting, no heading demotion, no trimming,
# no normalisation of blank lines. The one adjustment is that a newline is
# added after a source that does not end with one, so that the closing
# delimiter sits on its own line.

BEGIN_DELIMITER = "<!-- BEGIN SOURCE: {label} -->"
END_DELIMITER = "<!-- END SOURCE: {label} -->"


def read_source(path):
    """
    Read one source file. Returns (text, digest).

    The digest is taken over the bytes that will actually be written into the
    binder - text.encode("utf-8") - and not over a separate read of the file.
    That is what makes the manifest a statement about the binder rather than a
    statement about the tree at some other moment.

    Raises OSError for a filesystem refusal and UnicodeDecodeError for a file
    that is not text; both mean the binder cannot contain this file.
    """
    data = path.read_bytes()
    text = data.decode("utf-8-sig")
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:DIGEST_LENGTH]
    return text, digest


def assemble_parts(sources, root):
    """
    Read every source and build its section of the binder body.

    Returns (parts, missing, events). `missing` holds the files that could not
    be read: if it is not empty the binder has a hole in it, and every caller
    downstream treats that as loud.
    """
    parts = []
    missing = []
    events = []

    for source in sources:
        label = relative_to(source.path, root).replace("\\", "/")
        try:
            text, digest = read_source(source.path)
        except UnicodeDecodeError as error:
            missing.append(label)
            events.append(Event(
                "ERROR", source.path.parent,
                "{} is not UTF-8 text and was left out: {}"
                .format(source.path.name, error.reason)
            ))
            continue
        except OSError as error:
            missing.append(label)
            events.append(Event(
                "ERROR", source.path.parent,
                "{} could not be read and was left out: {}"
                .format(source.path.name, error)
            ))
            continue

        # The one permitted adjustment: guarantee the closing delimiter starts
        # on a line of its own. An empty file gets no added newline beyond the
        # one that separates the two delimiters.
        body = text
        if body and not body.endswith("\n"):
            body += "\n"

        parts.append(BinderPart(
            path=source.path,
            label=label,
            text="{}\n{}{}\n".format(
                BEGIN_DELIMITER.format(label=label),
                body,
                END_DELIMITER.format(label=label),
            ),
            digest=digest,
        ))

    return parts, missing, events


def build_binder_text(name, version, parts, missing):
    """
    Compose the whole binder: header, manifest, then the bodies.

    The manifest is written from the same `parts` list that produces the body,
    in the same order, using digests computed during assembly. The manifest and
    the body cannot describe different things because they are generated from
    one source of truth in one pass.
    """
    today = datetime.date.today().isoformat()

    lines = []
    lines.append("# {} Binder".format(name))
    lines.append("")
    lines.append("> **Generated Binder - do not edit directly.** Edit the "
                 "individual master documents")
    lines.append("> and regenerate the Binder.")
    lines.append("> **Binder Version {}** ({}).".format(version, today))
    lines.append("")
    lines.append("This Binder is a current-context consumption artefact; "
                 "authoritative masters remain")
    lines.append("individual files.")
    lines.append("")

    # An empty binder says so on its own face. The alternative - a file with a
    # manifest reading "(no files)" and nothing after it - looks like a build
    # that went wrong, and a reader has no way to tell whether the scope was
    # empty or the tool was.
    if not parts:
        lines.append("> **EMPTY BINDER - nothing was in scope when this was "
                     "built.**")
        lines.append(">")
        lines.append("> This is a statement about the tree, not a failure: "
                     "the scope genuinely")
        lines.append("> contained no files. If that is unexpected, the scope "
                     "settings are where")
        lines.append("> to look.")
        lines.append("")

    # An incomplete binder announces itself in its own first screenful. A
    # reader who never sees the console report or the log still cannot mistake
    # it for the whole topic.
    if missing:
        lines.append("> **INCOMPLETE BINDER - {} source file(s) could not be "
                     "read and are missing:**".format(len(missing)))
        for label in missing:
            lines.append("> - `{}`".format(label))
        lines.append(">")
        lines.append("> Do not treat this Binder as a complete statement of "
                     "its scope until it is rebuilt.")
        lines.append("")

    lines.append("## Binder manifest")
    lines.append("")
    if parts:
        for part in parts:
            lines.append("- `{}` - sha256 `{}`".format(part.label, part.digest))
    else:
        lines.append("- (no files)")
    lines.append("")

    header = "\n".join(lines) + "\n"

    sections = []
    for part in parts:
        sections.append("---\n\n" + part.text)

    return header + "\n".join(sections)


# ---------------------------------------------------------------------------
# Change detection
# ---------------------------------------------------------------------------
# The binder is a derived artefact. If every source is byte-for-byte what it was
# when the last binder was written, rebuilding produces the same content under a
# new version number and pushes a perfectly good binder into _superseded for
# nothing. That is merely untidy when someone runs the tool by hand, and
# genuinely wasteful once another tool runs it after every deploy.
#
# The comparison needs no new state, because the answer is already in the
# binder: the manifest lists every file it contains with a digest of that file's
# content. Comparing that manifest against the digests computed for this run
# answers "has anything in scope changed" exactly - additions and removals
# included, since the comparison is over the set of files as well as over the
# digests.
#
# Every uncertainty resolves towards rebuilding. No previous binder, an
# unreadable one, a manifest that will not parse, a previous build stamped
# INCOMPLETE, a source that could not be read this time, or --force: build. An
# unnecessary rebuild costs a version number. A wrongly skipped one leaves a
# binder that misrepresents the tree, which is the failure this tool exists to
# prevent.


def parse_binder_manifest(path):
    """
    Read the manifest out of an existing binder.

    Returns a dictionary of label -> digest, or None if the binder cannot serve
    as a baseline: unreadable, not UTF-8, no manifest heading, a manifest line
    in an unexpected shape, or a binder stamped INCOMPLETE. None means "cannot
    compare", and cannot compare always means rebuild.
    """
    try:
        text = path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeDecodeError):
        return None

    lines = text.splitlines()

    try:
        start = lines.index(MANIFEST_HEADING)
    except ValueError:
        return None

    # Only the header above the manifest is examined for the incomplete stamp,
    # so a source file that happens to discuss incomplete binders - this tool's
    # own design document, for one - cannot trip it.
    if any(INCOMPLETE_MARKER in line for line in lines[:start]):
        return None

    manifest = {}
    for line in lines[start + 1:]:
        entry = line.strip()
        if not entry:
            continue
        # The manifest ends where the body begins.
        if entry.startswith("---") or entry.startswith("<!-- BEGIN SOURCE"):
            break
        if entry == "- (no files)":
            continue
        match = MANIFEST_ENTRY.match(entry)
        if not match:
            # One unreadable entry means this binder's contents cannot be
            # established. Guessing at the rest would be worse than rebuilding.
            return None
        manifest[match.group("label")] = match.group("digest").lower()

    return manifest


def compare_to_manifest(manifest, parts):
    """
    Compare this run's assembled parts against a previous binder's manifest.

    Returns (unchanged, description). The description is written for the report
    in both cases, so a run always states what the comparison found rather than
    only stating what it decided.
    """
    current = {part.label: part.digest.lower() for part in parts}

    added = sorted(set(current) - set(manifest))
    removed = sorted(set(manifest) - set(current))
    changed = sorted(label for label in set(current) & set(manifest)
                     if current[label] != manifest[label])

    if not (added or removed or changed):
        return True, "{} file(s) in scope, all matching the manifest".format(
            len(current))

    counts = ", ".join(
        "{} {}".format(len(group), word)
        for group, word in ((added, "added"),
                            (removed, "removed"),
                            (changed, "changed"))
        if group
    )

    # Name a few. A run that rebuilds should say why in terms of the tree and
    # not only in numbers, but a scope-wide change must not print a hundred
    # lines to say so.
    named = (added + removed + changed)
    shown = named[:3]
    remainder = len(named) - len(shown)
    return False, "{} ({}{})".format(
        counts,
        ", ".join(shown),
        ", and {} more".format(remainder) if remainder else "",
    )


# ---------------------------------------------------------------------------
# Versioning and output
# ---------------------------------------------------------------------------

def next_binder_version(output_folder, name):
    """
    Work out this binder's version number by looking at the output folder.

    The folder is the truth; no version is recorded in settings, because a
    number kept in settings drifts from reality the first time a file is moved
    by hand. Scan for existing binders of this name, take the highest, add one.

    Returns (version, previous_path). previous_path is the binder being
    replaced, or None if this is the first.
    """
    pattern = binder_name_pattern(name)

    highest = 0
    previous = None
    if output_folder.is_dir():
        for entry in sorted(output_folder.iterdir()):
            if not entry.is_file():
                continue
            match = pattern.match(os.path.normcase(entry.name))
            if not match:
                continue
            number = int(match.group(1))
            if number > highest:
                highest = number
                previous = entry

    return highest + 1, previous


def write_binder(output_folder, filename, text):
    """
    Write the binder. Binary mode, UTF-8, no BOM, no newline translation.

    Text mode would rewrite "\\n" as "\\r\\n" on Windows, which would silently
    alter every source line ending in the file. Binary mode is the guarantee
    that what was read is what is written.
    """
    output_folder.mkdir(parents=True, exist_ok=True)
    path = output_folder / filename
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))
    return path


def supersede_previous(previous, dry_run):
    """
    Move the binder this run replaced into _superseded beside it.

    A tool cleans up after itself. The output folder is normally underscore-
    prefixed, so version cleanup skips it by design and would have to be
    explicitly pointed at it purely to tidy after every build. And this is not
    general supersession: the tool knows the single file it just replaced, so
    there is no scanning, grouping or version reasoning here.

    Nothing is ever overwritten.
    """
    folder = previous.parent
    destination = folder / SUPERSEDED_FOLDER_NAME / previous.name

    if dry_run:
        return Event("WOULD SUPERSEDE", folder,
                     "{} -> {}/".format(previous.name, SUPERSEDED_FOLDER_NAME))

    if destination.exists():
        return Event(
            "CONFLICT", folder,
            "{} left in place: {}/{} already exists"
            .format(previous.name, SUPERSEDED_FOLDER_NAME, previous.name)
        )

    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        # A last existence check immediately before the move: the destination
        # could have appeared since, and shutil.move would silently overwrite
        # it on Linux and macOS.
        if destination.exists():
            return Event(
                "CONFLICT", folder,
                "{} left in place: {}/{} appeared during the run"
                .format(previous.name, SUPERSEDED_FOLDER_NAME, previous.name)
            )
        shutil.move(str(previous), str(destination))
        return Event("SUPERSEDED", folder,
                     "{} -> {}/".format(previous.name, SUPERSEDED_FOLDER_NAME))
    except OSError as error:
        return Event("ERROR", folder,
                     "{} could not be superseded: {}"
                     .format(previous.name, error))


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def relative_to(path, root):
    """Show a path relative to the root when possible - shorter to read."""
    try:
        relative = path.relative_to(root)
    except ValueError:
        return str(path)
    return str(relative) if str(relative) != "." else "."


def build_report(name, scope, settings_path, dry_run, folder_count, events,
                 change_note=None):
    """
    Build the run report as a list of lines.

    One function produces both the on-screen report and the log entry, so the
    two can never drift apart.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = "DRY RUN (nothing written)" if dry_run else "LIVE"

    lines = []
    lines.append("=" * 72)
    lines.append("binder builder   {}   {}".format(timestamp, mode))
    lines.append("binder:   {}".format(name))
    lines.append("root:     {}".format(scope.root))
    lines.append("settings: {}".format(settings_path))
    if not scope.subfolders:
        lines.append("subfolders: false - root folder only")
    # Scope overrides are echoed only when in use. They decide which folders
    # were collected from, so a log entry is not self-explaining without them.
    if scope.include_text:
        lines.append("include:  {}".format(", ".join(scope.include_text)))
    if scope.exclude_text:
        lines.append("exclude:  {}".format(", ".join(scope.exclude_text)))
    lines.append("folders collected from: {}".format(folder_count))
    # Every run states what the change comparison found, including the runs
    # that went on to rebuild. A log entry that only recorded the skips would
    # leave the reader guessing why the other runs did not skip.
    if change_note:
        lines.append("change detection: {}".format(change_note))
    lines.append("-" * 72)

    if not events:
        lines.append("Nothing happened, which should not be possible - please "
                     "report this.")
    else:
        # Events are reported grouped by folder, which is how someone reading
        # the report actually thinks about the tree.
        current_folder = None
        for event in events:
            if event.folder != current_folder:
                current_folder = event.folder
                lines.append("")
                lines.append("[{}]".format(relative_to(event.folder,
                                                       scope.root)))
            lines.append("  {:<16} {}".format(event.kind, event.detail))

    counts = {}
    for event in events:
        counts[event.kind] = counts.get(event.kind, 0) + 1

    summary = ", ".join(
        "{} {}".format(counts[kind], kind.lower())
        for kind in REPORT_KINDS if kind in counts
    ) or "nothing to do"

    lines.append("")
    lines.append("-" * 72)
    lines.append("Result: {}".format(summary))
    lines.append("=" * 72)
    return lines


def append_to_log(log_path, lines):
    """
    Append one entry to the log. The log is never rewritten or trimmed.

    Failing to write the log must not lose the report that is already on
    screen, so a problem here is reported and swallowed.
    """
    try:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        # "a" is append mode: the file is created if absent, and writes always
        # go to the end. newline="\n" leaves line endings to us, so the log
        # looks the same on every platform.
        with open(log_path, "a", encoding="utf-8", newline="\n") as log_file:
            log_file.write("\n".join(lines))
            log_file.write("\n\n")
        return True
    except OSError as error:
        print("WARNING: could not write the log file {}: {}"
              .format(log_path, error))
        return False


# ---------------------------------------------------------------------------
# Several definitions in one folder
# ---------------------------------------------------------------------------
# A settings file is a binder definition, and a folder may hold any number of
# them: binder_builder_settings.json plus binder_builder_settings_<x>.json
# beside it. One run keeps them all current.
#
# This works because a build reads nothing global. Every path, every scope and
# every log in a build comes out of one Definition, so running four is running
# one four times - and change detection means the three that did not change
# cost a manifest comparison each and no writes at all.
#
# A binder is identified by its `name` setting. That was already required to be
# unique: it names the output file and drives the version scan, so two
# definitions sharing a name would supersede each other's binders on alternate
# runs. Sharing is therefore refused rather than resolved.


@dataclass
class Definition:
    """
    One binder definition: one settings file, resolved and checked.

    The whole of a binder is in here, which is what lets several of them sit in
    one folder without interfering: nothing about a build reads global state,
    so building four is building one, four times.
    """
    settings_path: Path
    name: str
    scope: Scope = None
    file_types: list = field(default_factory=list)
    exclude_files: list = field(default_factory=list)
    order: list = field(default_factory=list)
    output_folder: Path = None
    log_path: Path = None


def settings_sort_key(path):
    """The legacy plain settings file first, then the rest alphabetically."""
    folded = os.path.normcase(path.name)
    first = folded == os.path.normcase(LEGACY_SETTINGS_FILENAME)
    return (0 if first else 1, folded)


def discover_settings_files():
    """
    Every settings file in the script's own folder, in report order.

    A folder holding none at all gets the shipped default written into it, so a
    bare copy of the script explains itself rather than failing.
    """
    found = sorted((path for path in SCRIPT_DIR.glob(SETTINGS_GLOB)
                    if path.is_file()), key=settings_sort_key)
    if found:
        return found

    settings_path = SCRIPT_DIR / SETTINGS_FILENAME_FORMAT.format(
        name=DEFAULT_BINDER_NAME)
    create_default_settings(settings_path)
    return [settings_path]


def duplicate_names(definitions):
    """Definitions grouped by name, keeping only the names used twice."""
    groups = {}
    for definition in definitions:
        groups.setdefault(os.path.normcase(definition.name), []).append(
            definition)
    return {name: group for name, group in groups.items() if len(group) > 1}


def select_definitions(definitions, wanted):
    """
    Narrow the definitions to the ones named on the command line.

    A selector matches a binder's name, or the filename of its settings file
    with or without the extension, case-insensitively. Returns (chosen,
    unmatched); nothing is run while anything is unmatched, because "build
    these four" half-done is worse than not started.
    """
    if not wanted:
        return list(definitions), []

    chosen = []
    unmatched = []
    for selector in wanted:
        folded = os.path.normcase(selector.strip())
        match = None
        for definition in definitions:
            names = (os.path.normcase(definition.name),
                     os.path.normcase(definition.settings_path.name),
                     os.path.normcase(definition.settings_path.stem))
            if folded in names:
                match = definition
                break
        if match is None:
            unmatched.append(selector)
        elif not any(existing is match for existing in chosen):
            chosen.append(match)
    return chosen, unmatched


def describe_definitions(definitions, broken):
    """The --list output, and the "what is available" half of an error."""
    lines = ["binder definitions in {}".format(SCRIPT_DIR), ""]
    if not definitions and not broken:
        lines.append("  (none)")
    for definition in definitions:
        lines.append("  {}".format(definition.name))
        lines.append("      settings: {}".format(
            definition.settings_path.name))
        lines.append("      root:     {}".format(definition.scope.root))
        lines.append("      output:   {}".format(definition.output_folder))
    for settings_path, error in broken:
        lines.append("  (unreadable)")
        lines.append("      settings: {}".format(settings_path.name))
        lines.append("      problem:  {}".format(
            str(error).splitlines()[0]))
    return lines


def build_roll_up(statuses, broken):
    """
    The one line that says how the folder as a whole came out.

    Printed only when more than one binder ran, or when a settings file could
    not be read - so a folder holding a single definition reports exactly what
    it always did, and anything reading the last "Result:" line of the output
    keeps working either way.
    """
    counts = {}
    for status in statuses:
        counts[status] = counts.get(status, 0) + 1
    if broken:
        counts["unreadable"] = len(broken)

    tally = ", ".join(
        "{} {}".format(counts[word], word)
        for word in ("rebuilt", "unchanged", "empty", "with problems",
                     "unreadable")
        if word in counts
    ) or "nothing to do"

    return [
        "=" * 72,
        "Result: {} binder(s) - {}".format(len(statuses), tally),
        "=" * 72,
    ]


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def pause_before_exit():
    """
    Hold the console open so a double-clicked run can be read.

    Skipped when there is no interactive console attached - otherwise a
    scheduled or piped run would hang forever waiting for a keypress.
    """
    if not sys.stdin or not sys.stdin.isatty():
        return
    try:
        input("\nPress Enter to close...")
    except (EOFError, KeyboardInterrupt):
        pass


def load_definition(settings_path):
    """
    Read one settings file and resolve it into a Definition.

    Raises ValueError with a readable message for anything wrong with it. The
    caller reports that against this one definition and carries on with the
    others: one mistyped settings file must not stop the other three binders
    from being kept current.
    """
    settings = load_settings(settings_path)

    name = str(settings.get("name", "Documentation")).strip()
    if not name:
        raise ValueError('Setting "name" cannot be empty - it names the '
                         "binder and its file.")
    # The name becomes a filename, so it cannot contain path separators or
    # the characters Windows refuses in one.
    if any(character in name for character in '\\/:*?"<>|'):
        raise ValueError(
            'Setting "name" is "{}", which contains a character that '
            'cannot appear in a filename.'.format(name)
        )

    # The root is resolved first, because "~/" in the other settings is
    # measured from it.
    root = resolve_one_folder(
        tidy_setting_text(settings.get("root", ".."), "root"), "root"
    )
    if not root.is_dir():
        raise ValueError(
            'The "root" setting does not point at a folder that exists:\n'
            "  {}".format(root)
        )

    subfolders = read_flag(settings, "subfolders", True)
    scope = build_scope(root, subfolders,
                        read_string_list(settings, "include"),
                        read_string_list(settings, "exclude"))

    output_folder = resolve_one_folder(
        tidy_setting_text(settings.get("output", "~/_binder"), "output"),
        "output", root=root
    )
    # A definition that says nothing about its log gets one named for itself,
    # rather than all four definitions in a folder appending to one file.
    log_path = resolve_one_folder(
        tidy_setting_text(
            settings.get("log_file", LOG_FILENAME_FORMAT.format(name=name)),
            "log_file"),
        "log_file", root=root
    )

    return Definition(
        settings_path=settings_path,
        name=name,
        scope=scope,
        file_types=(read_string_list(settings, "file_types")
                    or list(DEFAULT_FILE_TYPES)),
        exclude_files=compile_exclude_files(
            read_string_list(settings, "exclude_files")),
        order=read_string_list(settings, "order"),
        output_folder=output_folder,
        log_path=log_path,
    )


def build_binder(definition, dry_run, force):
    """
    Build one binder. Returns a status word for the roll-up: "rebuilt",
    "unchanged", "empty", or "with problems".

    Everything below this line is the tool as it always was - one settings
    file, one scope, one binder. Running four of them is the caller's job.
    """
    name = definition.name
    scope = definition.scope
    root = scope.root
    settings_path = definition.settings_path
    file_types = definition.file_types
    exclude_files = definition.exclude_files
    order = definition.order
    output_folder = definition.output_folder
    log_path = definition.log_path

    version, previous = next_binder_version(output_folder, name)
    filename = BINDER_FILENAME.format(name=name, number=version)
    output_path = output_folder / filename

    # --- decide -----------------------------------------------------------
    folders = folders_to_collect(scope)
    sources, events = collect_files(scope, folders, file_types, exclude_files,
                                    order, output_folder, output_path, name)
    parts, missing, assembly_events = assemble_parts(sources, root)
    events.extend(assembly_events)

    # --- compare ----------------------------------------------------------
    # Asked before anything is reported as included, because a run that
    # rebuilds nothing should not claim to have included anything. Every branch
    # that cannot answer the question with confidence rebuilds.
    rebuild = True
    change_note = None
    if force:
        change_note = "not consulted (--force): rebuilding unconditionally"
    elif previous is None:
        change_note = "no previous binder to compare against: building"
    elif missing:
        change_note = ("not consulted: {} source file(s) could not be read "
                       "this run".format(len(missing)))
    else:
        manifest = parse_binder_manifest(previous)
        if manifest is None:
            change_note = ("{} could not be read as a baseline: rebuilding"
                           .format(previous.name))
        else:
            unchanged, description = compare_to_manifest(manifest, parts)
            rebuild = not unchanged
            change_note = "{}: {} - {}".format(
                previous.name, description,
                "rebuilding" if rebuild else "binder not rebuilt",
            )

    # --- act --------------------------------------------------------------
    # An empty scope is a fact about the tree, and the binder records it like
    # any other. It is called out separately because it is the one outcome that
    # is far more often a mistake in the settings than a true statement, and
    # nobody should have to infer it from a binder with nothing in it.
    if not parts:
        events.append(Event(
            "EMPTY", root,
            "no files in scope - {}".format(
                "the current binder already records that" if not rebuild
                else "an empty binder {} written so the tree is not "
                     "misrepresented".format("would be" if dry_run else "is"))
        ))

    if not rebuild:
        # Nothing is written, nothing is superseded, and no version number is
        # consumed. The previous binder remains the current one.
        events.append(Event(
            "WOULD CHECK" if dry_run else "NO CHANGES", output_folder,
            "no changes detected since {}; binder {} rebuilt"
            .format(previous.name, "would not be" if dry_run else "not")
        ))
    else:
        for part in parts:
            events.append(Event(
                "WOULD INCLUDE" if dry_run else "INCLUDED",
                part.path.parent,
                "{}  (sha256 {})".format(part.path.name, part.digest)
            ))

        binder_text = build_binder_text(name, version, parts, missing)

        if missing:
            events.append(Event(
                "INCOMPLETE", output_folder,
                "{} source file(s) could not be read; the binder is stamped "
                "INCOMPLETE and the previous binder has been left in place"
                .format(len(missing))
            ))

        written_ok = True
        if dry_run:
            events.append(Event(
                "WOULD WRITE", output_folder,
                "{}  ({} files, {} bytes)"
                .format(filename, len(parts),
                        len(binder_text.encode("utf-8")))
            ))
        else:
            try:
                written = write_binder(output_folder, filename, binder_text)
                events.append(Event(
                    "WRITTEN", output_folder,
                    "{}  ({} files, {} bytes)"
                    .format(written.name, len(parts), written.stat().st_size)
                ))
            except OSError as error:
                written_ok = False
                events.append(Event("ERROR", output_folder,
                                    "could not write {}: {}"
                                    .format(filename, error)))

        # Supersede only a genuinely successful, complete write. An incomplete
        # binder must not displace the last good one, and neither must a write
        # that failed.
        if previous is not None and written_ok and not missing:
            events.append(supersede_previous(previous, dry_run))

    # --- report -----------------------------------------------------------
    # Report in folder order rather than in the order things happened, so
    # everything concerning one folder appears together.
    events.sort(key=lambda event: (str(event.folder), event.kind))

    lines = build_report(name, scope, settings_path, dry_run, len(folders),
                         events, change_note)
    print("\n".join(lines))

    # Dry runs are logged too, clearly marked, so the log is a complete record
    # of every time the tool was pointed at the tree. Definitions sharing a
    # log_file share a log, in the order they ran.
    append_to_log(log_path, lines)
    print("\nLog: {}".format(log_path))

    # The status word feeds the roll-up line when more than one binder ran.
    # "with problems" wins over everything else: an ERROR is what decides the
    # exit code, and a run that both wrote a binder and hit an error wrote an
    # incomplete one.
    if any(event.kind == "ERROR" for event in events):
        return "with problems"
    if not rebuild:
        return "unchanged"
    return "empty" if not parts else "rebuilt"


def report_settings_problem(settings_path, error):
    """One block for a settings file that could not be used."""
    print("=" * 72)
    print("SETTINGS PROBLEM")
    print("settings: {}".format(settings_path))
    print("-" * 72)
    print(error)
    print("=" * 72)
    print("")


def run(dry_run, force, wanted, show_list):
    """
    Build every binder defined in this folder, or the ones named.

    Returns an exit code: 0 for success, 1 for a problem.
    """
    definitions = []
    broken = []                       # (settings_path, error)
    for settings_path in discover_settings_files():
        try:
            definitions.append(load_definition(settings_path))
        except (ValueError, OSError, UnicodeDecodeError) as error:
            broken.append((settings_path, error))

    # Two definitions with one name would take turns superseding each other's
    # binder. Nothing runs until it is sorted out.
    duplicates = duplicate_names(definitions)
    if duplicates:
        print("SETTINGS PROBLEM")
        print("Two binder definitions cannot share a name - the name decides "
              "the output")
        print("filename, so each build would supersede the other's binder.")
        for group in duplicates.values():
            print("")
            print('  "{}" is used by:'.format(group[0].name))
            for definition in group:
                print("    {}".format(definition.settings_path.name))
        return 1

    if show_list:
        print("\n".join(describe_definitions(definitions, broken)))
        return 1 if broken else 0

    chosen, unmatched = select_definitions(definitions, wanted)
    if unmatched:
        print("NOTHING RUN")
        print("No binder is defined here under {}:".format(
            "these names" if len(unmatched) > 1 else "this name"))
        for selector in unmatched:
            print('  "{}"'.format(selector))
        print("")
        print("\n".join(describe_definitions(definitions, broken)))
        return 1

    # A settings file that cannot be read is a fact about this folder rather
    # than about the selection, so it is reported either way - including when
    # the run was narrowed to binders that are perfectly fine.
    for settings_path, error in broken:
        report_settings_problem(settings_path, error)

    statuses = []
    for definition in chosen:
        statuses.append(build_binder(definition, dry_run, force))
        print("")

    if len(chosen) > 1 or broken:
        print("\n".join(build_roll_up(statuses, broken)))

    had_problems = bool(broken) or "with problems" in statuses
    return 1 if had_problems else 0


def main():
    parser = argparse.ArgumentParser(
        description="Assemble the documents of a defined scope into a single "
                    "binder file. Every {} in the script's own folder is one "
                    "binder definition - conventionally named {} - and all of "
                    "them are built unless some are named."
                    .format(SETTINGS_GLOB,
                            SETTINGS_FILENAME_FORMAT.format(name="<name>"))
    )
    parser.add_argument(
        "binders",
        nargs="*",            # zero or more; zero means every definition
        metavar="BINDER",
        help="the binder(s) to build, by name - or by settings filename. "
             "Default: every definition in this folder.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",  # present = True, absent = False
        help="report what would be assembled without writing anything",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="rebuild even when nothing in scope has changed since the last "
             "binder was written",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        dest="show_list",
        help="list the binder definitions in this folder and build nothing",
    )
    args = parser.parse_args()

    try:
        exit_code = run(args.dry_run, args.force, args.binders,
                        args.show_list)
    except KeyboardInterrupt:
        print("\nInterrupted.")
        exit_code = 1

    pause_before_exit()
    return exit_code


# When Python runs a file directly, it sets __name__ to "__main__". This guard
# is the conventional way to say "only do this when run, not when imported".
if __name__ == "__main__":
    sys.exit(main())
<!-- END SOURCE: Infrastructure/binder-builder/binder_builder.py -->

---

<!-- BEGIN SOURCE: Infrastructure/binder-builder/binder_builder_Documentation_settings.json -->
{
  "_comment": "Settings for the binder builder. This file IS the binder definition - it declares what the binder contains. One binder per copy of the tool: a second binder means a second folder with its own copy of the script and its own settings, not a second entry here. Any key starting with _comment is ignored by the tool - JSON has no comment syntax, so notes live in keys like this one.",

  "_comment_name": "The binder's name. Used in the heading (\"<name> Binder\"), in the binder filename (\"<name>_Binder_v<number>.md\"), and in this settings file's own name (\"binder_builder_<name>_settings.json\") and log (\"binder_builder_<name>.log\"). It also identifies this binder on the command line, and no two definitions in one folder may share it.",
  "name": "Documentation",

  "_comment_root": "The folder the binder is built from, including everything beneath it unless subfolders is false. A relative path is resolved against the folder this script lives in, so \"..\" means the parent folder. Give a full path such as \"C:/Users/you/Documents\" to point somewhere else. Forward slashes are safe on Windows.",
  "root": "..",

  "_comment_subfolders": "true walks the whole tree from root. false collects from root only.",
  "subfolders": true,

  "_comment_paths": "include and exclude accept three kinds of path. ABSOLUTE - \"C:/Docs/_binder\" - names one exact folder. ROOT-ANCHORED - \"~/_binder\" - names one exact folder, measured from the root above. RELATIVE - \"_binder\" - is a pattern rather than a place: it matches every folder in the tree whose path ends with those segments, so one entry covers a _binder subfolder wherever it appears. Note that ~ means the root of the tree here, never your home folder.",

  "_comment_defaults": "The tool skips two kinds of folder by default, without any entry in exclude. (1) Any folder whose name starts with an underscore. (2) The asset folders: assets, images, img and media. Use include to override a default skip for a specific folder. include does not include a default-skipped folder's own default-skipped children, so including _rebuild does not include _rebuild/_superseded.",

  "_comment_include": "Folders skipped by default that should be collected from anyway. See _comment_defaults above for what is skipped, and why including one folder does not include its underscore-prefixed children.",
  "include": [],

  "_comment_exclude": "Folders to skip entirely, along with everything inside them. Exclude always wins over include. A relative entry here is powerful: \"_superseded\" would skip every _superseded folder in the tree.",
  "exclude": [],

  "_comment_file_types": "File extensions to collect, without the dot.",
  "file_types": ["md", "yaml", "yml", "json", "txt", "py"],

  "_comment_exclude_files": "Files to skip. Applied AFTER file_types has chosen what to collect, so this setting only ever removes, and it is the last word. Three forms, the same convention include and exclude use for folders. FILENAME - \"*_WIP_*\" - matched against the name wherever the file appears. ROOT-ANCHORED - \"~/_rebuild/*.json\" - one exact path, measured from the root. TRAILING - \"_rebuild/*.json\" - a pattern rather than a place: any file whose path ends with those segments, so one entry covers a _rebuild folder wherever it appears.",

  "_comment_exclude_files_wildcards": "? matches one character. In the two path forms * stops at a folder separator and ** crosses them: \"~/_rebuild/*.json\" is JSON directly in _rebuild, while \"~/_rebuild/**/*.json\" is JSON in _rebuild and everything beneath it. The filename form has no separators to stop at.",

  "_comment_exclude_files_convention": "The working document - work in progress, working notes - is what belongs here: it is loaded separately when active state is needed. The test is durability, not cadence. Work registers and open-items documents outlive the session and belong IN the binder, so never exclude them here. Example: [\"*_WIP_*\", \"*_WIP.*\"]",
  "exclude_files": [],

  "_comment_order": "Optional. Filenames pulled to the front of the binder, in the order listed. Everything not named here follows, sorted by path. A name that matches nothing in scope is reported, not silently ignored.",
  "order": [],

  "_comment_output": "The folder the binder is written to. Absolute, or \"~/\" for root-anchored, or relative to the script folder. The default \"~/_binder\" is an underscore folder inside the root, so it is skipped by the walk and a binder can never contain itself.",
  "output": "~/_binder",

  "_comment_log_file": "Where the run log is appended. One entry per run, never overwritten. Absolute, or \"~/\" for root-anchored, or relative to the script folder. Leave this out entirely and the log is named for the binder - binder_builder_<name>.log - which is what keeps four definitions in one folder from interleaving four runs in one file. Set it explicitly to point several binders at one log on purpose.",
  "log_file": "binder_builder_Documentation.log"
}
<!-- END SOURCE: Infrastructure/binder-builder/binder_builder_Documentation_settings.json -->

---

<!-- BEGIN SOURCE: Infrastructure/binder-builder/BinderBuilder_Design_v10.md -->
# Binder Builder — Design

> **Version 10** (2026-09-08). **Reverses §5a's empty-scope rule.** An empty scope now writes an
> empty binder, stamped as empty on its own face, instead of writing nothing and leaving the
> previous binder in place. The old rule protected a good binder from being replaced by an empty
> one; what it actually produced was a binder that went on asserting content the scope no longer
> held. See D18.
>
> v9 (2026-09-08) named a settings file and its log for the binder they belong to —
> `binder_builder_{name}_settings.json` and `binder_builder_{name}.log` — so a folder holding
> four definitions can be read without opening any of them. Older filenames still work: the
> discovery glob was widened, not replaced.
>
> v8 (2026-09-08) gave `exclude_files` the same three path forms as `include` and
> `exclude`, so an exclusion can name where a file is and not only what it is called. Added §4c, the
> scope resolution order as five layers, requested in `binder-settings/aide-rebuild-chat/001`. Added
> a `_comment_defaults` key to the shipped settings so the invisible default skips are visible to a
> reader of the settings file. Existing settings files were unaffected: an entry with no `/` in it
> behaves exactly as it always did.
>
> v7 (2026-09-08) replaced the live-state convention with the durability test. v6 corrected v5's
> claim that registers are excluded. v5 (2026-09-07) added several binder definitions per folder —
> see §4b and BinderBuilder D13.

**Master/source folder:** `Documentation/Infrastructure/binder-builder`
**Run from:** a copied instance folder with its own settings and log, e.g. `Documentation/_tools`

---

## Contents

- **Objective and boundary** — what it does and what it deliberately doesn't.
- **Inputs** — settings file: root, folder scope, file scope, output.
- **Path logic** — absolute, folder-relative and root-relative forms.
- **Path forms for `exclude_files`** — the same three, applied to files.
- **Processing model** — walk, collect, order, assemble.
- **Change detection** — when a rebuild is skipped, and when it never is.
- **Several definitions in one folder** — many binders, one run.
- **Scope resolution, as layers** — the five layers, and what each can do.
- **Binder output format** — header, manifest, source delimiters.
- **Versioning and output placement.**
- **Execution behaviour** — live by default, dry run, double-click.
- **Definition of done.**
- **Decisions** — with reasons.

---

## 1. Objective and boundary

**Objective.** Gather the current documents of a defined scope into a single file that can be
dropped into an AI session's context, so a whole topic loads as one artefact rather than many.

**Boundary — hard.** It collects and assembles. It does **not** resolve versions (that is version
cleanup's job, run first) and it does **not** deploy. It is Infrastructure: it acts on the corpus
and is never loaded into an AI session itself.

**Shape.** A single-action tool, sibling to version cleanup. No actions framework, no shared base
class, no plugin system. One instance folder may define several binders (§4b); each is still one
settings file, one scope, one output.

**Pipeline position.** `version cleanup` → `binder builder`. Version cleanup leaves only current
documents in the live tree, so the binder builder can take what it finds without version reasoning.

---

## 2. Inputs — the settings file

JSON, read on launch. A settings file **is** a binder definition: it declares one binder's scope.
An instance folder may hold several of them — see §4b.

| Setting | Purpose |
|---|---|
| `root` | The path the binder is built from. Anchor for root-relative paths. |
| `subfolders` | `true` — walk the tree from root. `false` — process `root` only. |
| `include` | Folders to process that would otherwise be skipped. |
| `exclude` | Folders to skip. |
| `file_types` | Extensions to include. Default: `md`, `yaml`, `yml`, `json`, `txt`, `py`. |
| `exclude_files` | Files to skip. Filename patterns, or path-qualified patterns — see §3a. Applied after `file_types`; see §4c. |
| `order` | Optional. Filenames pulled to the front of the binder, in the order listed. |
| `output` | Folder the binder is written to. |
| `name` | The binder's name. Used in both the `# <name> Binder` heading and the `<name>_Binder_v<N>.md` filename. Must contain no path separator. |
| `log_file` | Log file location. Named to match version cleanup; the two tools must not disagree on the name of the same setting. |

The script writes a commented default settings file if none is present, rather than failing.

### Default folder exclusions

Skipped unless explicitly included:

- Folders with a leading underscore — this keeps the tool out of `_superseded` and out of its own
  `_binder` output.
- Asset folders by name: `assets`, `images`, `img`, `media`.

---

## 3. Path logic

Three forms, resolved as follows. **This supersedes the script-relative behaviour built into
version cleanup v1**; both tools should share this rule.

| Form | Example | Meaning |
|---|---|---|
| **Absolute** | `C:/…/Documentation/_binder` | Exact folder. Survives the instance being moved. |
| **Folder-relative** | `_binder` | A **pattern**, tested against every folder the walk reaches: matches any folder whose path **ends with those segments**. Multi-segment works — `_binder/current` matches any `…/_binder/current`, and the walk passes through the underscore parent to reach it without processing that parent. |
| **Root-relative** | `~/_binder` | Anchored to the `root` setting. One exact folder. |

**Ratified as the Infrastructure-wide convention** (version-cleanup/claude-code/001, 2026-09-04).

**Rejected as errors, not silently tolerated:** `..` inside a relative entry (a pattern has no
anchor for it), bare `~`, `~name`, and `~/` in the `root` setting.

**Consequence, deliberate:** `~` no longer means home directory anywhere in these settings. Home
expansion is dropped for include and exclude paths.

**Consequence, deliberate:** a short exclude entry is powerful. `"exclude": ["_superseded"]` removes
every such folder in the tree. That is the intent, but it means an innocuous-looking entry can take
out a whole class of folders. Prefer absolute or root-relative for anything non-obvious.

**Including a folder does not include its underscore children.** `_binder` included still skips
`_binder/_superseded`.

---

## 3a. Path forms for `exclude_files`

`exclude_files` takes the same three forms §3 gives `include` and `exclude`, read as files rather
than folders:

| Form | Example | Meaning |
|---|---|---|
| **Filename** | `*_WIP_*` | Matched against the name alone, wherever the file appears. |
| **Root-anchored** | `~/_rebuild/*.json` | One exact path, measured from `root`. |
| **Trailing** | `_rebuild/*.json` | A **pattern**: any file whose path ends with those segments, so one entry covers a `_rebuild` folder at any depth. |

**An entry with no `/` in it is the filename form and behaves exactly as it always did.** That is
what makes this change invisible to every settings file written before it.

### Wildcards

`?` matches one character. `*` and `**` differ between the forms, and the difference is the point:

| Pattern | `_rebuild/notes.json` | `_rebuild/sub/notes.json` |
|---|---|---|
| `~/_rebuild/*.json` | matches | **no** |
| `~/_rebuild/*/*.json` | **no** | matches |
| `~/_rebuild/**/*.json` | matches | matches |

In a path form **`*` stops at a folder separator and `**` crosses them**, `**` standing for zero or
more whole segments. In the filename form there are no separators to stop at, so `*` is
unrestricted as before.

**This is glob's rule, not `fnmatch`'s, and the substitution is deliberate.** `fnmatch`'s `*`
matches `/` as well as everything else, so `~/_rebuild/*.json` under `fnmatch` would also match
`_rebuild/anything/deep/x.json` and the qualification would mean nothing at all. See D15.

**Refused, not tolerated:** a bare `~`, `~name`, and `..` anywhere in a path form — the same
rejections §3 makes, for the same reason. A pattern that cannot mean anything is a settings error,
not a pattern that quietly matches nothing.

Matching is case-folded the way the local filesystem folds names, and paths are spelled with
forward slashes on every platform, so one settings file behaves the same everywhere.

**The report names the pattern that dropped a file** — `SKIPPED  x.json: matches exclude_files
pattern "~/_rebuild/*.json"` — which is the question anyone with four entries in a settings file
actually has.

---

## 4. Processing model

1. Resolve settings; resolve `root`.
2. Walk from `root` (or process `root` alone if `subfolders` is false), applying folder scope rules
   at each step.
3. Collect files matching `file_types` and not matching `exclude_files`.
4. Order: files named in `order` first, in that order; everything else alphabetically by path.
5. Assemble the binder.
6. Write it to `output`, append to the log, report on screen.

**Descend and process are two separate questions.** Reaching a folder nested inside an excluded
parent means walking *through* that parent without collecting from it — which is how a
`_binder/current` include pattern traverses the underscore-prefixed parent and collects only from
`current`. Fusing the two questions would make multi-segment include patterns unreachable.

**Live state is excluded by convention, not by rule.** The tool holds no opinion about which
filenames are live state and never has: it applies the `exclude_files` patterns a binder's own
settings give it, and hard-coding names into the tool is what this sentence exists to forbid.

The convention itself belongs to the corpus, not to this tool, and is stated here only so that a
settings file can be read against it. The test is one line:

> **The test is durability, not cadence.**
>
> The working document holds what is current-and-transient, plus pending content destined for
> masters not yet written. Everything that outlives the session is binder-class.

| Class | In the binder? |
|---|---|
| **The working document** — work in progress, working notes | **No.** Loaded separately when active state is needed. |
| **Work registers** | **Yes.** |
| **Open-items documents** | **Yes.** A parked question outlives the session by definition — that is what parking means. |

**Cadence is not the test, and mistaking it for one is the trap.** Registers and open-items
documents both churn at session cadence in raw terms. The discipline that makes them binder-safe is
that they are *written at master update*, and that discipline is available to any document. What
cannot be made binder-safe is content that is meaningless outside the session that produced it.

Items accumulate in the working document between master updates and move across when masters
update, so a reader wanting current register or open items checks the working document **as well
as** the register or open-items document.

**History, because both corrections were made against this tool's settings and both mattered.** v5
and earlier listed registers among the excluded, which was wrong (corrected v6, from
`tool-pipeline/aide-rebuild-chat/002`). v6 admitted registers on a cadence argument, which reached
the right answer by the wrong route and left open-items documents excluded; the owner replaced it
with the durability test in `tool-pipeline/aide-rebuild-chat/003`.

In both cases the running instance's `exclude_files` carried the pattern in question, invisible
only because no such document existed yet. Each would have dropped a document out of the binder the
moment the first masters landed — a binder that looks complete and quietly is not, which is the
failure §5a exists to make loud. A convention error in this table is not a documentation matter; it
is a defect waiting for its first input.

---

## 4a. Change detection

A binder is a derived artefact. If every in-scope file is byte-for-byte what it was when the last
binder was written, rebuilding produces the same content under a new version number and pushes a
perfectly good binder into `_superseded` for nothing. Untidy when someone runs the tool by hand;
wasteful once the FileUpdatePackage deployer runs it after every deploy.

**The comparison needs no new state.** The answer is already in the binder: §5's manifest lists
every file it contains with a digest of that file's content. Reading that manifest back and
comparing it against the digests this run computed answers "has anything in scope changed" exactly
— additions and removals included, because the comparison is over the *set* of files as well as
over the digests.

1. Assemble as normal, computing a digest per file. Nothing is written yet.
2. Parse the manifest of the current binder into filename → digest pairs.
3. Same set of labels, same digests → report `NO CHANGES`, write nothing, supersede nothing,
   consume no version number. Otherwise rebuild as normal.

**Every uncertainty resolves towards rebuilding.** The tool always builds when:

| Case | Why |
|---|---|
| No previous binder | First run. Nothing to compare against. |
| The previous binder cannot be read, or is not UTF-8 | No baseline. |
| Its manifest heading is absent, or any entry will not parse | The contents of that binder cannot be established, and guessing at the rest would be worse than rebuilding. |
| The previous binder is stamped `INCOMPLETE` | It is missing files by definition, so "nothing changed" measured against it would hold the hole open indefinitely. |
| A source could not be read *this* run | The run is already incomplete; §5a governs it, not this section. |
| `--force` | The stated override. |

The asymmetry is deliberate. An unnecessary rebuild costs a version number. A wrongly skipped one
leaves a binder that misrepresents the tree, which is the failure this tool exists to prevent.

**Report.** `NO CHANGES` live, `WOULD CHECK` in a dry run. Both name the binder compared against.
Every run — skipped or not — also carries a `change detection:` line in the report header stating
what the comparison found, so a log entry that rebuilt says why it rebuilt and not only that it did.

**The check is placed before the `INCLUDED` events are raised**, not after: a run that rebuilds
nothing must not claim to have included anything.

**The comparison reads the format §5 writes.** The manifest reader and the manifest writer are two
halves of one contract and have to change together. The reader is deliberately lenient about the
separator between the filename and the digest and strict about everything else, so a hand-tidied
binder still parses while an unrecognisable one falls back to rebuilding.

---

## 4b. Several definitions in one folder

Every `binder_builder_settings*.json` in the script's own folder is a binder definition. So a folder
holds `binder_builder_settings.json`, and beside it `binder_builder_settings_projectdesign.json`,
`binder_builder_settings_infrastructure.json`, and as many more as the corpus needs. **One run
builds all of them**, in file order — the plain name first, then the rest alphabetically.

**A binder is identified by its `name` setting.** That was already required to be unique: it names
the output file and drives the version scan, so two definitions sharing a name would supersede each
other's binder on alternate runs. Sharing is refused before anything runs, naming both files.

### File naming

The name goes in the filenames too, so a folder of four definitions can be read without opening any
of them:

| File | Form | Example |
|---|---|---|
| Settings | `binder_builder_{name}_settings.json` | `binder_builder_AIDE_Documentation_settings.json` |
| Log | `binder_builder_{name}.log` | `binder_builder_AIDE_Documentation.log` |

**The log name is derived, not required.** A definition that says nothing about `log_file` gets a
log named for itself, which is what keeps four definitions from interleaving four runs in one file.
Setting `log_file` explicitly still points several binders at one log, deliberately, and that
remains a legitimate choice — one file per folder in run order is exactly what someone auditing a
whole folder wants.

**The filename is a convention, not an input.** The tool reads the `name` *setting*, never the
filename, so the two can in principle disagree — nothing breaks if they do, and `--list` prints
them side by side, which is where a disagreement shows up. Enforcing agreement was considered and
rejected: it would break the two older spellings below for no gain beyond tidiness.

**Older filenames still work.** The discovery glob is `binder_builder*settings*.json`, deliberately
wider than the convention, and matches all three of:

- `binder_builder_{name}_settings.json` — the convention.
- `binder_builder_settings.json` — the original single-definition name. Sorts first when present.
- `binder_builder_settings_{x}.json` — the spelling this document recommended between v5 and v8.

A convention tidied after publication must not break the files written while the old one stood. See
D17.

### Selection

| Command | Effect |
|---|---|
| `python binder_builder.py` | Every definition in the folder. |
| `python binder_builder.py ProjectDesign Infrastructure` | Just those two. |
| `python binder_builder.py --list` | What is defined here. Builds nothing. |

A selector matches a binder's `name`, or the filename of its settings file with or without the
extension, case-insensitively. **A selector that matches nothing stops the whole run** and prints
what is available: "build these four", three-quarters done, is worse than not started.

`--dry-run` and `--force` apply to whatever was selected.

### Isolation

One definition failing must not take the others down — the entire point of the feature is that four
binders stay current, and one mistyped settings file is not a reason for three good binders to go
stale. So a settings file that cannot be read, or one whose `root` does not exist, is reported as
its own `SETTINGS PROBLEM` block and the run carries on with the rest. The run exits `1`.

An unreadable settings file is reported **whether or not the run was narrowed to other binders**. It
is a fact about the folder rather than about the selection.

### The roll-up

When more than one binder ran — or when a settings file could not be read — the run ends with one
line for the folder as a whole:

```text
========================================================================
Result: 4 binder(s) - 1 rebuilt, 2 unchanged, 1 with problems
========================================================================
```

It is **not** printed when a single definition ran cleanly. A folder holding one binder therefore
produces exactly the output it always did, and anything reading the last `Result:` line of this
tool's output — the FileUpdatePackage deployer does — keeps working in both cases, reading the
per-binder line when there is one binder and the roll-up when there are several.

The roll-up is not written to any log: definitions may have different `log_file` settings, and a
folder-level line has no single log to belong to. Every binder's own report is logged as always.

### What makes this safe

A build reads no global state. Every path, every scope, every digest and every log in a build comes
out of one definition, so building four is building one, four times. The `_binder` output folder can
be shared because the version scan, the self-inclusion guard and supersession all match on the
binder's own `<name>_Binder_v<N>.md` class (§6, D9) — `ProjectDesign_Binder_v3.md` and
`Infrastructure_Binder_v7.md` sit side by side without either touching the other.

**The exception, stated:** if an output folder is deliberately brought *into* a binder's scope with
an `include`, that binder's self-inclusion guard will skip its own binders and swallow its
neighbours'. The default `_binder` is underscore-prefixed and therefore outside every walk, so this
cannot happen by accident.

**Change detection is what makes it cheap** (§4a). Four definitions where nothing has changed cost
four manifest comparisons and no writes at all.

---

## 4c. Scope resolution, as layers

Scope is decided in five layers. **Each layer can only narrow what the previous one admitted**, and
at any level an exclusion beats an inclusion.

| Layer | Rule |
|---|---|
| **1 — Defaults** | Underscore folders and the asset folders `assets`, `images`, `img`, `media` are skipped unless overridden. |
| **2 — Include** | Overrides a default skip for named folders. Including a folder does not include its own default-skipped children. |
| **3 — Folder exclude** | Wins over include, always, along with everything beneath. |
| **4 — File types** | Only the listed extensions are collected from in-scope folders. |
| **5 — File exclude** | `exclude_files` drops matching files from what layer 4 admitted. The last word. |

**Layers 4 and 5 are sequential, not independent** — `exclude_files` is applied to what `file_types`
already selected. Confirmed against the build, and it has one observable consequence worth stating:
a file whose extension is not in `file_types` is dropped at layer 4 and never reaches layer 5, so it
produces no `SKIPPED` event. Only files that were genuinely in scope and then excluded are reported.
That is deliberate — §7 explains why unlisted extensions are silent — but it means the report shows
layer 5's decisions and not layer 4's.

Because layer 5 can only remove, a path-qualified pattern there **cannot conflict with a folder-level
include or exclude.** It can make an included folder contribute less; it can never make an excluded
folder contribute anything. That is what makes adding path qualification at layer 5 safe rather than
a second, competing scope language.

**The layers are stated in a settings file too, not only here.** `_comment_defaults` in the shipped
settings names layer 1 in plain language, because layer 1 is the only one with no entry anywhere to
show for it — a reader who has never seen this document would otherwise have to infer the underscore
and asset-folder rules from behaviour. See D16.

---

## 5. Binder output format

```markdown
# <Name> Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents
> and regenerate the Binder.
> **Binder Version <N>** (<date>).

This Binder is a current-context consumption artefact; authoritative masters remain
individual files.

## Binder manifest

- `<filename>` — sha256 `<12-char digest>`
- `<filename>` — sha256 `<12-char digest>`

---

<!-- BEGIN SOURCE: <filename> -->
<full file content, unmodified>
<!-- END SOURCE: <filename> -->

---

<!-- BEGIN SOURCE: <next filename> -->
…
```

- Source content is copied **unmodified**, with exactly two stated exceptions:
  - A trailing newline is added where a source lacks one, so the closing delimiter sits on its own
    line.
  - A leading byte-order mark is stripped. A BOM is a start-of-file marker; one left embedded
    halfway down a binder puts a stray `U+FEFF` in the middle of the text.
- **Encoding.** Read bytes and decode `utf-8-sig`. Write UTF-8 without BOM, **in binary mode** —
  text mode on Windows rewrites every `\n` as `\r\n` and would silently alter every source line
  ending in the binder.
- Manifest lists files in binder order.
- Digests are truncated sha256, twelve characters, computed over **the source content as read**,
  not the section as written. D3's purpose is answering "does this binder match the masters"; a
  digest including the tool's own added newline answers a different question.
- **No hand-written change note** in the header — see Decision D2.
- Where assembly is incomplete, a block near the top of the binder lists every missing file.

---

## 5a. Incomplete and empty runs

The two cases look alike and are opposite. **An incomplete binder is defective; an empty binder is
correct.** A binder missing files it should contain cannot be trusted about anything. A binder
containing nothing, because nothing was in scope, is an accurate statement about the tree.

| Case | Behaviour |
|---|---|
| **Empty scope** — no in-scope files found | **Write the binder.** It carries an `EMPTY BINDER` block in its header and a manifest reading `(no files)`. The previous binder is superseded as usual. Report `EMPTY`. |
| **Incomplete** — a source cannot be read or decoded | Write the binder, but do **not** supersede the previous one, so the last good binder stays available beside the holed one. Report `ERROR` naming the file, plus `INCOMPLETE`, and list the missing files in the binder's own header block and the log. |

The rule for the incomplete case is unchanged: **a defective binder never displaces a good one.**

**Change detection covers the empty case** (§4a), which is what stops it churning. An empty scope
whose current binder is already empty compares equal — nothing added, nothing removed — and reports
`NO CHANGES`. Only a transition into or out of empty writes anything.

**`EMPTY` is reported even when nothing is written**, because an empty scope is far more often a
mistake in the settings than a true statement about the tree, and nobody should have to infer it
from a binder with nothing in it.

---

## 6. Versioning and output placement

**Name:** `<name>_Binder_v<N>.md`, with its own counter independent of the documents inside.

**Version resolution:** scan the output folder for existing binders of that name, take the highest
`N`, write `N+1`. Self-managing; no version recorded in settings.

**Placement:** the output folder is declared in settings. Default `_binder` beside the masters — an
underscore folder, therefore excluded from the walk by default.

**Self-inclusion guard.** Skip any file in the output folder matching `<name>_Binder_v<N>.md`.

This is stated against the **artefact class**, not the artefact. A guard written against "the file
I am about to write" defends nothing, because that file does not exist when the guard runs — but
*last* run's binder does, and would be swallowed as an ordinary source, doubling the corpus on
every build. See Decision D9.

**Supersession:** on a successful and complete write, the binder builder moves the previous binder
of that name into `_superseded` inside the output folder. See Decision D7.

---

## 7. Execution behaviour

Matches version cleanup, so the tools behave alike:

- Python, standard library only, single readable script.
- Runs **live by default**; `--dry-run` reports what would be assembled and writes nothing.
- `--force` rebuilds even when §4a finds nothing changed. It is the only way to consume a version
  number deliberately.
- Naming one or more binders builds only those; `--list` shows what is defined. See §4b.
- Reads settings on launch — no arguments required, so **double-click works on Windows**, and a
  double-click builds every binder defined in the folder.
- Prints a clear report; **pauses for a keypress before exiting** so the console doesn't vanish.
- Appends one entry per run to the log: binder written, version, files included, any skipped.
- Cross-platform; Windows primary.

### Report vocabulary

`INCLUDED` / `WOULD INCLUDE` · `SKIPPED` · `UNMATCHED` · `NO CHANGES` / `WOULD CHECK` ·
`WRITTEN` / `WOULD WRITE` · `SUPERSEDED` / `WOULD SUPERSEDE` · `CONFLICT` · `EMPTY` ·
`INCOMPLETE` · `ERROR`

`NO CHANGES` is §4a: nothing in scope has changed, so no binder was written and the previous one
remains current. `WOULD CHECK` is the dry-run twin — the same comparison, reported rather than
acted on. Neither is a failure; both exit `0`.

`CONFLICT` and `ERROR` carry version cleanup's meanings exactly. `UNMATCHED` is an `order` entry
naming a file not in scope — a binder assembled in an order its author did not get is a quiet
defect, so it is reported. Files whose extension is simply not in `file_types` are **not** reported;
a document tree is full of them and listing each would bury the report.

**Exit code `0` unless an `ERROR` occurred**, matching version cleanup. An `EMPTY` run exits `0`:
it wrote a binder, and the binder is correct. See §10.

---

## 8. Definition of done

Point an instance at a scope and it produces a single, correctly-versioned binder containing every
in-scope current document, with a manifest matching its contents, source files copied unmodified,
a readable on-screen report and a log entry. Dry run produces the same report and writes nothing.

An `exclude_files` entry naming a path — `~/_rebuild/*.json` — drops exactly the files at that
path and no others; the same entry written without a `~/` prefix drops them under a folder of that
name at any depth; an entry with no `/` behaves as it always did. A pattern that cannot mean
anything stops that binder with an explanation rather than matching nothing quietly. The report
names the pattern that dropped each file.

A folder of four definitions can be read from its file listing alone: each settings file and each
log carries its binder's name. A settings file written under either older spelling is still
discovered and built.

Put four settings files in one folder and one run keeps all four binders current, each reported
separately and the folder summarised in one line. Name one on the command line and only that one is
built. Name something that is not defined and nothing is built at all. Break one settings file and
the other three still build.

Point it at a scope that is empty and it writes a binder saying so, stamped `EMPTY BINDER` in its
own header, rather than leaving a binder that asserts content the scope no longer holds. Run it
again with the scope still empty and it writes nothing further.

Run it a second time with the tree untouched and it writes nothing, supersedes nothing, consumes no
version number, and says `NO CHANGES` naming the binder it compared against. Change, add or remove
any in-scope file and the next run rebuilds. `--force` rebuilds regardless. A run that cannot
establish a baseline — no previous binder, an unreadable one, an unparseable manifest, a previous
build stamped `INCOMPLETE` — rebuilds rather than skipping.

---

## 9. Decisions

**D1 — The settings file is the binder definition.** No separate definition document. The scope
declaration and the run configuration are the same information; splitting them would create two
things to keep in step. *The second half of this decision — one instance folder per binder — is
reversed by D13; the first half stands and is what makes D13 work.*

**D2 — Drop the hand-written change note from the binder header.** The old format carried an
authored line describing what changed in that issue. A generator cannot write it, and the binder is
a disposable regenerated artefact — a changelog on it duplicates the version lines the masters
already carry. *Reversible if a real need appears: add a `note` setting.*

**D3 — Keep the sha256 manifest digests.** Weak keep. They cost nothing to generate and answer
"does this binder match the masters" if a verification tool ever wants them.

**D4 — No partitioned binder sets.** The old corpus split one topic across five binders plus a set
index because of volume. Real problem, not today's problem. Build one binder per instance; revisit
if a topic genuinely exceeds a usable context.

**D5 — Version resolution by scanning output, not by settings.** A version number in settings is
state that drifts from reality. The folder is the truth.

**D6 — Path logic is shared with version cleanup.** Folder-relative evaluated per walk step,
root-relative via `~/`, absolute exact; home expansion dropped. Two Infrastructure tools with
different path semantics would be a trap.

**D7 — The binder builder supersedes its own previous output.** On a successful write it moves the
prior binder of that name into `_superseded` within the output folder.

*Considered and rejected:* leaving it for version cleanup. Rejected because the default output
folder is `_binder`, which version cleanup skips by the underscore rule — it would have to be
explicitly included purely to tidy up after every build. And this is not general supersession: the
tool knows exactly which single file it just replaced, so there is no scanning, grouping or version
reasoning to duplicate.

**Principle:** a tool cleans up after itself. Version cleanup handles supersession it didn't cause.

**D8 — `output` and `name` are two settings.** v1 gave one key described as carrying both the
folder and the binder's name. One key cannot do both jobs; the heading and the filename need the
name, the write needs the folder. Split, with `name` rejecting any path separator.

**D9 — Guards are written against the artefact class, not the artefact.** v1's self-inclusion check
("if a resolved input file is the output path, skip") is a no-op: the output file does not exist
when the guard runs. The previous run's binder does, and was swallowed as a source in test — six
files became seven, and the corpus would double on every build. The rule is to match the class
`<name>_Binder_v<N>.md`.

*Generalisable:* any Infrastructure tool that both reads and writes inside one tree needs its guard
written this way. This belongs to the Infrastructure container definition when that is written.

**D10 — Digests cover source content, not the written section.** They differ by one byte where a
source lacks a trailing newline. D3's stated purpose is comparison against the masters, so the
digest must describe the master.

**D11 — BOM stripping is a stated exception to byte-for-byte copying.** Accepted deliberately, and
named here so it is not later read as a defect.

**D13 — Several definitions in one folder, discovered by glob.** v1 to v4 said one binder means one
instance folder. That was right for what the tool then was and is wrong for what it now is.

*What changed underneath it.* The original reasoning was that a second binder in one settings file
would mean a settings schema with a list of binders in it, and every setting then having to say
which binder it belonged to — a configuration format growing a dimension. That objection still
holds, and this is not that: **one file is still exactly one binder**, with the schema untouched.
What is new is that the folder, not the file, is the unit of "everything here".

*What made it worth doing.* Change detection (D12). Before it, running four definitions meant
writing four binders and consuming four version numbers on every run, so the cost of "keep them all
current" scaled with the number of binders and running them separately was no worse. With it, three
unchanged binders cost three manifest comparisons. "Rebuild whatever needs rebuilding" became a
single cheap act, and the tool should let someone do it in one command.

*Considered and rejected:* a `--settings` argument naming a file. It solves nothing on its own — the
user still runs the tool four times, and now has to remember four filenames — and it makes
double-click, which is how this tool is actually used, the one mode that cannot reach the other
binders.

*Considered and rejected:* a separate list file naming the definitions. A second thing to keep in
step with the folder, which is the same objection as D5 to version numbers in settings. The folder
is the truth.

*Identity is the `name` setting*, not the filename, because `name` already had to be unique — it
decides the output filename. A duplicate is refused before anything runs rather than resolved,
because both plausible resolutions (first wins, last wins) silently give someone a binder they did
not ask for.

**D18 — An empty scope writes an empty binder.** Reverses the rule v1 to v9 held, that an empty
scope writes nothing and leaves the previous binder alone.

*The original reasoning, and why it was wrong.* The old rule called an empty binder replacing a good
one "a loss of information dressed up as a successful build". That framing has a false premise: the
previous binder is **superseded, not deleted** — it moves to `_superseded` beside the new one, and
recovering it is a file move. Almost nothing is lost. What the rule produced instead was worse: a
binder sitting in the output folder, presenting as current, asserting content the scope no longer
held. A stale binder that looks authoritative is precisely the failure this tool exists to prevent,
and the old rule manufactured one deliberately.

*The case that exposed it.* Exclusions are tightened until everything in scope is excluded. The tool
reported `EMPTY`, wrote nothing, and left a binder that still contained every excluded file. The
report said the scope was empty; the binder said otherwise; the binder is what gets loaded into a
session.

*What replaces the guard.* Three things, none of which the old rule provided. The binder says
`EMPTY BINDER` in its own header, so a reader who never sees a report cannot mistake it. The run
reports `EMPTY` whether or not it wrote, so a misconfigured scope stays loud. And the previous
binder is in `_superseded`, one move from being restored.

*Consequence, accepted:* a typo in `root` now supersedes a good binder with an empty one. That is a
real regression in one narrow case, recoverable by moving a file, and it is preferred to the
alternative — a stale binder that nothing announces at all.

*Generalisable:* refusing to record an unwelcome state does not prevent the state, it only removes
the record. This tool's job is to describe the tree, including when the tree is empty.

**D17 — Settings and log are named for the binder; the glob is widened rather than replaced.**
`binder_builder_{name}_settings.json` and `binder_builder_{name}.log`. The reason is the one D13
created: once a folder can hold four definitions, four files called some variation of "settings"
have to be told apart, and opening each one to find out which binder it defines is exactly the
friction D13 was meant to remove.

*The glob is `binder_builder*settings*.json`, not the convention itself.* Three spellings now exist
in the wild — this document recommended `binder_builder_settings_{x}.json` between v5 and v8, and
`binder_builder_settings.json` predates definitions entirely. Narrowing the glob to the new
convention would have silently stopped discovering files written on this document's own advice, and
a binder that stops being built without saying so is the failure mode this tool most needs to avoid.
The cost of the wider glob is that it also matches names nobody intends to write; that costs
nothing, because an unintended match is a settings file that either parses or is reported.

*The log name is derived rather than mandated.* A definition may still name its log explicitly and
share one, which is the right answer for a folder someone audits as a whole.

*The filename is not read.* Identity stays in the `name` setting, per D13. The filename is a
convenience for humans reading a folder listing, and `--list` shows both so drift is visible.

**D15 — Path-qualified `exclude_files` uses glob's wildcards, not `fnmatch`'s.** In a path form
`*` stops at a folder separator and `**` crosses them.

*Why it cannot be `fnmatch`.* `fnmatch`'s `*` matches `/`, so `~/_rebuild/*.json` would also match
`_rebuild/deep/nested/x.json`. Every path-qualified pattern would then be silently recursive, the
qualification would carry no information, and there would be no way to express "this folder only" at
all. The one thing the feature exists to do could not be said.

*Consequence, accepted:* two wildcard dialects in one settings file — `fnmatch` for the filename
form, glob for the path forms. Considered and rejected: moving the filename form to glob as well.
Under glob, `*_WIP_*` still behaves identically because a filename contains no separators, so the
change would be invisible in every case anyone has written — but it would be a behaviour change to
existing settings for no benefit, and this design has consistently refused those.

*Consequence, accepted:* `~/_rebuild/*/*.json` means "exactly one folder below `_rebuild`", not
"`_rebuild` and everything under it". The recursive form is `~/_rebuild/**/*.json`. The request that
prompted this feature described the `*/` spelling as recursive; that reading is not available
without giving `*` `fnmatch` semantics and losing the non-recursive form entirely. Raised with the
requester rather than resolved silently.

**D16 — Defaults are documented in the settings file, not only in the design.** Layers 2 to 5 of
§4c each have a key in the settings file, so a reader sees them. Layer 1 has none: the underscore
rule and the asset-folder list are enforced by the tool with nothing in the settings to show for
them, and a reader who has never opened this document can only infer them from behaviour — usually
after being surprised. `_comment_defaults` states them where that reader is already looking.

*Generalisable:* any tool in this family whose behaviour includes a rule with no corresponding
setting should state that rule in the settings file. Silent defaults are the ones that get
rediscovered by accident.

**D14 — One bad definition does not stop the good ones.** A settings file that will not parse is
reported and skipped; the rest build. The feature exists so that four binders stay current, and
"three went stale because the fourth had a trailing comma" would defeat it. The run still exits `1`.

*Consequence, accepted:* a run can be partly successful, which neither sibling tool can be. The
roll-up line exists to make that legible in one line rather than requiring the reader to scan four
report blocks.

**D12 — Change detection compares against the binder's own manifest, and keeps no state of its
own.** The alternatives were a sidecar state file recording what the last run saw, and timestamp
comparison against the binder's modification time.

*A sidecar file was rejected* because it is a second source of truth that drifts the first time a
binder is moved, restored or hand-edited — the same reasoning as D5, which put the version number
in the folder rather than in settings. The binder already carries a digest per file; that manifest
*is* the record of what the last build saw, and it cannot drift from the binder because it is part
of it.

*Timestamps were rejected* because they answer a different question. A file touched but not
changed, a checkout that rewrites every modification time, a copy across a filesystem — all move
timestamps without moving content. D3 kept the digests for exactly this purpose and this is the
verification tool it anticipated.

*Consequence, accepted:* the reader in §4a is coupled to the writer in §5. They are two halves of
one contract and are marked as such in both places.

*Consequence, accepted:* a change that leaves every digest identical — a file renamed to a name that
sorts to the same place, then back — is invisible. A digest comparison is a content comparison, and
that is the question worth answering.

---

## 10. Open

- **`EMPTY` and `NO CHANGES` exit codes.** Both are `0`, consistent with treating expected outcomes
  as non-failures. A caller therefore cannot distinguish "binder rebuilt" from "nothing written"
  by exit code alone. The FileUpdatePackage deployer, which now chains this tool, does not need to:
  it reports the binder builder's outcome by reading its report, and a skipped rebuild is a correct
  outcome for it rather than a condition to handle. Prefer a distinct exit code for "nothing
  written" over overloading the failure code if a caller ever does need to branch on it. **Not
  now.**
- **Per-definition scheduling.** Every definition is built on every run. A binder whose scope is
  expensive to walk and rarely changes still gets walked. Not a problem at four definitions over a
  corpus this size; the shape of a fix, if it is ever needed, is a `skip_unless` or an interval in
  the settings — state in a settings file, which D5 warns about. **Not now.**
- **Path-logic duplication.** The three path forms now exist in two implementations. The trigger for
  extracting shared code is a **third tool needing it**, not a third mention. The logic is pure
  functions over paths with no state, which is what has kept copying cheap.
- **The `_superceded` misspelling** at the Documentation root remains, alongside correctly-spelled
  folders. Both are underscore-prefixed so both are skipped. A human act to reconcile.
<!-- END SOURCE: Infrastructure/binder-builder/BinderBuilder_Design_v10.md -->

---

<!-- BEGIN SOURCE: Infrastructure/binder-builder/README.md -->
# binder builder

Gathers the current documents of a defined scope into a single file, so a whole
topic can be dropped into an AI session's context as one artefact rather than
as many.

This folder is the **master copy**. To use the tool, copy `binder_builder.py`
and the settings file to wherever it should run from, then edit that copy's
settings — including renaming it for the binder it defines. Each instance keeps
its own settings and its own log beside the script, so instances never
interfere with each other.

**A settings file is a binder definition.** It declares the scope. To define a
second binder, put a second settings file beside the first — one run builds them
all. See *Several binders in one folder* below.

**Run version cleanup first.** It leaves only current documents in the tree, so
the binder builder can take what it finds without any version reasoning of its
own.

**It will not rebuild for nothing.** If no in-scope file has changed since the
last binder was written, the run reports `NO CHANGES` and writes nothing. See
*Change detection* below.

---

## What it produces

```markdown
# <Name> Binder

> **Generated Binder - do not edit directly.** Edit the individual master documents
> and regenerate the Binder.
> **Binder Version 3** (2026-09-04).

This Binder is a current-context consumption artefact; authoritative masters remain
individual files.

## Binder manifest

- `Alpha/Alpha_Design_v3.md` - sha256 `06f6435c91ff`
- `Beta/beta.yaml` - sha256 `75d068ad343e`

---

<!-- BEGIN SOURCE: Alpha/Alpha_Design_v3.md -->
…the file, exactly as it is on disk…
<!-- END SOURCE: Alpha/Alpha_Design_v3.md -->

---

<!-- BEGIN SOURCE: Beta/beta.yaml -->
…
```

Source content is copied **unmodified** — no reformatting, no heading demotion,
no trimming. The manifest lists the files in binder order, with a truncated
sha256 of each source, so a binder can be checked against its masters.

The one adjustment: a newline is added after a source that does not end with
one, so the closing delimiter starts on its own line.

---

## Installing Python on Windows

Only needed once per machine. The tool uses nothing beyond the Python standard
library, so there is nothing else to install.

1. Go to <https://www.python.org/downloads/windows/> and download the latest
   **Windows installer (64-bit)**. Python 3.8 or newer is required; any current
   release is fine.
2. Run the installer. On the first screen, **tick "Add python.exe to PATH"**
   before clicking Install. This is easy to miss and is the usual reason a
   `.py` file will not run afterwards.
3. Choose **Install Now**.
4. To check it worked, open PowerShell and run:

   ```
   python --version
   ```

   It should print something like `Python 3.13.1`.

### Making double-click work

The standard installer associates `.py` files with the Python launcher, so
double-clicking `binder_builder.py` in File Explorer should just run it. If it
instead opens in Notepad or asks which app to use:

1. Right-click `binder_builder.py` → **Open with** → **Choose another app**.
2. Pick **Python** (or browse to `C:\Windows\py.exe`).
3. Tick **Always use this app to open .py files**.

The script pauses with *"Press Enter to close..."* when it finishes, so the
console window stays open long enough to read the report.

### Running it from a terminal instead

```
python "C:\path\to\binder_builder.py"
```

---

## Settings

The script reads every `binder_builder*settings*.json` in **its own folder** —
not from wherever the terminal happens to be pointing. Each one is a binder. If
the folder holds none at all, the script writes a fresh
`binder_builder_Documentation_settings.json` with default values and
explanatory notes, then tells you to check it. Since a settings file is a binder
definition, a fresh one almost always needs editing — starting with its `name`,
and then its own filename to match.

```json
{
  "name": "Documentation",
  "root": "..",
  "subfolders": true,
  "include": [],
  "exclude": [],
  "file_types": ["md", "yaml", "yml", "json", "txt", "py"],
  "exclude_files": [],
  "order": [],
  "output": "~/_binder",
  "log_file": "binder_builder.log"
}
```

| Setting | Meaning |
| --- | --- |
| `name` | The binder's name — used in the heading and in the filename. |
| `root` | The folder the binder is built from. |
| `subfolders` | `true` walks the whole tree; `false` collects from `root` only. |
| `include` | Folders to collect from that would otherwise be skipped. |
| `exclude` | Folders to skip entirely, along with everything inside them. |
| `file_types` | Extensions to collect, without the dot. |
| `exclude_files` | Files to skip — by name, or by path. Applied after `file_types`. |
| `order` | Filenames pulled to the front of the binder, in the order listed. |
| `output` | The folder the binder is written to. |
| `log_file` | Where the run log is appended. |

### Which folders are skipped by default

- Any folder whose name starts with an underscore. This is what keeps the tool
  out of `_superseded` and out of its own `_binder` output — it is the
  mechanism that makes it impossible for a binder to contain a binder.
- The asset folders `assets`, `images`, `img` and `media`, by name.

List a folder in `include` to collect from it anyway. Including a folder does
**not** include its underscore-prefixed children: `_binder` included still skips
`_binder/_superseded`.

### The three path forms

**`root`, `output` and `log_file`** take a full path, a `~/` path measured from
`root`, or a path measured from the folder the script lives in — so `".."`
means "the folder above me", and an instance sitting in `Documentation/_tools`
builds from `Documentation` by default. (`root` itself cannot use `~/`, since it
is what defines the root.)

**`include` and `exclude`** take the same three forms, but the relative one
means something different:

| Form | Example | Means |
| --- | --- | --- |
| Absolute | `"C:/Docs/_binder"` | that one exact folder |
| Root-anchored | `"~/_binder"` | that one exact folder, measured from `root` |
| Relative | `"_binder"` | a **pattern**: every folder in the tree whose path ends with those segments |

**`exclude_files` takes the same three forms**, applied to files — see
*Excluding files by path* below.

The relative form is the useful one for a corpus. `"_binder"` is not a place,
it is a shape — it matches a `_binder` subfolder wherever one appears, at any
depth. Several segments work too: `"_binder/current"` matches any
`.../_binder/current`, and the walk passes *through* the underscore parent to
reach it without collecting that parent's own files.

Two consequences worth holding on to:

- `"~"` here means **the root of the tree**, never your home folder. The tool
  never expands `~` the way a shell would.
- A relative entry in `exclude` is powerful in the same way. `"_superseded"`
  would skip every `_superseded` folder in the tree, not one of them. Prefer
  absolute or root-anchored for anything non-obvious.

This is the same path model as version cleanup, deliberately. Two Infrastructure
tools with different path semantics would be a trap.

**Writing paths in JSON.** Use forward slashes (`"C:/Users/you/Documents"`) or
doubled backslashes (`"C:\\Users\\you"`); a single backslash is an escape
character in JSON and will break the file.

**Comments.** JSON has no comment syntax, so the notes in the shipped settings
file are carried as keys beginning with `_comment`. They are ordinary JSON and
the tool ignores them. Leave them, edit them, or delete them as you prefer.

### Excluding live state

The working document — work in progress, working notes — is loaded separately
when active state is actually needed, so it is normally kept out of the binder.
Do that through `exclude_files` in the binder's own settings rather than
expecting the tool to know the names:

```json
"exclude_files": ["*_WIP_*", "*_Working_*"]
```

**Work registers and open-items documents are a different case: they belong
*in* the binder.** The test is **durability, not cadence** — everything that
outlives the session is binder-class, and a parked question outlives the
session by definition. Both churn at session cadence in raw terms; what makes
them binder-safe is that they are written at master update. Do not add a
`*_WorkRegister_*` or `*_OpenItems_*` pattern here.

Items accumulate in the working document between master updates, so a reader
wanting current register or open items checks the working document as well.

`*` matches any run of characters and `?` matches one, matched
case-insensitively on Windows and case-sensitively elsewhere — the same way the
filesystem does.

### Excluding files by path

An `exclude_files` entry containing a `/` is matched against the file's **path**
rather than its name, using the same three forms as `include` and `exclude`:

| Form | Example | Means |
| --- | --- | --- |
| Filename | `"*_WIP_*"` | the name, wherever the file is |
| Root-anchored | `"~/_rebuild/*.json"` | that exact path, measured from `root` |
| Trailing | `"_rebuild/*.json"` | a **pattern**: any file whose path ends with those segments, so it covers a `_rebuild` folder at any depth |

**An entry with no `/` in it behaves exactly as it always did**, so nothing you
have already written changes.

In the two path forms, `*` stops at a folder separator and `**` crosses them:

| Pattern | `_rebuild/notes.json` | `_rebuild/sub/notes.json` |
| --- | --- | --- |
| `~/_rebuild/*.json` | matches | no |
| `~/_rebuild/*/*.json` | no | matches |
| `~/_rebuild/**/*.json` | matches | matches |

So `*/` is "exactly one folder down" and `**/` is "here and anything below".
Use `**` when you mean recursive.

A bare `~`, a `~name`, or a `..` anywhere in a path pattern is refused with an
explanation rather than quietly matching nothing.

The report names the pattern that dropped each file:

```
SKIPPED  tool_settings.json: matches exclude_files pattern "~/_rebuild/*.json"
```

### Ordering

Files named in `order` come first, in the order listed. Everything else follows,
sorted by path. Matching is on the filename alone, so an `order` entry catches
that file wherever it lives.

An `order` entry that matches nothing in scope is reported as `UNMATCHED` rather
than passed over, because a binder assembled in an order its author did not get
is a quiet defect.

---

## Several binders in one folder

Each settings file in the script's folder is one binder, and both the settings
and the log are named for the binder they belong to:

```
_tools/
├── binder_builder.py
├── binder_builder_AIDE_Documentation_settings.json
├── binder_builder_ProjectDesign_settings.json
├── binder_builder_Infrastructure_settings.json
├── binder_builder_Methodology_settings.json
├── binder_builder_AIDE_Documentation.log
├── binder_builder_ProjectDesign.log
├── binder_builder_Infrastructure.log
└── binder_builder_Methodology.log
```

So a folder of four binders can be read from the listing without opening
anything.

To add one, copy an existing settings file to
`binder_builder_<name>_settings.json`, edit it, and set its `name` to match.

**The filename is a convention, not an input.** The tool reads the `name`
*setting*, never the filename, so nothing breaks if they disagree — but
`--list` prints them side by side, which is where you will notice.

**The log name is derived.** Leave `log_file` out and each binder gets
`binder_builder_<name>.log` automatically, so four definitions do not interleave
four runs in one file. Set `log_file` explicitly if you would rather several
binders shared one — one file per folder in run order is exactly what someone
auditing a whole folder wants.

**Older filenames still work.** `binder_builder_settings.json`, and the
`binder_builder_settings_<something>.json` spelling this README recommended
earlier, are both still discovered and built. Rename them when convenient;
nothing forces it.

**Give each one a different `name`.** The name decides the output filename, so
two binders sharing one would take turns superseding each other's file. The tool
refuses to run at all if it finds a duplicate, and tells you which two files
clash.

They can share an output folder. `ProjectDesign_Binder_v3.md` and
`Infrastructure_Binder_v7.md` sit happily side by side in one `_binder`: each
definition only ever scans, supersedes and skips binders of its own name.

They can share a log too — that is what happens if you leave `log_file` alone,
and it gives you one file with every build in it, in order. Give a definition a
different `log_file` if you would rather it kept its own.

### Running them

```
python binder_builder.py
```

builds every binder defined in the folder — which is also what double-clicking
does. Each one gets its own report, and the run ends with a line for the folder:

```
========================================================================
Result: 4 binder(s) - 1 rebuilt, 3 unchanged
========================================================================
```

To build only some of them, name them:

```
python binder_builder.py ProjectDesign Infrastructure
```

The name is the `name` from the settings file, or the settings filename itself
if that is easier to remember; either way it is matched case-insensitively. Name
something that is not defined and **nothing** is built — the tool lists what is
available instead, on the grounds that "build these four", three-quarters done,
is worse than not started.

To see what is defined without building anything:

```
python binder_builder.py --list
```

`--dry-run` and `--force` apply to whatever you selected.

### If one definition is broken

It is reported on its own and the others still build. Four binders staying
current is the point of keeping them in one folder; three of them going stale
because the fourth has a trailing comma would defeat it. The run still exits `1`,
and the roll-up counts it:

```
Result: 4 binder(s) - 4 unchanged, 1 unreadable
```

### Why this is cheap

Change detection. Four definitions where nothing has changed cost four manifest
comparisons and no writes at all, so running the lot after every edit is a
sensible habit rather than an expensive one.

---

## Versioning and output

The binder is written as `<Name>_Binder_v<N>.md`, with a counter of its own,
independent of the versions of the documents inside it.

The version is worked out by **scanning the output folder** — highest `N` found,
write `N+1`. Nothing is recorded in settings, because a number kept in settings
drifts from reality the first time a file is moved by hand.

A run that finds nothing changed does not consume a version number — see
*Change detection* below.

On a successful write, the previous binder of that name is moved into
`_superseded` inside the output folder. A tool cleans up after itself; version
cleanup handles supersession it did not cause. Nothing is ever overwritten — if
the `_superseded` slot is taken, the run reports `CONFLICT` and leaves the file
alone.

---

## Change detection

The binder is a derived file. Rebuilding it when nothing has changed produces
the same content under a new version number and pushes a perfectly good binder
into `_superseded` for nothing.

So before writing, the tool compares what it just assembled against the
**manifest of the current binder** — the list of filenames and digests in that
binder's own header. Same files, same digests, and there is nothing to do:

```
change detection: Documentation_Binder_v7.md: 24 file(s) in scope, all matching the manifest - binder not rebuilt

[_binder]
  NO CHANGES       no changes detected since Documentation_Binder_v7.md; binder not rebuilt
```

Nothing is written, nothing is superseded, and no version number is used up.
The previous binder is still the current one.

Change, add or remove any in-scope file and the next run rebuilds, saying what
it noticed:

```
change detection: Documentation_Binder_v7.md: 1 changed, 1 added (Project Design/ProjectDesign_Design_v8.md, Project Design/ProjectDesign_Index_v8.md) - rebuilding
```

There is no state file. The comparison uses the digests the binder already
carries, so there is nothing that can drift out of step with it — and nothing
to clean up if a binder is moved or restored by hand.

**It builds whenever it cannot be sure.** No previous binder, a previous binder
it cannot read, a manifest it cannot parse, a previous build stamped
`INCOMPLETE`, or a source it could not read this time: all rebuild. An
unnecessary rebuild costs a version number; a wrongly skipped one leaves a
binder that misrepresents the tree.

**Timestamps are not used.** A file touched but not changed, or a checkout that
rewrites every modification time, would both trigger a pointless rebuild. The
comparison is over content.

To rebuild anyway:

```
python binder_builder.py --force
```

A dry run reports the same comparison as `WOULD CHECK` and writes nothing
either way.

---

## Running it

Live by default — there is no confirmation prompt. With no arguments it builds
every binder defined in the folder:

```
python binder_builder.py
```

One binder only:

```
python binder_builder.py ProjectDesign
```

Report only, writes nothing:

```
python binder_builder.py --dry-run
```

Rebuild even if nothing has changed:

```
python binder_builder.py --force
```

List the binder definitions in this folder and build nothing:

```
python binder_builder.py --list
```

The dry run takes exactly the same decisions as a live run — it reads every
source and computes every digest — and reports them with `WOULD INCLUDE` and
`WOULD WRITE` in place of `INCLUDED` and `WRITTEN`. It is the safe way to check
a new scope before letting the tool write anything.

---

## The report

| Kind | Meaning |
| --- | --- |
| `INCLUDED` | File placed in the binder, with its digest. |
| `WOULD INCLUDE` | Dry run — the same file, nothing written. |
| `SKIPPED` | In a collected folder, deliberately left out — an `exclude_files` match, or the tool's own output. |
| `UNMATCHED` | An `order` entry naming a file that is not in scope. |
| `NO CHANGES` | Nothing in scope has changed since the last binder. Nothing written, nothing superseded. |
| `WOULD CHECK` | Dry run — the same comparison, reported rather than acted on. |
| `WRITTEN` / `WOULD WRITE` | The binder itself. |
| `SUPERSEDED` / `WOULD SUPERSEDE` | The previous binder moved into `_superseded`. |
| `CONFLICT` | A destination name is already taken; nothing overwritten. |
| `EMPTY` | Nothing in scope. An empty binder is written, saying so. |
| `INCOMPLETE` | A source could not be read. The binder has a hole in it. |
| `ERROR` | A filesystem refusal — a locked file, permissions, an unreadable folder. |

Events are grouped by folder. The exit code is `0` unless at least one `ERROR`
occurred.

### Two cases worth understanding

**`EMPTY` — nothing was in scope.** The binder is still written, and says so on
its own first screenful:

```
> **EMPTY BINDER - nothing was in scope when this was built.**
>
> This is a statement about the tree, not a failure: the scope genuinely
> contained no files. If that is unexpected, the scope settings are where
> to look.
```

The previous binder is superseded as usual, so it is in `_superseded` and one
move from being restored if this was not what you wanted.

This is deliberate, and it is the opposite of what the tool used to do. Writing
nothing sounds safer, but it leaves a binder in the output folder presenting as
current while asserting content the scope no longer holds — and that binder is
what gets loaded into a session. A stale binder that looks authoritative is the
worst thing this tool could produce. An empty one that says it is empty is
merely surprising.

`EMPTY` is reported whether or not anything was written, because an empty scope
is far more often a settings mistake than a true statement. If you see it and
did not expect it, check `include`, `exclude_files` and `file_types` first.

Running again with the scope still empty writes nothing further — change
detection sees an empty binder and an empty scope and reports `NO CHANGES`.

**`INCOMPLETE` — a source could not be read.** The binder is written, but it has
a hole in it, so it is stamped as incomplete in three places: the report, the
log, and a block near the top of the binder itself naming every missing file.
The previous binder is **not** superseded, so the last good one stays available.
A plausible-looking binder that is quietly missing a document is the worst thing
this tool could produce, so it is made loud in every place someone might look.

---

## Text encoding

Stated explicitly rather than left to the platform:

- **Read** as UTF-8, with a byte-order mark removed if one is present. That BOM
  removal is the only deviation from byte-for-byte copying, and it is
  deliberate: a BOM is a start-of-file marker, and leaving one embedded halfway
  down a binder puts a stray character in the middle of the text.
- **Write** as UTF-8 without a BOM, in binary mode so that no line-ending
  translation can happen. Line endings pass through exactly as they were in the
  source.

A file that is not valid UTF-8 cannot go into the binder. It is reported as an
`ERROR`, and the binder it would have gone into is stamped `INCOMPLETE`.

---

## The log

Every run appends one entry to the log file, live and dry-run alike, each
stamped with the date, the mode and the root it was pointed at. The log is never
rewritten or trimmed. If it grows unwieldy, archive or delete it by hand; the
tool will start a fresh one.

---

## Scope

It collects and assembles. It does not resolve versions — that is version
cleanup's job, run first — and it does not deploy. It is Infrastructure: it acts
on the corpus and is never loaded into an AI session itself.
<!-- END SOURCE: Infrastructure/binder-builder/README.md -->

---

<!-- BEGIN SOURCE: Infrastructure/file-update-package/file_update_package.py -->
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
file update package - deploy a package of updated documents into the tree.

WHAT IT DOES
    Takes a FileUpdatePackage - a zip file produced by a Chat or Cowork
    session, carrying updated documentation files and a manifest describing
    them - and deploys those files into the master tree.

        find the newest package in the drop folder
        validate it: a zip, with a manifest, naming files it actually contains
        show the package's instructions to the user and wait, if it has any
        for each file: move the document it replaces into _superseded,
                       then write the new one
        run the binder builder
        move the package into _superseded
        report what happened, and hold the window open until it is read

WHAT IT DOES NOT DO
    It does not merge, patch or edit. A package carries whole files and this
    tool places them. It does not decide what should be in a package, and it
    does not resolve versions beyond moving the single file each manifest entry
    names - general supersession is version cleanup's job.

    It never overwrites. A file already sitting where a package wants to write,
    and not named as the one being replaced, is reported as a CONFLICT and left
    exactly where it is.

HOW IT IS RUN
    Live by default. Pass --dry-run to see the report without changing
    anything. It reads its settings from a JSON file sitting beside this
    script, so it can simply be double-clicked on Windows.

    The completion summary is the point of the run, not an afterthought: it is
    the user's confirmation that the deploy did what they expected, and the
    window stays open until they have read it.

DESIGN NOTE
    This is one tool that does one thing, and a sibling to version cleanup and
    the binder builder. The path logic, settings loader, plan/apply split and
    report shape below are deliberately the same as theirs, copied rather than
    imported: there is no shared module, no plugin system and no base class
    between them.

Python 3.8 or newer. Standard library only.
"""

import argparse
import datetime
import difflib
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
# Path(__file__) is this script's own file. .resolve() turns it into a full,
# unambiguous path, and .parent gives the folder holding it. Everything the
# tool reads or writes hangs off this folder rather than off the "current
# working directory", because the working directory depends on *how* the script
# was launched (double-click, terminal, scheduler) and is therefore unreliable.
# It also means each copy of the tool uses its own settings and its own log.
SCRIPT_DIR = Path(__file__).resolve().parent

SETTINGS_FILENAME = "file_update_package_settings.json"
SUPERSEDED_FOLDER_NAME = "_superseded"

# The manifest sits at the root of the package and is the package's statement
# of what it contains. A zip without one is not a FileUpdatePackage.
MANIFEST_NAME = "_manifest.json"

PACKAGE_SUFFIX = ".zip"

# Spots "C:" or "D:" at the start of a path, so a Windows path in a settings
# file being run on Mac or Linux fails loudly rather than being mistaken for a
# relative pattern that then silently never matches anything. Also used on
# manifest paths, where a drive letter is never legitimate.
WINDOWS_DRIVE = re.compile(r"^[A-Za-z]:")

# How long the binder builder is given before the deploy stops waiting for it.
# The trigger is best-effort: a binder builder that hangs must not hang the
# report of a deploy that has already happened.
BINDER_TIMEOUT_SECONDS = 600

# Folder names this corpus has settled on. The check that uses them does not
# rename anything - it only says, in the completion summary, that a folder is
# one character away from a convention. The known offender is the misspelled
# "_superceded" at the documentation root, which is deliberately left alone: it
# is underscore-prefixed, so every tool skips it, and reconciling it is a human
# act rather than a tool's.
CONVENTION_FOLDER_NAMES = (
    "_superseded",
    "_fileupdatepackages",
    "_binder",
    "_tools",
    "_config",
    "_rebuild",
)

# difflib's similarity ratio, 0.0 to 1.0. At 0.85 a one-character misspelling of
# a convention name is caught and an unrelated folder is not. The check is
# advisory - it never changes what the tool does or what it exits with - but a
# summary that cries wolf stops being read, so it is paired with the underscore
# rule below rather than being loosened.
NAMING_SIMILARITY = 0.85

# The settings file is shipped with the tool, but if someone deletes it - or
# copies just the .py file to a new location - we write this back out rather
# than failing. Keeping the defaults as *text* (not as a Python dictionary that
# gets dumped to JSON) means the file we create is byte-for-byte the file we
# ship, comments and ordering included.
#
# JSON has no comment syntax, so the explanatory lines are carried as ordinary
# keys beginning with "_comment". The loader ignores them. That keeps the file
# valid JSON, readable by any editor and parseable by the standard library.
DEFAULT_SETTINGS_JSON = """{
  "_comment": "Settings for the file update package deployer. Edit the values below. Any key starting with _comment is ignored by the tool - JSON has no comment syntax, so notes live in keys like this one.",

  "_comment_documentation_root": "The root of the document tree packages are deployed into. Manifest paths are measured from here. A relative path is resolved against the folder this script lives in, so \\"..\\" means the parent folder - which is what an instance sitting in _tools wants. Give a full path such as \\"C:/Users/you/Documents\\" to point somewhere else. Forward slashes are safe on Windows. This setting cannot use \\"~/\\", because \\"~/\\" means \\"measured from the documentation root\\" and this is the setting that defines it.",
  "documentation_root": "..",

  "_comment_paths": "The three settings below accept three kinds of path. ABSOLUTE - \\"C:/Docs/_fileupdatepackages\\". ROOT-ANCHORED - \\"~/_fileupdatepackages\\" - measured from the documentation root above. RELATIVE - \\"_fileupdatepackages\\" - measured from the folder this script lives in. Note that ~ means the documentation root here, never your home folder.",

  "_comment_drop_folder": "Where packages are put to be deployed. The newest unprocessed .zip in this folder is the one that gets processed; the rest wait. Processed packages are moved into a _superseded subfolder of it.",
  "drop_folder": "~/_fileupdatepackages",

  "_comment_binder_builder": "The binder builder script to run after a deploy. Point this at the running instance, not at the master copy, so it uses that instance's settings. Set it to \\"\\" to skip the trigger entirely.",
  "binder_builder": "~/_tools/binder_builder.py",

  "_comment_log_file": "Where the run log is appended. One entry per run, never overwritten. Absolute, or \\"~/\\" for root-anchored, or relative to the script folder.",
  "log_file": "file_update_package.log"
}
"""


# ---------------------------------------------------------------------------
# Small record types
# ---------------------------------------------------------------------------
# A dataclass is Python shorthand for "a class that just holds these fields".
# The lines below generate the constructor for us. Used here instead of loose
# tuples so that report code can say event.kind rather than event[0].

@dataclass
class Event:
    """One line of the report: something that happened, or failed to."""
    kind: str      # see REPORT_KINDS
    folder: Path   # the folder it concerns
    detail: str    # human-readable description


# The vocabulary, in the order a summary line lists it. The paired live and dry
# run words are the same shape the sibling tools use for MOVED/WOULD MOVE and
# INCLUDED/WOULD INCLUDE. CONFLICT and ERROR carry their meanings exactly.
REPORT_KINDS = (
    "DEPLOYED",        # an updated file written over its predecessor's place
    "WOULD DEPLOY",    # dry run equivalent
    "CREATED",         # a file that did not exist before
    "WOULD CREATE",
    "SUPERSEDED",      # the document a manifest entry replaces, moved aside
    "WOULD SUPERSEDE",
    "CONFLICT",        # a destination is taken, or a supersession is ambiguous
    "SKIPPED",         # nothing to do, or a package left waiting its turn
    "INVALID",         # not a package, or a manifest that cannot be trusted
    "BINDER",          # the binder builder was triggered, and what it said
    "PROCESSED",       # the package itself, moved into _superseded
    "WOULD PROCESS",
    "ERROR",           # filesystem refusal, or a failed binder builder run
)


@dataclass
class ManifestEntry:
    """One file a package asks to be deployed."""
    path: str          # as written in the manifest, forward slashes
    action: str        # "create" or "update"
    replaces: str      # filename of the document being superseded, or ""
    relative: Path     # the same path, validated and turned into a Path


@dataclass
class Manifest:
    """A package's statement of what it contains."""
    description: str = ""
    user_instructions: str = ""
    entries: list = field(default_factory=list)


@dataclass
class Outcome:
    """
    The facts the completion summary states that the event list cannot.

    Counts are derived from the events, so they are not held here. What is held
    is everything the summary must say about the run as a whole: which package,
    whether the user saw its instructions, what the binder builder did, and
    whether the package was filed away afterwards.
    """
    package: Path = None
    package_line: str = ""      # name, date and size, taken before it moves
    description: str = ""
    instructions: str = "none in this package"
    binder: str = "not triggered"
    package_state: str = "left in the drop folder"
    entry_count: int = 0        # files the manifest asked for
    naming: list = field(default_factory=list)   # (relative path, expected)


# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------

def load_settings(settings_path):
    """
    Read the settings file, creating it from the shipped defaults if missing.

    Returns a plain dictionary. Raises ValueError with a readable message if
    the file exists but is not valid JSON - a mistyped settings file should
    stop the run with an explanation, not with a stack trace.
    """
    if not settings_path.exists():
        print("No settings file found. Creating one with default values:")
        print("  {}".format(settings_path))
        print("Check the paths in it, then run the tool again.")
        print("")
        settings_path.write_text(DEFAULT_SETTINGS_JSON, encoding="utf-8")

    text = settings_path.read_text(encoding="utf-8")
    try:
        settings = json.loads(text)
    except json.JSONDecodeError as error:
        # The exception carries the line and column of the problem, which is
        # the single most useful thing to show someone fixing the file.
        raise ValueError(
            "The settings file is not valid JSON.\n"
            "  file: {}\n"
            "  problem: {} (line {}, column {})\n"
            "Common causes: a missing comma, a trailing comma after the last "
            "item, or a single backslash inside a path (write \\\\ or use /)."
            .format(settings_path, error.msg, error.lineno, error.colno)
        )

    if not isinstance(settings, dict):
        raise ValueError(
            "The settings file must contain a JSON object (a {{ ... }} block), "
            "but it contains {}.".format(type(settings).__name__)
        )

    return settings


# ---------------------------------------------------------------------------
# Path forms
# ---------------------------------------------------------------------------
# The same three spellings the sibling tools accept:
#
#   absolute        "C:/Docs/_fileupdatepackages"   one exact folder
#   root-anchored   "~/_fileupdatepackages"         measured from the root
#   relative        "_fileupdatepackages"           measured from the script
#
# This tool has no include or exclude lists, so there is nowhere for the
# folder-relative *pattern* form to apply: every setting here names one place,
# and the relative spelling is therefore resolved against the script folder,
# exactly as `root`, `output` and `log_file` are in the other two tools.
#
# Note that "~" does NOT mean the home folder here. Python's expanduser is
# deliberately never called on these settings, so "~/" always means the
# documentation root and can never quietly resolve to C:\\Users\\someone.

def tidy_setting_text(value, label):
    """Trim a settings value and normalise its separators to forward slashes."""
    text = str(value).strip().replace("\\", "/")
    if not text:
        raise ValueError('Setting "{}" contains an empty path.'.format(label))
    return text


def resolve_one_folder(text, label, root=None):
    """
    Resolve a settings value that names ONE place: absolute, "~/" measured from
    the documentation root, or relative to the script's own folder.
    """
    if text.startswith("~"):
        if root is None:
            raise ValueError(
                'Setting "{}" cannot use "~/", because "~/" means "measured '
                'from the documentation root" and this setting is what defines '
                'that root. Use a full path, or a path relative to the script '
                'folder - ".." is the folder above this script, which is what '
                'an instance sitting in a _tools folder wants.'.format(label)
            )
        if not text.startswith("~/"):
            raise ValueError(
                'Setting "{}": "~" means the documentation root, so it has to '
                'be written as "~/something".'.format(label)
            )
        return (root / text[2:]).resolve()

    path = Path(text)
    if not path.is_absolute():
        if WINDOWS_DRIVE.match(text):
            raise ValueError(
                'Setting "{}" is "{}", which looks like a Windows path, but '
                "this is not Windows.".format(label, text)
            )
        # resolve() also removes any ".." segments, so two spellings of the
        # same folder compare equal later on.
        path = SCRIPT_DIR / path
    return path.resolve()


def normalise(path):
    """
    Case-fold a path the way the local filesystem does.

    os.path.normcase lowercases on Windows, where FOO and foo are the same
    folder, and changes nothing on Mac or Linux. Comparing paths through it
    avoids both false misses on Windows and false matches elsewhere.
    """
    return Path(os.path.normcase(str(path)))


def is_inside(path, folder):
    """True if `path` is `folder` itself, or anywhere beneath it."""
    try:
        normalise(path).relative_to(normalise(folder))
        return True
    except ValueError:
        # relative_to raises when path is not under folder. Catching that is
        # the standard pathlib way of asking this question.
        return False


def relative_to(path, root):
    """Show a path relative to the root when possible - shorter to read."""
    try:
        relative = path.relative_to(root)
    except ValueError:
        return str(path)
    return str(relative) if str(relative) != "." else "."


# ---------------------------------------------------------------------------
# Finding the package
# ---------------------------------------------------------------------------

def find_packages(drop_folder):
    """
    Every unprocessed package in the drop folder, newest first.

    Only the top level is looked at, which is what keeps processed packages -
    which live in the _superseded subfolder - from being found again. The sort
    is by modification time, with the name as a tie-breaker so that two files
    written in the same second still come out in a stable order.
    """
    if not drop_folder.is_dir():
        return []

    packages = []
    for entry in sorted(drop_folder.iterdir()):
        if not entry.is_file():
            continue
        if entry.suffix.lower() != PACKAGE_SUFFIX:
            continue
        try:
            modified = entry.stat().st_mtime
        except OSError:
            modified = 0.0
        packages.append((modified, os.path.normcase(entry.name), entry))

    packages.sort(key=lambda item: (item[0], item[1]), reverse=True)
    return [entry for _modified, _name, entry in packages]


def describe_package(path):
    """A short "when and how big" line for the report header."""
    try:
        stat = path.stat()
    except OSError:
        return path.name
    when = datetime.datetime.fromtimestamp(stat.st_mtime)
    return "{}  ({}, {:,} bytes)".format(
        path.name, when.strftime("%Y-%m-%d %H:%M"), stat.st_size)


# ---------------------------------------------------------------------------
# Reading and validating the manifest
# ---------------------------------------------------------------------------
# Validation is a gate, not a filter. A package either deploys as a whole or is
# rejected as a whole: a manifest naming a file the zip does not contain is a
# package built wrongly, and deploying the half of it that happens to be
# present would leave the tree in a state nobody designed.
#
# The one thing checked with real suspicion is the shape of each path. A zip is
# an untrusted input, and a member path containing ".." or a drive letter would
# write outside the documentation root - the "zip slip" mistake. Every path is
# therefore checked before it is used, and the resolved destination is checked
# again to be inside the root.

def safe_relative_path(text):
    """
    Turn a manifest path into a relative Path, or raise ValueError.

    Refused: an empty path, an absolute one, a drive letter, and any ".."
    segment. A manifest path is always measured from the documentation root and
    always points downwards.
    """
    if not isinstance(text, str) or not text.strip():
        raise ValueError("the path is empty")

    tidied = text.strip().replace("\\", "/")
    while tidied.startswith("./"):
        tidied = tidied[2:]

    if tidied.startswith("/") or Path(tidied).is_absolute():
        raise ValueError('"{}" is an absolute path'.format(text))
    if WINDOWS_DRIVE.match(tidied):
        raise ValueError('"{}" names a drive'.format(text))

    segments = [part for part in tidied.split("/") if part and part != "."]
    if not segments:
        raise ValueError('"{}" does not name a file'.format(text))
    if ".." in segments:
        raise ValueError(
            '"{}" contains "..", which would write outside the documentation '
            "root".format(text)
        )
    if tidied.endswith("/"):
        raise ValueError('"{}" names a folder, not a file'.format(text))

    return Path(*segments)


def read_manifest(archive, names):
    """
    Read and check the manifest. Returns (manifest, problems).

    `problems` is a list of readable strings. If it is not empty the package is
    INVALID and nothing at all is deployed from it.
    """
    problems = []

    if MANIFEST_NAME not in names:
        return None, ["the package contains no {}".format(MANIFEST_NAME)]

    try:
        raw = archive.read(MANIFEST_NAME).decode("utf-8-sig")
    except (KeyError, OSError, zipfile.BadZipFile) as error:
        return None, ["{} could not be read: {}".format(MANIFEST_NAME, error)]
    except UnicodeDecodeError:
        return None, ["{} is not UTF-8 text".format(MANIFEST_NAME)]

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as error:
        return None, [
            "{} is not valid JSON: {} (line {}, column {})"
            .format(MANIFEST_NAME, error.msg, error.lineno, error.colno)
        ]

    if not isinstance(data, dict):
        return None, [
            "{} must contain a JSON object, but it contains {}"
            .format(MANIFEST_NAME, type(data).__name__)
        ]

    manifest = Manifest(
        description=str(data.get("description", "")).strip(),
        user_instructions=str(data.get("user_instructions", "")).strip(),
    )

    listed = data.get("files")
    if not isinstance(listed, list) or not listed:
        return None, [
            '{} has no "files" list, or it is empty'.format(MANIFEST_NAME)
        ]

    seen = {}
    for position, item in enumerate(listed, start=1):
        where = "files entry {}".format(position)
        if not isinstance(item, dict):
            problems.append("{} is not an object".format(where))
            continue

        try:
            relative = safe_relative_path(item.get("path", ""))
        except ValueError as error:
            problems.append("{}: {}".format(where, error))
            continue

        path = str(item.get("path", "")).strip().replace("\\", "/")
        action = str(item.get("action", "")).strip().lower()
        if action not in ("create", "update"):
            problems.append(
                '{} ({}): action is "{}", but it must be "create" or "update"'
                .format(where, path, item.get("action", ""))
            )
            continue

        replaces = str(item.get("replaces", "") or "").strip()
        if replaces and action != "update":
            problems.append(
                '{} ({}): "replaces" is only meaningful on an update'
                .format(where, path)
            )
            continue
        if replaces and ("/" in replaces or "\\" in replaces):
            problems.append(
                '{} ({}): "replaces" is a filename, not a path - "{}" contains '
                "a folder separator".format(where, path, replaces)
            )
            continue

        # The archive must actually contain what the manifest promises.
        if path not in names:
            problems.append(
                "{}: the package does not contain \"{}\"".format(where, path))
            continue

        # Two entries writing the same destination is a package built wrongly:
        # whichever ran second would hit its own predecessor as a CONFLICT.
        key = os.path.normcase(str(relative))
        if key in seen:
            problems.append(
                '{} ({}): the same path is listed twice (entries {} and {})'
                .format(where, path, seen[key], position)
            )
            continue
        seen[key] = position

        manifest.entries.append(ManifestEntry(
            path=path, action=action, replaces=replaces, relative=relative,
        ))

    if not manifest.entries and not problems:
        problems.append('{} lists no usable files'.format(MANIFEST_NAME))

    return manifest, problems


# ---------------------------------------------------------------------------
# The user instructions gate
# ---------------------------------------------------------------------------

def acknowledge_instructions(instructions, dry_run):
    """
    Show the package's instructions and wait for the user to acknowledge them.

    Deliberately placed BEFORE any file is written, so that stopping here -
    with Ctrl+C - stops a deploy that has not started rather than one that is
    half done.

    Returns a phrase for the completion summary. The wait is skipped when there
    is no interactive console, for the same reason the exit pause is: a run
    triggered by another tool must not block forever on a keypress nobody is
    there to press.
    """
    print("")
    print("=" * 72)
    print("INSTRUCTIONS FROM THIS PACKAGE")
    print("-" * 72)
    for line in instructions.splitlines() or [instructions]:
        print(line)
    print("=" * 72)

    if dry_run:
        print("(dry run - a live run would wait for you here)")
        return "present, shown; not gated in a dry run"

    if not sys.stdin or not sys.stdin.isatty():
        print("(no interactive console - continuing without acknowledgement)")
        return "present, shown; NOT acknowledged - no interactive console"

    try:
        input("\nPress Enter to continue with the deploy, "
              "or Ctrl+C to stop... ")
    except EOFError:
        return "present, shown; not acknowledged - console closed"
    return "present, shown and acknowledged"


# ---------------------------------------------------------------------------
# Deploying
# ---------------------------------------------------------------------------

def find_replaced_file(documentation_root, target, replaces):
    """
    Find the document a manifest entry supersedes. Returns a list of matches.

    Looked for beside the new file first, which is where a superseded version
    almost always is - v7 and v8 of one document live in the same folder. Only
    if it is not there is the rest of the tree searched, and _superseded
    folders are skipped throughout: a file already filed away is not a
    candidate for being filed away again.

    A list is returned rather than one path because "found in three places" is
    a real answer, and one this tool must not resolve by guessing.
    """
    wanted = os.path.normcase(replaces)

    beside = target.parent / replaces
    if beside.is_file():
        return [beside]

    found = []
    for dirpath, dirnames, filenames in os.walk(documentation_root):
        # dirnames[:] = ... replaces the contents of the existing list rather
        # than rebinding the name. os.walk only notices the former.
        dirnames[:] = sorted(
            name for name in dirnames
            if os.path.normcase(name) != SUPERSEDED_FOLDER_NAME
        )
        for filename in filenames:
            if os.path.normcase(filename) == wanted:
                found.append(Path(dirpath) / filename)
    return found


def supersede(path, dry_run):
    """
    Move one document into _superseded beside it. Returns an Event.

    Nothing is ever overwritten: a taken destination is a CONFLICT and the file
    stays where it is. This is the same shape, and the same guarantee, as the
    binder builder's supersession of its own previous output.
    """
    folder = path.parent
    destination = folder / SUPERSEDED_FOLDER_NAME / path.name

    if dry_run:
        return Event("WOULD SUPERSEDE", folder,
                     "{} -> {}/".format(path.name, SUPERSEDED_FOLDER_NAME))

    if destination.exists():
        return Event(
            "CONFLICT", folder,
            "{} left in place: {}/{} already exists"
            .format(path.name, SUPERSEDED_FOLDER_NAME, path.name)
        )

    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        # A last existence check immediately before the move: the destination
        # could have appeared since, and shutil.move would silently overwrite
        # it on Linux and macOS.
        if destination.exists():
            return Event(
                "CONFLICT", folder,
                "{} left in place: {}/{} appeared during the run"
                .format(path.name, SUPERSEDED_FOLDER_NAME, path.name)
            )
        shutil.move(str(path), str(destination))
        return Event("SUPERSEDED", folder,
                     "{} -> {}/".format(path.name, SUPERSEDED_FOLDER_NAME))
    except OSError as error:
        return Event("ERROR", folder,
                     "{} could not be superseded: {}".format(path.name, error))


def write_member(archive, member, target):
    """
    Write one file out of the package.

    Binary mode throughout: the bytes in the package are the bytes on disk,
    with no encoding assumption and no line-ending translation. zipfile's own
    extract() is deliberately not used, because it derives the destination from
    the member name - and the destination here has already been validated.
    """
    data = archive.read(member)
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "wb") as handle:
        handle.write(data)
    return len(data)


def deploy_entry(archive, entry, documentation_root, dry_run):
    """
    Deploy one manifest entry. Returns a list of Events, in the order they
    happened: the supersession first, then the write.

    The two questions are asked in this order deliberately. An update whose
    predecessor sits at the same path can only be written after that
    predecessor has been moved aside, and the never-overwrite check that
    follows is then a genuine test rather than a formality.
    """
    events = []
    target = (documentation_root / entry.relative).resolve()
    folder = target.parent

    # Belt and braces after safe_relative_path: the resolved destination must
    # still be inside the documentation root. A symbolic link in the tree could
    # otherwise carry a well-formed relative path somewhere else entirely.
    if not is_inside(target, documentation_root):
        return [Event(
            "CONFLICT", documentation_root,
            "{}: resolves outside the documentation root and was not deployed"
            .format(entry.path)
        )]

    # Does anything stand between this entry and its destination? Normally the
    # answer is simply "is something already there", but an update whose
    # predecessor sits at the destination itself clears its own way.
    occupied = target.exists()

    if entry.action == "update":
        # No "replaces" named means the entry updates the file at its own path,
        # which is the file that then has to be moved aside.
        wanted = entry.replaces or target.name
        matches = find_replaced_file(documentation_root, target, wanted)

        if len(matches) == 1:
            previous = matches[0]
            event = supersede(previous, dry_run)
            events.append(event)
            cleared = event.kind in ("SUPERSEDED", "WOULD SUPERSEDE")

            if normalise(previous) == normalise(target):
                # The document being replaced IS the destination. In a live run
                # it has just been moved; in a dry run it has not, but it would
                # have been, and reporting a conflict against a file the run
                # itself would have moved would make the dry run a liar.
                if not cleared:
                    events.append(Event(
                        "CONFLICT", folder,
                        "{}: not deployed - {} could not be moved out of the "
                        "way".format(entry.path, previous.name)
                    ))
                    return events
                occupied = False
        elif not matches:
            events.append(Event(
                "SKIPPED", folder,
                "{}: nothing superseded - \"{}\" is not in the documentation "
                "tree".format(entry.path, wanted)
            ))
        else:
            events.append(Event(
                "CONFLICT", folder,
                "{}: \"{}\" was found in {} places and none were moved ({})"
                .format(entry.path, wanted, len(matches),
                        ", ".join(relative_to(match, documentation_root)
                                  for match in matches))
            ))

    # Never overwrite. By this point an update's predecessor has been moved out
    # of the way, so anything still sitting at the destination is a file this
    # package did not account for.
    if occupied:
        events.append(Event(
            "CONFLICT", folder,
            "{}: not deployed - a file already exists there and the package "
            "did not name it as superseded".format(entry.path)
        ))
        return events

    # The live word and its dry-run twin, kept as a pair rather than derived
    # from one another: "WOULD " + "DEPLOYED" would read "WOULD DEPLOYED".
    kind, would = (("CREATED", "WOULD CREATE") if entry.action == "create"
                   else ("DEPLOYED", "WOULD DEPLOY"))
    if dry_run:
        events.append(Event(
            would, folder,
            "{}  ({:,} bytes)".format(entry.path,
                                      archive.getinfo(entry.path).file_size)
        ))
        return events

    try:
        written = write_member(archive, entry.path, target)
        events.append(Event(kind, folder,
                            "{}  ({:,} bytes)".format(entry.path, written)))
    except (OSError, zipfile.BadZipFile, KeyError) as error:
        events.append(Event("ERROR", folder,
                            "{} could not be written: {}"
                            .format(entry.path, error)))
    return events


# ---------------------------------------------------------------------------
# The binder builder trigger
# ---------------------------------------------------------------------------

def trigger_binder_builder(script_path, dry_run):
    """
    Run the binder builder. Returns (Event, summary phrase).

    Best-effort by design: the deploy has already happened by the time this
    runs, and a binder that could not be rebuilt does not undo it. A failure
    here is reported as an ERROR against the binder step and the deploy still
    stands.

    The binder builder decides for itself whether a rebuild is needed - it
    compares the tree against the manifest of the current binder - so this is
    an unconditional call, made after every deploy.

    stdin is closed rather than inherited, which is what stops the binder
    builder pausing for a keypress at the end of its own run: it skips that
    pause when it has no interactive console.
    """
    folder = script_path.parent

    if dry_run:
        return (Event("BINDER", folder,
                      "would run {}".format(script_path.name)),
                "would be triggered (dry run)")

    if not script_path.is_file():
        return (Event("ERROR", folder,
                      "binder builder not run: {} does not exist"
                      .format(script_path)),
                "NOT triggered - {} does not exist".format(script_path))

    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(folder),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=BINDER_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return (Event("ERROR", folder,
                      "binder builder did not finish within {} seconds"
                      .format(BINDER_TIMEOUT_SECONDS)),
                "FAILED - did not finish within {} seconds"
                .format(BINDER_TIMEOUT_SECONDS))
    except OSError as error:
        return (Event("ERROR", folder,
                      "binder builder could not be started: {}".format(error)),
                "FAILED - could not be started: {}".format(error))

    output = result.stdout.decode("utf-8", errors="replace")
    # The binder builder's own summary line is the one thing worth carrying up
    # into this report. Its full report is in its own log, which the line that
    # follows points at.
    outcome = ""
    for line in output.splitlines():
        if line.startswith("Result:"):
            outcome = line[len("Result:"):].strip()
    if not outcome:
        outcome = "no result line in its output"

    if result.returncode != 0:
        return (Event("ERROR", folder,
                      "binder builder exited {}: {}"
                      .format(result.returncode, outcome)),
                "ran and FAILED (exit {}) - {}"
                .format(result.returncode, outcome))

    return (Event("BINDER", folder, "binder builder run: {}".format(outcome)),
            "triggered - {}".format(outcome))


# ---------------------------------------------------------------------------
# Folder naming check
# ---------------------------------------------------------------------------
# Advisory only. It reports, it never renames, and it never changes the exit
# code. A misspelled underscore folder is skipped by every tool in this family
# for the same reason a correctly spelled one is, so it does no damage - but it
# silently splits a convention in two, and the only way that gets noticed is if
# something says so.

def check_folder_naming(documentation_root):
    """
    Find folders whose names are near-misses of a convention name.

    Returns a list of (path relative to the root, the name it probably meant).

    Only folders whose names begin with an underscore are considered, which is
    the class every convention name belongs to.
    """
    findings = []
    for dirpath, dirnames, _filenames in os.walk(documentation_root):
        for name in sorted(dirnames):
            lowered = name.lower()
            # Only underscore folders are candidates. Every convention name is
            # one, and the restriction is what keeps an ordinary folder out of
            # the summary: "file-update-package", the master folder of this very
            # tool, scores 0.86 against "_fileupdatepackages" on similarity
            # alone and is obviously not a misspelling of it.
            if not lowered.startswith("_"):
                continue
            if lowered in CONVENTION_FOLDER_NAMES:
                continue
            close = difflib.get_close_matches(
                lowered, CONVENTION_FOLDER_NAMES, n=1,
                cutoff=NAMING_SIMILARITY)
            if close:
                folder = Path(dirpath) / name
                findings.append(
                    (relative_to(folder, documentation_root), close[0]))
    return findings


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def count_kinds(events):
    """How many of each kind of event, for the summary line and the totals."""
    counts = {}
    for event in events:
        counts[event.kind] = counts.get(event.kind, 0) + 1
    return counts


def build_completion_summary(events, outcome, dry_run):
    """
    The block that holds the window open, as a list of lines.

    This is the primary output of the tool. Someone who reads nothing else
    should be able to tell from these lines whether the deploy did what they
    expected, and if it did not, which file was involved and why.
    """
    counts = count_kinds(events)
    deployed = counts.get("DEPLOYED", 0) + counts.get("WOULD DEPLOY", 0)
    created = counts.get("CREATED", 0) + counts.get("WOULD CREATE", 0)
    superseded = counts.get("SUPERSEDED", 0) + counts.get("WOULD SUPERSEDE", 0)
    conflicts = [event for event in events if event.kind == "CONFLICT"]
    errors = [event for event in events if event.kind == "ERROR"]
    invalid = [event for event in events if event.kind == "INVALID"]

    def row(label, value):
        return "  {:<22}{}".format(label, value)

    lines = []
    lines.append("=" * 72)
    lines.append("COMPLETION SUMMARY{}".format(
        "   (DRY RUN - nothing was changed)" if dry_run else ""))
    lines.append("-" * 72)

    if outcome.package is None:
        lines.append(row("package:", "none - nothing to deploy"))
    else:
        lines.append(row("package:", outcome.package.name))
        if outcome.description:
            lines.append(row("", outcome.description))

    lines.append(row("files updated:", deployed))
    lines.append(row("files created:", created))
    lines.append(row("files superseded:", superseded))

    lines.append(row("conflicts:", len(conflicts)))
    for event in conflicts:
        lines.append("    - {}".format(event.detail))

    lines.append(row("errors:", len(errors)))
    for event in errors:
        lines.append("    - {}".format(event.detail))

    # A rejected package is not an error in the tool - nothing was attempted
    # and nothing failed - so it is counted separately from one, and the row
    # only appears when there is something to say.
    if invalid:
        lines.append(row("package rejected:",
                         "nothing in it was deployed"))
        for event in invalid:
            lines.append("    - {}".format(event.detail))

    lines.append(row("user instructions:", outcome.instructions))
    lines.append(row("binder builder:", outcome.binder))
    lines.append(row("the package is now:", outcome.package_state))

    # The naming check speaks here and nowhere else. It is advisory: it names
    # what it found and leaves the decision to a person.
    if outcome.naming:
        lines.append(row("folder naming:",
                         "{} folder(s) close to a convention name but not "
                         "matching it".format(len(outcome.naming))))
        for found, expected in outcome.naming:
            lines.append("    - {}  (expected \"{}\")".format(found, expected))
    else:
        lines.append(row("folder naming:", "no misspelled folders found"))

    lines.append("-" * 72)

    # The final status line. Note that conflicts count as errors here: the
    # deploy did not do everything the package asked for, and saying otherwise
    # on the one line most likely to be read alone would be a lie of omission.
    # Did every file the manifest asked for actually land?
    complete = (outcome.entry_count > 0
                and deployed + created == outcome.entry_count
                and not conflicts)

    if errors or conflicts or invalid:
        if deployed + created == 0:
            status = "FAILED - nothing was deployed"
        elif complete:
            status = ("COMPLETED WITH ERRORS - every file was deployed, but a "
                      "later step failed")
        else:
            status = "COMPLETED WITH ERRORS - the deploy is incomplete"
    elif outcome.package is None:
        status = "COMPLETED SUCCESSFULLY - there was nothing to do"
    elif dry_run:
        status = "COMPLETED SUCCESSFULLY - dry run, nothing was changed"
    else:
        status = "COMPLETED SUCCESSFULLY"

    lines.append(status)
    lines.append("=" * 72)
    return lines


def build_report(settings_path, documentation_root, drop_folder, dry_run,
                 events, outcome):
    """
    Build the run report as a list of lines.

    One function produces both the on-screen report and the log entry, so the
    two can never drift apart.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = "DRY RUN (nothing changed)" if dry_run else "LIVE"

    lines = []
    lines.append("=" * 72)
    lines.append("file update package   {}   {}".format(timestamp, mode))
    lines.append("documentation root: {}".format(documentation_root))
    lines.append("settings:           {}".format(settings_path))
    lines.append("drop folder:        {}".format(drop_folder))
    if outcome.package is not None:
        lines.append("package:            {}".format(outcome.package_line))
        if outcome.description:
            lines.append("description:        {}".format(outcome.description))
    lines.append("-" * 72)

    if not events:
        lines.append("Nothing happened, which should not be possible - please "
                     "report this.")
    else:
        # Events are reported in the order they happened rather than sorted:
        # a deploy is a sequence, and a supersession followed by the write that
        # depended on it reads as one story. The folder heading still changes
        # as the run moves through the tree.
        current_folder = None
        for event in events:
            if event.folder != current_folder:
                current_folder = event.folder
                lines.append("")
                lines.append("[{}]".format(
                    relative_to(event.folder, documentation_root)))
            lines.append("  {:<17} {}".format(event.kind, event.detail))

    counts = count_kinds(events)
    summary = ", ".join(
        "{} {}".format(counts[kind], kind.lower())
        for kind in REPORT_KINDS if kind in counts
    ) or "nothing to do"

    lines.append("")
    lines.append("-" * 72)
    lines.append("Result: {}".format(summary))
    lines.extend(build_completion_summary(events, outcome, dry_run))
    return lines


def append_to_log(log_path, lines):
    """
    Append one entry to the log. The log is never rewritten or trimmed.

    Failing to write the log must not lose the report that is already on
    screen, so a problem here is reported and swallowed.
    """
    try:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        # "a" is append mode: the file is created if absent, and writes always
        # go to the end. newline="\n" leaves line endings to us, so the log
        # looks the same on every platform.
        with open(log_path, "a", encoding="utf-8", newline="\n") as log_file:
            log_file.write("\n".join(lines))
            log_file.write("\n\n")
        return True
    except OSError as error:
        print("WARNING: could not write the log file {}: {}"
              .format(log_path, error))
        return False


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def pause_before_exit():
    """
    Hold the console open so a double-clicked run can be read.

    Skipped when there is no interactive console attached - otherwise a
    scheduled or piped run would hang forever waiting for a keypress.
    """
    if not sys.stdin or not sys.stdin.isatty():
        return
    try:
        input("\nPress Enter to close...")
    except (EOFError, KeyboardInterrupt):
        pass


def run(dry_run):
    """The whole job. Returns an exit code: 0 for success, 1 for a problem."""
    settings_path = SCRIPT_DIR / SETTINGS_FILENAME

    try:
        settings = load_settings(settings_path)

        # The documentation root is resolved first, because "~/" in the other
        # settings is measured from it.
        documentation_root = resolve_one_folder(
            tidy_setting_text(settings.get("documentation_root", ".."),
                              "documentation_root"),
            "documentation_root",
        )
        drop_folder = resolve_one_folder(
            tidy_setting_text(settings.get("drop_folder",
                                           "~/_fileupdatepackages"),
                              "drop_folder"),
            "drop_folder", root=documentation_root,
        )
        binder_setting = str(settings.get("binder_builder",
                                          "~/_tools/binder_builder.py")).strip()
        binder_path = None
        if binder_setting:
            binder_path = resolve_one_folder(
                tidy_setting_text(binder_setting, "binder_builder"),
                "binder_builder", root=documentation_root,
            )
        log_path = resolve_one_folder(
            tidy_setting_text(settings.get("log_file",
                                           "file_update_package.log"),
                              "log_file"),
            "log_file", root=documentation_root,
        )
    except ValueError as error:
        print("SETTINGS PROBLEM")
        print(error)
        return 1

    if not documentation_root.is_dir():
        print("SETTINGS PROBLEM")
        print('The "documentation_root" setting does not point at a folder '
              "that exists:")
        print("  {}".format(documentation_root))
        print("  (from settings file {})".format(settings_path))
        return 1

    events = []
    outcome = Outcome()
    # The naming check runs on every run, package or no package. It is the one
    # thing here that reports on the tree rather than on the deploy, and a run
    # that found nothing to deploy is as good a moment to mention it as any.
    outcome.naming = check_folder_naming(documentation_root)

    packages = find_packages(drop_folder)

    if not packages:
        events.append(Event(
            "SKIPPED", drop_folder,
            "no packages found in {}".format(
                drop_folder if drop_folder.is_dir()
                else "{} (the folder does not exist)".format(drop_folder))
        ))
        return finish(events, outcome, settings_path, documentation_root,
                      drop_folder, dry_run, log_path)

    package = packages[0]
    outcome.package = package
    # Described now, while it is still where it was found: by the time the
    # report is built the package may have been moved into _superseded.
    outcome.package_line = describe_package(package)
    # Only the newest is processed. Batching packages would mean deciding what
    # to do when the third of five conflicts, and the answer to that is a
    # person looking at the report - so the rest simply wait their turn.
    for waiting in packages[1:]:
        events.append(Event(
            "SKIPPED", drop_folder,
            "{}: waiting - only the newest package is processed in a run"
            .format(waiting.name)
        ))

    # --- validate ---------------------------------------------------------
    if not zipfile.is_zipfile(package):
        events.append(Event("INVALID", drop_folder,
                            "{} is not a zip file".format(package.name)))
        return finish(events, outcome, settings_path, documentation_root,
                      drop_folder, dry_run, log_path)

    try:
        archive = zipfile.ZipFile(package)
    except (zipfile.BadZipFile, OSError) as error:
        events.append(Event("INVALID", drop_folder,
                            "{} could not be opened: {}"
                            .format(package.name, error)))
        return finish(events, outcome, settings_path, documentation_root,
                      drop_folder, dry_run, log_path)

    with archive:
        names = set(archive.namelist())
        manifest, problems = read_manifest(archive, names)

        if problems:
            # Validation is a gate: a package that is wrong in one place is not
            # deployed in the places it happens to be right.
            for problem in problems:
                events.append(Event(
                    "INVALID", drop_folder,
                    "{}: {}".format(package.name, problem)))
            return finish(events, outcome, settings_path, documentation_root,
                          drop_folder, dry_run, log_path)

        outcome.description = manifest.description
        outcome.entry_count = len(manifest.entries)

        # --- the gate -----------------------------------------------------
        if manifest.user_instructions:
            outcome.instructions = acknowledge_instructions(
                manifest.user_instructions, dry_run)

        # --- deploy -------------------------------------------------------
        for entry in manifest.entries:
            events.extend(deploy_entry(archive, entry, documentation_root,
                                       dry_run))

    counts = count_kinds(events)
    wrote_something = any(counts.get(kind) for kind in
                          ("DEPLOYED", "WOULD DEPLOY",
                           "CREATED", "WOULD CREATE"))
    incomplete = bool(counts.get("CONFLICT") or counts.get("ERROR"))

    # --- the binder builder ----------------------------------------------
    if binder_path is None:
        outcome.binder = "not triggered - no binder_builder set in settings"
    elif not wrote_something:
        outcome.binder = "not triggered - no files were deployed"
    else:
        event, phrase = trigger_binder_builder(binder_path, dry_run)
        events.append(event)
        outcome.binder = phrase

    # --- file the package away -------------------------------------------
    # A partial deploy leaves the package in the drop folder. Whoever sorts the
    # conflict out needs the package still to hand, and a package filed under
    # _superseded reads as one that was fully applied.
    if incomplete:
        outcome.package_state = ("left in the drop folder - the deploy was "
                                 "not complete")
    elif not wrote_something:
        outcome.package_state = "left in the drop folder - nothing was deployed"
    else:
        event = supersede(package, dry_run)
        if event.kind in ("SUPERSEDED", "WOULD SUPERSEDE"):
            event = Event(
                "WOULD PROCESS" if dry_run else "PROCESSED", drop_folder,
                "{} -> {}/".format(package.name, SUPERSEDED_FOLDER_NAME))
            outcome.package_state = "{}moved to {}/".format(
                "would be " if dry_run else "", SUPERSEDED_FOLDER_NAME)
        else:
            outcome.package_state = ("left in the drop folder - it could not "
                                     "be moved")
        events.append(event)

    return finish(events, outcome, settings_path, documentation_root,
                  drop_folder, dry_run, log_path)


def finish(events, outcome, settings_path, documentation_root, drop_folder,
           dry_run, log_path):
    """
    Report, log, and return the exit code.

    Every path out of run() comes through here, so a run that stopped at
    validation produces the same shaped report - and the same completion
    summary - as one that deployed twenty files.
    """
    lines = build_report(settings_path, documentation_root, drop_folder,
                         dry_run, events, outcome)
    print("\n".join(lines))

    # Dry runs are logged too, clearly marked, so the log is a complete record
    # of every time the tool was pointed at the tree.
    append_to_log(log_path, lines)
    print("\nLog: {}".format(log_path))

    # Exit code follows the sibling tools: 0 unless something refused. Note the
    # consequence, which is stated in the design document: a CONFLICT and an
    # INVALID package both exit 0, because nothing failed - the tool did
    # exactly what it should with what it was given. The completion summary is
    # where a person reads that, and it says FAILED in plain words.
    return 1 if any(event.kind == "ERROR" for event in events) else 0


def main():
    parser = argparse.ArgumentParser(
        description="Deploy a FileUpdatePackage into the documentation tree. "
                    "Reads its settings from {} beside the script."
                    .format(SETTINGS_FILENAME)
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",  # present = True, absent = False
        help="report what would be deployed without changing anything",
    )
    args = parser.parse_args()

    try:
        exit_code = run(args.dry_run)
    except KeyboardInterrupt:
        print("\nInterrupted.")
        exit_code = 1

    pause_before_exit()
    return exit_code


# When Python runs a file directly, it sets __name__ to "__main__". This guard
# is the conventional way to say "only do this when run, not when imported".
if __name__ == "__main__":
    sys.exit(main())
<!-- END SOURCE: Infrastructure/file-update-package/file_update_package.py -->

---

<!-- BEGIN SOURCE: Infrastructure/file-update-package/file_update_package_settings.json -->
{
  "_comment": "Settings for the file update package deployer. Edit the values below. Any key starting with _comment is ignored by the tool - JSON has no comment syntax, so notes live in keys like this one.",

  "_comment_documentation_root": "The root of the document tree packages are deployed into. Manifest paths are measured from here. A relative path is resolved against the folder this script lives in, so \"..\" means the parent folder - which is what an instance sitting in _tools wants. Give a full path such as \"C:/Users/you/Documents\" to point somewhere else. Forward slashes are safe on Windows. This setting cannot use \"~/\", because \"~/\" means \"measured from the documentation root\" and this is the setting that defines it.",
  "documentation_root": "..",

  "_comment_paths": "The three settings below accept three kinds of path. ABSOLUTE - \"C:/Docs/_fileupdatepackages\". ROOT-ANCHORED - \"~/_fileupdatepackages\" - measured from the documentation root above. RELATIVE - \"_fileupdatepackages\" - measured from the folder this script lives in. Note that ~ means the documentation root here, never your home folder.",

  "_comment_drop_folder": "Where packages are put to be deployed. The newest unprocessed .zip in this folder is the one that gets processed; the rest wait. Processed packages are moved into a _superseded subfolder of it.",
  "drop_folder": "~/_fileupdatepackages",

  "_comment_binder_builder": "The binder builder script to run after a deploy. Point this at the running instance, not at the master copy, so it uses that instance's settings. Set it to \"\" to skip the trigger entirely.",
  "binder_builder": "~/_tools/binder_builder.py",

  "_comment_log_file": "Where the run log is appended. One entry per run, never overwritten. Absolute, or \"~/\" for root-anchored, or relative to the script folder.",
  "log_file": "file_update_package.log"
}
<!-- END SOURCE: Infrastructure/file-update-package/file_update_package_settings.json -->

---

<!-- BEGIN SOURCE: Infrastructure/file-update-package/FileUpdatePackage_Design_v1.md -->
# FileUpdatePackage Deployer — Design

> **Version 1** (2026-09-07). First issue. Third tool in the Infrastructure family, after version
> cleanup and the binder builder, and the one that closes the loop: it takes the output of a Chat or
> Cowork session and puts it into the master tree.

**Master/source folder:** `Documentation/Infrastructure/file-update-package`
**Run from:** a copied instance folder with its own settings and log, e.g. `Documentation/_tools`

---

## Contents

- **Objective and boundary** — what it does and what it deliberately doesn't.
- **Inputs** — the settings file, and the package format.
- **Path logic** — absolute, root-anchored and script-relative forms.
- **Processing model** — find, validate, gate, deploy, trigger, file away.
- **Execution behaviour** — live by default, dry run, double-click, the completion summary.
- **Folder naming check** — advisory, and why it is here.
- **Definition of done.**
- **Decisions** — with reasons.

---

## 1. Objective and boundary

**Objective.** Deploy a FileUpdatePackage — a zip of updated documents produced by a Chat or Cowork
session — into the master document tree, superseding what it replaces, and leave the user in no
doubt about what happened.

**Boundary — hard.** It places whole files. It does **not** merge, patch or edit content, it does
not decide what belongs in a package, and it does not do general version resolution — it moves the
single document each manifest entry names, and nothing else. It is Infrastructure: it acts on the
corpus and is never loaded into an AI session itself.

**It never overwrites.** A file already sitting where a package wants to write, and not named as
the one being replaced, is a `CONFLICT`: reported, skipped, left exactly as it was.

**Shape.** A single-action tool, sibling to version cleanup and the binder builder. No actions
framework, no shared base class, no plugin system.

**Pipeline position.**

```text
(a session produces a package)
        ↓
file update package  →  binder builder
```

The deployer triggers the binder builder itself, so a deploy leaves the binder current. Version
cleanup remains a separate, human-run pass over the tree: the deployer supersedes only what a
manifest names.

---

## 2. Inputs

### 2.1 The settings file

JSON, read on launch, from the script's own folder.

| Setting | Purpose |
|---|---|
| `documentation_root` | The root of the tree packages deploy into. Manifest paths are measured from here, and it is the anchor for `~/` in the other settings. |
| `drop_folder` | Where packages are put to be deployed. Default `~/_fileupdatepackages`. |
| `binder_builder` | The binder builder script to run after a deploy. Point it at the **running instance**, not the master, so it uses that instance's settings. Empty string skips the trigger. |
| `log_file` | Log file location. Named to match both siblings. |

The script writes a commented default settings file if none is present, rather than failing.

### 2.2 The package

A zip file carrying documents at their paths relative to the documentation root, plus a manifest at
the zip root:

```json
{
  "created": "2026-09-07T10:00:00Z",
  "description": "Project Design master files — binder sweep complete",
  "files": [
    {
      "path": "Project Design/ProjectDesign_Design_v8.md",
      "action": "update",
      "replaces": "ProjectDesign_Design_v7.md"
    },
    { "path": "Project Design/ProjectDesign_Index_v8.md", "action": "create" }
  ],
  "user_instructions": "Review the new Overview document before publishing."
}
```

| Field | Meaning |
|---|---|
| `path` | Where the file goes, relative to the documentation root, forward slashes. |
| `action` | `create` — the file is new. `update` — it replaces an existing document. |
| `replaces` | *Update only, optional.* The **filename** of the document being superseded. The tool finds it and moves it to `_superseded`. Omitted, an update supersedes the file at its own `path` — see D4. |
| `description` | Optional. Shown in the report header and the completion summary. |
| `user_instructions` | Optional. Shown to the user, who must acknowledge before the deploy proceeds. |
| `created` | Optional, informational. The tool orders packages by filesystem modification time, not by this field. |

**`Documentation/_config/repo_config.json`** maps topic names to folder paths for whoever is
*building* a package. The tools do not read it; they have their own settings.

---

## 3. Path logic

The same three forms as the sibling tools, ratified as the Infrastructure-wide convention
(version-cleanup/claude-code/001, 2026-09-04):

| Form | Example | Meaning |
|---|---|---|
| **Absolute** | `C:/…/Documentation/_fileupdatepackages` | Exact folder. |
| **Root-anchored** | `~/_fileupdatepackages` | Measured from `documentation_root`. |
| **Script-relative** | `..` | Measured from the folder holding the script. |

`documentation_root` itself cannot use `~/`, because it is what `~/` means — the same rule and the
same error message as `root` in both siblings. See D2.

**The folder-relative *pattern* form does not appear here.** In the siblings it exists for `include`
and `exclude`, which describe *classes* of folder across a tree. This tool has no such setting:
every path names one place. Nothing is missing — there is nowhere for a pattern to apply.

`~` never means the home folder. Home expansion is not performed anywhere in these settings.

**Manifest paths are not settings paths.** They come from an untrusted zip and are checked
separately and harder — see §4.2.

---

## 4. Processing model

1. Resolve settings; resolve `documentation_root`.
2. Run the folder naming check over the tree (§6).
3. Find every `.zip` in the top level of the drop folder. None → `SKIPPED`, exit `0`.
4. Take the **newest by modification time**. Report the rest as `SKIPPED` — waiting, not processed.
5. Validate the package as a whole (§4.1). Any problem → `INVALID`, nothing is deployed.
6. If the manifest carries `user_instructions`: show them and wait for acknowledgement (§4.3).
7. For each manifest entry in order (§4.4): supersede what it replaces, then write the new file.
8. Trigger the binder builder (§4.5), unless nothing was written.
9. Move the package into `_superseded` inside the drop folder — **only if the deploy was complete**.
10. Report, log, print the completion summary, hold the window open.

### 4.1 Validation is a gate, not a filter

A package deploys as a whole or is rejected as a whole. Rejected for: not a zip; no `_manifest.json`;
a manifest that is not valid JSON or not an object; no `files` list; an entry with no usable `path`;
an `action` that is not `create` or `update`; `replaces` on a create; `replaces` containing a folder
separator; the same destination listed twice; and — the important one — **a manifest naming a file
the zip does not contain**.

A package that is wrong in one place is not deployed in the places it happens to be right. Deploying
the good half of a badly-built package leaves the tree in a state nobody designed, and leaves the
session that built it believing its work landed.

### 4.2 Package paths are untrusted input

Every manifest `path` is checked before it is used: no absolute paths, no drive letters, no `..`
segment, no trailing separator, not empty. The resolved destination is then checked again to be
inside the documentation root, which catches the case a purely textual check cannot — a symbolic
link in the tree carrying a well-formed relative path somewhere else entirely.

Files are written from `zipfile.read()` into a validated destination rather than with
`ZipFile.extract()`, which derives the destination from the member name.

### 4.3 The user instructions gate

If the manifest carries `user_instructions`, they are printed in a banner and the tool waits for
Enter **before anything is written**. Stopping there — Ctrl+C — stops a deploy that has not started,
rather than one that is half done.

The wait is skipped, and the summary says so in those words, when there is no interactive console.
A run triggered by another tool must not block forever on a keypress nobody is there to press. This
is the same reasoning as the exit pause in both siblings.

### 4.4 One entry, in order

| Step | Behaviour |
|---|---|
| **Find what it replaces** | Beside the new file first — v7 and v8 of one document live in the same folder — then the rest of the tree, skipping `_superseded` folders throughout. |
| **Found once** | Move it into `_superseded` beside itself. `SUPERSEDED`. |
| **Not found** | `SKIPPED`, naming it. The new file still deploys. |
| **Found more than once** | `CONFLICT`, naming every place. **Nothing is moved** — see D5. The new file still deploys. |
| **Destination taken** | `CONFLICT`. Nothing is written and nothing is overwritten, ever. |
| **Otherwise** | Write the file. `DEPLOYED` for an update, `CREATED` for a create. |

An update whose predecessor sits at the destination itself clears its own way: the supersession
moves it, and the never-overwrite check that follows is then a genuine test rather than a formality.
A dry run reports this correctly rather than reporting a conflict against a file it would itself
have moved.

### 4.5 The binder builder trigger

Run unconditionally after any deploy that wrote something, with no arguments, in live mode. The
binder builder's own change detection (BinderBuilder_Design_v4 §4a) decides whether a rebuild is
actually needed, so this tool does not have to know or care.

`stdin` is closed rather than inherited, which is what stops the binder builder pausing for a
keypress at the end of its own run. Its `Result:` line is carried up into this report; its full
report is in its own log.

**Best-effort.** The deploy has already happened by the time this runs. A binder builder that is
missing, that will not start, that exits non-zero or that runs past its timeout is reported as an
`ERROR` on that step and the deploy stands — including the package being filed away, because the
files did land.

### 4.6 Partial deploys keep their package

A run with any `CONFLICT` or file-level `ERROR` leaves the package in the drop folder. Whoever sorts
the conflict out needs the package still to hand, and a package sitting under `_superseded` reads as
one that was fully applied. The report says which files landed and which did not.

---

## 5. Execution behaviour

Matches both siblings, so the three tools behave alike:

- Python, standard library only, single readable script.
- Runs **live by default**; `--dry-run` reports what would be deployed and changes nothing.
- Reads settings on launch — no arguments required, so **double-click works on Windows**.
- Appends one entry per run to the log, dry runs included and marked.
- Cross-platform; Windows primary.

### Report vocabulary

`DEPLOYED` / `WOULD DEPLOY` · `CREATED` / `WOULD CREATE` · `SUPERSEDED` / `WOULD SUPERSEDE` ·
`CONFLICT` · `SKIPPED` · `INVALID` · `BINDER` · `PROCESSED` / `WOULD PROCESS` · `ERROR`

`CONFLICT` and `ERROR` carry version cleanup's meanings exactly. `SKIPPED` covers both nothing-to-do
cases: no packages at all, a package waiting its turn, and a `replaces` that names nothing in the
tree. `INVALID` is §4.1 — the package was rejected and nothing in it was deployed.

**Events are reported in the order they happened**, not sorted, unlike both siblings. A deploy is a
sequence: a supersession and the write that depended on it read as one story. The folder heading
still changes as the run moves through the tree.

### The completion summary

The primary output, not an afterthought. Every run ends with it, whatever happened, and the window
stays open until it has been read:

```text
========================================================================
COMPLETION SUMMARY
------------------------------------------------------------------------
  package:              good.zip
                        Project Design master files - binder sweep complete
  files updated:        1
  files created:        1
  files superseded:     1
  conflicts:            0
  errors:               0
  user instructions:    present, shown and acknowledged
  binder builder:       triggered - 24 included, 1 written, 1 superseded
  the package is now:   moved to _superseded/
  folder naming:        1 folder(s) close to a convention name but not matching it
    - _superceded  (expected "_superseded")
------------------------------------------------------------------------
COMPLETED SUCCESSFULLY
========================================================================
```

Every conflict and every error is listed individually with its filename and reason. The final line
is one of:

| Status | When |
|---|---|
| `COMPLETED SUCCESSFULLY` | No conflicts, no errors. Also the "nothing to do" case, and a clean dry run. |
| `COMPLETED WITH ERRORS - every file was deployed, but a later step failed` | The files landed; something after them did not — in practice, the binder builder. |
| `COMPLETED WITH ERRORS - the deploy is incomplete` | Some files landed and some did not. |
| `FAILED - nothing was deployed` | An `INVALID` package, or every entry conflicted. |

**Exit code `0` unless an `ERROR` occurred**, matching both siblings. Note the consequence, stated
so it is not later read as a defect: a `CONFLICT` and an `INVALID` package both exit `0`, because
nothing failed — the tool did exactly what it should with what it was given. See §8.

---

## 6. Folder naming check

Every run, before anything else, walks the documentation root and reports any folder whose name is a
near-miss of a convention name — `_superseded`, `_fileupdatepackages`, `_binder`, `_tools`,
`_config`, `_rebuild` — using a similarity threshold rather than a fixed list of misspellings.

**Only underscore folders are candidates.** Every convention name is one, and the restriction is
what keeps the check honest: `Infrastructure/file-update-package`, the master folder of this very
tool, scores above the threshold against `_fileupdatepackages` on similarity alone and is plainly
not a misspelling of it. A summary that cries wolf stops being read.

**It is advisory.** It never renames anything, never blocks a deploy, and never changes the exit
code. It speaks in the completion summary and nowhere else.

It is here because a misspelled underscore folder is invisible to every tool in this family: they
all skip underscore folders, so `_superceded` does no damage and produces no complaint — it just
quietly splits a convention in two, and stays split until something says so. The known instance is
`Documentation/_superceded`, recorded in BinderBuilder_Design_v3 §10 and deliberately left alone;
reconciling it is a human act. Naming it on every run is how it stops being forgotten. See D7.

---

## 7. Definition of done

Drop a well-formed package into the drop folder and run the tool. Each `update` supersedes the
document it names and lands in its place; each `create` lands where it should; nothing anywhere is
overwritten. Instructions in the package are shown and acknowledged before any file is touched. The
binder builder runs afterwards and its outcome is reported. The package is moved to `_superseded`.
The completion summary states, without the user having to interpret anything, how many files were
updated, created and superseded, every conflict and error with its filename and reason, whether the
binder was rebuilt, and a final status line — and the window stays open until it is read.

A dry run reports all of that and changes nothing.

An empty drop folder reports `SKIPPED` and exits `0`. A package that is not a zip, has no manifest,
has an unparseable manifest, or names a file it does not contain, is rejected whole — `INVALID`,
nothing deployed, the package left where it is. A path containing `..` never writes outside the
documentation root. A partial deploy names what landed and what did not, and keeps its package. A
misspelled convention folder anywhere in the tree is named in the summary.

---

## 8. Decisions

**D1 — A third tool, not a mode of an existing one.** Deploying is a different job from tidying
versions and from assembling a binder, and it is the only one of the three that takes an external
input. The three run in sequence and share nothing but conventions.

*Consequence, accepted:* the path logic now exists in three implementations. The trigger for
extracting shared code was stated in BinderBuilder_Design_v3 §10 as "a third tool needing it" — and
this is that third tool. It is still not extracted: this tool needs only the one-place resolver,
about forty lines of pure functions over paths with no state, and not the pattern matching that
makes up the bulk of the siblings' path code. A shared module carrying two thirds dead weight for
each importer is worse than the copy. **Re-examine when a fourth tool arrives, or when any tool needs
the pattern form changed.**

**D2 — `documentation_root` cannot use `~/`.** The tool-pipeline brief proposed
`"documentation_root": "~/"`. Rejected as circular: `~/` means "measured from the documentation
root", so it cannot appear in the setting that defines that root. Both siblings reject `~/` in
`root` for exactly this reason and say so in an error message. The shipped default is `".."`, which
is what an instance sitting in `_tools` wants, and the setting comment says why.

**D3 — Newest package only; the rest wait.** Batching would mean deciding what to do when the third
of five packages conflicts, and the honest answer is "a person looks at the report". One package per
run keeps the completion summary about one deploy. Waiting packages are reported by name, so nothing
is silently held back.

Ordering is by filesystem modification time rather than by the manifest's `created` field: the field
is written by whatever produced the package and cannot be relied on, and the file's own timestamp is
the fact the drop folder actually carries.

**D4 — `replaces` is optional on an update.** Where it is absent, the entry supersedes the file at
its own `path`. This is the natural reading of "update" for a document whose filename does not carry
a version, and it never overwrites: the existing file is moved to `_superseded` exactly as a named
one would be.

*Considered and rejected:* treating a missing `replaces` as `INVALID`. Rejected because the
resulting behaviour would be worse — a package that plainly means "here is the new version of this
file" would be refused for a field that adds nothing in that case.

**D5 — An ambiguous `replaces` moves nothing.** A filename found in three folders is a question this
tool must not answer by guessing. All three are named in a `CONFLICT`, none is moved, and the new
file still deploys — so the outcome is visible in the tree as well as in the report, and version
cleanup will surface it again on its next pass.

This is version cleanup's `AMBIGUOUS` shape, reported here as `CONFLICT` because the vocabulary for
this tool was fixed at seven words and a near-duplicate would have to earn its place.

**D6 — The binder builder trigger is best-effort, and it is unconditional.** Unconditional because
the binder builder now decides for itself whether a rebuild is needed (v4 §4a); a deployer that
tried to predict that would duplicate the judgement and eventually disagree with it. Best-effort
because the deploy has already happened: a binder that could not be rebuilt is a stale binder, not a
lost document. It is reported as an `ERROR` and the run exits `1`, but the deploy stands and the
package is still filed away.

**D7 — The folder naming check is advisory and lives here.** It could sit in any of the three tools.
It is here because this is the tool that writes *into* the tree at paths a session composed, which
is exactly where a split convention would first do harm — a package built against `_superceded`
would file documents somewhere no tool looks.

It never renames. Renaming a folder is a decision with consequences the tool cannot see, and the
misspelling it will find most often is a known one that has already been left deliberately.

**D8 — `CONFLICT` and `INVALID` exit `0`.** Consistent with both siblings, where the exit code
reports whether the tool failed rather than whether the outcome was the desired one. The completion
summary is the human channel and it says `FAILED` in plain words. Recorded here because the two
channels disagreeing looks like a defect if it is not written down as a choice. See §9.

---

## 9. Open

- **Exit codes for expected-but-unwanted outcomes.** `EMPTY` in the binder builder, and `CONFLICT`
  and `INVALID` here, all exit `0`. A future orchestrator chaining these tools would want to
  distinguish "did nothing" from "did what was asked". Prefer distinct codes over overloading the
  failure code. **Not now** — the only chaining that exists is this tool calling the binder builder,
  and it reads the report rather than the exit code.
- **Package provenance.** The manifest's `created` field is carried but not used, and there is no
  record in the deployed tree of which package a document arrived in. The log has it. Whether that
  is enough is a question for the first time someone asks "where did this file come from".
- **Path-logic duplication.** Three implementations now. See D1 for the trigger to revisit.
- **The `_superceded` misspelling** at the Documentation root remains, and is now reported on every
  deploy rather than only in a design document. Still a human act to reconcile.
<!-- END SOURCE: Infrastructure/file-update-package/FileUpdatePackage_Design_v1.md -->

---

<!-- BEGIN SOURCE: Infrastructure/file-update-package/README.md -->
# file update package

Deploys a **FileUpdatePackage** — a zip of updated documents produced by a Chat
or Cowork session — into the master document tree, superseding what it replaces
and rebuilding the binder afterwards.

This folder is the **master copy**. To use the tool, copy
`file_update_package.py` and `file_update_package_settings.json` to wherever it
should run from, then edit that copy's settings. Each instance keeps its own
settings file and its own log beside the script, so instances never interfere
with each other.

**It never overwrites.** A file already sitting where a package wants to write,
and not named as the one being replaced, is reported as a `CONFLICT` and left
exactly where it is.

---

## What a package looks like

A zip file containing the documents at their paths relative to the
documentation root, plus a manifest called `_manifest.json` at the zip root:

```
ProjectDesign_2026-09-07.zip
├── _manifest.json
└── Project Design/
    ├── ProjectDesign_Design_v8.md
    └── ProjectDesign_Index_v8.md
```

```json
{
  "created": "2026-09-07T10:00:00Z",
  "description": "Project Design master files - binder sweep complete",
  "files": [
    {
      "path": "Project Design/ProjectDesign_Design_v8.md",
      "action": "update",
      "replaces": "ProjectDesign_Design_v7.md"
    },
    {
      "path": "Project Design/ProjectDesign_Index_v8.md",
      "action": "create"
    }
  ],
  "user_instructions": "Review the new Overview document before publishing."
}
```

| Field | Meaning |
| --- | --- |
| `path` | Where the file goes, measured from the documentation root. Forward slashes. |
| `action` | `create` for a new file, `update` for one that replaces an existing document. |
| `replaces` | Update only, optional. The **filename** — not a path — of the document being superseded. The tool finds it and moves it into `_superseded`. |
| `description` | Optional. Shown in the report and the completion summary. |
| `user_instructions` | Optional. Shown to you, and the tool waits for you to acknowledge them before it touches anything. |
| `created` | Optional, informational. Packages are ordered by file modification time, not by this. |

**Leaving `replaces` out of an update** means "this replaces the file already at
this path" — that file is moved into `_superseded` and the new one written in
its place. Use it for documents whose filenames do not carry a version.

`Documentation/_config/repo_config.json` maps topic names to folder paths, for
whoever is *building* a package. The tool does not read it; it has its own
settings.

---

## What it does

1. Finds the newest unprocessed `.zip` in the drop folder. Any others wait their
   turn and are reported by name.
2. Validates the package — a zip, with a manifest, that names files it actually
   contains. Anything wrong and the whole package is rejected: `INVALID`, and
   nothing at all is deployed.
3. Shows the package's instructions, if it has any, and waits for you.
4. For each file: moves the document it replaces into `_superseded`, then writes
   the new one.
5. Runs the binder builder. It decides for itself whether a rebuild is needed.
6. Moves the package into `_superseded` inside the drop folder — but only if the
   deploy was complete.
7. Prints a completion summary and holds the window open until you have read it.

---

## Installing Python on Windows

Only needed once per machine. The tool uses nothing beyond the Python standard
library, so there is nothing else to install.

1. Go to <https://www.python.org/downloads/windows/> and download the latest
   **Windows installer (64-bit)**. Python 3.8 or newer is required; any current
   release is fine.
2. Run the installer. On the first screen, **tick "Add python.exe to PATH"**
   before clicking Install. This is easy to miss and is the usual reason a
   `.py` file will not run afterwards.
3. Choose **Install Now**.

Double-clicking `file_update_package.py` in File Explorer runs it. If it opens
in Notepad instead, right-click it → **Open with** → **Choose another app** →
pick **Python**, and tick **Always use this app to open .py files**.

Or from a terminal:

```
python "C:\path\to\file_update_package.py"
```

---

## Settings

The script reads `file_update_package_settings.json` from **its own folder** —
not from wherever the terminal happens to be pointing. If that file is missing,
the script writes a fresh one with default values and explanatory notes, then
tells you to check it.

```json
{
  "documentation_root": "..",
  "drop_folder": "~/_fileupdatepackages",
  "binder_builder": "~/_tools/binder_builder.py",
  "log_file": "file_update_package.log"
}
```

| Setting | Meaning |
| --- | --- |
| `documentation_root` | The root of the tree packages deploy into. Manifest paths are measured from here. |
| `drop_folder` | Where packages are put to be deployed. |
| `binder_builder` | The binder builder to run afterwards. Point it at the **running instance**, so it uses that instance's settings. Set it to `""` to skip the trigger. |
| `log_file` | Where the run log is appended. |

### The three path forms

| Form | Example | Means |
| --- | --- | --- |
| Absolute | `"C:/Docs/_fileupdatepackages"` | that exact folder |
| Root-anchored | `"~/_fileupdatepackages"` | measured from `documentation_root` |
| Script-relative | `".."` | measured from the folder holding the script |

`"~"` here means **the documentation root**, never your home folder. The tool
never expands `~` the way a shell would.

`documentation_root` cannot itself use `"~/"` — it is what `"~/"` means. Use
`".."`, which is what an instance sitting in a `_tools` folder wants, or a full
path.

This is the same path model as version cleanup and the binder builder,
deliberately. Three Infrastructure tools with different path semantics would be
a trap. (The *pattern* form those two accept in `include` and `exclude` has no
equivalent here: every setting in this tool names one place.)

**Writing paths in JSON.** Use forward slashes (`"C:/Users/you/Documents"`) or
doubled backslashes; a single backslash is an escape character in JSON and will
break the file.

---

## Running it

Live by default — the only prompt is the package's own instructions, if it has
any:

```
python file_update_package.py
```

Report only, changes nothing:

```
python file_update_package.py --dry-run
```

The dry run takes the same decisions as a live run — it validates the package,
works out what would be superseded and what would conflict — and reports them
with `WOULD DEPLOY`, `WOULD CREATE` and `WOULD SUPERSEDE`. It is the safe way to
look at a package you did not build yourself.

---

## The completion summary

This is the point of the run. It is printed whatever happened, and the window
stays open until you have read it:

```
========================================================================
COMPLETION SUMMARY
------------------------------------------------------------------------
  package:              ProjectDesign_2026-09-07.zip
                        Project Design master files - binder sweep complete
  files updated:        1
  files created:        1
  files superseded:     1
  conflicts:            0
  errors:               0
  user instructions:    present, shown and acknowledged
  binder builder:       triggered - 24 included, 1 written, 1 superseded
  the package is now:   moved to _superseded/
  folder naming:        no misspelled folders found
------------------------------------------------------------------------
COMPLETED SUCCESSFULLY
========================================================================
```

Every conflict and every error is listed individually, with the filename and the
reason. The last line is one of:

| Status | When |
| --- | --- |
| `COMPLETED SUCCESSFULLY` | Nothing went wrong. Also the "no packages to deploy" case. |
| `COMPLETED WITH ERRORS - every file was deployed, but a later step failed` | The files landed; something after them did not — in practice the binder builder. |
| `COMPLETED WITH ERRORS - the deploy is incomplete` | Some files landed, some did not. |
| `FAILED - nothing was deployed` | The package was rejected, or every file in it conflicted. |

---

## The report

| Kind | Meaning |
| --- | --- |
| `DEPLOYED` / `WOULD DEPLOY` | An updated file written into place. |
| `CREATED` / `WOULD CREATE` | A file that did not exist before. |
| `SUPERSEDED` / `WOULD SUPERSEDE` | The document being replaced, moved into `_superseded`. |
| `CONFLICT` | A destination is taken, or a `replaces` matched more than one file. Nothing overwritten, nothing moved. |
| `SKIPPED` | No packages to deploy, a package waiting its turn, or a `replaces` naming a file that is not in the tree. |
| `INVALID` | The package was rejected. Nothing in it was deployed. |
| `BINDER` | The binder builder was triggered, and what it said. |
| `PROCESSED` / `WOULD PROCESS` | The package itself, moved into `_superseded`. |
| `ERROR` | A filesystem refusal, or a binder builder run that failed. |

Events appear in the order they happened, so a supersession and the write that
depended on it read as one story. The exit code is `0` unless an `ERROR`
occurred — note that a `CONFLICT` and a rejected package both exit `0`, because
nothing failed: the tool did exactly what it should with what it was given. The
completion summary is where you read the outcome.

### Three cases worth understanding

**`INVALID` — the package was rejected.** Validation is a gate, not a filter. A
package that is wrong in one place is not deployed in the places it happens to
be right, because deploying half of a badly-built package leaves the tree in a
state nobody designed. Fix the package and drop it in again.

**`CONFLICT` — something was in the way.** Either a file already sits where the
package wants to write and the package did not name it as superseded, or a
`replaces` filename was found in several folders and the tool will not guess
which one you meant. Nothing is overwritten and nothing is moved. The run says
exactly which file and why.

**A partial deploy keeps its package.** If anything conflicted, the zip stays in
the drop folder rather than moving to `_superseded` — you will need it when you
sort the conflict out, and a package filed away reads as one that was fully
applied.

---

## The folder naming check

Every run walks the tree and reports any folder whose name is *nearly* one of
the conventions — `_superceded` where `_superseded` was meant, and so on. It
appears in the completion summary and nowhere else.

Only folders whose names start with an underscore are looked at, which is the
class every convention name belongs to. An ordinary folder is never flagged.

It is advisory. It never renames anything, never blocks a deploy and never
changes the exit code.

It exists because a misspelled underscore folder is invisible to every tool in
this family: they all skip underscore folders, so a misspelling does no damage
and raises no complaint — it just quietly splits a convention in two and stays
that way. Naming it on every run is how it stops being forgotten.

---

## The log

Every run appends one entry to the log file, live and dry-run alike, each
stamped with the date and the mode. The entry is the whole report, completion
summary included. The log is never rewritten or trimmed.

---

## Scope

It places whole files. It does not merge, patch or edit content, it does not
decide what belongs in a package, and it does not do general version resolution
— it moves the single document each manifest entry names. Tidying the rest of
the tree is version cleanup's job.
<!-- END SOURCE: Infrastructure/file-update-package/README.md -->

---

<!-- BEGIN SOURCE: Infrastructure/Infrastructure_CLI_Decisions_v1.md -->
Infrastructure — CLI Decisions | decisions | Infrastructure_CLI_Decisions@v1 | 2026-09-10

## Utility registration — convention scanning over alternatives

Three options were on the table: convention-based scanning of a subpackage, a registry file listing available utilities, and decorator-based registration.

Convention scanning was chosen (strong recommendation, agreed). There are three utilities now and likely only a handful more over time. A registry file is a second artefact to maintain for no benefit at this scale — every time a utility is added, the registry must also be updated, which is exactly the kind of coordination step that adds friction without adding value. Decorators add a layer of indirection that buys nothing when everything lives in one package. Convention scanning is the simplest thing that works: drop a module in the folder following the agreed shape, and it appears.

The CLI-growth consideration was raised by Dave: this dispatcher may become the full AIDE CLI. The response was that convention scanning does not paint the design into a corner — a folder of utilities following a shared shape is exactly the foundation a bigger CLI would want. The temptation to pre-build grouping, categories, or a richer interface was explicitly named as the apparatus trap. The consideration is logged but does not drive the current design.

## Settings format — JSON over YAML

The three existing utilities already use JSON settings files. YAML is friendlier to hand-edit but would be a new format to introduce for no demonstrated gain. Matching what is already in use on the project costs nothing and avoids a format split between existing utility settings and the new dispatcher settings.

## Settings merge — deep merge over full replacement

Deep merge means a per-project settings file overrides individual values without needing to restate the surrounding structure. The alternative — full replacement per key — would force a project to copy an entire settings block just to change one value inside it. That is more brittle and harder to keep in step with the global defaults as they evolve.

## Three-layer settings — package defaults separated from user global

The original design had two layers: global settings with the installed package, and per-project overrides. This missed a problem: pip overwrites the package directory on every update, so any user-edited global settings (a custom exclude list, a repo URL override) would be lost on the next `aide update`.

The fix separates immutable package defaults (shipped with the package, never edited) from user-global settings (`~/.aide/settings.json`, survives updates). Per-project remains the third layer. The auto-update state file already lived at `~/.aide/state.json`, so the convention was already established — settings just needed to follow it.

## The `_aide` folder — Dave's initiative

The original proposal placed per-project settings under `_utilities`. Dave pushed back: he wanted the number of root-level operational folders kept lean and preferred one generic home for machine-facing files rather than several purpose-specific ones. The folder would hold settings, logs, and utilities as a subfolder only if needed.

The name `_aide` was chosen over `_system` because it matches the framework name and the existing underscore-prefix convention already established for operational folders (`_index`, `_archived`, `_binders`, `_fileupdatepackages`). The underscore sorts it to the top of the directory listing and signals that it is infrastructure, not content.

## Auto-update frequency — daily over every-launch

Checking on every launch adds a network call and a slight delay each time the dispatcher runs, which gets annoying with frequent use. Once a day catches updates promptly without that friction. The manual `aide update` command is always available for an on-demand check, so the daily cadence never blocks a user who wants to check sooner.

## Auto-update version detection — git tags over commit hashes

The package is installed from a git repository, so git tags are the natural version signal. Commit hashes do not indicate whether a change is meaningful — a documentation-only commit and a breaking change look the same. Release tags carry explicit version semantics.

## Auto-update offline behaviour — graceful skip over retry

Dave asked specifically about the retry model. The decision was: no retry loop, no background process, no machinery. If the daily check fails because the network is unreachable, the dispatcher does not update the "last checked" timestamp. The next launch sees the check is still due and tries again naturally. Offline means "still due," not "retry now." This keeps the auto-update behaviour proportionate — a single quiet check, never a blocker.

## Include/exclude form — deny list over allow list

By default, every utility the dispatcher discovers is available. To hide one, name it in an exclude list. The alternative — an allow list where every utility must be explicitly enabled — means that adding a new utility requires updating every project's settings to make it visible. That contradicts the low-fuss spirit of convention scanning: a new module in the subpackage should just work everywhere unless deliberately turned off.

## Include/exclude as a settings concern, not a registration concern

Registration discovers everything that exists in the subpackage. Settings decide what is shown. Mixing the two — having registration itself honour include/exclude rules — would mean the dispatcher's scanning logic needs to know about settings before it has finished loading them. Keeping the concerns separate is both simpler and more predictable: scan first, filter second.

## Include/exclude scope — both global and per-project

This rides on the deep-merge settings model already settled. A global exclude hides a utility everywhere. A per-project exclude hides it for that project only. A per-project override can also restore a globally excluded utility. No new mechanism — it is just another setting following the same merge rules.

---

Version note: v1 — reasoning from voice session 2026-09-10. All four items were settled in conversation; this document records the alternatives considered and the reasons for each choice.
<!-- END SOURCE: Infrastructure/Infrastructure_CLI_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: Infrastructure/Infrastructure_CLI_Design_v1.md -->
Infrastructure — CLI Design | design | Infrastructure_CLI_Design@v1 | 2026-09-10

## Summary

The `aide` command is the single entry point to AIDE's infrastructure utilities. It is a Python package distributed via pip from a git repository, installed as a console entry point so that `aide` is available on PATH. On launch it scans for available utilities, applies settings, and presents an interactive menu. Each utility can also be invoked directly as a subcommand.

This document specifies four things: how utilities are discovered, how settings work, how the tool keeps itself current, and how individual utilities can be included or excluded. It is the handoff to a Code session for the build.

Infrastructure owns this design. The individual utility designs (the binder builder, the file-update packager, version cleanup) live with their owning area — File Operations in Working Practices.

---

## Distribution and entry point

The `aide` package is a standard Python package hosted in a git repository and installed with pip. A `console_scripts` entry point registers `aide` as a command, so it is available on PATH after installation.

No PyPI publication. The install source is the git repository directly.

---

## Utility registration

Utilities live as modules in a `utilities/` subpackage inside the `aide` package. The dispatcher scans this subpackage at startup and picks up every module that follows the standard shape:

- A `name` attribute — the display name shown in the menu and used as the subcommand.
- A `description` attribute — a short line shown alongside the name.
- A `run` function — the entry point the dispatcher calls.

Any module in the subpackage that exposes these three things is a utility. No separate registration step, no manifest, no decorator — presence in the subpackage and conformance to the shape is registration.

The three existing utilities each become a module in this subpackage following this shape: the binder builder, the file-update packager, and version cleanup. Their internal logic is unchanged; only the entry point is standardised.

**Consideration noted:** this dispatcher may grow into the full AIDE CLI later, but the design does not anticipate that. The registration model is simple enough to extend if that direction is taken, without needing to be redesigned for it now.

---

## Interactive menu and subcommand support

When invoked without arguments, `aide` presents an interactive menu listing every registered utility by name and description. The user selects one and it runs.

When invoked with a utility name as a subcommand (e.g. `aide binder`), the dispatcher calls that utility's `run` function directly, bypassing the menu. This supports both interactive use and scripting.

The auto-update check (described below) and the manual update command are also available through the menu and as subcommands.

---

## Per-project batch launcher

When invoked from within a project that has an `_aide/` folder, the dispatcher can run a defined sequence of utilities in order. The batch configuration lives in the project settings file. This supports common workflows — for example, running version cleanup, the binder builder, and a git commit in sequence.

---

## Settings

### Format

JSON. This matches the format already used by the existing utility settings files.

### Locations

Three levels, each overriding the one before:

- **Package defaults** live with the installed package. Immutable — shipped as part of the package and overwritten on every update. Never edited by the user.
- **User global** live at `~/.aide/settings.json` (on Windows, `C:\Users\<user>\.aide\`). The user's own global settings — their exclude list, repo URL, anything they want everywhere. Survives updates. Created on first use if absent; skipped silently if missing.
- **Per-project settings** live under `_aide/` at the documentation root of the project. These override both layers above for work in that project.

### Merge behaviour

Deep merge at each layer. Package defaults are merged with user-global settings, then the result is merged with per-project settings. A key present in a higher layer replaces the same key from the layer below; everything else is inherited.

This means each layer only declares what it changes. A user who wants a global exclude list sets it once in `~/.aide/settings.json`. A project that needs different exclude rules states those rules and inherits everything else.

---

## The `_aide` folder

Underscore-prefixed folder at the documentation root. It is the single home for machine-facing operational files in a project:

- Settings (the per-project settings file).
- Logs (if utilities produce them).
- Any other operational state the dispatcher or utilities need per-project.

The underscore prefix keeps it sorted to the top of the directory and signals that it is infrastructure, not content. It sits outside AIDE's document processing — consistent with the convention that underscore-prefixed folders are outside binder scope.

---

## Auto-update

### Automatic check

On launch, the dispatcher checks whether a newer version is available. It does this by comparing the installed version against git release tags in the source repository — no separate update server, no package index query.

The check runs at most once per day. The dispatcher records a "last checked" timestamp and skips the check if less than 24 hours have passed.

### Graceful offline behaviour

If the check fails (no network, repository unreachable), the dispatcher does not retry, does not block, and does not update the "last checked" timestamp. The next launch will try again naturally because the timestamp was not advanced. No retry loop, no error beyond a quiet log entry.

### Manual update

`aide update` forces an immediate update check and applies any available update. Available both as a subcommand and as an item in the interactive menu.

When a newer version is found (by either the automatic or manual check), the dispatcher reports what is available and applies it. The mechanism is a pip install from the git repository — the same command used for initial installation, pointed at the newer tag.

---

## Include and exclude

### Principle

Registration finds everything. Settings decide what is shown.

This is a settings concern, not a registration concern. The dispatcher scans the `utilities/` subpackage and discovers all conforming modules. The settings then filter which of those are presented in the menu and available as subcommands.

### Mechanism

A deny list in settings. Every discovered utility is available by default. To hide one, name it in the exclude list. There is no allow list — the default is "everything on."

### Scope

Both global and per-project, on the same deep-merge model as all other settings. A global exclude hides a utility everywhere. A per-project exclude hides it for that project only, without affecting global availability.

The merge means a project can exclude utilities that are globally available, or (by overriding the exclude list) restore utilities that are globally excluded. The same deep-merge rules apply.

---

## What this document does not cover

- The internal design of the three existing utilities — those are owned by File Operations in Working Practices.
- The broader question of whether utilities grow into a full AIDE CLI — that is a future direction, noted as a consideration, not designed for.
- The content of the global settings file beyond the structures needed for merge and exclude — each utility defines what settings it needs.

---

Version note: v1 — design document from voice session 2026-09-10. All four items were settled in conversation; this document records the design for handoff to a Code session.
<!-- END SOURCE: Infrastructure/Infrastructure_CLI_Design_v1.md -->

---

<!-- BEGIN SOURCE: Infrastructure/Infrastructure_Working_v1.md -->
Infrastructure | working | Infrastructure_Working@v1 | 2026-09-10

## Confirmed direction — session 2026-09-10

### Utility distribution model

Utilities are distributed as a pip package installed from git. `pip install git+https://github.com/...` installs the package and registers the `aide` command on PATH. Updates via `pip install --upgrade` or a self-update command (`aide update`).

The design-to-distribution workflow: update the utility design → rebuild the utility → commit to the utilities repo → user runs `aide update` or is prompted when a new version is available.

This mirrors the AIDE framework's approach to deploying capabilities: design, build, publish, and the consumer installs and updates.

### The aide dispatcher

A single entry point command — `aide` — on PATH. Behaviour:

- **No arguments** — interactive text menu listing available utilities. User selects and runs.
- **With subcommand** — runs directly, e.g. `aide binder-build`, for users who know what they want.
- **Customisation** — allows configuring settings for utilities within the interactive interface.

The dispatcher also serves as the registration point for utilities — adding a utility means adding a module to the package and registering a subcommand. New utilities appear in the menu automatically.

### Per-project launcher

A simple batch file (or similar) placed in the project's documentation folder. Runs the `aide` dispatcher targeting the current folder. Provides right-click or double-click access from Explorer without requiring a terminal.

### Settings model

Global defaults with per-project overrides. Global settings live with the central utility installation. Per-project settings live in the project's documentation folder (in `_utilities/` or `_config/`). The dispatcher merges them — global provides defaults, per-project overrides where needed.

Log files can go to a subfolder under the per-project settings location.

When launching, the execution folder is passed to the utility. The utility probes for settings files relative to the execution location, loads and uses them. If settings are edited within the aide interactive interface, they are written back to the same location.

### Items needing further design

- Utility registration mechanism — how the dispatcher discovers available utilities (subdirectory scan, config file, or package entry points)
- Detailed settings file format and merging rules
- Auto-update behaviour — check on launch, prompt, or silent
- Include/exclude mechanism — option to manually include or exclude utilities, install by default or prompt for new ones

---

Version note: v1 — initial working document from session 2026-09-10. Confirmed direction, not complete design.
<!-- END SOURCE: Infrastructure/Infrastructure_Working_v1.md -->

---

<!-- BEGIN SOURCE: Infrastructure/version-cleanup/README.md -->
# version cleanup

Moves superseded document versions out of the live tree, so a folder only ever
shows the current version of each document.

This folder is the **master copy**. To use the tool, copy `version_cleanup.py`
and `version_cleanup_settings.json` to wherever it should run from, then edit
that copy's settings. Each instance keeps its own settings file and its own log
beside the script, so instances never interfere with each other.

---

## What it does

In each folder it visits, it looks for files whose names are identical apart
from a `_v<number>` suffix immediately before the extension. The highest number
stays put; every lower version moves into a `_superseded` subfolder of the same
folder.

| Files in a folder | Result |
| --- | --- |
| `Foo_v8.md`, `Foo_v9.md` | `Foo_v8.md` moves, `Foo_v9.md` stays |
| `Foo.md`, `Foo_v1.md` | `Foo.md` moves — no suffix counts as v0 |
| `Foo_v3.md` on its own | nothing happens |
| `Foo_v1.md`, `Foo_v2.txt` | nothing happens — extensions must match too |

Grouping is **per folder**. The walk is recursive, but `Foo_v8.md` in one folder
is never compared with `Foo_v9.md` in another. Anything more complicated than
that is a manual job.

Folders whose name starts with an underscore are skipped, which is what keeps
the tool out of the `_superseded` folders it creates.

Nothing is ever overwritten. If a file of the same name is already sitting in
`_superseded`, the source file is left where it is and the run reports a
conflict.

---

## Installing Python on Windows

Only needed once per machine. The tool uses nothing beyond the Python standard
library, so there is nothing else to install.

1. Go to <https://www.python.org/downloads/windows/> and download the latest
   **Windows installer (64-bit)**. Python 3.8 or newer is required; any current
   release is fine.
2. Run the installer. On the first screen, **tick "Add python.exe to PATH"**
   before clicking Install. This is easy to miss and is the usual reason a
   `.py` file will not run afterwards.
3. Choose **Install Now**.
4. To check it worked, open PowerShell and run:

   ```
   python --version
   ```

   It should print something like `Python 3.13.1`.

### Making double-click work

The standard installer associates `.py` files with the Python launcher, so
double-clicking `version_cleanup.py` in File Explorer should just run it. If it
instead opens in Notepad or asks which app to use:

1. Right-click `version_cleanup.py` → **Open with** → **Choose another app**.
2. Pick **Python** (or browse to `C:\Windows\py.exe`).
3. Tick **Always use this app to open .py files**.

The script pauses with *"Press Enter to close..."* when it finishes, so the
console window stays open long enough to read the report.

### Running it from a terminal instead

```
python "C:\path\to\version_cleanup.py"
```

---

## Settings

The script reads `version_cleanup_settings.json` from **its own folder** — not
from wherever the terminal happens to be pointing. If that file is missing, the
script writes a fresh one with default values and explanatory notes, then tells
you to check it.

```json
{
  "root": "..",
  "include": [],
  "exclude": [],
  "log_file": "version_cleanup.log"
}
```

| Setting | Meaning |
| --- | --- |
| `root` | The folder to tidy, including everything beneath it. |
| `include` | Underscore-prefixed folders to process anyway. |
| `exclude` | Folders to skip entirely, along with everything inside them. |
| `log_file` | Where the run log is appended. |

**`root` and `log_file`** take a full path, or a path measured from the folder
the script lives in — so `".."` means "the folder above me", and an instance
sitting in `Documentation/_tools` tidies `Documentation` by default.

**`include` and `exclude`** take three kinds of path:

| Form | Example | Means |
| --- | --- | --- |
| Absolute | `"C:/Docs/_binder"` | that one exact folder |
| Root-anchored | `"~/_binder"` | that one exact folder, measured from `root` |
| Relative | `"_binder"` | a **pattern**: every folder in the tree whose path ends with those segments |

The relative form is the useful one for a corpus. `"_binder"` is not a place,
it is a shape — it matches a `_binder` subfolder wherever one appears, at
any depth. Several segments work too: `"_binder/current"` matches any
`.../_binder/current`.

Two consequences worth holding on to:

- `"~"` here means **the root of the tree being tidied**, never your home
  folder. The tool never expands `~` the way a shell would.
- A relative entry in `exclude` is powerful in the same way. `"_superseded"`
  would skip every `_superseded` folder in the tree, not one of them.

**Writing paths in JSON.** Use forward slashes (`"C:/Users/you/Documents"`) or
doubled backslashes (`"C:\\Users\\you"`); a single backslash is an escape
character in JSON and will break the file.

**Comments.** JSON has no comment syntax, so the notes in the shipped settings
file are carried as keys beginning with `_comment`. They are ordinary JSON and
the tool ignores them. Leave them, edit them, or delete them as you prefer.

**Exclude always wins over include**, and excluding a folder excludes
everything inside it.

To reach a folder nested inside an underscore-prefixed one, just name the
folder you actually want — the walk passes through the underscore folder to
get there without processing its own files.

Example: process every `_binder` in the tree, plus the one `_holding` folder
at the top, and stay out of one scratch area entirely.

```json
{
  "root": "..",
  "include": ["_binder", "~/_holding"],
  "exclude": ["~/Working Practices/scratch"],
  "log_file": "version_cleanup.log"
}
```

The run report echoes the include and exclude lists whenever they are in use,
so a log entry always says which rules produced it.

---

## Running it

Live by default — there is no confirmation prompt:

```
python version_cleanup.py
```

Report only, changes nothing:

```
python version_cleanup.py --dry-run
```

The dry run produces exactly the same report as a live run, with `WOULD MOVE`
in place of `MOVED`. It is the safe way to check a new `root` or a new
include/exclude list before letting the tool loose on a tree.

---

## The log

Every run appends one entry to the log file, live and dry-run alike, each
stamped with the date, the mode and the root it was pointed at. The log is
never rewritten or trimmed. If it grows unwieldy, archive or delete it by hand;
the tool will start a fresh one.

---

## When it declines to act

Two cases where the tool deliberately does nothing and tells you instead:

- **CONFLICT** — a file of that name already exists in `_superseded`. Two
  different documents are competing for one archive slot. Resolve it by hand.
- **AMBIGUOUS** — two files in the folder claim the same version number, which
  can only happen through leading zeros (`Foo_v08.md` and `Foo_v8.md`). Nothing
  in that group moves, because which one is current is genuinely unclear.

---

## Scope

It tidies versions. It does not build binders and it does not deploy anything.
Those are separate tools, run in sequence.
<!-- END SOURCE: Infrastructure/version-cleanup/README.md -->

---

<!-- BEGIN SOURCE: Infrastructure/version-cleanup/version_cleanup.py -->
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
version cleanup - move superseded document versions out of the live tree.

WHAT IT DOES
    Walks a folder tree. In each folder it looks for files whose names are
    identical apart from a "_v<number>" suffix just before the extension.
    The highest number stays where it is; every lower version is moved into a
    "_superseded" subfolder of the folder it came from.

        Foo_v8.md + Foo_v9.md   ->  Foo_v8.md moves, Foo_v9.md stays
        Foo.md    + Foo_v1.md   ->  Foo.md moves (no suffix counts as v0)
        Foo_v3.md alone         ->  nothing happens

    Grouping is always within a single folder. The walk is recursive, but
    Foo_v8.md in one folder is never compared with Foo_v9.md in another.

HOW IT IS RUN
    Live by default. Pass --dry-run to see the report without changing
    anything. It reads its settings from a JSON file sitting beside this
    script, so it can simply be double-clicked on Windows.

DESIGN NOTE
    This is one tool that does one thing. Sibling tools (binder assembly is
    next) will be separate scripts run in sequence, so there is deliberately no
    plugin system, no action registry and no shared base class here.

Python 3.8 or newer. Standard library only.
"""

import argparse
import datetime
import json
import os
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
# Path(__file__) is this script's own file. .resolve() turns it into a full,
# unambiguous path, and .parent gives the folder holding it. Everything the
# tool reads or writes hangs off this folder rather than off the "current
# working directory", because the working directory depends on *how* the script
# was launched (double-click, terminal, scheduler) and is therefore unreliable.
# It also means each copy of the tool uses its own settings and its own log.
SCRIPT_DIR = Path(__file__).resolve().parent

SETTINGS_FILENAME = "version_cleanup_settings.json"
SUPERSEDED_FOLDER_NAME = "_superseded"

# The matching rule, as a regular expression, applied to a filename with its
# extension already stripped off:
#   ^          start of the name
#   (?P<base>.+)   one or more characters, captured as "base" - the document
#                  identity. ".+" rather than ".*" so a file literally named
#                  "_v1.md" is not read as an empty document name.
#   _[vV]      the literal separator; upper or lower case v is accepted
#   (?P<number>\d+)  one or more digits, captured as "number"
#   $          end of the name - the suffix must be the last thing before the
#              extension, so "Foo_v2_draft.md" is deliberately not a match.
VERSION_SUFFIX = re.compile(r"^(?P<base>.+)_[vV](?P<number>\d+)$")

# Spots "C:" or "D:" at the start of a settings path, so a Windows path in a
# settings file being run on Mac or Linux fails loudly rather than being
# mistaken for a relative pattern that then silently never matches anything.
WINDOWS_DRIVE = re.compile(r"^[A-Za-z]:")

# The settings file is shipped with the tool, but if someone deletes it - or
# copies just the .py file to a new location - we write this back out rather
# than failing. Keeping the defaults as *text* (not as a Python dictionary that
# gets dumped to JSON) means the file we create is byte-for-byte the file we
# ship, comments and ordering included.
#
# JSON has no comment syntax, so the explanatory lines are carried as ordinary
# keys beginning with "_comment". The loader ignores them. That keeps the file
# valid JSON, readable by any editor and parseable by the standard library.
DEFAULT_SETTINGS_JSON = """{
  "_comment": "Settings for the version cleanup tool. Edit the values below. Any key starting with _comment is ignored by the tool - JSON has no comment syntax, so notes live in keys like this one.",

  "_comment_root": "The folder to tidy, including everything beneath it. A relative path is resolved against the folder this script lives in, so \\"..\\" means the parent folder. Give a full path such as \\"C:/Users/you/Documents\\" to point somewhere else. Forward slashes are safe on Windows.",
  "root": "..",

  "_comment_paths": "include and exclude accept three kinds of path. ABSOLUTE - \\"C:/Docs/_binder\\" - names one exact folder. ROOT-ANCHORED - \\"~/_binder\\" - names one exact folder, measured from the root above. RELATIVE - \\"_binder\\" - is a pattern rather than a place: it matches every folder in the tree whose path ends with those segments, so one entry covers a _binder subfolder wherever it appears. Note that ~ means the root of the tree here, never your home folder.",

  "_comment_include": "Folders whose names start with an underscore are skipped by default. List any that should be processed anyway. Example: [\\"_binder\\"] processes every _binder folder in the tree; [\\"~/_binder\\"] processes only the one at the top.",
  "include": [],

  "_comment_exclude": "Folders to skip entirely, along with everything inside them. Exclude always wins over include. A relative entry here is powerful: \\"_superseded\\" would skip every _superseded folder in the tree.",
  "exclude": [],

  "_comment_log_file": "Where the run log is appended. One entry per run, never overwritten. Absolute, or \\"~/\\" for root-anchored, or relative to the script folder.",
  "log_file": "version_cleanup.log"
}
"""


# ---------------------------------------------------------------------------
# Small record types
# ---------------------------------------------------------------------------
# A dataclass is Python shorthand for "a class that just holds these fields".
# The lines below generate the constructor for us. Used here instead of loose
# tuples so that report code can say event.kind rather than event[0].

@dataclass
class Event:
    """One line of the report: something that happened, or failed to."""
    kind: str      # MOVED / WOULD MOVE / CONFLICT / AMBIGUOUS / ERROR
    folder: Path   # the folder it happened in
    detail: str    # human-readable description


@dataclass
class PlannedMove:
    """One file that should move, and where it should move to."""
    source: Path
    destination: Path
    reason: str    # e.g. "v7 superseded by v9"


# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------

def load_settings(settings_path):
    """
    Read the settings file, creating it from the shipped defaults if missing.

    Returns a plain dictionary. Raises ValueError with a readable message if
    the file exists but is not valid JSON - a mistyped settings file should
    stop the run with an explanation, not with a stack trace.
    """
    if not settings_path.exists():
        print("No settings file found. Creating one with default values:")
        print("  {}".format(settings_path))
        print("Review it, then run the tool again if the defaults are wrong.")
        print("")
        settings_path.write_text(DEFAULT_SETTINGS_JSON, encoding="utf-8")

    text = settings_path.read_text(encoding="utf-8")
    try:
        settings = json.loads(text)
    except json.JSONDecodeError as error:
        # The exception carries the line and column of the problem, which is
        # the single most useful thing to show someone fixing the file.
        raise ValueError(
            "The settings file is not valid JSON.\n"
            "  file: {}\n"
            "  problem: {} (line {}, column {})\n"
            "Common causes: a missing comma, a trailing comma after the last "
            "item, or a single backslash inside a path (write \\\\ or use /)."
            .format(settings_path, error.msg, error.lineno, error.colno)
        )

    if not isinstance(settings, dict):
        raise ValueError(
            "The settings file must contain a JSON object (a {{ ... }} block), "
            "but it contains {}.".format(type(settings).__name__)
        )

    return settings


# ---------------------------------------------------------------------------
# Path forms
# ---------------------------------------------------------------------------
# Three spellings are accepted, because the tree needs two different kinds of
# statement: "this exact folder" and "any folder shaped like this".
#
#   absolute        "C:/Docs/_binder"   one exact folder
#   root-anchored   "~/_binder"         one exact folder, measured from root
#   relative        "_binder"           a PATTERN: every folder whose path
#                                       ends with those segments
#
# The relative form is the interesting one. It is not resolved once at startup;
# it is a shape the walk tests every folder against, so a single "_binder"
# entry covers a _binder subfolder wherever one turns up in the tree. Several
# segments work too: "_binder/current" matches any .../_binder/current.
#
# Note that "~" does NOT mean the home folder here. Python's expanduser is
# deliberately never called on these settings, so "~/" always means the root of
# the tree being tidied and can never quietly resolve to C:\Users\someone.

def tidy_setting_text(value, label):
    """Trim a settings value and normalise its separators to forward slashes."""
    text = str(value).strip().replace("\\", "/")
    if not text:
        raise ValueError('Setting "{}" contains an empty path.'.format(label))
    return text


def resolve_one_folder(text, label, root=None):
    """
    Resolve a settings value that names ONE place: absolute, "~/" measured from
    the root, or relative to the script's own folder.

    Used for the root and the log file. Include and exclude go through
    parse_scope_entry instead, because they also accept patterns.
    """
    if text.startswith("~"):
        if root is None:
            raise ValueError(
                'Setting "{}" cannot use "~/", because "~/" means "measured '
                'from the root" and this setting is what defines the root. '
                'Use a full path, or a path relative to the script folder.'
                .format(label)
            )
        if not text.startswith("~/"):
            raise ValueError(
                'Setting "{}": "~" means the root folder, so it has to be '
                'written as "~/something".'.format(label)
            )
        return (root / text[2:]).resolve()

    path = Path(text)
    if not path.is_absolute():
        if WINDOWS_DRIVE.match(text):
            raise ValueError(
                'Setting "{}" is "{}", which looks like a Windows path, but '
                "this is not Windows.".format(label, text)
            )
        # resolve() also removes any ".." segments, so two spellings of the
        # same folder compare equal later on.
        path = SCRIPT_DIR / path
    return path.resolve()


def parse_scope_entry(text, label, root):
    """
    Classify one include or exclude entry.

    Returns ("folder", Path) for the absolute and "~/" forms, or
    ("pattern", (segments...)) for the relative form.
    """
    if text.startswith("~"):
        return ("folder", resolve_one_folder(text, label, root))

    path = Path(text)
    if path.is_absolute():
        return ("folder", path.resolve())
    if WINDOWS_DRIVE.match(text):
        raise ValueError(
            'Setting "{}" contains "{}", which looks like a Windows path, but '
            "this is not Windows.".format(label, text)
        )

    # Anything else is a pattern. Splitting on "/" and dropping empty pieces
    # tolerates a stray leading or trailing slash.
    segments = tuple(part for part in text.split("/") if part)
    if not segments or "." in segments:
        raise ValueError(
            'Setting "{}" contains "{}", which does not name anything.'
            .format(label, text)
        )
    if ".." in segments:
        raise ValueError(
            'Setting "{}" contains "{}". A relative entry is a pattern tested '
            'against every folder in the tree, so ".." has no meaning in one. '
            'Write "~/..." to anchor at the root, or give a full path.'
            .format(label, text)
        )
    return ("pattern", segments)


def normalise(path):
    """
    Case-fold a path the way the local filesystem does.

    os.path.normcase lowercases on Windows, where FOO and foo are the same
    folder, and changes nothing on Mac or Linux. Comparing paths through it
    avoids both false misses on Windows and false matches elsewhere.
    """
    return Path(os.path.normcase(str(path)))


# ---------------------------------------------------------------------------
# Folder scope
# ---------------------------------------------------------------------------

def is_inside(path, folder):
    """True if `path` is `folder` itself, or anywhere beneath it."""
    try:
        normalise(path).relative_to(normalise(folder))
        return True
    except ValueError:
        # relative_to raises when path is not under folder. Catching that is
        # the standard pathlib way of asking this question.
        return False


@dataclass
class Scope:
    """
    Everything the walk needs in order to decide which folders are in play.

    Entries arrive already sorted into exact folders and patterns, so the walk
    itself stays readable: it asks questions, it does not parse settings.
    """
    root: Path
    include_folders: list = field(default_factory=list)
    include_patterns: list = field(default_factory=list)
    exclude_folders: list = field(default_factory=list)
    exclude_patterns: list = field(default_factory=list)
    include_text: list = field(default_factory=list)   # as typed, for the report
    exclude_text: list = field(default_factory=list)

    def parts_below_root(self, path):
        """The folder's path as case-folded segments measured from the root."""
        try:
            relative = path.relative_to(self.root)
        except ValueError:
            return None
        return tuple(os.path.normcase(part) for part in relative.parts)

    def matches_pattern(self, path, patterns):
        """
        True if the folder's path ENDS WITH one of the patterns.

        This trailing-segment test is what makes "_binder" mean "any _binder
        folder, wherever it appears". Because the comparison is made against
        the path measured from the root, a pattern can never reach above the
        root, and the root itself is never matched: it has no segments to
        compare.
        """
        parts = self.parts_below_root(path)
        if parts is None:
            return False
        for pattern in patterns:
            length = len(pattern)
            if length > len(parts):
                continue
            wanted = tuple(os.path.normcase(part) for part in pattern)
            if parts[-length:] == wanted:
                return True
        return False

    def leads_to_include_pattern(self, path):
        """
        True if something deeper down could still match a multi-segment
        include pattern.

        For "_binder/current", a folder ending in "_binder" is not itself
        included, but the walk has to pass through it to reach "current".
        Testing every *proper* prefix of every pattern is exactly that
        lookahead. Single-segment patterns have no proper prefix and contribute
        nothing here, which is right: they match the folder itself or not at
        all.
        """
        parts = self.parts_below_root(path)
        if parts is None:
            return False
        for pattern in self.include_patterns:
            for length in range(1, len(pattern)):
                if length > len(parts):
                    continue
                wanted = tuple(os.path.normcase(part)
                               for part in pattern[:length])
                if parts[-length:] == wanted:
                    return True
        return False

    def is_excluded(self, path):
        """Excluded folders, and everything inside them, are never touched."""
        if any(is_inside(path, folder) for folder in self.exclude_folders):
            return True
        return self.matches_pattern(path, self.exclude_patterns)

    def is_included(self, path):
        """True if this exact folder was named, or it matches a pattern."""
        if any(normalise(path) == normalise(folder)
               for folder in self.include_folders):
            return True
        return self.matches_pattern(path, self.include_patterns)

    def should_descend(self, path):
        """
        Should the walk go *into* this folder?

        Note the difference between descending and processing. An underscore
        folder that is not itself included may still need to be walked through,
        because something deeper down is on the include list. It is traversed,
        but its own files are left alone.
        """
        if self.is_excluded(path):
            return False
        if not path.name.startswith("_"):
            return True
        if self.is_included(path):
            return True
        # Is this folder on the way to an exactly-named include?
        if any(is_inside(folder, path) for folder in self.include_folders):
            return True
        return self.leads_to_include_pattern(path)

    def should_process(self, path):
        """Should this folder's own files be compared and tidied?"""
        if self.is_excluded(path):
            return False
        if not path.name.startswith("_"):
            return True
        # The underscore rule is what keeps the tool out of the _superseded
        # folders it creates. Only an explicit include overrides it.
        return self.is_included(path)


def build_scope(root, include_values, exclude_values):
    """Turn the raw include and exclude settings into a Scope."""
    scope = Scope(root=root)

    for label, values in (("include", include_values),
                          ("exclude", exclude_values)):
        if values is None:
            continue
        if not isinstance(values, list):
            raise ValueError(
                'Setting "{}" must be a list of paths, written in square '
                'brackets, for example ["_binder"].'.format(label)
            )
        for value in values:
            text = tidy_setting_text(value, label)
            kind, resolved = parse_scope_entry(text, label, root)
            if label == "include":
                scope.include_text.append(text)
                target = (scope.include_folders if kind == "folder"
                          else scope.include_patterns)
            else:
                scope.exclude_text.append(text)
                target = (scope.exclude_folders if kind == "folder"
                          else scope.exclude_patterns)
            target.append(resolved)

    return scope


def folders_to_process(scope):
    """
    Walk the tree from the root and return the folders whose files should be
    compared, in a stable, predictable order.
    """
    found = []
    root = scope.root

    # os.walk visits every folder beneath root. With topdown=True (the default)
    # it hands us the list of subfolder names *before* descending, and editing
    # that list in place prunes the walk - the standard way to skip whole
    # branches cheaply. Pruning is also what makes exclusion inherited: once a
    # folder is skipped, nothing inside it is ever looked at, so there is no
    # need to ask again further down. Symbolic links to folders are not
    # followed by default, which is what we want: a link should not cause the
    # same tree to be tidied twice.
    for dirpath, dirnames, _filenames in os.walk(root):
        current = Path(dirpath)

        # dirnames[:] = ... replaces the contents of the existing list rather
        # than rebinding the name. os.walk only notices the former.
        dirnames[:] = sorted(
            name for name in dirnames if scope.should_descend(current / name)
        )

        if current == root:
            # The root was chosen deliberately by whoever edited the settings,
            # so the underscore rule does not apply to it. An explicit exclude
            # still does.
            process = not scope.is_excluded(current)
        else:
            process = scope.should_process(current)

        if process:
            found.append(current)

    return found


# ---------------------------------------------------------------------------
# The matching rule
# ---------------------------------------------------------------------------

def split_version(file_path):
    """
    Split a filename into (document identity, extension, version number).

    Path.stem is the filename without its final extension; Path.suffix is that
    extension including the dot. A file with no _v suffix is version 0, which
    is what makes "Foo.md is superseded by Foo_v1.md" fall out of the same
    comparison as everything else rather than needing a special case.
    """
    stem = file_path.stem
    extension = file_path.suffix

    match = VERSION_SUFFIX.match(stem)
    if match:
        return match.group("base"), extension, int(match.group("number"))
    return stem, extension, 0


def plan_folder(folder):
    """
    Work out what should move in one folder. Nothing is changed here.

    Returns (moves, events). Splitting the decision from the action is what
    makes --dry-run trustworthy: the dry run and the live run take exactly the
    same decisions, and only the second half of the program differs.
    """
    moves = []
    events = []

    # Group the folder's files by (identity, extension). A dictionary of lists:
    # the key identifies the document, the list holds its versions.
    groups = {}
    try:
        entries = sorted(folder.iterdir())
    except OSError as error:
        events.append(Event("ERROR", folder, "cannot read folder: {}".format(error)))
        return moves, events

    for entry in entries:
        if not entry.is_file():
            continue  # subfolders are visited in their own right by the walk
        base, extension, version = split_version(entry)
        # setdefault returns the existing list for this key, or inserts a new
        # empty list first. Saves the usual "if key not in dict" dance.
        groups.setdefault((base, extension), []).append((version, entry))

    for (base, extension), members in sorted(groups.items()):
        if len(members) < 2:
            continue  # a file with no versioned sibling stays put

        numbers = [version for version, _entry in members]
        highest = max(numbers)

        # Two files can only share a version number through leading zeros
        # (Foo_v08 and Foo_v8) or a case difference in the _v. Which one is
        # current is then genuinely unclear, so the tool declines to guess and
        # leaves the whole group alone for a human to sort out.
        if len(set(numbers)) != len(numbers):
            names = ", ".join(entry.name for _version, entry in members)
            events.append(Event(
                "AMBIGUOUS", folder,
                "{}{}: duplicate version numbers, nothing moved ({})"
                .format(base, extension, names)
            ))
            continue

        superseded_dir = folder / SUPERSEDED_FOLDER_NAME

        for version, entry in sorted(members):
            if version == highest:
                continue  # the current version stays exactly where it is

            destination = superseded_dir / entry.name

            # Never overwrite. An existing file of the same name in
            # _superseded means two different documents are competing for one
            # archive slot; that is a decision for a person, not for a script.
            if destination.exists():
                events.append(Event(
                    "CONFLICT", folder,
                    "{} left in place: {}/{} already exists"
                    .format(entry.name, SUPERSEDED_FOLDER_NAME, entry.name)
                ))
                continue

            moves.append(PlannedMove(
                source=entry,
                destination=destination,
                reason="v{} superseded by v{}".format(version, highest),
            ))

    return moves, events


# ---------------------------------------------------------------------------
# Doing the work
# ---------------------------------------------------------------------------

def apply_moves(moves, dry_run):
    """
    Carry out the planned moves (or, in a dry run, describe them).

    Returns the list of events describing what happened.
    """
    events = []

    for move in moves:
        folder = move.source.parent

        if dry_run:
            events.append(Event(
                "WOULD MOVE", folder,
                "{}  ({})".format(move.source.name, move.reason)
            ))
            continue

        try:
            # Created lazily, so folders with nothing to archive never gain an
            # empty _superseded. mkdir with exist_ok=True is a no-op if it is
            # already there.
            move.destination.parent.mkdir(exist_ok=True)

            # A last existence check immediately before the move. plan_folder
            # already checked, but the destination could have appeared since -
            # and shutil.move would silently overwrite it on Linux and macOS.
            if move.destination.exists():
                events.append(Event(
                    "CONFLICT", folder,
                    "{} left in place: {}/{} appeared during the run"
                    .format(move.source.name, SUPERSEDED_FOLDER_NAME,
                            move.source.name)
                ))
                continue

            shutil.move(str(move.source), str(move.destination))
            events.append(Event(
                "MOVED", folder,
                "{}  ({})".format(move.source.name, move.reason)
            ))
        except OSError as error:
            # A locked file, a read-only folder, a permissions problem. Report
            # it and carry on with the rest - one bad file should not abandon
            # the whole tree half-tidied.
            events.append(Event(
                "ERROR", folder,
                "{} could not be moved: {}".format(move.source.name, error)
            ))

    return events


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def build_report(scope, settings_path, dry_run, folder_count, events):
    """
    Build the run report as a list of lines.

    One function produces both the on-screen report and the log entry, so the
    two can never drift apart.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = "DRY RUN (nothing changed)" if dry_run else "LIVE"

    lines = []
    lines.append("=" * 72)
    lines.append("version cleanup   {}   {}".format(timestamp, mode))
    lines.append("root:     {}".format(scope.root))
    lines.append("settings: {}".format(settings_path))
    # Scope overrides are echoed only when in use. They decide which folders
    # were touched, so a log entry is not self-explaining without them.
    if scope.include_text:
        lines.append("include:  {}".format(", ".join(scope.include_text)))
    if scope.exclude_text:
        lines.append("exclude:  {}".format(", ".join(scope.exclude_text)))
    lines.append("folders processed: {}".format(folder_count))
    lines.append("-" * 72)

    if not events:
        lines.append("Nothing to do - every document in the tree is already "
                     "at its current version.")
    else:
        # Events are reported grouped by folder, which is how someone reading
        # the report actually thinks about the tree.
        current_folder = None
        for event in events:
            if event.folder != current_folder:
                current_folder = event.folder
                lines.append("")
                lines.append("[{}]".format(relative_to(event.folder,
                                                       scope.root)))
            lines.append("  {:<11} {}".format(event.kind, event.detail))

    counts = {}
    for event in events:
        counts[event.kind] = counts.get(event.kind, 0) + 1

    summary = ", ".join(
        "{} {}".format(counts[kind], kind.lower())
        for kind in ("MOVED", "WOULD MOVE", "CONFLICT", "AMBIGUOUS", "ERROR")
        if kind in counts
    ) or "no changes"

    lines.append("")
    lines.append("-" * 72)
    lines.append("Result: {}".format(summary))
    lines.append("=" * 72)
    return lines


def relative_to(path, root):
    """Show a path relative to the root when possible - shorter to read."""
    try:
        relative = path.relative_to(root)
    except ValueError:
        return str(path)
    return str(relative) if str(relative) != "." else "."


def append_to_log(log_path, lines):
    """
    Append one entry to the log. The log is never rewritten or trimmed.

    Failing to write the log must not lose the report that is already on
    screen, so a problem here is reported and swallowed.
    """
    try:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        # "a" is append mode: the file is created if absent, and writes always
        # go to the end. newline="" leaves line endings to us, so the log looks
        # the same on every platform.
        with open(log_path, "a", encoding="utf-8", newline="\n") as log_file:
            log_file.write("\n".join(lines))
            log_file.write("\n\n")
        return True
    except OSError as error:
        print("WARNING: could not write the log file {}: {}"
              .format(log_path, error))
        return False


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def pause_before_exit():
    """
    Hold the console open so a double-clicked run can be read.

    Skipped when there is no interactive console attached - otherwise a
    scheduled or piped run would hang forever waiting for a keypress.
    """
    if not sys.stdin or not sys.stdin.isatty():
        return
    try:
        input("\nPress Enter to close...")
    except (EOFError, KeyboardInterrupt):
        pass


def run(dry_run):
    """The whole job. Returns an exit code: 0 for success, 1 for a problem."""
    settings_path = SCRIPT_DIR / SETTINGS_FILENAME

    try:
        settings = load_settings(settings_path)
        # The root is resolved first, because "~/" in the other settings is
        # measured from it.
        root = resolve_one_folder(
            tidy_setting_text(settings.get("root", ".."), "root"), "root"
        )
        scope = build_scope(root, settings.get("include"),
                            settings.get("exclude"))
        log_path = resolve_one_folder(
            tidy_setting_text(settings.get("log_file", "version_cleanup.log"),
                              "log_file"),
            "log_file", root=root
        )
    except ValueError as error:
        print("SETTINGS PROBLEM")
        print(error)
        return 1

    if not root.is_dir():
        print("SETTINGS PROBLEM")
        print('The "root" setting does not point at a folder that exists:')
        print("  {}".format(root))
        print("  (from settings file {})".format(settings_path))
        return 1

    folders = folders_to_process(scope)

    all_events = []
    for folder in folders:
        moves, plan_events = plan_folder(folder)
        all_events.extend(plan_events)
        all_events.extend(apply_moves(moves, dry_run))

    # Report in folder order rather than in the order things happened, so
    # conflicts and moves in the same folder appear together.
    all_events.sort(key=lambda event: (str(event.folder), event.kind))

    lines = build_report(scope, settings_path, dry_run, len(folders),
                         all_events)
    print("\n".join(lines))

    # Dry runs are logged too, clearly marked, so the log is a complete record
    # of every time the tool was pointed at the tree.
    append_to_log(log_path, lines)
    print("\nLog: {}".format(log_path))

    had_problems = any(event.kind in ("ERROR",) for event in all_events)
    return 1 if had_problems else 0


def main():
    parser = argparse.ArgumentParser(
        description="Move superseded document versions into _superseded "
                    "subfolders. Reads its settings from {} beside the script."
                    .format(SETTINGS_FILENAME)
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",  # present = True, absent = False
        help="report what would move without changing anything",
    )
    args = parser.parse_args()

    try:
        exit_code = run(args.dry_run)
    except KeyboardInterrupt:
        print("\nInterrupted.")
        exit_code = 1

    pause_before_exit()
    return exit_code


# When Python runs a file directly, it sets __name__ to "__main__". This guard
# is the conventional way to say "only do this when run, not when imported".
if __name__ == "__main__":
    sys.exit(main())
<!-- END SOURCE: Infrastructure/version-cleanup/version_cleanup.py -->

---

<!-- BEGIN SOURCE: Infrastructure/version-cleanup/version_cleanup_settings.json -->
{
  "_comment": "Settings for the version cleanup tool. Edit the values below. Any key starting with _comment is ignored by the tool - JSON has no comment syntax, so notes live in keys like this one.",

  "_comment_root": "The folder to tidy, including everything beneath it. A relative path is resolved against the folder this script lives in, so \"..\" means the parent folder. Give a full path such as \"C:/Users/you/Documents\" to point somewhere else. Forward slashes are safe on Windows.",
  "root": "..",

  "_comment_paths": "include and exclude accept three kinds of path. ABSOLUTE - \"C:/Docs/_binder\" - names one exact folder. ROOT-ANCHORED - \"~/_binder\" - names one exact folder, measured from the root above. RELATIVE - \"_binder\" - is a pattern rather than a place: it matches every folder in the tree whose path ends with those segments, so one entry covers a _binder subfolder wherever it appears. Note that ~ means the root of the tree here, never your home folder.",

  "_comment_include": "Folders whose names start with an underscore are skipped by default. List any that should be processed anyway. Example: [\"_binder\"] processes every _binder folder in the tree; [\"~/_binder\"] processes only the one at the top.",
  "include": [],

  "_comment_exclude": "Folders to skip entirely, along with everything inside them. Exclude always wins over include. A relative entry here is powerful: \"_superseded\" would skip every _superseded folder in the tree.",
  "exclude": [],

  "_comment_log_file": "Where the run log is appended. One entry per run, never overwritten. Absolute, or \"~/\" for root-anchored, or relative to the script folder.",
  "log_file": "version_cleanup.log"
}
<!-- END SOURCE: Infrastructure/version-cleanup/version_cleanup_settings.json -->

---

<!-- BEGIN SOURCE: Infrastructure/version-cleanup/VersionCleanup_Design_v3.md -->
# Version Cleanup — Design

> **Version 3** (2026-09-04). Corrects the master folder path after the rename to `version-cleanup`.
> v2 added objective, contents, definition of done and sibling
> relationships; records the three-form path model's ratification as an Infrastructure-wide
> convention; reframes verification as required cases rather than a build record. No behaviour
> change from v1.

## Contents

- **Position and objective** — what this is, what it must achieve, its boundary.
- **The matching rule** — document identity, version comparison, deliberate limits.
- **Folder scope** — descend versus process, and the three path forms.
- **Archive behaviour** — where superseded files go and what is never overwritten.
- **Execution model** — master/instance deployment and script-folder resolution.
- **The three files** — script, settings contract, log contract.
- **Run modes and report vocabulary.**
- **Definition of done, idempotence, boundary, required verification cases.**

## Position

Version cleanup is the first piece of **Infrastructure** for the AIDE documentation corpus:
machinery that acts on the document tree but is never loaded into an AI session. It has no
authority over document content and states no methodology; it enforces one physical property of
the tree.

It is a **single-action tool**, not a framework. Sibling tools are separate scripts run in
sequence. There is deliberately no action registry, plugin system or shared base class. Any
commonality between siblings is resolved when the duplication is visible, not in anticipation of
it.

### Relationship to siblings

Version cleanup runs **first** in the corpus pipeline, so tools downstream can take what they find
without version reasoning:

```text
version cleanup  →  binder builder  →  (later siblings)
```

Binder builder supersedes its own previous output within its own folder, so version cleanup never
needs pointing at `_binder`. The governing principle: **a tool cleans up after itself; version
cleanup handles supersession it did not cause.**

## Objective

Keep the live document tree holding exactly one version of each document, so anything reading the
tree — a person, a sibling tool, or an AI loading context — finds the current document without
having to reason about which one it is.

```text
document tree containing many versions per document
  → walk each folder
  → group that folder's files by document identity
  → keep the highest version in place
  → move every lower version into that folder's _superseded
  → report + append log entry
```

## The matching rule

Two files are the same document at different versions when their filenames are identical except
for a `_v<number>` suffix immediately before the extension, and their extensions match.

```text
identity  =  (filename with any trailing _v<number> removed, extension)
version   =  the digits in that suffix, or 0 when there is no suffix
```

| Case | Behaviour |
| --- | --- |
| `Foo_v8.md`, `Foo_v9.md` | `Foo_v8.md` superseded |
| `Foo.md`, `Foo_v1.md` | `Foo.md` superseded — absent suffix is v0 |
| `Foo_v3.md` alone | stays, suffix or not |
| `Foo_v1.md`, `Foo_v2.txt` | different documents — extension is part of identity |
| `Foo_v2_draft.md` | no match — the suffix must be terminal |

Treating an unsuffixed file as v0 removes the special case: `Foo.md` versus `Foo_v1.md` is decided
by the same comparison as `Foo_v8.md` versus `Foo_v9.md`.

Highest number stays; all lower versions move. Version numbers are compared numerically, so
`_v10` outranks `_v9`.

### Deliberate limits

- **Case.** `_v` and `_V` are both recognised. The document identity itself is compared with exact
  case, so `Foo_v1.md` and `foo_v2.md` are two documents and neither moves. Conservative by intent.
- **Ties.** Two files can share a version number only through leading zeros (`Foo_v08.md`,
  `Foo_v8.md`). Which is current is then genuinely unclear, so the tool reports `AMBIGUOUS` and
  moves nothing in that group.
- **Compound extensions.** Only the final extension is treated as the extension, so
  `Foo_v8.tar.gz` has identity `Foo_v8.tar` and never matches. Not a concern for a document corpus.

**The general shape:** where a rule does not determine an answer, report it and move nothing. This
applies to every case in this class, not only ties.

## Folder scope

Grouping is **per folder**. The walk is recursive and visits every folder, but each folder is
compared only against itself. Cross-folder version relationships are handled manually and are out
of scope.

Two distinct questions are asked of every folder:

| Question | Rule |
| --- | --- |
| **Descend** into it? | Not excluded, and either its name does not start with `_`, or it is on the include list, or it is an ancestor of something on the include list. |
| **Process** its own files? | Not excluded, and either its name does not start with `_`, or it is on the include list. |

The distinction matters: an underscore-prefixed folder that merely sits on the path to an included
folder is walked through without its own files being touched.

- The underscore rule is what keeps the tool out of the `_superseded` folders it creates. It is
  the mechanism, not a convention layered on top of one.
- The **root** is an explicit choice in the settings file, so the underscore rule does not apply
  to it. An explicit exclude still does.
- Exclude wins over include. Pruning at an excluded folder is what makes exclusion inherited:
  once a branch is skipped, nothing inside it is ever asked about again.
- Directory symlinks are not followed, so a link cannot cause one tree to be tidied twice.

### Path forms for include and exclude

The tree needs two different kinds of statement: *this exact folder*, and *any folder shaped
like this*. Three spellings carry them.

| Form | Example | Resolution |
| --- | --- | --- |
| Absolute | `C:/Docs/_binder` | one exact folder |
| Root-anchored | `~/_binder` | one exact folder, measured from `root` |
| Relative | `_binder` | a **pattern**, tested against every folder the walk reaches |

**Status: ratified as the Infrastructure-wide convention** (2026-09-04). This is not a local choice
of this tool. Binder builder and later siblings use the same vocabulary; a divergent path model in
a sibling is a defect.

A relative entry is not resolved once at startup. It is a shape, matched when a folder's path
**ends with** the entry's segments, so `_binder` covers a `_binder` subfolder at any depth and
`_binder/current` matches any `.../_binder/current`. The comparison is made against the path
measured from the root, so a pattern can never reach above the root, and the root itself is never
matched by one.

Consequences taken deliberately:

- `~` means the **root of the tree**, never the home folder. `expanduser` is never called on
  these settings, so `~/` cannot quietly resolve to a user profile directory. This is a one-way
  door on that character across Infrastructure.
- The `root` setting itself cannot use `~/`, since it is what defines the root. It takes an
  absolute path or one relative to the script folder, and rejects `~/` with that explanation.
- `..` is rejected inside a relative entry. A pattern has no anchor for it, so silently accepting
  one would produce an entry that never matches.
- Path comparison goes through `os.path.normcase`: case-insensitive on Windows, case-sensitive
  elsewhere. Matching therefore follows the local filesystem rather than diverging from it.
- The multi-segment form needs lookahead. A folder matching a *proper prefix* of an include
  pattern is descended into but not processed, which is how `_binder/current` reaches `current`
  through an underscore-prefixed parent.
- A relative `exclude` entry is correspondingly broad: `_superseded` would skip every such folder
  in the tree. That is the intent, and it is stated in the shipped settings file.

## Archive behaviour

Superseded files move into `_superseded`, a subfolder of the folder the file came from. It is
created lazily — a folder with nothing to archive never gains an empty `_superseded`.

**Nothing is ever overwritten.** If the destination name already exists, the source file is left
in place and the run reports `CONFLICT`. Two different documents competing for one archive slot is
a decision for a person. The destination is re-checked immediately before the move, because
`shutil.move` overwrites silently on Linux and macOS.

Files are moved, not copied and deleted; source and destination are always on the same volume.

## Execution model

```text
Documentation/Infrastructure/version-cleanup/        ← master, source of truth
        │  copy
        ▼
Documentation/_tools/                                ← instance: own settings, own log
```

Each instance resolves its settings file, its log and its root against **the folder holding the
script**, never against the current working directory. The working directory varies with how the
script was launched (double-click, terminal, scheduler) and is unreliable; the script folder does
not. This is also what gives each instance its own settings and its own log without any instance
registry.

Changes are made to the master and redeployed by copying. Instances are not edited in place except
for their settings file.

## The three files

| File | Role |
| --- | --- |
| `version_cleanup.py` | The script. Standard library only, Python 3.8+, cross-platform. |
| `version_cleanup_settings.json` | Per-instance configuration, read on launch. |
| `version_cleanup.log` | Append-only record, one entry per run. Created on first run. |

`README.md` and this design document travel with the master and are not required at runtime.

### Settings contract

```json
{
  "root": "..",
  "include": [],
  "exclude": [],
  "log_file": "version_cleanup.log"
}
```

- **JSON** — no third-party parser needed, editable by hand, and a syntax error is reported with
  line and column rather than as a stack trace.
- JSON has no comment syntax, so the shipped defaults carry their explanatory notes as keys
  beginning with `_comment`. The loader ignores them. The alternative — a JSONC dialect with a
  hand-written comment stripper — buys nothing and adds a parser to maintain.
- `root` and `log_file` resolve against the script folder when relative, so `".."` means "the
  folder above the tool" — the right default for an instance living in `Documentation/_tools`.
  `include` and `exclude` use the three path forms above.
- A missing settings file is written from the shipped defaults rather than being an error, so a
  bare `.py` copied to a new location bootstraps itself.

### Log contract

Append-only, one entry per run, never rewritten or trimmed. Dry runs are logged too, clearly
marked, so the log is a complete record of every time the tool was pointed at the tree. The
on-screen report and the log entry are produced by one function and cannot drift apart.

## Run modes

| Mode | Behaviour |
| --- | --- |
| default | Live. No confirmation prompt. |
| `--dry-run` | Identical report, `WOULD MOVE` in place of `MOVED`, nothing changed. |

Planning and acting are separate stages: `plan_folder` decides, `apply_moves` acts. A dry run
executes the same decision code as a live run, which is what makes it a trustworthy preview rather
than a parallel implementation.

The script pauses for a keypress before exiting so a double-clicked run can be read. The pause is
skipped when no interactive console is attached, so a scheduled run cannot hang on it.

## Report vocabulary

| Kind | Meaning |
| --- | --- |
| `MOVED` | File moved into `_superseded`. |
| `WOULD MOVE` | Dry run — the same file, unmoved. |
| `CONFLICT` | Destination name already taken; source left in place. |
| `AMBIGUOUS` | Duplicate version numbers in one group; nothing in the group moved. |
| `ERROR` | Filesystem refusal — locked file, permissions, unreadable folder. |

Events are grouped by folder in the report. A single failure does not abandon the run: the tool
reports it and continues, so the tree is never left half-tidied by an unrelated locked file.

Exit code is `0` unless at least one `ERROR` occurred. Conflicts and ambiguities are expected
outcomes requiring human attention, not failures of the run.

## Definition of done

Point an instance at a tree and afterwards that tree holds one version of each document, with
lower versions moved into `_superseded` beside where they lived, a readable on-screen report, and
one appended log entry. A dry run produces the identical report and changes nothing. Conflicts and
ambiguities are reported rather than resolved.

## Idempotence

Running the tool twice over the same tree produces no further movement. `_superseded` folders are
underscore-prefixed and therefore outside scope on the second pass; every remaining folder holds
one version per document, so no group has a superseded member.

## Out of scope — hard boundary

Version cleanup tidies versions. It does not assemble binders, does not deploy, does not edit
document content, does not rename files, and does not delete anything. Superseded material is
moved, never removed. Deletion from `_superseded` is a human act.

## Required verification cases

The cases the tool must handle. This is the regression set for any future change, not a record of
one build.

- **Matching** — multi-version groups including `_v10` versus `_v9`; unsuffixed v0; lone versioned
  files; extension mismatch; leading-zero ambiguity.
- **Scope** — nested folders; default underscore skip; all three include forms (a relative pattern
  catching several `_binder` folders at different depths, root-anchored catching only the top one,
  absolute catching one exact folder); a multi-segment pattern traversing an underscore parent
  without processing it; relative and root-anchored excludes.
- **Refusals** — pre-existing archive conflict; malformed JSON; missing root; `..` in a relative
  entry; bare `~`; `~name`; `~/` in the root setting.
- **Repeatability** — a second live run over a tidied tree moving nothing.
<!-- END SOURCE: Infrastructure/version-cleanup/VersionCleanup_Design_v3.md -->

---

<!-- BEGIN SOURCE: Principles/Principles_Decisions_v4.md -->
# Principles — Decisions

> **Version 4** (2026-09-08). Authored fresh in the AIDE rebuild. Compacted
> from v3 where decisions still stand; new decisions added from the design pass.
>
> Created: 2026-08-27 | Last modified: 2026-09-08

## D1 — Principles is a top-level topic, independently deployable

Principles is a cross-cutting concern applying to every project and scenario.
It is a top-level topic, not a subtopic of anything else. The standard works
both as part of AIDE and on its own, because base reasoning guidance is useful
in general AI sessions that are not doing full-AIDE work.

## D2 — Principles is base guidance, not a personalised configuration

The standard defines the portable default. Putting user or team preferences
directly into the base was rejected because the base would stop being portable
and every consumer would inherit one party's local choices.

## D3 — Principles and Working Practices are sibling concerns

Working Practices is not a child of Principles. Principles owns judgement
premises; Working Practices owns practical cross-surface collaboration and
operating conventions. Both can be independently useful.

## D4 — Guidance Profiles use a delta model, housed in Working Practices

Guidance Profiles may add, refine or explicitly override named base guidance
using small deltas. Unmentioned base guidance remains effective.
Equal-specificity contradictions fail visibly unless explicitly ordered.

No generic profile component is created yet — Principles and Working Practices
are the demonstrated consumers, and wider generalisation waits for evidence.

The profile mechanism and its review are housed in Working Practices. The open
question is whether the model earns its place for a solo developer — review
starts from these decisions (formerly D4 and D5).

## D5 — Portability is the defining test, meaning universality

A premise belongs in Principles only if it holds outside AIDE. Anything true
only inside AIDE drops to methodology or working practices. "Interaction"
premises qualify — a universal interaction premise is still a principle. The
real filter is "independent of platform or methodology."

Adopted during the rebuild design pass (2026-09-07) to make the existing
implicit test explicit.

## D6 — The information-holder boundary premise moved to Working Practices

The old P6 ("information holder decides the boundary") was about which
component, project or domain should answer a boundary question — AIDE-context
behaviour, not a universal premise. It fails the portability test and moves to
Working Practices.

## D7 — Authoritative evidence replaced declaration-over-inference wording

The original seed said "Domains are declared, not detected." The confirmed
model now permits implicit resolution from recognised authoritative structures.
Replaced with "authoritative evidence over incidental inference" — the deeper
intent (rejecting accidental presence or proximity inference) is preserved, the
rigid declaration-only rule is not.

The premise's AIDE-specific examples (declared relationships, folder proximity)
are demoted to illustration beneath the premise statement, so they do not read
as part of it.

## D8 — Operational seed behaviours moved without loss

Concrete behaviours from the original seed — coded-reference glossing,
verification before assertion, no-silent-state-change behaviour and others —
are represented in Working Practices. They remain valuable but are operational
conventions rather than root reasoning premises.

## D9 — Definition of done identified as a candidate premise

Definition of done has been promoted to a generic block type owned by Working
Practices, carrying a testable-or-assessable invariant. Whether it also earns a
place as a Principles premise is an open question — it reopens the Principles
element list once Working Practices completes its definition.
<!-- END SOURCE: Principles/Principles_Decisions_v4.md -->

---

<!-- BEGIN SOURCE: Principles/Principles_Design_v4.md -->
# Principles — Design

> **Version 4** (2026-09-08). Authored fresh in the AIDE rebuild from the
> confirmed design pass. Not a modification of v3 — the previous version is a
> source of knowledge only.
>
> Created: 2026-08-27 | Last modified: 2026-09-08

## Brief

**Purpose.** Define the durable, portable reasoning and interaction premises
that guide how any AI reasons, designs, challenges and chooses an approach —
independent of platform or methodology.

**Objective.** Produce a lean, deployable standard that works as part of AIDE
or on its own.

**Defining test.** Portability, which means universality: does the premise hold
outside AIDE? If it only makes sense inside AIDE, it is not a principle — it
belongs to methodology or working practices.

**Definition of done.** The standard exists, passes the portability test for
every premise it contains, is lean enough to be memory-resident alongside other
standards, and covers only premises that earn their place.

---

## Model

Principles is **base guidance** — the default reasoning premises that apply
when no more specific guidance is in effect. It is a top-level cross-cutting
concern and can be deployed independently without full AIDE.

The premises are durable. They change rarely and only on evidence that a premise
is wrong, missing or has been overtaken. Each premise carries its own rationale
so the reasoning is visible without reaching for a separate document.

The standard is the deployable output; this design document is the internal
authority for future change.

---

## Premises

### P1 — Value over compliance

Everything in the system exists to create value for the person doing the work.
Rules are justified when they protect something important, preserve integrity or
enable a capability. Rules for their own sake create friction.

*Test:* what does this enable, and what does compliance cost? Persistent routing
around a rule is evidence the rule or its model should be re-examined.

### P2 — Purpose before mechanism

Ask what something is for before deciding how it works. A mechanism with unclear
purpose cannot be evaluated properly. Purpose settles whether a thing should
exist; mechanism settles how.

*Failure mode:* structural or model problems being answered by adding mechanism.

### P3 — Model before elaboration

State the model before building detailed machinery on it. Elaboration should be
checked against a visible model rather than gradually replacing it.

*Failure mode:* detailed mechanisms make an average or misunderstood premise look
settled merely because later work depends on it.

### P4 — Keep the working set human-comprehensible

The active conceptual working set should remain small enough for the human owner
to hold and challenge at once. Too much detail too early does not only slow
work — it removes the human from meaningful design participation.

Use layered progression: intent and premises, then model, then detail.

### P5 — Authoritative evidence over incidental inference

Prefer explicit declarations and authoritative structural relationships over
conclusions drawn from mere presence, proximity or naming coincidence. Inference
is valid where the governing model explicitly defines what authoritative
evidence supports it.

*Illustration (AIDE-specific, not part of the premise):* a solution's declared
or member-project relationship is authoritative evidence; files merely sharing a
folder do not become related by proximity.

### P6 — Observation over prediction

Design mechanisms against demonstrated problems and repeated failure modes
before adding enforcement for hypothetical ones. Leave room for foreseeable
future capability without building unused machinery prematurely.

### P7 — Loud failure over quiet absorption

When authoritative completion is not possible, stop or surface the unresolved
condition clearly. Do not turn uncertainty, missing information or contradictory
authority into output that merely looks complete.

Failure messages should guide remediation.

### P8 — Verified truth over plausible assertion

Where a fact depends on records, environment state or another authority, verify
it when reasonably available. If it cannot be verified, identify the uncertainty
rather than manufacture a plausible value.

### P9 — Confirmed state over assumed state

Actions that materially change state must not be silently treated as completed
when they were only proposed, generated or handed off. State changes should be
confirmed by the authority, tool or environment that can actually perform or
observe them.

---

## Boundary with Working Practices

Principles states judgement premises. Working Practices states concrete
collaboration and operating conventions that may implement those premises. Both
are top-level sibling concerns — neither is a child of the other.

*Test:* a principle says what underlying premise should guide judgement. A
working practice says how to practically work, communicate or hand over.
Operational conventions stay in Working Practices even when motivated by a
principle.

---

## Guidance Profiles

Guidance Profiles are moved to Working Practices for review there. The concept
is not abandoned — the decisions behind it (the delta model, no generic profile
subsystem yet) travel with it. Review starts from the existing decisions and
asks whether the profile model earns its place for a solo developer.

This design records only that the mechanism exists and is housed elsewhere.

---

## Open items

- **Definition of done** is identified as a candidate premise. It has been
  promoted to a generic block type owned by Working Practices with a
  testable-or-assessable invariant. Whether it also earns a place as a
  Principles premise is open — revisit when Working Practices completes its
  definition.

---

## Intended output

Produce the standard `AIDE_Principles` — short, portable, platform-neutral,
independently deployable. The standard is authored separately once the Standards
component defines its form.
<!-- END SOURCE: Principles/Principles_Design_v4.md -->

---

<!-- BEGIN SOURCE: Standards/_index.md -->
# Standards

Role: component design

Standards defines how to create, design, build, and use a standard within the AIDE framework. It is a methodological component — it does not hold all standards. Individual standards are designed and owned by the component or area they serve, under the what-knows-most-about-it principle.

As a capability, Standards owns the definition of what a standard is, the authoring guidance (including leanness), and the pipeline from reference knowledge to deployed standard.
<!-- END SOURCE: Standards/_index.md -->

---

<!-- BEGIN SOURCE: Standards/Standards_Working_v1.md -->
Standards | working | Standards_Working@v1 | 2026-09-10

## Confirmed items — session 2026-09-09

### Reference concept and its relationship to standards

A reference is a design-time document type recording knowledge and concepts. When reference knowledge needs to reach the AI platform, it is authored into a standard — it is not a separate capability or output type. Standards already encompass information delivery.

The strength model's fourth level (information) exists specifically for this case: reference-origin content carried in a standard for awareness, with no compliance expectation. The pipeline is: knowledge captured as a reference document during design → authored into a standard when it needs to reach the platform → deployed with information-level strength.

Reference is a document type only, not an output type. The distinction matters: a reference informs the design process; a standard is what reaches the platform. The standard is the delivery mechanism for both governance content and reference knowledge.

---

Version note: v1 — initial working document from session 2026-09-09.
<!-- END SOURCE: Standards/Standards_Working_v1.md -->

---

<!-- BEGIN SOURCE: Working Practices/_index.md -->
# Working Practices

Role: component design
Aliases: WP, workprac

Working Practices owns the conventions and behaviours for how an AI and user actually work together across surfaces. Cross-cutting operational conventions covering file handling, work management, content capture, content delivery, and how the human and AI collaborate.

## Parts

**File Operations** (prefix `WP_FileOps_`)
How files are physically managed — delivery, placement, versioning lifecycle, separation of design and output, git integration.

**Work Management** (prefix `WP_WorkManagement_`)
How work is tracked, progresses, and completes — work items, definition of done, pending content, development lifecycle, WIP conventions.

**Capture and Organisation** (prefix `WP_Capture_`)
How content is captured during work and allocated to its home — capture-and-place rules, session-end allocation, process document types.

**Content Delivery** (prefix `WP_ContentDelivery_`)
How content is assembled and delivered to the AI platform — binder concept, inclusion rules, context loading.

**Human-AI Collaboration** (prefix `WP_HumanAI_`)
How the AI works with the human — the human working model, tiering, confidence, drift detection, anomalies channel.
<!-- END SOURCE: Working Practices/_index.md -->

---

<!-- BEGIN SOURCE: Working Practices/FileOps/WP_FileOps_Working_v1.md -->
Working Practices — File Operations | working | WP_FileOps_Working@v1 | 2026-09-10

## Confirmed items — session 2026-09-10

### File delivery rules

Two rules for when files are updated outside of a FileUpdatePackage:

1. **Chat delivery** — when outputting an updated file for download, instruct the user where to save it based on the path in the document header.
2. **Code / Cowork direct file access** — check the file's physical location against the path in the header; move it if they disagree.

### Design and output separation

Design documents and the outputs they produce are separate. The design folder holds the specification. What gets built from it lives where it is consumed:

- Utilities → `_utilities/`
- Skills → deployed to the skills location
- Standards → deployed as capabilities
- Plugins → deployed to the marketplace

The design folder is always "why and how." The output is always elsewhere, wherever it runs.

### Superseded file handling

Git is the version history. The `_superseded` folder pattern is dropped. When a new version lands, the version-cleanup utility deletes the old version from the working tree and commits the deletion with a descriptive message. Rollback means `git checkout` of the previous version.

### Archived file handling

One `_archived` folder at the documentation root. Files that are no longer active but worth keeping — retired references, completed reviews, outdated knowledge. Moving a file there removes it from binder scope (underscore-prefixed folders are outside AIDE processing) while keeping it in the repo and searchable.

### Utility git commit behaviour

Utilities stage and commit their own changes with descriptive messages. When the FileUpdatePackage applies an update, or version-cleanup removes an old file, or the binder builder regenerates, the utility stages the changes, commits with a clear message (e.g. "FUP: applied Principles_2026-09-08"), and the user does not need to remember to commit.

### FUP move action

The FileUpdatePackage needs a move or rename action for when a document's path changes. The header is updated (authoritative change), the FUP manifest records the move (old path, new path), and the utility executes it. Extends the existing action vocabulary (create, replace) with move.

---

Version note: v1 — initial working document from session 2026-09-10.
<!-- END SOURCE: Working Practices/FileOps/WP_FileOps_Working_v1.md -->

---

<!-- BEGIN SOURCE: Working Practices/WP_Capture_Working_v1.md -->
Working Practices — Capture and Organisation | working | WP_Capture_Working@v1 | 2026-09-10

## Confirmed items

### Capture-and-place rules (confirmed earlier, restated)

Three AI obligations: continuous silent capture, placement by destination definitions, batched surfacing at natural breaks. Homeless pieces are named, not dropped. Claude errs toward over-capture.

### Session-end allocation convention (confirmed 2026-09-10)

At the end of a session or at a checkpoint, work through the session's output and confirm what goes where. It is acceptable to park items in WIP for a quick state save, and in a working document for a longer one, but the key discipline is allocating logic to its home. WIP and working knowledge should ultimately move to their destination and not sit in transition for too long.

This convention applies to every session that produces design decisions, not just formal design passes. The allocation step is part of capture-and-place, not a separate process.

### Process document types (confirmed 2026-09-09)

Three process-supporting document types owned by Workflow (Working Practices), not by Documentation Methodology:

- **Report** — a process document recording findings, analysis, or review results
- **Resource** — a reference or knowledge document supporting the work
- **Working document** — holds incomplete material, confirmed items awaiting placement, and in-progress thinking

These are workflow documents, not design outputs. Documentation Methodology owns the doctype mechanics; Working Practices owns these specific types because they serve the working process.

---

Version note: v1 — initial working document from sessions 2026-09-09 and 2026-09-10.
<!-- END SOURCE: Working Practices/WP_Capture_Working_v1.md -->

---

<!-- BEGIN SOURCE: Working Practices/WP_ContentDelivery_Working_v1.md -->
Working Practices — Content Delivery | working | WP_ContentDelivery_Working@v1 | 2026-09-10

## Confirmed items — session 2026-09-10

### Binder concept ownership

The binder exists to solve a workflow problem: assembling and delivering content to the AI platform for use in a session. Working Practices owns the concept — why the binder exists, how it is used, what it includes, how it delivers content. Documentation Methodology owns the binder as a doctype definition — its structure as a document.

### Three-tier inclusion model

What lives in a project folder falls into three tiers based on its relationship to the AI session:

1. **In the binder** — needed for thinking and reasoning. Design documents, and any other file the AI needs to see to do its work. The test: does it need to be there for thinking and reasoning? If so, include it.

2. **Known to the framework** — part of the project but not needed in context. Listed in the folder's `_index.md`. The framework knows it exists, can reference it, but does not load it. Scripts, settings files, assets.

3. **Just present** — incidental files. AIDE has no opinion. Logs, temp files, personal notes.

The binder is the context-loading mechanism. The `_index` is the awareness mechanism. Files that need neither are just files.

The key question for inclusion is not whether a file is a governed document, but whether it is needed for the work. A utility script that is the project's deliverable may belong in the binder when working on that utility, even though it has no declaration header.

---

Version note: v1 — initial working document from session 2026-09-10.
<!-- END SOURCE: Working Practices/WP_ContentDelivery_Working_v1.md -->

---

<!-- BEGIN SOURCE: Working Practices/WP_WorkManagement_Working_v1.md -->
Working Practices — Work Management | working | WP_WorkManagement_Working@v1 | 2026-09-10

## Development lifecycle — phase vs mode (confirmed 2026-09-09)

The development lifecycle has stages: research, design, build, deploy, review. These are **phases** — they describe what kind of work is being done at a point in time.

AIDE implements these phases as **modes**. A mode is a state the AI session operates in, shaped by which standards and tools are loaded and active. The distinction matters because phases are a general concept (any development process has them) while modes are AIDE's specific mechanism for making them real in a session.

The lifecycle concept is owned by Working Practices because it describes how work progresses — it is a workflow concern. Individual modes (the design mode, the build mode) are shaped by the components that own those phases — Project Design owns what happens during design, Build owns what happens during build.

## Pending content — items awaiting placement

The following confirmed items need design work before they can be placed in this document:

- **Work items** — the generic workflow entity (settled 2026-09-07, owned by WP). Definition, two axes (type and state), four states (open, current, closed, plus any additions). Full content is in the settled rebuild decisions
- **Definition of done** — generic block type owned by WP. The testable-or-assessable invariant. Full content in settled rebuild decisions
- **Pending content rule** — WIP holds current state AND pending content for unwritten masters. A master is not authoritative alone between updates. Full content in WIP v22
- **WP1–WP13** — the original Working Practices design items from the old corpus, to be reconciled against current decisions per finding F10 in the rebuild guide

---

Version note: v1 — initial working document from sessions 2026-09-09 and 2026-09-10.
<!-- END SOURCE: Working Practices/WP_WorkManagement_Working_v1.md -->
