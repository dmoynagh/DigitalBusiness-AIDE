> identity: Core_Structure_Standard@v1 | doctype: standard | updated: 2026-09-22 | uses: DocumentationMethodology_SchemaAuthoring_Standard@v1

# Core — Structure Standard

Use when creating, modifying, or validating an `_index.md` file, or working with folder metadata, document sources, or role vocabulary.

## Applicability

Information. This standard applies when creating an `_index.md`, changing a folder's role or contents, deciding whether a folder needs an `_index.md`, or working out how a document management tool discovers document sources.

## Schema definitions

Information. The doctype and block types Core owns, using the Documentation Methodology definition contract.

### Index (doctype)

- **Purpose:** Folder metadata file. Describes what a folder is and indexes what it contains. Not AIDE-specific — a generic folder metadata concept. AIDE governance by Declaration opt-in: add a Declaration with `doctype: index` and DocMeth rules apply. When the role declares Documentation Solution or Documentation Project, the file identifies a document source for the document management tool. One per folder.
- **Owner / Residence:** Core / Structure
- **Format constraint:** markdown.
- **Format conventions:** filename is `_index.md`. Leading underscore sorts it to the top of a directory listing. Identity is always `_index` — no per-instance identity. No versioning.
- **Included block types:** Parts (optional), Files (optional).
- **Identity fields (not block types):** role, aliases — key-value lines after the heading, before the body.

### Parts (block type)

- **Purpose:** Declares segments within the folder's scope — virtual subfolders grouping related files without a physical directory. Each entry carries the same metadata a subfolder's own `_index` would carry.
- **Owner / Residence:** Core / Structure
- **Fields per entry:** name (required), role (required), description (required), prefix (optional — filename convention identifying members), files (optional — explicit list of members not covered by the prefix).
- **Optionality:** optional within the Index doctype.
- **Density:** standard (one entry per part, descriptive).
- **Recognition:** by subheading — `Parts`.

### Files (block type)

- **Purpose:** Carries metadata for files that do not or cannot carry their own Declaration. The tier 2 awareness mechanism from the three-tier file model — the framework knows a file exists because the `_index` lists it.
- **Owner / Residence:** Core / Structure
- **Fields per entry:** filename (required), info (required — freeform text, no enforced structure).
- **Optionality:** optional within the Index doctype.
- **Density:** compact (table).
- **Recognition:** by subheading — `Files`.

## Operational guidance

### Document ordering within the `_index`

1. Declaration — first line, fixed (DocMeth)
2. Heading — names the scope
3. Role — identity field
4. Aliases — identity field
5. Description — free prose
6. Parts — defined block (if used)
7. Files — defined block (if used)
8. Free content — notes, orientation, anything the author wants

### Role vocabulary

Known values:

- **Documentation Solution** — a document source containing projects
- **Documentation Project** — a document source, standalone or within a solution
- **Component** — a framework component
- **Part** — a segment or grouping within a scope
- **Area** — same as Part for now

Multiple values separated by comma. Custom values are permitted — they work, they just aren't values the framework recognises. The list grows as new kinds demonstrate the need.

### When the `_index` is required

A folder must have an `_index.md` to be discoverable as a document source (Documentation Solution or Documentation Project). Below source level, the `_index` is optional — it earns its place when a folder's contents are not obvious from the files alone.

### Identity and versioning

Every `_index.md` carries the same identity: `_index`. Scope disambiguation comes from the heading, the binder source path, or the filesystem. No versioning — the file reflects current state. The Declaration is `> identity: _index | doctype: index`.

### Document source discovery

The document management tool discovers sources by scanning configured roots for `_index.md` files and reading their roles. Sessions reference sources by name (the heading); the tool maps names to local paths.

Source naming resolution:

- Solution name: `AIDE_Documentation`
- Project short form (when unambiguous): `Core`
- Qualified form (when project names collide): `AIDE_Documentation\Core`

### Free content

After the defined blocks, the author may include any additional content that aids understanding — notes, references, orientation material. This is permitted but not governed; it is not part of the Index doctype's composition.

### Creating an `_index`

Place an `_index.md` in the folder. Add a Declaration (`> identity: _index | doctype: index`) for AIDE governance. Add a heading naming the scope, role and aliases fields, a description, and any applicable blocks. A bare `_index.md` with just a heading and role is valid folder metadata. A fully declared one with Parts and Files is a complete index.

### Modifying an `_index`

The `_index` reflects current state — update it when the folder's structure, role, or contents change. Parts entries migrate to subfolders (with their own `_index`) when the split test is met. Document listings are not maintained as structural elements; files carry their own identity in their Declarations.

---

Version note: v1 — initial standard, absorbing the retired Core Schema Standard's Index doctype and adding the Parts and Files block types, role vocabulary, and document source discovery guidance from Core_Structure_Design_v2 and Core_Structure_Decisions_v2. 2026-09-22.
