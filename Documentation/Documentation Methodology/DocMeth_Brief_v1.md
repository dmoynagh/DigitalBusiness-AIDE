Documentation Methodology — Brief | brief | DocumentationMethodology_Brief@v1 | 2026-09-11

## Purpose

Documentation Methodology provides document structure and authoring standards to documents that opt into them via the AIDE Framework.

It defines structures, behaviours, features and building blocks that govern how a document is composed, how its content is navigated, and how it is used.

It produces standards for two consumers: AIDE framework development, to define and extend the methodology's building blocks; and framework users, to author and use governed documents.

## Value

A framework of flexible consistency that makes documents easier to manage, author and navigate. Documents carry defined structure and parts so that knowledge can be applied to them, not just inferred from content.

The methodology facilitates, it does not dictate. Documents opt in where the methodology adds value, and can use its architecture and features in full or in part. Users and machines can step outside the defined standards and create custom conventions. Where DocMeth conventions are adopted, its full functionality applies. Where they are not, DocMeth assists where it can — but not where its assistance is unwanted. Nothing is enforced; the benefit scales with adoption.

Low friction — adopting the methodology should cost less effort than the value it returns. The framework is scalable, relevant and empowering — it serves the document, not the other way around.

## Objectives

1. An extensible definition structure that lets any component define new document types and building blocks without modifying the methodology itself.
2. A recognition mechanism that lets a consumer identify a governed document and determine its type from a partial read.
3. A composition model that lets documents be assembled from reusable parts without inheritance.
4. Definitions and logic defined once, reused and applied where needed or specified.
5. Support a defined range of document formats. Each format must produce unambiguous output from the same abstractions.
6. Document identity and versioning that is authoritative regardless of filename or location.
7. Consistent writing and integrity conventions across all governed content.
8. Documents are living — they carry the structural information needed to participate in change. They declare their dependencies, can be detected as behind, and can receive updates.

## Requirements

- The definition contract must be self-contained: a consumer must be able to define a new doctype or block type from the standard alone, without inventing conventions.
- The primary format (markdown) must produce deterministic output from the abstractions — no ambiguity in how blocks render.
- Block optionality in a doctype must be separate from the rules governing a block once included.

## Scope and boundaries

**In scope:**

- The meta-model: what a doctype is, what a block type is, how they compose.
- The definition contract: the grammar for defining new doctypes and block types.
- The common block catalogue: blocks available to any document.
- Identity, versioning, and lifecycle states.
- Format support and rendering conventions.
- Language and integrity rules for governed content.
- The binder as a doctype (structure and reading rules; the concept and tooling are owned elsewhere).
- Guidance on where doctype and block-type definitions should live within a component's document set.

**Out of scope:**

- Individual doctype and block-type definitions owned by other components.
- The binder concept, tooling, and inclusion rules (Working Practices / Infrastructure).
- Change management delivery mechanism (Migration).
- Packaging and deployment of standards (Infrastructure / Deployment).
- The strength model vocabulary — required, recommended, optional, information (Standards).
- Path authority and root scope (Core Structure).

## Considerations

**Schema definition placement.** When a component defines doctypes or block types, the default recommendation is a separate schema standard with its own version track, distinct from the component's operational standards. This keeps schema changes and operational changes on independent migration paths and improves discoverability for consumers defining new documents. The split test is the override — if the schema definitions are small and change at the same rate as the operational content, keeping them together is acceptable. DocMeth provides this as guidance; the component owner decides.

**Two-consumer distinction.** The definition contract serves framework developers (defining and extending types); the authored standard serves framework users (authoring and using documents). Both must be served by the same standard, but the definition contract is the gap the current design does not address.

## Linked build outcome

DocumentationMethodology_Standard_v2 — reauthored from the completed design.

## Definition of done — black-box acceptance test

Given only the resulting standard, an independent AI must be able to:

- Define a new doctype
- Define a new block type
- Author a governed document conforming to a known doctype
- Recognise the structure of a governed document it has not seen before
- Apply the versioning rules correctly

— without inventing any convention not stated in the standard.

---

Version note: v1 — standalone brief split from design per the split test. 2026-09-11.
