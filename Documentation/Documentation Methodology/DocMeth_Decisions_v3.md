Documentation Methodology — Decisions | decisions | DocMeth_Decisions@v3 | 2026-09-11

## D1 — DocMeth owns grammar only, not individual definitions

Individual doctype and block-type definitions live with the component that knows the most about them. DocMeth defines what a doctype is, what a block is, how they compose, and the common catalogue of blocks usable by any document. This is the "grammar versus vocabulary" line: DocMeth owns the rules of the language; components own the words.

The alternative — DocMeth as a central registry of all types — was considered and rejected. A registry would accumulate detail from every component and become the single largest document in the framework, would require every component to file definitions with DocMeth rather than owning them, and would create a coordination bottleneck where no component can define a new type without a DocMeth update. The what-knows-most-about-it ownership rule settles it.

## D2 — Composition, not inheritance

Doctypes compose blocks by inclusion. A doctype includes a block as defined and does not modify it — no field suppression, no field addition, no shape adjustment on inclusion. Where two doctypes need different shapes, those are two blocks sharing a smaller common block if warranted.

Override-on-include is inheritance under another name: it brings back precedence when two doctypes adjust the same block differently, drift when the base changes underneath, and a reader unable to tell what shape a block actually has. The accepted cost is duplication between near-identical blocks, which is visible; override chains are not. Revisit on a demonstrated case per the demonstrated-requirement rule.

Also cut as over-engineered: multiple doctype inheritance, abstract doctypes, block self-assignment to doctypes (push model), collision precedence machinery.

## D3 — Declaration as conformance marker and activation trigger

The Declaration's presence is both the corpus recognition mechanism (is this a governed document?) and the activation trigger (DocMeth applies). This dual role avoids needing a separate governance flag. A document without a Declaration is outside the methodology — legitimate, at the user's risk.

The Declaration is fixed and not overridable. Its core fields (identity, doctype, date) are the minimum needed for recognition. Dependencies and blocktypes render within the Declaration blockquote because they are part of the machine-readable header, not separate blocks.

## D4 — Dependencies in the Declaration

Dependencies was originally a separate header block, then a footer block in the old model. It now renders within the Declaration blockquote as a labelled field using the grouping syntax for ownership tracking. The currency check gates use, so a partial read from the top must be able to answer "may I use this" without reading to the end.

## D5 — Common catalogue scope

The common catalogue holds blocks usable by any document regardless of component: Declaration, Dependencies, Header, Footer, Contents, Summary, Version note, Title, Description. Nine blocks.

Tags was parked in the original catalogue session (no demonstrated consumer), resurrected as a Core capability (2026-09-09), and confirmed as Core-owned. Its block definition belongs to Core, not to DocMeth's common catalogue. Tags is deferred from the definition contract — the concept is sound but ahead of demonstrated requirement.

References remains parked — no consumer has appeared. It returns on its own merits when one does.

## D6 — Contents and Summary are optional

Both blocks earn their place by function, not by rule. Contents earns inclusion when a reader could not decide from the Declaration alone whether to keep reading. Summary earns inclusion when the document's substance needs a compressed statement. Machine-focused documents (standards delivered as skills, tools, utilities) often need neither.

The doctype owner decides the default for their type: on, off, or conditional. This avoids DocMeth mandating blocks that add no value in many document types while ensuring they appear where they do add value.

## D7 — The Contents/Summary edge as a grammar rule

Contents maps what is where (navigation); Summary gives what the document establishes (substance). The edge between them was flagged by Standards as a common issue for standards authors and carried to DocMeth as document-structure grammar.

DocMeth owns the edge definition because it defines both blocks. Standards raised the issue; DocMeth resolves it as a standing rule.

## D8 — The split test as grammar

The split test (externalise a block when keeping it in would compromise the primary role of its host) was carried from Project Design as part of the grammar. It belongs in DocMeth because it governs the relationship between a block and its host document — a structural concern, not a design-process concern.

The split test is the inverse of the elasticity model: same content, container chosen by scale. The trigger is not a size threshold but a functional test — does the block's presence compromise the host?

## D9 — Language rules as grammar

The four language rules (plain English, meaning first / code second, use existing terms, flag new terms) were carried from the design-approach work. They belong in DocMeth because they govern how any governed document is written, not just design documents.

The aide-design-check skill currently carries these rules. Once DocMeth's standard is authored, the skill consumes the standard rather than carrying the rules itself.

## D10 — Rendering model without explicit mapping tables

The format rendering rule states that each format's own existing standards provide a clear default mapping. No additional mapping tables are authored at this stage. The portability flag is the safety net: it catches real problems at the point they appear.

If a format gap appears — where the format's conventions do not provide an unambiguous answer — DocMeth authors the mapping then, not before.

## D11 — No Infrastructure link for rendering

The grammar tells the AI how to express a block in each format, and the AI applies those rules when authoring. No separate renderer utility is needed. If a utility ever needed to render blocks, that utility's spec would consume DocMeth's grammar.

## D12 — Owner and residence is optional, not required

Defining any doctype or block type should include naming its owner and residence, but this is implicit from the hosting location for most definitions. Stated only when the hosting location doesn't make ownership obvious (e.g. common catalogue blocks, cross-component definitions). The process discipline — decide the owner when you define the thing — stays as methodology.

Supersedes the original required rule carried from Project Design. The requirement was about ensuring the decision is made at definition time, not about mandating a field in every definition.

## D13 — Lifecycle states are grammar

Three semantic lifecycle states (Current, Superseded, Archived) belong to DocMeth because they describe what state any governed document can be in, regardless of who owns the doctype. They are independent of physical storage — Working Practices owns how the file system represents them.

## D14 — The claimed-versus-verified rule

Do not compose plausible metadata where the fact should be observed or read. This rule belongs in DocMeth as a document-integrity rule because it governs how metadata is produced in any governed document. It joins the four language rules as a fifth writing/integrity rule.

## D15 — The definition contract is facilitative, not prescriptive

The definition contract is the language for defining doctypes and block types. Name and purpose are the only required properties. Everything else is available vocabulary — stated when it adds value, omitted when it doesn't. A minimal definition is two lines. A complex definition uses as many properties as it needs.

The alternative — a mandatory property list where every definition must address every field — was rejected as counter to the facilitate-not-control principle. It would create boilerplate in simple definitions, discourage defining small utility blocks, and impose ceremony that adds no value where the content shape is obvious.

## D16 — Declaration header evolved to labelled blockquote

The original Declaration was a single pipe-delimited line with positional fields (title, doctype, identity, date). The evolved form is a multi-line blockquote with labelled fields, accommodating dependencies and blocktypes within the Declaration rather than as separate header blocks.

Labelled fields replace positional because the field set has grown beyond what positional ordering can carry unambiguously. Blockquote provides visual distinction and structural detectability in markdown.

## D17 — Title separated from Declaration

Title is a self-describing block recognised by placement (at the top of the document), not a Declaration field. This follows the four self-describing blocks model (title, description, contents, summary) where title and description are inferred from natural document convention in prose formats and keyed in structured formats.

The Declaration carries the machine-readable identity; title is the human-readable name. They serve different consumers and belong in different blocks.

## D18 — Dependency implications as a definition property

Both doctypes and block types carry dependency implications — the standard(s) a document inherits by using the type. A block type is defined in a standard; using it creates a dependency. Without this property, the change management chain breaks: there is no way to know a document is behind when the defining standard changes.

Dependencies are populated in the document header automatically from the types the document uses. This is integral to the living-document objective, not an optional convenience.

## D19 — Format constraint as a doctype property

A doctype can constrain the permitted formats when the type requires it. Standards must be markdown for session loading. Settings files must be JSON or YAML. The format-fits-the-job principle says format is a considered choice — the doctype is the thing that carries the consideration. Constraining the options is not dictating; it's the type knowing what it needs.

## D20 — Density has no default

Neither compact nor expanded is assumed as a default. Density is stated when it matters (blocks with fields that could render either way), omitted when the content shape makes the rendering obvious, and not applicable to blocks without structured fields. This avoids forcing half of all definitions to override a default that doesn't suit them.

## D21 — Tags deferred from the definition contract

The tags concept is sound — a general-purpose identification and grouping primitive owned by Core, with group ownership and collapse behaviour. However, its primary customer (root scope scanning) lost urgency when root scope was parked. The grouping syntax is independently useful in dependency and blocktype fields. Tags returns to the definition contract when a consumer demonstrates need.

## D22 — Containers settled at four, general role deferred

Four containers are settled: Header, Footer, Body, and Declaration. Any block type can serve as a container by being targeted for placement by other blocks. New containers are created by defining a block type and having the doctype position it — no additional mechanism needed. A general formal treatment of the container role is deferred until the four settled containers prove insufficient.

## D23 — Lifecycle terminal path dropped from doctype contract

A doctype may describe completion, withdrawal, or other terminal paths in its documentation, but this is not a formal property in the definition contract. A declared property would require every definition to address it even when the answer is "none." The capability exists without mandating the field.

## D24 — Self-describing blocks and the aggregation model

Four blocks make a document self-describing: title, description, contents, summary. Title and description are new common blocks added to the catalogue. They are recognised by placement in prose formats and by key in structured formats, following the format rendering rule — no special inference machinery.

The aggregation model consumes self-describing blocks: one model, several output forms (index, navigation view, concatenated collation). Aggregation picks how deep it needs to go. The binder is kept separate to protect its role.

---

Version note: v3 — D15-D24 added from definition contract design session. D3 and D4 updated for header format evolution. D5 updated for title and description. D12 softened from required to optional. 2026-09-11. Replaces v2.
