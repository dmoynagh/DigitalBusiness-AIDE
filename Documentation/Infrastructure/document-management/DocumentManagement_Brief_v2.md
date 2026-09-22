> identity: DocumentManagement_Brief@v2 | doctype: brief | updated: 2026-09-23

# Document Management — Brief

A local MCP server that gives every local AI surface a common, reliable way to work with documents in AIDE document sources.

## Purpose

AI-assisted document work currently relies on surface-native file access (Code's filesystem, Chat's file output) with no shared operational layer. Each surface has different capabilities, different git behaviour, and no common way to discover or address document sources. Convention enforcement depends entirely on skills firing and the AI following them correctly — every surface, every model, every session must get it right independently.

A shared document operations server solves three problems: surfaces that cannot access files directly gain access through it, surfaces that can access files gain safety guarantees they don't have natively, and the token-cost bottleneck (a 2-line change currently costs ~4,000 output tokens regenerating the whole file) is eliminated through partial-update operations.

## Objectives

1. **Efficient document updates.** A caller can update a document without regenerating the entire file.
2. **Safe operations by default.** The server prevents common errors — partial matches, writes to readonly sources, untracked deletions — without the caller needing to manage safety.
3. **Source discovery.** The server knows where document sources are and exposes them by name, so callers address sources, not filesystem paths.
4. **Complete lifecycle operations.** All common document operations — read, write, copy, rename, delete, browse, version management — are available through the server, including operations that currently require manual steps or separate CLI invocations.
5. **Reduce manual burden.** Git management is handled by the server. A multi-file update session produces one commit without the caller managing staging or commit timing.

## Scope and boundaries

**In scope:** Source discovery and listing. File reads and writes (text and binary). Partial-update operations on text. Copy, rename, delete with safety. Directory browsing. Git staging and commit. Binder build. Config-driven source management with readonly enforcement.

**Out of scope:** Mobile and web surfaces (local filesystem only). Remote GitHub API operations and push to remote. AIDE document conventions including versioning, declarations, and cleanup decisions — these are owned by a governing skill that orchestrates multi-step sequences using the server's operations. Document structure decisions (owned by Core Structure). The docmeth rules themselves (owned by DocMeth).

## Requirements

- Python, delivered as a marketplace plugin MCP server per the tested delivery model.
- Machine-level config shared across surfaces.
- Readonly sources must reject all writes.
- Format-agnostic file operations — the server has no knowledge of AIDE vocabulary.
- Errors must return enough information for the caller to decide what to do next.

## Linked build outcome

The MCP server, deployed via the `aide` plugin in the `digitalbusiness-aide` marketplace. Plus a governing skill that provides the AIDE document intelligence — versioning sequences, declaration management, convention enforcement, cleanup decisions — using the server's operations.

## Definition of done

1. The server discovers document sources and lists them by name.
2. A caller can browse the contents of any discovered source.
3. A caller can read any file and write to any non-readonly source.
4. A caller can partially update a text file without replacing the whole file.
5. Copy, rename, and delete work on any file, with delete handling git and non-git sources safely.
6. A multi-file update session produces one git commit on caller command.
7. Errors are reported with enough detail for the caller to act.
8. Binder build is available as a server operation.
9. The server runs on Desktop and Code via the marketplace plugin.
10. A governing skill exists that orchestrates AIDE document conventions using the server's operations.

---

Version note: v2 — solution-space content (tool surface, git model, error model, config schema, patching specifics) moved to design document. Brief retains problem-space: purpose, objectives, scope, requirements, definition of done. 2026-09-23. Replaces v1.
