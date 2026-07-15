# NIS2 Compliance Check

`v0.5.2` · updated 2026-07-15

Checks a Kiteworks folder for external sharing of flagged documentation under NIS2, and saves a report. Most of NIS2 is outside what this can check; it says so.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/nis2-compliance-check)** — live examples, screenshots, and full detail.

## What's new

Refined the NIS2 checks and PII term matching; refreshed the branded report and safety pre-check.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install nis2-compliance-check@kiteworks-lite
```

**Claude Desktop:** download `nis2-compliance-check.plugin` (or the identical `nis2-compliance-check.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Check the Vendor Share folder for NIS2 exposure risks”
- “Summarize this folder's NIS2 exposure and save a report”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
