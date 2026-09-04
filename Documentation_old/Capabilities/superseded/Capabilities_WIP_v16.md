# Capabilities — WIP

> **Version 16** (2026-09-02). Replaces the Review-D-only continuation state with compact continuation
> state for the active Capability architecture redesign. Detailed current design state is preserved in
> `Capabilities_Working_CapabilityArchitectureRedesign_v1.md`.

## Current position

Completed architecture reviews:

- Review A — Core substrate — Complete at High.
- Review B — Documentation/work-state model — Complete at High.
- Review C — Capabilities semantic architecture — Complete at High.

Held:

- **Review D — design-to-production — ON HOLD.** Its previous baseline is stale while the Capability
  production/build model and AI Deployment seam are being redesigned.

External overlapping WIP:

- **AI Deployment** — active design WIP in another working context. Coordinate through handoff until
  that work is committed; require a return seam handoff after its design is finalised.

All other relevant Topics are currently understood to be committed/persisted and may be changed from
any sufficiently sourced working context.

## Active working record

Authoritative continuation detail for the current uncommitted design work:

`Capabilities_Working_CapabilityArchitectureRedesign_v1.md`

It currently records the confirmed direction for:

- required Capability Definition document;
- Capability / Capability Element / Element Type model;
- flexible many-to-many Design contribution model;
- `Update Capability Elements` design-side production action;
- Element Production source/dependency checkpoints;
- distinct document, Element release, Capability release and Package/build identities;
- Current Migration and versioned Element migration/release history;
- Platform Definition and designer-owned Build Platforms;
- Capabilities-owned specialised Capability Build Standards/Tools;
- `Build Capability` orchestration and Build-side `Capability Builder`;
- complete Capability Package contract and post-Build actions;
- Deployment Registry producer boundary;
- section-first / document-as-host documentation architecture;
- Topic ownership versus disposable Working Contexts;
- mandatory session/work-unit reconciliation at completion;
- Binder as declared Topic work/context boundary with compact-first partitioning; and
- the candidate Knowledge semantic/document type, still under review.

## Cross-topic reconciliation pending

Do not yet issue fragmented DocMeth/Project Design/Working Practices handoffs merely because those
Topics own affected semantics. Once the remaining related concepts have been covered, load the current
relevant Binders and reconcile the committed Topics together from one sufficiently sourced working
context.

Expected affected committed Topics currently include at least:

- Documentation Methodology;
- Project Design;
- Working Practices;
- Capabilities;
- possibly Core/Build where concrete ownership or platform/build rules require changes.

Use Project Handoff where work genuinely overlaps active WIP or must continue in another context.
AI Deployment currently meets that condition.

## Next actions

1. Continue the current design discussion and capture remaining related concepts.
2. Resolve the proposed Knowledge semantic/documentation model.
3. Update the detailed Working record as confirmed design changes.
4. Load current Binders/masters for every materially affected committed Topic.
5. Perform one coherent cross-topic architecture/reconciliation pass.
6. Reconcile the resulting Capability design into Capabilities masters/Standards/Tools.
7. Incorporate the final AI Deployment return handoff when its WIP is committed.
8. Re-baseline and resume Review D only after the design-to-production seam is current.

---
Dependencies: !AIDE_DocumentationMethodology@v26, AIDE_Review@v3, AIDE_Messaging@v2
References: Capabilities_WorkRegister_v17, Capabilities_OpenItems_v15, Capabilities_Working_CapabilityArchitectureRedesign_v1
