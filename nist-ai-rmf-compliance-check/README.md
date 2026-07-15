# NIST AI RMF Compliance Check

`v0.6.2` · updated 2026-07-15

Checks a Kiteworks folder for AI-related documents that are shared externally or contain personal data, under NIST AI RMF. Most of NIST AI RMF is outside what this can check; it says so.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/nist-ai-rmf-compliance-check)** — live examples, screenshots, and full detail.

## What's new

Refined the NIST AI RMF checks and PII term matching; refreshed the branded report and safety pre-check.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install nist-ai-rmf-compliance-check@kiteworks-lite
```

**Claude Desktop:** download `nist-ai-rmf-compliance-check.plugin` (or the identical `nist-ai-rmf-compliance-check.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Check the Vendor Share folder for the NIST AI RMF exposure risks”
- “Summarize this folder's the NIST AI RMF exposure and save a report”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
