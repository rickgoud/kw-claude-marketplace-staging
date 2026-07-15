# ISM (Australia) Compliance Check

`v0.6.2` · updated 2026-07-15

Checks a Kiteworks folder for classification-marked content and external sharing under Australia's ISM, and saves a report. Most of ISM is outside what this can check; it says so.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/ism-au-compliance-check)** — live examples, screenshots, and full detail.

## What's new

Refined the Australian ISM checks and PII term matching; refreshed the branded report and safety pre-check.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install ism-au-compliance-check@kiteworks-lite
```

**Claude Desktop:** download `ism-au-compliance-check.plugin` (or the identical `ism-au-compliance-check.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Check the Vendor Share folder for the Australian ISM exposure risks”
- “Summarize this folder's the Australian ISM exposure and save a report”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
