Documentation Methodology | working | DocMeth_Working@v6 | 2026-09-12

## Session history

Sessions 2026-09-10 through 2026-09-11 confirmed items, design pass, old-material pass, rework session, and definition contract session. All settled items moved to Design v3→v4 and Decisions v3→v4.

## Cross-review — 2026-09-11/12

External cross-review of Design v3, Decisions v3, and three standards (Schema v1, Authoring v1, Definitions v1) produced 14 findings. All findings triaged as real defects or partly valid; none rejected. All applied in Design v4, Decisions v4, and all three standards at v2.

Key resolutions:
- Declaration is first block; Title and Description follow it (F1)
- Minimal markdown rendering default defined (F2)
- Canonical marker syntax `<!-- aide:block:TypeName -->` (F3)
- Definition representation made normative (F4)
- Conditional completeness rules added (F5)
- Field-level optionality added (F6)
- Implicit dependency rule: hosting standard is default (F7)
- Dependencies resolved as Declaration field, not separate block (F8)
- Type-reference resolution with dot-qualified naming (F9)
- Governed-document scaffold defined (F10)
- Self-conformance defects fixed (F11)
- Date = "date this version was produced" (F12)
- Identity grammar and filename grammar named separately (F13)
- D25 records three-standard split supersedes brief constraint (F14)
- Declaration fields renamed: `uses` (was dependencies), `blocks` (was blocktypes)
- Component alias uniqueness carried to Core

## Open items

- **Cross-review round 2** — resubmit Design v4, Decisions v4, and three standards at v2 for acceptance test rerun.
- **DocMeth overview** — build after design settles fully.
- **Schema review** — survey all components with doctype/block-type definitions against the contract (assessment produced, DocMeth_Schema_Review_v1). Rework is a separate task per component.
- **Standards header migration** — all DocMeth documents still use the old positional Declaration format. Migration to the blockquote format is a separate task after the standards are accepted. Carry to Migration.
- **PD carries** — PD-F1, PD-F2, PD-F3 in Design v4 carries section. Add to AIDE_Documentation_WIP.
- **Core carry** — component alias uniqueness rule. Add to AIDE_Documentation_WIP.

---

Version note: v6 — cross-review findings absorbed. All settled material in design and decisions. 2026-09-12.
