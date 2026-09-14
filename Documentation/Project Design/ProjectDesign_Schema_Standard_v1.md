> identity: ProjectDesign_Schema_Standard@v1 | doctype: standard | updated: 2026-09-14 | uses: DocumentationMethodology_SchemaAuthoring_Standard@v1

# Project Design — Schema Standard

The doctypes and block types defined by Project Design, using the Documentation Methodology definition contract.

## What this standard is for

Information. This standard defines Project Design's types — the block types that carry the functionality, and the doctypes that host them. For the definition grammar, see the Documentation Methodology Schema Standard. For rules governing how these types are used, see the Project Design Standard.

## Block types

### Brief

- **Purpose:** Define the problem and the bar for success before designing. The problem space; the design is the solution space.
- **Subheadings:**
  - Purpose (required)
  - Objectives (required)
  - Definition of done (required) — see Included blocktypes
  - Requirements (required)
  - Scope and boundaries (required)
  - Linked build project or build outcome (required when the design feeds a build, omitted otherwise)
  - Considerations (optional)
  - Target / outcome (optional)
- **Included blocktypes:** Definition of done (required) — a generic block type owned by Working Practices. The brief consumes it because its invariant (testable-or-assessable) has demonstrated shared meaning beyond the brief. Provisional: the defining standard is not yet published; `uses` will be updated when Working Practices publishes its schema.
- **Recognition:** by subheading — `Brief`, or by placement at the head of a design document.

Information. The brief is a composite block — its subheadings form a unit that can sit inline in a design or be the body of a standalone brief document. The split test governs when it branches out. Custom content beyond the defined subheadings is permitted. What each subheading should contain and the boundary tests between them are defined in the Project Design Standard.

Information. The Definition of done block type is owned by Working Practices, whose schema standard is not yet published. When it is, `ProjectDesign_Schema_Standard` will add it to its `uses` field.

### Work register

- **Purpose:** The ledger of confirmed work owed and not yet delivered.
- **Fields:**
  - source (required)
  - commitment (required)
  - what must change (required)
  - target (required)
  - state (required) — owed, handed off, returned pending reconciliation, or reconciled
  - origin tag (required) — design-generated or directly-entered
  - handoff reference (optional)
  - return reference (optional)
  - area (optional)
- **Recognition:** by subheading — `Work register` or `Register`.

Information. The register can sit inline in the design for small projects and split to its own document per the split test. Writing rules, state semantics, immutability after handoff, and maintenance rules are defined in the Project Design Standard.

### Overview

- **Purpose:** A project-scale snapshot — concise context for anything discussed without re-reading the documentation set. Also a deviation detector.
- **Recognition:** by subheading — `Overview`, or by placement in a design document.

Information. The overview can sit inline in a design or brief for small projects and be the body of a standalone overview document. The split test governs when it branches out. Content guidance and the summary suppression rule are defined in the Project Design Standard.

## Doctypes

### Brief

- **Purpose:** A standalone document hosting the brief block.
- **Included blocktypes:** Brief (required), Contents (recommended), Version note (optional).

### Design

- **Purpose:** The confirmed model and approach — the authoritative delivery of the brief. Sufficient on its own to produce outcomes. Carries its own live reasoning inline.
- **Included blocktypes:** Brief (optional — inline per the split test), Work register (optional — inline per the split test), Contents (recommended), Summary (recommended), Version note (optional).

Information. Design composition is criteria and advice, not a schema. The criteria, advice, reasoning routing, and coverage check are defined in the Project Design Standard. Placement rules and the summary suppression rule are defined in the Project Design Standard.

### Overview

- **Purpose:** A project-scale snapshot — concise context for anything discussed without re-reading the documentation set. Also a deviation detector.
- **Included blocktypes:** Overview (required), Contents (optional), Version note (optional).

Information. The overview sits inline in the design or the brief for small projects and splits to its own document per the split test. Content guidance and the summary suppression rule are defined in the Project Design Standard.

### Work register

- **Purpose:** A standalone document hosting the work register block.
- **Included blocktypes:** Work register (required), Contents (optional), Version note (optional).

---

Version note: v1 — initial schema standard. Defines Project Design's three block types and four doctypes using the Documentation Methodology definition contract. 2026-09-12.
