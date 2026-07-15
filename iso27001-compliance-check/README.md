# ISO 27001 Compliance Check

`v0.5.2` · updated 2026-07-15

Checks a Kiteworks folder for the narrow slice of ISO 27001 a file-sharing platform can actually see -- sensitive content and external sharing -- and saves a report. Most of ISO 27001 is outside what this can check; it says so.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/iso27001-compliance-check)** — live examples, screenshots, and full detail.

## What's new

Refined the ISO 27001 checks and PII term matching; refreshed the branded report and safety pre-check.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install iso27001-compliance-check@kiteworks-lite
```

**Claude Desktop:** download `iso27001-compliance-check.plugin` (or the identical `iso27001-compliance-check.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Check the Vendor Share folder for ISO 27001 exposure risks”
- “Summarize this folder's ISO 27001 exposure and save a report”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
