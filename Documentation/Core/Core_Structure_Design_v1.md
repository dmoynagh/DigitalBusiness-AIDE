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
