> identity: Messaging_Decisions@v4 | doctype: decisions | updated: 2026-09-15

# Messaging — Decisions

## Summary

Reasoning and resolutions from the Messaging design pass. Twenty-eight decisions: D1 is new to the rebuild (positioning change); D2–D15 carry substance from the legacy Messaging design; D16–D17 are structural decisions from the rebuild; D18–D21 remediate first cross-review findings F1–F7; D22–D25 remediate second cross-review findings R1–R4; D26–D28 remediate third cross-review findings R5–R7.

---

## D1. Messaging is format and methodology, not transport

**Decision.** Messaging defines the envelope — format, structure, addressing, acknowledgment conventions. It does not carry anything; it defines what is carried.

**Reason.** The Core design pass (Core D4) repositioned Messaging from a Delivery role to Foundation. Messages travel by Orchestration transport (automated) or by copy-paste (manual, always available). The transport is irrelevant to the message format. This makes Messaging structurally equivalent to Documentation Methodology — a grammar, not plumbing. Foundation becomes three grammars: framework structure (Core), document structure (Documentation Methodology), communication structure (Messaging).

**Consequence.** Messaging no longer owns or implies a transport mechanism. Orchestration owns automated channels; Build owns platform-specific delivery mechanics.

---

## D2. Preserve the AI-MESSAGE envelope

**Decision.** Retain the existing one-envelope structured-text model and change only mechanisms whose old architectural assumptions no longer hold.

**Reason.** The system has worked successfully in real copy-paste operation. Blank-sheet review during the original design did not reveal a simpler alternative with equivalent identity, receipt, and recovery properties.

---

## D3. Identity, threading and readability remain separate

**Decision.** Keep Thread, Message-ID, Version, In-Reply-To, Topic, and Timestamp as separate concepts. Timestamp never identifies or threads a message.

**Reason.** The earlier combined approach caused concrete ordering and thread-resolution failures. Separate roles cost little in the envelope and remove ambiguity.

---

## D4. Sender-partitioned Message-ID

**Decision.** Use `{Thread}/{From-slug}/{NNN}` with each sender owning only its own sequence. Never reconstruct an identifier from recollection.

**Reason.** The parties need no shared counter. Collisions are visually attributable. Identifier evidence can be carried by conversation, WIP, or open items without a global registry.

---

## D5. Version distinct from Message-ID and file version

**Decision.** A revised message keeps its Message-ID and advances only the sender-owned envelope Version after known relay. A persisted document's file version remains a separate Documentation Methodology document version.

**Reason.** New-message identity, revision identity, and document-file revision answer different questions. Conflating them would make replies and durable copies ambiguous.

---

## D6. Expects as the response contract; receipt and fulfilment are separate

**Decision.** Keep Answer, Decision, Code, Review, Action, Ack, None as the response contract. None is exclusive; Ack may combine with a substantive expectation. A reply may prove receipt without closing the original message — a holding reply leaves the substantive expectation open.

**Reason.** Expects turns a received message into an explicit requested outcome without embedding a workflow-specific task system. Separating receipt from fulfilment supports the useful holding-reply behaviour, where receipt is demonstrated but the substantive ask remains outstanding. The previous statement that any reply closes the message contradicted this real behaviour.

---

## D7. STATE as best-effort receipt integrity

**Decision.** Retain counterparty-scoped Awaiting, Held/open, and optional Held/closed state on ordinary traffic. STATE's evidential value is explicitly proportional to the relevant evidence retained by the constructing context. The inference rule is intentionally asymmetric: presence of an unexpected identifier is a mismatch signal; absence proves nothing.

**Reason.** STATE demonstrates receipt as a by-product of communication rather than adding a mandatory acknowledgement exchange. No cheaper mechanism found in review provides equivalent probability of exposing a missed relay. Making the evidence-strength limit explicit prevents false confidence without reintroducing the obligations ledger. Conversation, WIP, and open items state can be incomplete; treating omission as proof would turn a best-effort integrity mechanism into false assurance.

---

## D8. No dedicated obligations register

**Decision.** Messaging does not require a permanent obligations or sent-items register. Use visible conversation first, WIP for active continuation state, open items for durable obligations, and a persisted message only when its body needs retrieval.

**Reason.** The old register mixed receipt bookkeeping with durable work persistence. Documentation Methodology now supplies purpose-specific WIP and open items mechanisms, so retaining another live ledger would duplicate state and create reconciliation burden. Drafted-but-unsent messages are not a separate canonical durable state — draft generation does not establish delivery, and a permanent draft ledger adds friction to the light tier without strengthening the epistemic boundary.

**Rejected alternative.** Keep the old register for tidiness or continuity. Rejected because its unique value disappears once receipt-state construction is allowed to consume the existing durable state sources.

---

## D9. Light default; persist only when the body needs retrieval

**Decision.** Conversation is the default residence. A message document is justified when the actual body must be independently retrievable — not merely because an exchange is long, important, or crosses a session.

**Reason.** WIP and open items can preserve continuation and obligation cheaply. Persisting every durable ask would recreate a message archive and undermine the original low-friction tiering.

---

## D10. Lifecycle removed from the envelope

**Decision.** Do not carry Lifecycle inside AI-MESSAGE. When persisted, generic lifecycle, filename, metadata, and Current/Superseded/Archived mechanics are supplied by Documentation Methodology.

**Reason.** Lifecycle is a property of the governed persisted document, not of a light transport envelope. The old field reflected a prior Documentation Methodology ownership split that no longer applies.

---

## D11. Persisted message semantics remain Messaging-owned

**Decision.** A persisted message preserves the complete envelope as its substantive record. Envelope Version remains independent of document version. Another party's body is not silently rewritten. Generic document mechanics remain Documentation Methodology-owned.

**Reason.** This preserves message fidelity while respecting the one-owner boundary established by Documentation Methodology. Forwarding and convergence provenance (Forwarded-From, optional Merged-From) remain optional explicit fields, solving real provenance questions while imposing no cost on ordinary messages when omitted.

---

## D12. Source marking and out-of-band protections

**Decision.** Keep `[human]`, `[project: <ref>]`, and human-supplied `, out-of-band` marking only where provenance changes weight. The AI does not infer out-of-band attribution.

**Reason.** Cross-context AI messages otherwise blur AI-generated wording, human statements, and recorded project positions. The markers are cheap when sparse and prevent materially different sources being presented as equivalent. The inference prohibition came from observed failures — a confident, well-formed attribution that was wrong.

---

## D13. Drafting protections as operational requirements

**Decision.** Obtain a clock rather than inventing timestamps; never reconstruct identifiers from memory; never infer out-of-band attribution; output one envelope; render it as one fenced copy block.

**Reason.** These rules came from observed failures. They are construction checks rather than stylistic preferences. Each was stated, adopted, and then violated in the very exchanges that adopted it. Making them procedural steps rather than rules to bear in mind is what gave them teeth.

---

## D14. Receive as a first-class logical action

**Decision.** The canonical tool defines Receive as a logical action for pasted or returned envelope processing. Seven user-facing commands remain: /msg, /msg-reply, /msg-fwd, /msg-promote, /msg-ack, /msg-query, /msg-reconcile. Receive need not have its own slash command.

**Reason.** Receive was already significant runtime behaviour — parsing, STATE checking, Expects surfacing — but lacked an explicit logical-action home. Every existing command still has one clear job.

---

## D15. Platform mechanics to Build; no bootstrap by default

**Decision.** Claude skills, ChatGPT/Codex representations, pasted-envelope trigger implementation, clock/file APIs, and similar mechanics are Build outputs, not canonical messaging semantics. Normal tool discovery should recognise the strong `=== AI-MESSAGE ===` marker without a bootstrap contribution. Create one only when platform evidence demonstrates otherwise.

**Reason.** The envelope is platform-neutral. Baking the currently successful Claude implementation into the standard would make implementation evidence into architecture. Bootstrap is intentionally thin and should not become a universal eager include — no current evidence shows Messaging requires session-start processing merely to recognise an envelope later.

---

## D16. Single design document

**Decision.** Merge the legacy separate design (Capabilities Messaging Design v3) and tool design (Capabilities Messaging Tool Design v2) into a single Messaging design document.

**Reason.** Both are Messaging's responsibility. The tool is small enough — eight logical actions, each a short contract — that a separate design document creates maintenance overhead without proportionate value. Other components in the rebuild follow the same pattern of one design per component.

---

## D17. Legacy skill and model superseded

**Decision.** The current `workflow-messaging` skill, the Capability/Element/Release model (Capabilities Messaging Definition v3), and the obligations register concept are all superseded by this design pass. The new standard and tool are the authoritative sources. The skill is rebuilt from them.

**Reason.** The skill references legacy concepts — the obligations register, Lifecycle in the envelope, Workflow ownership framing — that are superseded by the register-free model (D8), the Lifecycle removal (D10), and the component repositioning (D1). The old Capability/Element model is replaced by the simpler component model settled in the rebuild. The substance of the messaging system is unchanged; the framing is updated.

---

## D18. One slug rule for Thread, From-slug, and Version prefix (remediates F1)

**Decision.** A single transformation — lowercase, non-alphanumeric to hyphen, collapse and trim — produces Thread, the From-slug component of Message-ID, and the identity used to match a Version owner prefix. The Version prefix displays in the owner's normal capitalisation for readability but is compared case-insensitively via the same slug.

**Reason.** Cross-review found that Message-ID's `{Thread}/{From-slug}/{NNN}` and Version's `<owner-prefixed vN>` each named a transformation without defining it, leaving a fresh AI unable to construct or validate identity fields deterministically. Defining two separate transformations would have been two things to keep in sync for no benefit — one rule serving three uses closes the gap without adding a second concept. From/To stability guidance was added alongside it, since a party identity that is chosen once per context and reused is what makes the slug stable across a thread's life.

---

## D19. Reconcile split into three explicit moments (remediates part of F3)

**Decision.** Reconcile is defined as three distinct steps, each with its own Type/In-Reply-To/Expects: initiate (New, Expects: Answer), respond (Reply, In-Reply-To set, Expects: None), and process-the-response (no new envelope).

**Reason.** Cross-review found that Reconcile conflated three operationally different envelopes under one heading; separating them removes the ambiguity about whether "Reconcile" means initiating, answering, or reading a response. (QueryReceipt's contract, the other half of F3, went through further remediation in D23 and D26.)

---

## D20. Promote's Documentation Methodology dependency stated as an ambient guarantee (remediates F4)

**Decision.** Promote hands the governed-document operation — filename, version, metadata, lifecycle, index — to Documentation Methodology. This is explicitly stated to be safe because the main DocumentationMethodology standard is universal and exempt from `uses` declarations under the rebuild's source-defined propagation model: every session is guaranteed to have it present. No `uses: DocumentationMethodology_Standard` entry is added to the tool, because universal dependencies are by definition exempt from that declaration.

**Reason.** Cross-review found the dependency real but unstated, making the acceptance test conditional on unproven context. The fix is not to declare a `uses` entry — that would misapply the exemption rule that already covers this case — but to say plainly, at the point Promote relies on it, that the guarantee exists and where it comes from. This keeps Messaging from duplicating Documentation Methodology's rules while removing the silence cross-review flagged.

---

## D21. Authoring-discipline cleanup: idempotency, strength, trigger duplication, carry test (remediates F2, F5, F6, F7)

**Decision.** Four standing authoring corrections, applied directly in the standard and tool rather than recorded as design content:

- **Idempotency (F2).** Declared per action in a table near the tool's opening, not only for three of eight actions at the bottom.
- **Strength (F5).** The Receipt escalation selection rules ("use Acknowledge when…", "use QueryReceipt when…", "use Reconcile when…") are Required, not Information — they are discriminating operational guidance, not awareness content. Only the separate statement that these mechanisms cannot guarantee delivery remains Information.
- **Trigger duplication (F6).** The tool carries exactly one trigger description. An earlier expanded `## Trigger` section duplicated the opening description at roughly 358 characters, well outside the 130-character budget. It was removed.
- **Carry test (F7).** Build/bootstrap material — that skills, commands, and triggers are Build concerns, and that no bootstrap contribution is required by default — is design-time knowledge for Build, not something a runtime Messaging consumer acts on. It stays in this design and is not carried into the standard.

**Reason.** All four are authoring-standard compliance issues rather than model defects. Fixing them in the standard and tool, with this decision recording why, keeps the design document from re-litigating settled authoring rules it does not own.

---

## D22. Promote's duplicate check moved to a strict precondition; idempotency reclassified (remediates R1)

**Decision.** The check for whether an exact envelope/version is already persisted is a precondition, evaluated before any write or registration — not a step that runs after creation to notice a duplicate. The design's Promote procedure and the tool's Promote procedure both order it as step 3, ahead of document creation.

Promote's idempotency classification changes from "No" to "Yes, for the same exact envelope/version" — not idempotent across different envelope/versions, since each is a distinct persist decision.

**Reason.** The second cross-review found the v2 design listed the duplicate check as a late step, after creation and registration had already occurred — at which point it could not prevent the duplication it was meant to prevent. This directly contradicted the tool, which had the check correctly ordered as a precondition. Once the check genuinely gates creation, Tools Authoring Standard v8's operational idempotency test — is it safe to rerun — is satisfied for the same envelope/version.

---

## D23. QueryReceipt's response is one Reply to the query, carrying receipt evidence for the questioned message in Content (remediates R2)

**Decision.** When responding to a QueryReceipt, the recipient composes exactly one Reply whose In-Reply-To cites the query's own Message-ID @ Version — never the originally questioned message's. That Reply's Content explicitly names the questioned Message-ID @ Version and states whether it is held. If the query's Expects included Answer, the same Reply's Content also states what was understood. No second envelope is issued.

**Reason.** The second cross-review found "Expects: Ack" on a QueryReceipt ambiguous between acknowledging the query itself or the originally questioned message, and found "Answer, Ack" additionally unclear on envelope count. Settling the correlation explicitly removes both ambiguities with no change to the one-envelope-per-output rule (D13).

---

## D24. Platform compatibility vocabulary stays in the design only, not the tool (remediates R3)

**Decision.** The compatibility slash-command vocabulary (`/msg`, `/msg-reply`, etc.) and the statement that Build may expose it are removed from the tool's Platform commands section and retained only in the design's Platform and bootstrap section.

**Reason.** A runtime executor of Compose, Receive, Reply, and the other actions has no operational use for the slash-command mapping — it is information for whoever builds the platform representation, not for whoever performs the action. The design already owns this boundary; duplicating a shorter version of it into the tool served no consumer.

---

## D25. "Relay" replaced with delivery-neutral wording (remediates R4)

**Decision.** The tool's trigger description and the design's system-model diagram no longer use "relay" to describe what Messaging or its tool does. The trigger reads "Compose, forward, or process a structured AI-MESSAGE for another AI, session, project, or platform" — describing the actions Messaging actually owns without implying it performs delivery.

**Reason.** The second cross-review found that "relay...to another AI" reads as though the Messaging tool transports the message, contradicting D1's central positioning that Messaging defines what is carried and Orchestration moves it.

---

## D26. QueryReceipt response added as a recognised positive-evidence form; construction procedure consolidated to the tool (remediates R5)

**Decision.** The canonical positive-receipt-evidence list gains a fifth form: an exact QueryReceipt response that names the questioned Message-ID @ Version and positively states it is held. This is added in both the design (Receipt integrity and STATE, Positive receipt evidence) and the standard.

The design's QueryReceipt subsection is trimmed to state only the semantic rule — that a conforming response is positive evidence — and points to the tool for how the query and response are actually constructed. The standard's QueryReceipt-specific material is likewise trimmed to the semantic rule; the full two-sided construction procedure (Type, In-Reply-To, Expects choices for both the outbound query and the inbound response) lives only in the tool.

**Reason.** The third cross-review found a genuine internal inconsistency: D23 had defined a new evidence form (a QueryReceipt response's Content statement) without adding it to the canonical list of what counts as positive receipt evidence, so the general evidence rules and the specific QueryReceipt contract disagreed with each other. Cross-review also correctly identified that the standard, in stating D23's full procedure, had begun duplicating the tool's authority over its own invokable action — a violation of the sibling-outputs model (Tools Authoring Standard v8), where the tool is the single authority for how an action is performed and the standard carries only the application-time semantic rule.

---

## D27. Receive's idempotency split into parsing (idempotent) and dispatch (not idempotent, inherits the invoked action's contract) (remediates R6)

**Decision.** Receive itself — parsing, validating, checking STATE, surfacing Topic/Expects, interpreting working state — is idempotent and does not itself emit an envelope. When Receive recommends or hands off to Reply, Acknowledge, or Reconcile, that is a separate invocation of the named action, governed by that action's own procedure and its own idempotency entry in the table. Receive's own table row is reworded to make this explicit, and its "recommend/execute" language is changed to "recommend" — execution is the named action's step, not Receive's.

**Reason.** The third cross-review found the idempotency table declaring Receive unconditionally idempotent while Receive's own procedure said it may execute Reply, Acknowledge, or Reconcile — all separately declared non-idempotent. Rerunning Receive under the old wording could re-trigger a non-idempotent action as a side effect, which the table's "Yes" did not warn about. Splitting Receive into a pure-processing effect and a separate dispatch removes the contradiction without inventing a new duplicate-guard mechanism: the invoked action already carries the guard it needs (e.g. Promote's precondition check, D22), and Receive no longer claims an idempotency guarantee that covers effects it doesn't itself control.

---

## D28. Remaining "relay" instance removed from the Review boundary statement (remediates R7)

**Decision.** The Boundaries section's Review entry — "Messaging owns the envelope, relay, and receipt behaviour Review consumes" — is corrected to "Messaging owns the envelope, correlation, and receipt behaviour Review consumes."

**Reason.** D25 removed "relay" from the trigger and system-model diagram but missed this instance. "Owns...relay...behaviour" read as transport ownership, directly adjacent to and in tension with the Orchestration entry two lines below, which states Orchestration owns transport channels and routing. "Correlation" names what Messaging actually owns in this context — Message-ID, Thread, and In-Reply-To matching — without repeating the delivery implication.

---

Version note: v4 — remediates third cross-review findings R5–R7 (D26–D28 added). D1–D25 unchanged in substance. 2026-09-15. Replaces v3.
