# AI Deployment OpenAI — Reference

> **Version 3** (2026-09-02). Adds the current GitHub marketplace distribution baseline while
> retaining the runtime-execution evidence boundary.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

## Established evidence

The tested local OpenAI plugin/skill route cannot be treated as one common private deployment
channel across ChatGPT Chat and Codex.

The evidence established:

- a representation being visible/installed in one surface does not prove its skill body is
  executable in another runtime;
- Codex local plugin/marketplace behaviour and ChatGPT Chat runtime availability are distinct;
- ChatGPT web discovery of a local plugin was not established by the local route;
- standalone/personal skill availability across Work, Chat and Codex also differed in testing;
- UI presence or install state is therefore weaker evidence than a runtime content probe; and
- deployment architecture must model **surface**, **representation** and **distribution channel**
  separately.

## Architectural conclusion

Do not use the previously proposed “one local OpenAI plugin install = common ChatGPT + Codex
deployment route” as architecture.

Keep hosted/public/account-synchronised routes as empirical target-adapter work. The generic
Deployment model does not need those results before it can operate.

## Current GitHub marketplace baseline

Current official OpenAI documentation checked on 2026-09-02 establishes that:

- workspace administrators can import plugin marketplaces from public or private GitHub
  repositories;
- a marketplace may be located in a repository subdirectory and may track the default branch, a
  named branch/tag or a fixed commit;
- native `.agents/plugins/marketplace.json`, Claude-compatible marketplace manifests and a
  standalone Claude plugin manifest are supported import formats;
- new marketplaces use daily sync and `Sync now` requests an update;
- repository sync and workspace installation/access policy are separate; and
- removing a repository entry does not delete the imported workspace plugin—it becomes
  `No longer in source`, so runtime removal requires an explicit workspace/plugin action.

Accordingly, `DigitalBusiness-AIDE-Marketplace/openai` is the preferred initial distribution route
for `aide-core-openai`. Use the native OpenAI representation even though compatible import formats
exist; import compatibility does not prove equal runtime behaviour.

Codex is required reach for this output. ChatGPT is additional intended reach only where the
configured plan/workspace/role/surface supports it. A missing unsupported ChatGPT surface is not
automatically a degraded Build; failure in the configured required Codex target is.

## Evidence discipline

A reconstructed answer, prior reported probe value, project file read, or filesystem read is not
accepted as proof that a runtime executed the deployed capability. Verification should use a
fresh, target-appropriate runtime probe where execution availability is the claim.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDeployment_Design_v6
References: Capabilities_OpenAIPlatform_TestRecord_2026-08-30_v3_WORKING, Workflow_Platform_Working_2026-09-02-1_v1, https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex, https://help.openai.com/en/articles/20001504-importing-and-syncing-plugin-marketplaces-from-github
