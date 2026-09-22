> identity: DocumentManagement_Brief@v1 | doctype: brief | updated: 2026-09-23

# Document Management — Brief

A local MCP server that provides safe, format-agnostic file primitives over git-backed and non-git repositories — reading, writing, browsing, copying, patching, and maintaining documents across AIDE document sources. The server provides the reliable operations; a governing skill loaded in session provides the AIDE document intelligence.

## Purpose

AI-assisted document work currently relies on surface-native file access (Code's filesystem, Chat's file output) with no shared operational layer. Each surface has different capabilities, different git behaviour, and no common way to discover or address document sources. Convention enforcement depends entirely on skills firing and the AI following them correctly.

The document management server provides a single set of file primitives available to every local surface, with safety guarantees (unique-match patching, readonly enforcement, delete-safety) built into the operations. It also solves the token-cost bottleneck: a 2-line change to a document currently costs ~4,000 output tokens regenerating the whole file; patch-style updates through the server drop that to ~150–200 tokens.

## Objectives

1. **Efficient document updates.** Patch and replace operations on text files that avoid regenerating entire files.
2. **Safe, reliable file primitives.** Operations that are hard to get wrong — unique-match validation on patches, git staging tracked by the server, readonly enforcement, delete safety (git-backed sources delete, non-git sources move to `_recycle`). The server is infrastructure the AI can trust.
3. **Source discovery and management.** Discover document sources via configured scan roots and `_index.md` markers, expose them by name with metadata (including git-backed flag), and manage the config that controls what the server sees.
4. **Document lifecycle operations.** File reads (text with optional line-count limit for partial reads, or binary), writes (text and binary), patch (text only, keyed-data unique-match), copy, rename, delete, directory browsing (with glob filter), mkdir, repo listing, and binder builds — the operations that currently require manual steps or separate CLI invocations.
5. **Reduce manual burden.** Git staging handled per operation, commit on caller command so a multi-file update session produces one commit. No manual git management required.

## Scope and boundaries

**In scope:**

- Source discovery and listing (with git-backed flag)
- Directory browsing with optional glob filter
- File reads and writes — text and binary, format-agnostic
- Partial text reads (line-count limit)
- Patch updates on text files via keyed-data unique-match
- Copy, rename, delete (git-backed: actual delete; non-git: move to `_recycle` at source root)
- Mkdir
- Git staging per operation, commit on caller command
- Git status
- Binder build (bundled Python script, caller-initiated)
- Config-driven source management with readonly enforcement
- Optional YAML→HTML rendering
- On-demand board query

**Out of scope:**

- Mobile and web surfaces — local filesystem only
- Remote GitHub API operations; push to remote
- AIDE document conventions including versioning, declarations, and cleanup decisions — owned by the governing skill, which has the standards loaded and orchestrates multi-step sequences using the server's primitives
- Document structure decisions — owned by Core Structure
- The docmeth rules themselves — owned by DocMeth; the server has no knowledge of AIDE vocabulary

## Requirements

- Python, delivered as a marketplace plugin MCP server per the tested delivery model.
- Config at `~/.aide/config.yaml` — machine-level, shared across surfaces.
- Readonly flag on configured sources must be respected (reject writes).
- Keyed-data convention for safe patching (unique-match validation on text files).
- Format-agnostic file operations. The server has no knowledge of AIDE vocabulary.
- Stage-and-batch git model — each file operation stages, caller commands commit.
- Errors return enough information for the caller to decide what to do next. The server does not recover, retry, or swallow errors.
- Each primitive succeeds or fails independently. The AI manages multi-step sequences.

## Tool surface

| Tool | Behaviour |
| --- | --- |
| list sources | discovered sources with metadata and git-backed flag |
| browse | directory listing, optional glob filter |
| read | text (optional line limit) or binary |
| write | text or binary, full replace |
| patch | text only, keyed-data unique-match |
| copy | any file |
| rename | any file |
| delete | git-backed: actual delete; non-git: move to `_recycle` |
| mkdir | create directory |
| commit | caller-commanded, covers all staged changes |
| status | staged and modified files |
| binder build | caller-initiated |

## Linked build outcome

The MCP server, deployed via the `aide` plugin in the `digitalbusiness-aide` marketplace. Plus a governing skill that provides the AIDE document intelligence — versioning sequences, declaration management, convention enforcement, cleanup decisions — using the server's primitives.

## Definition of done

1. The server discovers document sources from config and `_index.md` markers, and lists them by name with metadata.
2. A caller can browse the folder structure of any discovered source, with glob filtering.
3. A caller can read any file — text with optional line limit, or binary.
4. A caller can write to any non-readonly source — text or binary.
5. Text files can be updated via patch (keyed-data unique-match).
6. Copy, rename, and delete operations work on any file, with delete respecting the git/non-git safety model.
7. Git changes are staged per operation and committed on caller command, producing one commit per update session.
8. Errors return actionable information; no silent failures.
9. Binder build is available as a server operation.
10. The server runs on Desktop and Code via the marketplace plugin.
11. A governing skill exists that orchestrates AIDE document conventions using the server's primitives.

---

Version note: v1 — initial brief from the document management design session. 2026-09-23.
