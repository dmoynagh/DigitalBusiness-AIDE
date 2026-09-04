# AI Deployment OpenAI — Reference

> **Version 1** (2026-08-30). Consolidates the empirical OpenAI deployment evidence used to
> establish the initial AI Deployment target model.

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

## Evidence discipline

A reconstructed answer, prior reported probe value, project file read, or filesystem read is not
accepted as proof that a runtime executed the deployed capability. Verification should use a
fresh, target-appropriate runtime probe where execution availability is the claim.

---
Dependencies: !AIDE_DocumentationMethodology@v18, AIDeployment_Design_v1
References: Capabilities_OpenAIPlatform_TestRecord_2026-08-30_v3_WORKING
