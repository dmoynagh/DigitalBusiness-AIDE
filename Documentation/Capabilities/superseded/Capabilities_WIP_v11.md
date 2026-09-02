# Capabilities — WIP

> **Version 11** (2026-09-01). Review B is formally complete at High and its continuation thread
> has been removed. The peer architecture Review programme now advances to Review C — Capabilities.

## Current position

Programme:

`AIDE Architecture — Peer Review Programme`

WorkRegister:

`WR17 — Peer-review major Capabilities architecture slices`

Completed:

- `Review A — Core substrate` — Complete at High.
- `Review B — Documentation/work-state model` — Complete at High.

Next slice:

`Review C — Capabilities`

Current lifecycle state:

`Preparing Review C`

## Review B closure

Durable result:

`Capabilities_Architecture_Review_2026-09-01-2_DocumentationWorkState_v1`

Final state:

```text
Rounds: 2
R1: Robust / High / Full — Claude Opus 5
R2: Inspect / High / Full — Claude Opus 5
Outcome: Complete
Final level: High
Round 3: not required
```

Final verified closing inputs:

- `DocumentationMethodology_Binder_v7.md`
- `WorkingPractices_Binder_v4.md`
- `ProjectDesign_Binder_v3.md`
- `Build_Binder_v5.md`

The Review B active continuation thread is complete and is not carried forward in this WIP.

## Active thread — Review C — Capabilities

Purpose:

Review the current Capabilities architecture and peer capability set as an integrated semantic
system before the later design-to-production and final coherence slices.

Expected current Capabilities source families include:

- parent Capabilities architecture;
- Standards / Tools;
- Tags / Scope;
- Dependencies / Migration;
- Review;
- Messaging;
- current live OpenItems and WR17 state; and
- cross-project seams needed to test capability ownership and conformance behaviour.

Do not use the temporary `AIDE_Bundle_StandardsTools_v5` as semantic authority where a newer current
Binder/canonical source exists.

### Required carried observation — Dependencies / conformance

Review C must explicitly test together:

1. **Review A carry**
   - a Documentation Methodology conformance checkpoint can appear cyclic if treated identically to
     a functional dependency when `AIDE_Index` and Documentation Methodology reference each other.

2. **Review B carry**
   - current executable in-body version references, footer dependency/conformance checkpoints and
     ordinary references currently have different practical roles;
   - Review B corrected only concrete stale executable references needed for its own truthfulness;
   - the general policy/semantics remain unresolved and belong in the Dependencies portion of
     Review C.

The objective is not to make every reference “current” mechanically. It is to determine the correct
semantic model and operational consequence.

### Review E carry — do not resolve in C unless evidence requires it

Possible merge:

`OpenItems + WorkRegister`

Review B preserved both, but deliberately deferred the integrated simplification question until
Review E after Reviews C and D.

Do not reopen the merge merely as a theoretical simplification exercise during Review C.

## Next action

1. Preflight the **current** Capabilities Binder set and identify any stale Binder that must be
   regenerated before Review C.
2. Define Review C subject, objective, scope and source set.
3. Construct the Round 1 request under `AIDE_Review@v2`.
4. Use a new Review thread for Review C.
5. Do not begin Review D until Review C is complete or explicitly escalated.

---
Dependencies: !AIDE_DocumentationMethodology@v26, AIDE_Review@v2, AIDE_Messaging@v1
References: Capabilities_WorkRegister_v16, Capabilities_OpenItems_v15, Capabilities_Architecture_Review_2026-08-31-1_CoreSubstrate_v2, Capabilities_Architecture_Review_2026-09-01-2_DocumentationWorkState_v1
