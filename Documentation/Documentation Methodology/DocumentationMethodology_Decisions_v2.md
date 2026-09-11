Documentation Methodology — Decisions | decisions | DocumentationMethodology_Decisions@v2 | 2026-09-11

## D1 — DocMeth owns grammar only, not individual definitions

Individual doctype and block-type definitions live with the component that knows the most about them. DocMeth defines what a doctype is, what a block is, how they compose, and the common catalogue of blocks usable by any document. This is the "grammar versus vocabulary" line: DocMeth owns the rules of the language; components own the words.

The alternative — DocMeth as a central registry of all types — was considered and rejected. A registry would accumulate detail from every component and become the single largest document in the framework, would require every component to file definitions with DocMeth rather than owning them, and would create a coordination bottleneck where no component can define a new type without a DocMeth update. The what-knows-most-about-it ownership rule settles it.

## D2 — Composition, not inheritance

Doctypes compose blocks by inclusion. A doctype includes a block as defined and does not modify it — no field suppression, no field addition, no shape adjustment on inclusion. Where two doctypes need different shapes, those are two blocks sharing a smaller common block if warranted.

Override-on-include is inheritance under another name: it brings back precedence when two doctypes adjust the same block differently, drift when the base changes underneath, and a reader unable to tell what shape a block actually has. The accepted cost is duplication between near-identical blocks, which is visible; override chains are not. Revisit on a demonstrated case per the demonstrated-requirement rule.

Also cut as over-engineered: multiple doctype inheritance, abstract doctypes, block self-assignment to doctypes (push model), collision precedence machinery.

## D3 — Declaration as conformance marker and activation trigger

The Declaration's presence is both the corpus recognition mechanism (is this a governed document?) and the activation trigger (DocMeth applies). This dual role avoids needing a separate governance flag. A document without a Declaration is outside the methodology — legitimate, at the user's risk.

The Declaration is fixed, compact, and not overridable. Its fields (title, doctype, identity, date) are the minimum needed for recognition and identity. Variable-length content was kept out — the Dependencies block is separate specifically because adding a variable-length list to the Declaration would change its character.

## D4 — Dependencies as a separate block, moved to header

Dependencies was originally a footer block in the old model. Moved to header, immediately after Declaration, because the currency check gates use — a partial read from the top must be able to answer "may I use this" without reading to the end. This is the boundary proximity principle applied to the consumer that runs first.

Kept as a separate block rather than folded into the Declaration for the reason stated in D3: Declaration is fixed and compact.

## D5 — Common catalogue scope

The common catalogue holds blocks usable by any document regardless of component: Declaration, Dependencies, Header, Footer, Contents, Summary, Version note. Seven blocks.

Tags was parked in the original catalogue session (no demonstrated consumer), resurrected as a Core capability (2026-09-09), and confirmed as Core-owned during this design pass. Its block definition belongs to Core, not to DocMeth's common catalogue, because DocMeth's grammar already describes how any component-defined block places into a document.

References remains parked — no consumer has appeared. It returns on its own merits when one does.

## D6 — Contents and Summary are optional

Both blocks earn their place by function, not by rule. Contents earns inclusion when a reader could not decide from the Declaration alone whether to keep reading. Summary earns inclusion when the document's substance needs a compressed statement. Machine-focused documents (standards delivered as skills, tools, utilities) often need neither.

The doctype owner decides the default for their type: on, off, or conditional. This avoids DocMeth mandating blocks that add no value in many document types while ensuring they appear where they do add value.

## D7 — The Contents/Summary edge as a grammar rule

Contents maps what is where (navigation); Summary gives what the document establishes (substance). The edge between them was flagged by Standards as a common issue for standards authors and carried to DocMeth as document-structure grammar.

DocMeth owns the edge definition because it defines both blocks. Standards raised the issue; DocMeth resolves it as a standing rule. The rule is brief because the blocks' own definitions already do most of the work — Contents is "a semantic map" and Summary is "what the document establishes." The edge rule reinforces that their purposes must not blur.

## D8 — The split test as grammar

The split test (externalise a block when keeping it in would compromise the primary role of its host) was carried from Project Design as part of the grammar. It belongs in DocMeth because it governs the relationship between a block and its host document — a structural concern, not a design-process concern.

The split test is the inverse of the elasticity model: same content, container chosen by scale. A brief block lives inline for a small project and branches to its own document when it grows. The trigger is not a size threshold but a functional test — does the block's presence compromise the host?

## D9 — Language rules as grammar

The four language rules (plain English, meaning first / code second, use existing terms, flag new terms) were carried from the design-approach work. They belong in DocMeth because they govern how any governed document is written, not just design documents.

The aide-design-check skill currently carries these rules. Once DocMeth's standard is authored, the skill consumes the standard rather than carrying the rules itself. The design-approach skill's own placement question (Project Design's standard) is about the design checks, not the language rules — those are separable.

## D10 — Rendering model without explicit mapping tables

The format rendering rule states that each format's own existing standards provide a clear default mapping. No additional mapping tables are authored at this stage — markdown conventions, HTML semantic elements, YAML mappings, and JSON key-value structures all provide unambiguous defaults for the abstractions DocMeth defines (fields, compact, expanded, containers).

The original design explored a per-format default mapping table. On discussion, the conclusion was that these mappings are implicit in the format itself and spelling them out would be speculative work for formats with no consuming documents (no document currently uses HTML, YAML, or JSON as its primary format). The portability flag is the safety net: it catches real problems at the point they appear.

If a format gap appears — where the format's own conventions do not provide an unambiguous answer — DocMeth authors the mapping then, not before.

## D11 — No Infrastructure link for rendering

The WIP assigned "renderers per format" to Infrastructure. On review, this was answering a question that doesn't exist: the grammar tells the AI how to express a block in each format, and the AI applies those rules when authoring. No separate renderer utility is needed.

If a utility ever needed to render blocks (a binder builder producing HTML output, for example), that utility's spec would consume DocMeth's grammar. But the grammar is complete without a renderer spec alongside it.

## D12 — The ownership-designation rule

Defining any doctype or block type must include naming its owner and residence. This was carried from Project Design where it was identified as a recurring problem — things get defined, residence gets deferred, and placement has to re-derive a decision that was obvious at definition time.

DocMeth owns the requirement to designate a home. Each definition states which home. Clean separation: the grammar says "you must name an owner"; each definition does so.

## D13 — Lifecycle states are grammar

Three semantic lifecycle states (Current, Superseded, Archived) belong to DocMeth because they describe what state any governed document can be in, regardless of who owns the doctype. They are independent of physical storage — Working Practices owns how the file system represents them.

The legacy binder carried these in §13. They survived the old-material review because they are genuinely common across all documents and are not specific to any workflow or component.

## D14 — The claimed-versus-verified rule

Do not compose plausible metadata where the fact should be observed or read. This rule was a requirement-weight item in the legacy standard and has been a recurring problem in practice — most notably composed timestamps in messaging that were future-dated or wrong because a value was produced rather than read.

The rule belongs in DocMeth as a document-integrity rule because it governs how metadata is produced in any governed document. It joins the four language rules as a fifth writing/integrity rule.

---

Version note: v2 — decisions authored from the design pass, 2026-09-11. D13-D14 added from legacy binder review. Replaces the v1 shell.
