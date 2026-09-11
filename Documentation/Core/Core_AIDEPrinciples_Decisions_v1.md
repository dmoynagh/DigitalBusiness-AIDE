Core AIDEPrinciples | decisions | Core_AIDEPrinciples_Decisions@v1 | 2026-09-10

## Summary

Reasoning behind the AIDE-specific principles, the strength model, and the aliases mechanism.

## Facilitate not constrain — placement

"Facilitate not constrain" was deferred during the Core brief (2026-09-08) pending a home. It was tested against the Principles component and failed the portability test — it is about AIDE specifically, not about all AI work. Placed in Core as an AIDE-specific operating principle.

The principle was then reworded to "facilitate and extend, not create friction or restrict" during the voice session (2026-09-09) to better express the active posture — AIDE does not just avoid constraining, it actively empowers.

## The design pattern it produces

Dave articulated the principle's mechanical consequence: functionality is attached to the structure and data it needs. The framework does not gate features behind compliance — it looks for the data a feature needs and applies the feature when that data is present. This is the "define it and you get functionality" incentive model operating at the principle level.

Examples: add a version tag to a document's identity and versioning applies. Add a doctype declaration and doctype logic fires. Add a dependency block and change management tracks it. Each feature activates from its own trigger data, not from a global compliance flag.

## Strength model — the fourth level

The original model had three levels (must/should/could, or required/recommended/optional). The fourth level — information — was added during the voice session (2026-09-09) when the reference document type was discussed.

The case: reference knowledge sometimes needs to reach the AI platform but carries no compliance expectation. A reference document is authored into a standard for delivery, not for governance. Without a fourth level, reference-origin content would carry "optional" strength, implying it is a choice to be made. "Information" correctly signals that the content is there to inform, with no decision or compliance attached.

## Aliases — why they matter

Arose during the session (2026-09-10) from the practical problem of referring to Documentation Methodology repeatedly in conversation and documents. The full name is precise but costly to type and read. Dave already uses "DocMeth" and "WP" (for Working Practices) naturally.

Rather than treating this as informal shorthand, aliases are declared alongside the thing they name. This makes them discoverable, unambiguous, and usable by both humans and AI — an AI seeing "DocMeth" can resolve it to Documentation Methodology because the alias is recorded.

Aliases are placed in the `_index.md` for the thing they name. This keeps them with the authoritative description rather than in a central registry.

---

Version note: v1 — initial decisions from sessions 2026-09-09 and 2026-09-10.
