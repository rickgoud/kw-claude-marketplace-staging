# WCAG Compliance Check

`v0.6.2` · updated 2026-07-15

Runs a shallow accessibility structure check (tagged PDFs, document/slide metadata, alt text, and HTML heading structure) over PDF, Word, PowerPoint, and HTML files in a Kiteworks folder under WCAG, and saves a report. This is not a full WCAG conformance test.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/wcag-compliance-check)** — live examples, screenshots, and full detail.

## What's new

Refined the WCAG checks and PII term matching; refreshed the branded report and safety pre-check.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install wcag-compliance-check@kiteworks-lite
```

**Claude Desktop:** download `wcag-compliance-check.plugin` (or the identical `wcag-compliance-check.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Check the Vendor Share folder for WCAG exposure risks”
- “Summarize this folder's WCAG exposure and save a report”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
