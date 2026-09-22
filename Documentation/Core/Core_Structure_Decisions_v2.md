> identity: Core_Structure_Decisions@v2 | doctype: decisions | updated: 2026-09-22

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
- Container description → the `_index.md` folder metadata file
- Classification ("this is a document source") → the role field in `_index.md`

Root scope was compensating for a problem (context flattening) that binders already solve. Identified during discussion as the likely origin of the concept — when files were in flat folders for context loading, logical structure needed to be declared. With binders carrying relative paths, the need disappeared.

## Container labels — vocabulary not types

Considered whether folder roles should be a formal type system with defined nesting rules (solution design contains project designs, project designs contain component designs, etc). Decided against: the labels describe what something is, not what it is allowed to contain. Nesting rules would impose structure the facilitate-not-constrain principle argues against, and no current functionality depends on knowing what's inside what.

Four labels were originally chosen from existing vocabulary Dave already uses (solution design, project design, component design, area/part) — mirroring the .NET solution/project mental model. This session replaces them; see "Role vocabulary replaced" below.

## AIDE document naming

Explored several options for the file name:
- `_AIDE.md` — sorts to top but brands every folder with the framework name
- Named after the container (e.g. `Principles_AIDE.md`) — self-describing but doesn't stand out
- `_folder.md` — generic but describes the container, not the function
- `_index.md` — generic, familiar concept, describes the function (indexing), room to grow

Chose `_index.md`. The underscore sorts it to the top. "Index" describes what it does rather than what it is about. The name is generic enough to work for any project whether using AIDE fully or partially. At the time, the concept was still called the "AIDE document" within framework terminology, with the file on disk given a name that doesn't advertise. This session removes that framing entirely — see "Generic folder metadata, not AIDE-specific" below.

## Path authority chain

Applied the same pattern as identity and filename: header is authoritative, file system mirrors. This was a deliberate alignment — both follow the principle that a document should be self-describing and survive being detached from its context. A file pasted without its folder still states where it belongs.

Considered whether the physical-folders-as-structure decision created tension with header-as-authority. It does not — the physical structure is the expected organisation, the header is what the document says about itself. They agree in the normal case; the header wins on conflict.

## Three-tier file model

Arose from the question of what the binder should include. Initially framed as "governed documents only" versus "everything." Dave's test was sharper: does it need to be there for thinking and reasoning? A utility script that is the project's deliverable needs to be in context when working on that utility. A log file never does.

The three tiers:
1. In the binder — needed for thinking and reasoning in the AI session
2. Known to the framework — listed in the `_index`, not loaded into context. The framework knows it exists
3. Just present — incidental files AIDE has no opinion about

This is recorded as a decisions entry because it affects binder design (owned by Working Practices / Content Delivery) and will be referenced from there. The structural implication — the `_index` as the awareness mechanism for tier 2, via the Files block — belongs here.

## Design and output separation

Design documents and the outputs they produce are separate. The design folder holds the specification; what gets built from it lives where it is consumed. This arose from Infrastructure where utility design docs sat alongside the Python scripts they specified. The scripts are outputs, not design — they belong where they run (_utilities), not where they were designed.

The principle applies broadly: utilities to _utilities, skills to the skills deployment location, standards to capabilities, plugins to the marketplace. The design folder is always "why and how"; the output is always elsewhere.

## Generic folder metadata, not AIDE-specific

The `_index.md` was originally conceived as an "AIDE document" — a framework concept with a generic filename. Reframed this session: it is a generic folder metadata file. AIDE is a consumer. The generic name was already chosen to avoid framework branding; the reframe makes that the defining characteristic, not a naming convenience. Other tools can read and write the file as long as they respect the structure. AIDE governance is by Declaration opt-in, the same mechanism every other document uses.

## Role vocabulary replaced

Old container labels (`solution design`, `project design`, `component design`, `area / part`) replaced with explicit names: Documentation Solution, Documentation Project, Component, Part, Area. The old labels described what a folder was used for; the new ones name what it is. Documentation Solution and Documentation Project double as document source type identifiers for the document management tool — no additional field required.

## Document source discovery from role

Rather than a separate `document-source` field, documentation solutions and projects are inherently document sources. The document management tool discovers them by scanning configured roots, finding `_index.md` files, and reading their roles. The alternative — an explicit field — was rejected because it would duplicate what the role already says. Source naming uses the heading, with qualified form (solution\project) when project names collide.

## No document root field

The `_index.md` sits in the folder it describes — its location is the document root. A field declaring "documents are elsewhere" was considered and rejected because it contradicts the file's fundamental concept.

## Index identity is `_index`, same for every instance

Follows the default convention that identity matches filename. Scope disambiguation comes from the heading, the binder source path, or the filesystem. Scope-specific identities (`Core_Index`, `WP_Index`) were considered and rejected — they break the default, create per-file identity maintenance, and every delivery context already provides disambiguation.

## No versioning on index files

The index reflects current state. Version history is not meaningful for folder metadata. The doctype can state that versioning is not used even though the file is governed.

## Parts as a block type

A part is a virtual subfolder — same metadata as a physical subfolder's `_index`, without the directory. Fields: name, role, description, prefix (optional), files list (optional, for members not covered by the prefix). When a part outgrows its host, it promotes to a subfolder with its own `_index` — the data migrates, same split-test logic.

## Files as a block type

Tier 2 of the three-tier file model made concrete — metadata for files that do not or cannot carry their own Declaration. Two-column structure: filename and freeform info. No enforced column structure in the info field.

## Document listing dropped as a structural element

Every field in the old document tables (prefix, name, version, type) duplicates information each file carries in its own Declaration. Maintained duplicates drift — several existing `_index` files already had stale version numbers. An author can include a document listing as free content for orientation, but it is not part of the Index doctype's composition.

## Components table, cross-cutting files, and key definitions sections dropped

All were duplicates of information carried authoritatively elsewhere (the AIDE Map, the Core Design, each component's own `_index`). Same pattern as the document listing: useful editorial content stays as free content at the author's discretion, not structural metadata.

## Versioning detection model

Declaration presence is the gate — no Declaration, no versioning logic. Detection priority: (1) doctype declaration overrides everything, (2) identity `@v*` suffix, (3) filename `_v*` convention. Ungoverned files with coincidental `_v##` suffixes are ignored. User can instruct versioning be applied to such files, which causes the identity to be written in — the file becomes governed from that point.

---

Version note: v2 — Added this session's decisions: generic folder metadata reframe, role vocabulary replacement, document source discovery, no document root field, fixed `_index` identity, no versioning on index files, Parts and Files block types, dropped document-listing and other duplicate structural elements, versioning detection model. All v1 decisions preserved. 2026-09-22. Replaces v1.
