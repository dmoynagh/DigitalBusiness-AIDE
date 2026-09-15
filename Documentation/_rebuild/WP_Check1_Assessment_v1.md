# Working Practices — Check 1 Assessment

Check 1 question: could the design below be executed excellently from this overview, by someone who has the brief and was not part of the conversation?

---

## Assessment: PASS with noted gaps

The overview/design is complete enough to drive design work. The model is clear: two levels (component-level standing obligations, areas below), two confirmed areas (Working State, Content Delivery), one parked (FileOps), one extracted to a new component (Assurance). The boundaries are stated and the placement test is concrete.

### What is well settled

- Capture-and-place — fully specified: three obligations, destination map, session-end allocation, proactive preservation, four methodology rules
- WIP — three-role model, multiple WIPs, tracking, merge-with-master, visibility requirements
- Work items — definition, two axes, five fates, governing rule, scalable implementation, distinct from work register
- Work plan — named workstreams, maintained by AI, lives in WIP
- Pending content rule — staging model, merge requirement
- Content Delivery — binder concept ownership, three-tier inclusion model
- Workflow commands — concept defined, four confirmed commands, reference guide as output
- Boundaries — clear on all fronts

### Gaps and open items

1. **FileOps** — parked. Needs a focused review to determine whether it earns its place, dissolves, or is redefined. The design cannot be called complete until this is resolved, but the rest of the design does not depend on the outcome.

2. **Development lifecycle — thin.** The phase/mode distinction is stated but not developed. What does it mean in practice for a session to be "in design mode" versus "in build mode"? Which standards and tools load? How does the transition happen? This is probably deferred until more components have standards that could load, but it should be noted as an area that needs future work.

3. **Workflow command methodology — concept only.** How new commands are defined, documented, and added to the reference guide is stated as a purpose but not designed. The concept is clear; the methodology is future work.

4. **Old-material pass not yet run.** WP1–WP13 from the old corpus have not been reconciled against this design. Per finding F10 and the rebuild method, this is a required step before WP can be called complete.

5. **No-knowledge-lost three behaviours — partially absorbed.** The three behaviours from the WIP (session-close sweep, session-start check, periodic consolidation prompt) are covered by capture-and-place and proactive knowledge preservation, but they are not explicitly named in the design. The session-close sweep is session-end allocation. The session-start check and consolidation prompt are implied but not stated. Consider making them explicit.

6. **Schema definitions not yet written.** Doctypes (WIP, working document, report, resource) and block types (work item, work plan, definition-of-done as a generic block) need formal definitions per the documentation methodology schema contract. This is a separate task, not a design gap.

### Recommendation

Proceed to authoring. The gaps are either parked with reasoning (FileOps), future work that doesn't block the current design (lifecycle modes, command methodology), or mechanical tasks (old-material pass, schema definitions). The model is clear enough to drive execution.

---

Version note: v1 — Check 1 assessment of WP_Design_v1. 2026-09-15.
