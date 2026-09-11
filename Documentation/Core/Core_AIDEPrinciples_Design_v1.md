Core AIDEPrinciples | design | Core_AIDEPrinciples_Design@v1 | 2026-09-10

## Brief

**Purpose.** Produce a standard that delivers the operating principles specific to AIDE as a framework.

**Scope.** AIDE-specific tenets that shape how the framework behaves and how its features are adopted. Distinct from the Principles component, which owns universal, portable premises governed by the portability test. Content that fails the portability test — it is about AIDE, not about all AI work — lives here.

**Target outcome.** A deployed standard carrying these principles, the strength model, and the aliases mechanism, so that any AIDE-governed session applies them.

## Facilitate and extend, not create friction or restrict

AIDE empowers. It adds functionality where needed but does not do so from a position of control or dictation. If a user wants to add AIDE's features to a document or project, in full or in part, AIDE applies them where it can. If the user chooses not to, they manage those items on their own.

This leads to a design pattern: functionality is attached to the structure and data it needs to function. Add a particular block type to a document which has the data needed for a component feature to function, and it will be applied.

## Opt-in for benefit, opt-out loses the benefit only

Adopting an AIDE convention activates the functionality it provides. Not adopting it means managing that concern yourself — nothing breaks, nothing is imposed. The cost of opting out is losing the benefit, not gaining a penalty.

AIDE is ambient until something triggers its behaviour. The presence of declarations in the header — the doc type above all — is what brings AIDE into play. This is opt-in by self-description.

## Strength model

Items in standards carry strength — four levels defining how strongly they apply:

- **Required** — must be followed
- **Recommended** — should be followed; deviation needs a reason
- **Optional** — available for use; adoption is a choice
- **Information** — reference-origin content provided for awareness; no compliance expectation

The fourth level (information) exists for content that originated as reference knowledge and was authored into a standard for delivery to the platform. It carries no compliance weight — it informs, it does not direct.

## Aliases

Named things in AIDE — components, areas, parts — may have aliases: shorter or alternative names used for convenience. An alias is an equivalent reference to the same thing.

Aliases are declared where the named thing is described. For a component, that is the `_index.md` in its folder. For example, Documentation Methodology carries the aliases DocMeth and DM.

The purpose is practical — reducing typing and making conversation easier without losing precision. An alias resolves to exactly one thing; where ambiguity exists, the full name is used.

---

Version note: v1 — initial design. Principles from voice session 2026-09-09; aliases from session 2026-09-10.
