Documentation Methodology — Decisions | decisions | DocMeth_Decisions@v6 | 2026-09-12

## D1 — DocMeth owns grammar only, not individual definitions

Individual doctype and block-type definitions live with the component that knows the most about them. DocMeth defines what a doctype is, what a block is, how they compose, and the common catalogue of blocks usable by any document. This is the "grammar versus vocabulary" line: DocMeth owns the rules of the language; components own the words.

The alternative — DocMeth as a central registry of all types — was considered and rejected. A registry would accumulate detail from every component and become the single largest document in the framework, would require every component to file definitions with DocMeth rather than owning them, and would create a coordination bottleneck where no component can define a new type without a DocMeth update. The what-knows-most-about-it ownership rule settles it.

## D2 — Composition, not inheritance

Doctypes compose blocks by inclusion. A doctype includes a block as defined and does not modify it — no field suppression, no field addition, no shape adjustment on inclusion. Where two doctypes need different shapes, those are two blocks sharing a smaller common block if warranted.

Override-on-include is inheritance under another name: it brings back precedence when two doctypes adjust the same block differently, drift when the base changes underneath, and a reader unable to tell what shape a block actually has. The accepted cost is duplication between near-identical blocks, which is visible; override chains are not. Revisit on a demonstrated case per the demonstrated-requirement rule.

Also cut as over-engineered: multiple doctype inheritance, abstract doctypes, block self-assignment to doctypes (push model), collision precedence machinery.

## D3 — Declaration as conformance marker and activation trigger

The Declaration's presence is both the corpus recognition mechanism (is this a governed document?) and the activation trigger (DocMeth applies). This dual role avoids needing a separate governance flag. A document without a Declaration is outside the methodology — legitimate, at the user's risk.

The Declaration is the first block in a governed document, fixed topmost. Title and Description follow it, recognised by placement. The Declaration is fixed and not overridable. Its fields (identity, doctype, date, uses, blocks) are labelled. Dependencies (`uses`) and blocktypes (`blocks`) are Declaration fields, not separate blocks.

## D4 — Dependencies as a Declaration field

Dependencies (`uses`) is a labelled field within the Declaration, not a separate block type. It was originally a separate header block, then a footer block in the old model. Folding it into the Declaration keeps all machine-readable governance information in one container, readable in a single partial read from the top.

The grouping syntax `name:[item1, item2]` tracks which owner contributed each dependency.

## D5 — Common catalogue scope

The common catalogue holds blocks usable by any document regardless of component: Declaration, Title, Description, Header, Body, Footer, Contents, Summary, Version note. Nine blocks. (Dependencies is a Declaration field, not a separate block.)

Tags was parked in the original catalogue session (no demonstrated consumer), resurrected as a Core capability (2026-09-09), and confirmed as Core-owned. Its block definition belongs to Core, not to DocMeth's common catalogue.

References remains parked — no consumer has appeared. It returns on its own merits when one does.

## D6 — Contents and Summary are optional

Both blocks earn their place by function, not by rule. Contents earns inclusion when a reader could not decide from the Declaration alone whether to keep reading. Summary earns inclusion when the document's substance needs a compressed statement. Often not relevant for machine-focused or skill-delivered documents. The doctype owner decides the default for their type: on, off, or conditional.

## D7 — The Contents/Summary edge as a grammar rule

Contents maps what is where (navigation); Summary gives what the document establishes (substance). The edge between them was flagged by Standards as a common issue for standards authors and carried to DocMeth as document-structure grammar. DocMeth owns the edge definition because it defines both blocks.

## D8 — The split test as grammar

The split test (externalise a block when keeping it in would compromise the primary role of its host) was carried from Project Design as part of the grammar. It belongs in DocMeth because it governs the relationship between a block and its host document — a structural concern, not a design-process concern. The trigger is not a size threshold but a functional test.

## D9 — Language rules as grammar

The four language rules (plain English, meaning first / code second, use existing terms, flag new terms) were carried from the design-approach work. They belong in DocMeth because they govern how any governed document is written. The aide-design-check skill currently carries these rules. Once DocMeth's standard is authored, the skill consumes the standard rather than carrying the rules itself.

## D10 — Rendering model with minimal markdown defaults

The format rendering rule states that each format's own existing standards provide a clear default mapping. A small set of deterministic markdown defaults is defined: heading levels follow nesting, compact fields render as pipe-delimited labelled lines, expanded fields render as labelled list items, containers are structural with no literal rendering, title is `#`, description is first paragraph beneath title.

Block definitions override these defaults when needed. No full mapping system — the defaults handle the common case. If a format gap appears beyond what the defaults cover, DocMeth authors the mapping then.

## D11 — No Infrastructure link for rendering

The grammar tells the AI how to express a block in each format, and the AI applies those rules when authoring. No separate renderer utility is needed. If a utility ever needed to render blocks, that utility's spec would consume DocMeth's grammar.

## D12 — Owner and residence is optional, not required

Owner and residence is implicit from the hosting location for most definitions. Stated only when not obvious. The process discipline — decide the owner when you define the thing — stays as methodology.

## D13 — Lifecycle states are grammar

Three semantic lifecycle states (Current, Superseded, Archived) belong to DocMeth because they describe what state any governed document can be in. They are independent of physical storage — Working Practices owns how the file system represents them.

## D14 — The claimed-versus-verified rule

Do not compose plausible metadata where the fact should be observed or read. This rule belongs in DocMeth as a document-integrity rule. It joins the four language rules as a fifth writing/integrity rule.

## D15 — The definition contract is facilitative, not prescriptive

The definition contract is the language for defining doctypes and block types. Name and purpose are the only always-required properties. Everything else is available vocabulary — stated when it adds value, omitted when it doesn't.

The alternative — a mandatory property list where every definition must address every field — was rejected as counter to the facilitate-not-control principle.

## D16 — Declaration header evolved to labelled blockquote

The original Declaration was a single pipe-delimited line with positional fields. The evolved form is a multi-line blockquote with labelled fields. Labelled fields replace positional because the field set has grown beyond what positional ordering can carry unambiguously. Blockquote provides visual distinction and structural detectability in markdown.

## D17 — Title and Description as self-describing blocks after Declaration

Title and Description are self-describing blocks recognised by placement, following the Declaration. Order: Declaration → Title → Description → Contents → Summary → Body.

Title and description are inferred from natural document convention in prose formats (position and shape) and keyed in structured formats. This follows the format rendering rule — no special inference machinery.

## D18 — Dependency implications as an implicit default

A type defined in a versioned standard implicitly carries that defining standard as its dependency implication. The document's `uses` field is populated automatically. A definition only states dependency implications explicitly when they differ from the defining standard.

This applies to component schema standards and to DocMeth's own Definitions Standard equally. It preserves low-friction design and avoids repetitive boilerplate while guaranteeing the living-document change-management chain.

## D19 — Format constraint as a doctype property

A doctype can constrain the permitted formats when the type requires it. The format-fits-the-job principle says format is a considered choice — the doctype is the thing that carries the consideration.

## D20 — Density has no default

Neither compact nor expanded is assumed. Density is stated when it matters, omitted when the content shape makes it obvious, and not applicable to blocks without structured fields.

## D21 — Tags deferred from the definition contract

Tags is deferred. The concept is sound but ahead of demonstrated requirement. The grouping syntax is independently useful in `uses` and `blocks` fields. Tags returns when a consumer demonstrates need.

## D22 — Containers settled at four, general role deferred

Four containers are settled: Header, Footer, Body, and Declaration. Any block type can serve as a container by being targeted for placement. New containers are created by defining a block type and having the doctype position it — no additional mechanism needed. A general formal treatment of the container role is deferred until the four settled containers prove insufficient.

## D23 — Lifecycle terminal path dropped from doctype contract

A doctype may describe terminal paths in its documentation, but this is not a formal property in the definition contract.

## D24 — Self-describing blocks and the aggregation model

Four blocks make a document self-describing: title, description, contents, summary. Title and Description are common blocks. The aggregation model consumes self-describing blocks: one model, several output forms. The binder is kept separate.

## D25 — Three-standard split supersedes single-standard constraint

The brief's statement that both consumers "must be served by the same standard" is superseded. The three standards (Schema, Authoring, Definitions) serve different consumers with different change cadences. This follows the schema placement guidance DocMeth itself defines.

The brief is a historical record and is not rewritten. This decision records the departure.

## D26 — Conditional completeness rules

Name and purpose are always required. Other properties become required when omitting them would leave the definition ambiguous: a block whose position does not identify it must state its recognition; a block with structured fields must declare them. This preserves the facilitative model while preventing definitions that cannot subsequently be rendered or recognised.

## D27 — Field-level optionality

The Fields vocabulary item accepts per-field optionality (required, recommended, or optional) and value constraints. This separates block-level optionality (the doctype's choice to include a block) from field-level rules (the block's own internal structure), as the brief requires.

## D28 — Governed-document scaffold

The methodology provides an implicit scaffold for every governed document: Declaration, Title, Description, Header, Body, Footer. Doctypes add content blocks beyond this scaffold. Containers exist structurally even when empty. This eliminates ambiguity about what a doctype must explicitly include versus what the methodology provides.

## D29 — Type-reference resolution

Type names must be unique within their owning component. Independently owned components may use the same name without coordination. Unqualified names are the default when unique within the document's active `uses` scope. Dot-qualified form (`pd.brief`) disambiguates on collision, using the component's declared alias as prefix. The pattern extends to framework-level (`aide.pd.brief`) when needed, but the framework prefix is not defined until demonstrated.

Resolution path: a type's authoritative definition is in the defining standard listed in the document's `uses` field.

Component alias uniqueness is carried to Core Structure.

## D30 — Default markdown rendering

A small set of deterministic defaults closes the gap between the format rendering rule and the brief's requirement for unambiguous markdown output. Heading levels follow nesting, compact fields are pipe-delimited labelled lines, expanded fields are labelled list items, containers are structural, title is `#`, description is first paragraph beneath title. Block definitions override when needed.

## D31 — Declaration field renames

`dependencies` renamed to `uses`; `blocktypes` renamed to `blocks`. Shorter, plainer, consistent with the plain-English rule. `identity` and `doctype` retained — already short and unambiguous.

## D32 — Date semantics

The Declaration `date` field means "the date this version was produced." One meaning, no ambiguity. Created date and modified date were considered and rejected — created date is historical metadata, modified date is what the Declaration date already is, and maintaining both creates a composed-metadata risk.

## D33 — Identity reference grammar and filename mirror grammar

Two named grammars for the same versioning model. The identity reference grammar (`Name@vN`, `Name@vN-draftN`) is the primary, authoritative form. The filename mirror grammar (`Name_vN.ext`, `Name_vN-draftN.ext`) is decorative — never authoritative, identity wins on conflict. Draft numbering is required — every draft carries its sequence number, no unnumbered draft form exists.

## D34 — Canonical marker syntax

The marker for block-type recognition is an HTML comment with the `aide:block:` prefix: `<!-- aide:block:TypeName -->`. For repeated instances: `<!-- aide:block:TypeName:instance-id -->`. The `aide:` namespace prevents collision. The `block:` segment is extensible for future marker types.

## D35 — Definition representation

A definition is written as a heading naming the type, followed by labelled properties as list items. Name is the heading. Purpose is the first property. In structured formats, a keyed object with the same property names. This makes the representation normative rather than observable only by imitation.

## D36 — Dependencies resolved as Declaration field

Dependencies (`uses`) is a Declaration field, not a separate block type. The Declaration is a container for all machine-readable governance information. Everything needed for a partial-read governance check is in one block.

## D37 — Footer recognition is by placement, not by marker

Footer is recognised by its position at the bottom of the document, with the horizontal rule as the boundary signal in markdown. This is placement recognition, not marker recognition. The `aide:block` marker syntax is reserved exclusively for typed block markers. A format-specific boundary convention is not a marker in the definition-contract sense.

## D38 — Manifest as a binder block type

The binder's manifest is a block type: it has fields (relative paths, structural metadata) and a defined format. The BEGIN/END source concatenation is a format convention of the binder doctype, not a block type — it describes how the binder renders its included content, not a content definition.

## D39 — blocks field lists non-scaffold typed blocks

The `blocks` field in the Declaration lists non-scaffold typed blocks actually present in the document. The scaffold (Declaration, Title, Description, Header, Body, Footer) is provided by the methodology and not re-stated. This prevents redundancy and makes `blocks` meaningful — it shows what the doctype adds.

## D40 — Declaration overrides the compact rendering default

Declaration renders compact fields across multiple lines (one per field group) rather than on a single line, because some fields are optional and variable-length. This is an explicit override of the default compact rendering rule, stated in the Declaration's definition.

## D41 — Dependency implications propagate to uses

Dependency implications from the document's doctype and included block types populate the Declaration's `uses` field automatically. This is the connecting rule between the implicit dependency mechanism and the `uses` field. The `uses` field is syntactically optional but present whenever resolved dependencies exist.

## D42 — Format conventions as a doctype property

Format conventions is a doctype vocabulary property for format-specific structural behaviour owned by the doctype — rendering conventions beyond what block definitions and the default markdown rendering cover. Binder demonstrated the need: its BEGIN/END source-document delimiting is a format convention, not a block definition.

---

Version note: v6 — D41-D42 added. Round 3 corrections. 2026-09-12. Replaces v5.
