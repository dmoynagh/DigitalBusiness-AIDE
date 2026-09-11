Core — Tags | working | Core_Tags_Working@v1 | 2026-09-10

## Status

Tags resurrected from the held candidates list during the 2026-09-09 voice session. Confirmed as a Core capability with its own area (prefix Core_Tags). Four items identified for design; standard as output, tools deferred.

## Confirmed design (2026-09-09)

### What tags are

A flat list of string keys placed in a document's header. Tags label a document for classification, discovery, and feature activation. They are a Core capability because they serve any component — not owned by a single consumer.

### Named groups

Tags may be organised into named groups for ownership purposes. A group declares which component or area owns a set of tag definitions. Groups are an authoring-time concept only — they are invisible to consumers.

**Collapse behaviour.** When tags are consumed (by search, by a tool, by any logic reading a document), groups collapse to a single flat list of distinct keys. A consumer never sees group boundaries. This keeps the consumer interface simple regardless of how many groups or owners contribute tags.

### Producer/consumer model

Any component can define tags (producer). Any logic can read tags (consumer). The openness is deliberate — tags are a shared vocabulary, not a controlled namespace. Collision between independently-defined tags sharing a key is possible and is resolved by the tag definition, not by the framework.

## Items for design

1. **Tag definition** — what a tag definition looks like, where it lives, what it must state
2. **Group-ownership model** — how groups are declared, how ownership is expressed
3. **Collapse behaviour** — the precise rule for flattening groups to a distinct list
4. **Producer/consumer openness** — any constraints on who can define or read tags, or fully open

## Output

A standard. Tools deferred — no demonstrated need for tag-manipulation tooling yet.

---

Version note: v1 — initial working document from session 2026-09-09.
