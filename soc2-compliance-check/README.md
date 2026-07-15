# SOC 2 Compliance Check

`v0.5.2` · updated 2026-07-15

Checks a Kiteworks folder for the narrow slice of SOC 2 a file-sharing platform can actually see -- sensitive content and external sharing -- and saves a report. Most of SOC 2 is outside what this can check; it says so.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/soc2-compliance-check)** — live examples, screenshots, and full detail.

## What's new

Refined the SOC 2 checks and PII term matching; refreshed the branded report and safety pre-check.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install soc2-compliance-check@kiteworks-lite
```

**Claude Desktop:** download `soc2-compliance-check.plugin` (or the identical `soc2-compliance-check.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Check the Vendor Share folder for SOC 2 exposure risks”
- “Summarize this folder's SOC 2 exposure and save a report”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
