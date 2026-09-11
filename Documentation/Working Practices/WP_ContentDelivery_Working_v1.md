Working Practices — Content Delivery | working | WP_ContentDelivery_Working@v1 | 2026-09-10

## Confirmed items — session 2026-09-10

### Binder concept ownership

The binder exists to solve a workflow problem: assembling and delivering content to the AI platform for use in a session. Working Practices owns the concept — why the binder exists, how it is used, what it includes, how it delivers content. Documentation Methodology owns the binder as a doctype definition — its structure as a document.

### Three-tier inclusion model

What lives in a project folder falls into three tiers based on its relationship to the AI session:

1. **In the binder** — needed for thinking and reasoning. Design documents, and any other file the AI needs to see to do its work. The test: does it need to be there for thinking and reasoning? If so, include it.

2. **Known to the framework** — part of the project but not needed in context. Listed in the folder's `_index.md`. The framework knows it exists, can reference it, but does not load it. Scripts, settings files, assets.

3. **Just present** — incidental files. AIDE has no opinion. Logs, temp files, personal notes.

The binder is the context-loading mechanism. The `_index` is the awareness mechanism. Files that need neither are just files.

The key question for inclusion is not whether a file is a governed document, but whether it is needed for the work. A utility script that is the project's deliverable may belong in the binder when working on that utility, even though it has no declaration header.

---

Version note: v1 — initial working document from session 2026-09-10.
