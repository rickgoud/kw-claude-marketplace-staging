# HIPAA Compliance Check

`v0.5.2` · updated 2026-07-15

Scans a Kiteworks folder for PHI-shaped content, external sharing, and files past HIPAA's 6-year documentation-retention window, and saves a report.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/hipaa-compliance-check)** — live examples, screenshots, and full detail.

## What's new

Refined the HIPAA checks and PII term matching; refreshed the branded report and safety pre-check.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install hipaa-compliance-check@kiteworks-lite
```

**Claude Desktop:** download `hipaa-compliance-check.plugin` (or the identical `hipaa-compliance-check.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Check the Vendor Share folder for HIPAA exposure risks”
- “Summarize this folder's HIPAA exposure and save a report”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
