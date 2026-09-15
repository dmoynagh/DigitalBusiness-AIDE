Build | working | Build_Input_Working@v1 | 2026-09-15

# Build — Input (seed material for the design pass)

Items confirmed during the FileOps review that belong to Build but cannot be settled until Build has its own design pass.

---

## Design-build separation principle

Design and build are segmented areas with a handoff point between them — a work package, document, instruction, or other transitional artefact. File management likely mirrors that split: build outputs reside outside the design area, because the two areas are separate.

**Stated as a leaning, not a hard rule.** There may be cases where an output relates to design activity. The concrete conventions are worked out when Build is designed.

Source: FileOps review, redistributed from `WP_FileOps_Working_v1.md` (design-and-output separation item). Original content was a placeholder sketch, not a settled decision.

## AIDE's own framework outputs — the near-term question

AIDE itself has several kinds of build output, and each needs a home decision:

- Standards deployed as skills
- Skills output from tools
- Packages and deployments
- Other framework artefacts

Different kinds of build outcome need different handling. .NET solutions are already a well-defined structure (solutions, projects), so that's fairly cut and dried. Framework outputs are not — they don't have an established convention.

This is likely the first concrete problem Build tackles: deciding where AIDE's own outputs go, since those outputs are needed before any general convention is established.

---

Version note: v1 — seed material from the FileOps review session. Not a brief or design — raw input for the Build design pass. 2026-09-15.
