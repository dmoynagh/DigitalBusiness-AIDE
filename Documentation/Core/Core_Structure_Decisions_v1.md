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
