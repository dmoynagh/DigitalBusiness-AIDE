# Documentation Methodology Standardisation — Installation & Migration

Generated: 2026-08-31

## 1. Master folder / GPT Project

Destination:

```text
AIDE/Document Methodology/
```

Add as current masters:

- `DocumentationMethodology_Index_v3.md`
- `DocumentationMethodology_Design_v15.md`
- `DocumentationMethodology_Decisions_v16.md`
- `AIDE_DocumentationMethodology_Standard_v18.md`

Keep unchanged/current:

- `DocumentationMethodology_Guide_v18.md`

Replace generated project context artefact:

- `DocumentationMethodology_Binder.md`

Move to `AIDE/Document Methodology/superseded/`:

- `DocumentationMethodology_Index_v2.md`
- `DocumentationMethodology_Design_v14.md`
- `DocumentationMethodology_Decisions_v15.md`

If you still hold the earlier v1/v14 files, they remain superseded history as before.

The old Binder is generated and may simply be replaced; preserving it is optional.

## 2. Common Bundle

Destination:

```text
AIDE/bundles/
```

Add:

- `AIDE_Bundle_StandardsTools_v3.md`

Move the previously issued current bundle:

- `AIDE_Bundle_StandardsTools_v2.md`

to:

```text
AIDE/bundles/superseded/
```

(or your existing equivalent superseded location).

## 3. GPT Project context change

Replace `AIDE_Bundle_StandardsTools_v1.md` with
`AIDE_Bundle_StandardsTools_v3.md` in every AIDE GPT Project:

- Core
- Project Design
- Build
- Capabilities
- AI Deployment
- Document Methodology

For **Document Methodology**, keep:

- `DocumentationMethodology_Binder.md`
- `AIDE_Bundle_StandardsTools_v3.md`

For the other AIDE GPT Projects, the separately-added
`DocumentationMethodology_Guide_v18.md` is no longer required merely to provide operational
methodology behaviour, because `AIDE_DocumentationMethodology@v18` is now in the common Bundle.

You may keep the Guide in a project temporarily where its richer explanatory detail is useful;
doing so is optional rather than part of the baseline runtime environment.

## 4. v17 → v18 document migration

Do **not** mass-rewrite unchanged v17 documents.

When a governed v17 document is next modified/saved:

1. if a modern Documentation Methodology dependency checkpoint already exists, use it;
2. otherwise, an unambiguous legacy `Methodology: v17` line supplies the synthetic starting
   checkpoint `AIDE_DocumentationMethodology@v17`;
3. apply the v18 OnUpdate transition;
4. replace the legacy Methodology line with a truthful
   `Dependencies: !AIDE_DocumentationMethodology@v18` checkpoint;
5. convert true legacy `Depends on` relationships to `Dependencies:` syntax;
6. preserve citation-only `References:`;
7. adopt v18 metadata/state placement for metadata/state actually present; and
8. avoid unrelated content rewrites.

Merely reading a v17 document does not migrate it.

A task requiring a v18-only structure may explicitly require migration first.

## 5. Minimal acceptance probes

After installing Bundle v2, use three small checks:

### Probe A — current v18 document

Input already has:

```text
Dependencies: !AIDE_DocumentationMethodology@v18
```

Expected: no DocMeth migration required.

### Probe B — legacy v17 document, read-only use

Input has:

```text
Methodology: v17
```

Expected: interpret v17 state for migration awareness but do not alter the document.

### Probe C — legacy v17 document being updated

Input has:

```text
Methodology: v17
```

Expected after successful save:

```text
Dependencies: !AIDE_DocumentationMethodology@v18
```

and no contradictory legacy `Methodology: v17` line.

## 6. What this pass deliberately does not do

- It does not mass-migrate the existing AIDE corpus.
- It does not create a DocMeth-specific Tool.
- It does not create a new capability release `@v19`.
- It does not change the existing Guide merely to restate the new Standard.
- It does not rebuild unrelated project Binders; only the common Bundle changes for those projects.
