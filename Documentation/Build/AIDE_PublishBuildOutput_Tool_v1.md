
# AIDE Publish Build Output — Tool

> **Identity:** `AIDE_PublishBuildOutputTool@v1`
> **Common name:** Publish Build Output
> **Version 1** (2026-09-02). First generic Build-owned post-Build publication Tool.

## Purpose

Publish/copy a successfully validated Build output to a nominated ordinary filesystem or repository
location without claiming deployment or registry state.

## Inputs

- validated Build output identity and source location;
- integrity evidence where available;
- explicit destination;
- replacement/atomicity behaviour supported by the destination; and
- current authority to write there.

## Procedure

1. Verify source identity, validation status and destination authority.
2. Refuse an AI Deployment Registry destination unless an applicable AI-Deployment-owned Tool owns it.
3. Publish/copy using the safest destination-supported replacement behaviour.
4. Verify the resulting bytes/state against the intended output/integrity evidence.
5. Return `Published | Partial | Blocked | Failed`, actual destination state and resumption guidance.

## Boundary

This Tool does not install, activate, register or verify runtime deployment. It does not infer
credentials, destination paths or replacement policy.

```yaml
MigrationSummary:
  CurrentVersion: v1
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Build@v6
References: Build_PostBuild_Design_v1
