> identity: Core_Structure_Design@v2 | doctype: design | updated: 2026-09-22

## Summary

Defines how AIDE documentation is physically organised and navigated. Physical folders are the structure. Documents self-declare their identity and path in their headers, which is authoritative — the file system mirrors it. A folder may carry an `_index.md` file: generic folder metadata, not an AIDE-specific concept. AIDE governs it the same way it governs any document — by Declaration opt-in. Role vocabulary replaces the old container labels and doubles as the mechanism by which a document management tool discovers named document sources. There is no logical overlay, no root scope mechanism, and no formal folder-type system — the conventions empower organisation without imposing it.

## Physical folders are the structure

Folder hierarchy on disk is the organisational structure. There is no separate logical layer. Documents live where the folders put them, and paths resolve from the physical tree.

This decision followed from the removal of root scope (see below) and the recognition that the binder manifest preserves relative paths when documents are loaded into flat AI context. The need to reconstruct structure from declarations disappears when the binder already carries it.

## Path authority

The path declared in a document's header is authoritative. The file's position on disk mirrors it. If they disagree, the header is what the document says it is and the file is in the wrong place. This is the same relationship as identity and filename — header wins, filename mirrors.

A mismatch between header path and physical location is a detectable signal AIDE can flag.

### Path maintenance

To change a document's path: update the path in the header. The FileUpdatePackage carries the move to the file system via a move action. For files updated outside an update package in chat, instruct the user where to save based on the header path. For Code or Cowork working directly on files, check the file's physical location against the header path and move if they disagree.

## Role vocabulary

Container labels are replaced by an explicit role vocabulary. Declared in the `_index.md` file via a `role` field. Plain string value; multiple values combine on one line, comma-separated.

Known values:

- **Documentation Solution** — a document source containing projects
- **Documentation Project** — a document source, standalone or within a solution
- **Component** — a framework component
- **Part** — a segment or grouping within a scope
- **Area** — same as Part for now, flagged as potentially distinct

Using a known value gives AIDE inference — it recognises what the folder is for. Using a custom value works, it just is not one AIDE knows about. The list grows as new kinds demonstrate the need. No nesting rules are defined — the values describe what something is, not what it is allowed to contain.

## Folder metadata — `_index.md`

A file named `_index.md` placed in a folder describes the folder and indexes what it contains. It is a generic folder metadata concept, not owned or invented by AIDE — AIDE is a consumer of it, the same as any other tool that wants to read or write a folder's metadata as long as it respects the structure defined here.

AIDE governance works the same way it works for any document: add a Declaration and the file becomes governed. The doctype (`index`) gives it schema and change management under Documentation Methodology's rules. A bare `_index.md` with no Declaration is still valid folder metadata for any tool that reads it — it just isn't governed by AIDE.

### Purpose

Describes what this folder is (via the role field) and indexes what it contains. In a mixed folder holding multiple parts, the body carries a parts list. Each entry in the parts list has a name, a role, and a description, and optionally a file-prefix convention and an explicit file list.

### When it earns its place

A folder must have an `_index.md` to be discoverable as a document source — see Document source discovery, below. Below source level, the `_index` remains optional. It earns its place when a folder's contents are not obvious from the files alone — typically when a folder holds multiple parts or when a reader needs orientation. Single-part folders with a handful of clearly-named files do not need one.

### Document source discovery

When a `_index.md` declares a role of Documentation Solution or Documentation Project, it identifies the folder as a named document source. The name is the heading. A document management tool discovers sources by scanning configured roots for `_index.md` files and reading their roles — role and heading are sufficient, no separate field is needed. Sessions reference sources by name; the tool maps names to local paths.

Source naming resolution:

- Solution name alone: `AIDE_Documentation`
- Project name alone (short form, when unambiguous): `Core`
- Qualified form (when project names collide): `AIDE_Documentation\Core`

### Format

Markdown is the natural choice when the content mixes structured fields (role, aliases, parts, files) and descriptive prose. It handles the dual-consumer requirement: structured fields for machine parsing, prose for human and AI orientation. If a future `_index` is primarily machine-consumed structured data, yaml or json would be the right format. Format fits the job.

### Document ordering within the `_index`

1. Declaration — first line, fixed (DocMeth)
2. Heading — names the scope
3. Role — identity field
4. Aliases — identity field
5. Description — free prose
6. Parts — defined block (if used)
7. Files — defined block (if used)
8. Free content — notes, orientation, anything the author wants

### Versioning

Index files are governed documents (by Declaration opt-in) but do not carry versioned identities. The Declaration is `> identity: _index | doctype: index` — no `@v*` suffix. The file reflects current state, not a point-in-time publication.

## Root scope — parked

Root scope was explored as a mechanism for declaring a folder as a root of a design project, component design, or similar container. It was parked: no consumer exists. Physical folder structure provides organisation, the binder manifest preserves paths for context loading, and the path in document headers provides self-description. Root scope was compensating for context flattening, which the binder already solves.

Root scope returns if a feature demonstrates it needs a formal root declaration.

## Binder as structure preservation

The binder manifest records relative paths for every document it includes. When documents leave the file system and enter flat AI context, the manifest is what preserves their structural relationships. This is not a new mechanism — binders already do this. It is documented here because it is the reason root scope is unnecessary and physical folders are sufficient.

---

Version note: v2 — Retired the "AIDE document" framing: `_index.md` is generic folder metadata, AIDE a consumer, governed by Declaration opt-in like any other document. Replaced the four container labels with an explicit role vocabulary (Documentation Solution, Documentation Project, Component, Part, Area) that doubles as document source discovery. Added document ordering and versioning conventions for index files. 2026-09-22. Replaces v1.
