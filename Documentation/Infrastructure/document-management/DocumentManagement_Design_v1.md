> identity: DocumentManagement_Design@v1 | doctype: design | updated: 2026-09-23

# Document Management — Design

## Summary

A Python MCP server providing safe, format-agnostic file primitives over document sources. Twelve tools cover discovery, browsing, reading, writing, patching, copying, renaming, deleting, directory creation, git staging, committing, and binder builds. The server has no knowledge of AIDE vocabulary — all document intelligence lives in a governing skill loaded in session.

---

## Model and approach

### Central principle — dumb server, smart skill

The server provides reliable file primitives. The AI in session, with the governing skill loaded, provides the AIDE document intelligence. The server never interprets declarations, understands versioning grammar, decides what is superseded, or knows what a doctype is.

This split exists because AIDE vocabulary evolves through standards, and standards change through the normal design-build-deploy cycle. If the server embedded that vocabulary, every standards change would require a server rebuild and redeployment. With the split, standards changes update the governing skill only — the server is stable infrastructure that changes when file operations change, not when document conventions change.

The boundary is clean: the server does things to files, the AI decides which things to do. Multi-step sequences (version-copy, cleanup passes, declaration updates) are orchestrated by the AI using the server's primitives, the same way a developer uses git commands without git knowing what the files mean.

### What the server owns

File operations with safety guarantees. Source discovery and config. Git staging and commit mechanics. The `_recycle` safety net for non-git sources. Keyed-data unique-match validation on patches. Readonly enforcement. Error reporting.

### What the server does not own

Any AIDE document convention. Versioning decisions, declaration management, cleanup decisions, document identity, docmeth rules, doctype awareness. These are the governing skill's concern.

---

## Source discovery

The server discovers document sources at startup by scanning configured roots.

**Discovery algorithm:**

1. Read `~/.aide/config.yaml` for scan roots and explicit includes.
2. For each scan root (when auto-discover is on), walk immediate subdirectories looking for `_index.md` files.
3. Read each `_index.md` — if the role field declares Documentation Solution or Documentation Project, register as a source.
4. Source name comes from the `_index` heading. Qualified naming (`Solution\Project`) used when project names collide across solutions.
5. Detect whether the source is git-backed by checking for a `.git` directory at or above the `_index` location.
6. Add any explicit includes from config.
7. Apply excludes.

Registered sources are held in memory for the server's lifetime. A restart re-scans. No file-watching or hot-reload — the set of sources changes rarely and a restart is trivial.

---

## Config

Machine-level config at `~/.aide/config.yaml`, read at startup, shared across all surfaces.

```yaml
scan-roots:
  - C:\Users\david\dev\repos

auto-discover: true   # default: true — scan roots for _index.md sources

include:               # explicitly add sources not under scan roots
  - path: C:\Users\david\docs\client-project
    name: client-project       # optional — overrides _index heading
    readonly: true             # optional — default false

exclude:               # skip discovered sources by path or name
  - C:\Users\david\dev\repos\archived-project
```

**Semantics:**

- `scan-roots` — directories to scan for repos and folders containing `_index.md`. Not recursive beyond one level of subdirectories.
- `auto-discover` — when true (default), the server walks scan roots on startup. When false, only explicit includes are registered.
- `include` — sources added by explicit path. Each may carry a name override and a readonly flag.
- `exclude` — paths or names to skip during auto-discovery. Does not affect explicit includes.
- `readonly` — when true, the server rejects all write, patch, delete, rename, copy, and mkdir operations on that source. Reads and browse are unaffected.

---

## Tool surface

Twelve tools. Each succeeds or fails independently. All file-mutating operations on git-backed sources stage the change automatically.

### list_sources

Returns all discovered sources with metadata: name, path, git-backed flag, readonly flag. No parameters.

### browse

List contents of a directory within a source.

- **source** — source name
- **path** — directory path within the source (optional — defaults to source root)
- **pattern** — glob filter (optional — e.g. `MyDoc_v*.md`)

Returns entries with: name, type (file or directory), size. Underscore-prefixed directories are included but flagged.

### read

Read a file's contents.

- **source** — source name
- **path** — file path within the source
- **lines** — return only this many lines from the top (optional, text files only)

For text files, returns the content as text. For binary files, returns base64-encoded content. When `lines` is specified, returns only the requested number of lines — the caller uses this to inspect file headers without loading the full document.

### write

Write or overwrite a file's entire content.

- **source** — source name
- **path** — file path within the source
- **content** — the full file content (text or base64 for binary)

Creates the file if it doesn't exist. Overwrites if it does. Stages the change in git-backed sources. Rejected on readonly sources.

### patch

Apply a partial update to a text file using keyed-data unique-match.

- **source** — source name
- **path** — file path within the source
- **old** — the text to find (must match exactly once in the file)
- **new** — the replacement text (empty string to delete the matched text)

The server validates that `old` matches exactly once before applying. On zero matches or multiple matches, the operation fails and returns the match count. This is the primary efficiency mechanism — a caller updates two lines without regenerating the file. Stages the change in git-backed sources. Rejected on readonly sources and binary files.

### copy

Copy a file within or across sources.

- **source** — source name of the original
- **path** — file path of the original
- **dest_source** — destination source name (optional — same source if omitted)
- **dest_path** — destination file path

Stages the new file in git-backed destinations. Rejected if the destination source is readonly.

### rename

Rename or move a file within a source.

- **source** — source name
- **path** — current file path
- **new_path** — new file path

Stages both the deletion of the old path and the addition of the new path. Rejected on readonly sources.

### delete

Remove a file from a source. Safety behaviour depends on the source type — the caller does not need to know or branch.

- **source** — source name
- **path** — file path to delete

On git-backed sources: actual file deletion, staged. Git retains the history. On non-git sources: the file is moved to a `_recycle` directory at the source root, preserving its relative path within `_recycle` to avoid name collisions. Rejected on readonly sources.

### mkdir

Create a directory within a source.

- **source** — source name
- **path** — directory path to create

Creates intermediate directories as needed. No git staging (git doesn't track empty directories). Rejected on readonly sources.

### commit

Commit all staged changes in a source's git repo.

- **source** — source name
- **message** — commit message

The caller decides when to commit — typically once at the end of an update session. All changes staged by prior operations (write, patch, copy, rename, delete) are included. Fails if the source is not git-backed or if there are no staged changes.

### status

Show the current state of a source's git working tree.

- **source** — source name

Returns staged files, modified-but-unstaged files, and untracked files. Fails with a clear message if the source is not git-backed.

### binder_build

Run the binder builder for a source.

- **source** — source name

Invokes the bundled Python binder-builder script against the source's document root. The binder builder has its own settings and configuration. The output is staged and included in the next commit. Caller-initiated — never runs automatically.

---

## Git model

**Stage per operation, commit on command.** Every file-mutating operation (write, patch, copy, rename, delete) stages its changes automatically via `git add`. The caller commands `commit` when the update session is complete. One commit message covering the batch.

If the caller doesn't commit (session drops, forgets), changes are staged but uncommitted — visible via `status`, trivially committable or discardable. This is a feature: the human can review staged changes before committing if desired.

No branch-based staging, no commit-per-file, no automatic commits. The model matches how git is actually used.

**Implementation:** `subprocess.run(["git", ...])` for all git operations. No git library dependency. The server shells out to the git binary on the user's PATH.

---

## Error model

Each operation succeeds or fails independently. The server reports failures and stops — it does not recover, retry, or swallow errors. The AI manages multi-step sequences and decides what to do when a step fails.

**Error categories and what the server returns:**

- **Patch mismatch** — zero matches or multiple matches. Returns the match count so the caller can widen or narrow the match string.
- **Readonly rejection** — operation attempted on a readonly source. Returns the source name and the operation attempted.
- **File not found** — names the path that was not found.
- **Source not found** — names the source that was not recognised.
- **Git failure** — returns git's error output verbatim.
- **Filesystem error** — returns the OS error (permissions, locked file, disk full).

Every error returns a structured response with: success flag, error type, and a human-readable message containing enough detail for the caller to act.

---

## Delete safety

The server handles delete differently based on whether the source is git-backed:

- **Git-backed source** — actual filesystem deletion, staged via `git add`. The file's history is preserved in git. This is the established convention: git is the version history.
- **Non-git source** — the file is moved to `_recycle` at the source root rather than deleted. The file's relative path within the source is preserved under `_recycle` to avoid name collisions. The `_recycle` directory is underscore-prefixed and therefore outside AIDE processing scope.

The caller always calls `delete`. The server determines the source type from discovery metadata and applies the appropriate behaviour. The caller does not need to know or branch — one operation, consistent safety.

---

## Packaging and delivery

Delivered as part of the `aide` plugin in the `digitalbusiness-aide` marketplace, following the tested MCP delivery model. Same pattern as the Orchestration dispatch server: a Python MCP server file in the plugin, registered via both the desktop app (Code/Cowork) and web UI (Chat).

The binder-builder Python script is bundled inside the plugin so that `binder_build` has no external dependency beyond the script itself and the source's binder settings.

---

## Boundaries

The server does not:

- Interpret, parse, or validate AIDE declarations, doctypes, or identity fields
- Make versioning decisions or know the versioning grammar
- Decide what is superseded or what to clean up
- Load, read, or reference any AIDE standard or skill
- Push to remote repositories
- Operate on non-local filesystems
- Watch for file changes or run operations automatically

---

Version note: v1 — initial design from the document management design session. 2026-09-23.
