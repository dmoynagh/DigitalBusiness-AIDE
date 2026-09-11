Working Practices — File Operations | working | WP_FileOps_Working@v1 | 2026-09-10

## Confirmed items — session 2026-09-10

### File delivery rules

Two rules for when files are updated outside of a FileUpdatePackage:

1. **Chat delivery** — when outputting an updated file for download, instruct the user where to save it based on the path in the document header.
2. **Code / Cowork direct file access** — check the file's physical location against the path in the header; move it if they disagree.

### Design and output separation

Design documents and the outputs they produce are separate. The design folder holds the specification. What gets built from it lives where it is consumed:

- Utilities → `_utilities/`
- Skills → deployed to the skills location
- Standards → deployed as capabilities
- Plugins → deployed to the marketplace

The design folder is always "why and how." The output is always elsewhere, wherever it runs.

### Superseded file handling

Git is the version history. The `_superseded` folder pattern is dropped. When a new version lands, the version-cleanup utility deletes the old version from the working tree and commits the deletion with a descriptive message. Rollback means `git checkout` of the previous version.

### Archived file handling

One `_archived` folder at the documentation root. Files that are no longer active but worth keeping — retired references, completed reviews, outdated knowledge. Moving a file there removes it from binder scope (underscore-prefixed folders are outside AIDE processing) while keeping it in the repo and searchable.

### Utility git commit behaviour

Utilities stage and commit their own changes with descriptive messages. When the FileUpdatePackage applies an update, or version-cleanup removes an old file, or the binder builder regenerates, the utility stages the changes, commits with a clear message (e.g. "FUP: applied Principles_2026-09-08"), and the user does not need to remember to commit.

### FUP move action

The FileUpdatePackage needs a move or rename action for when a document's path changes. The header is updated (authoritative change), the FUP manifest records the move (old path, new path), and the utility executes it. Extends the existing action vocabulary (create, replace) with move.

---

Version note: v1 — initial working document from session 2026-09-10.
