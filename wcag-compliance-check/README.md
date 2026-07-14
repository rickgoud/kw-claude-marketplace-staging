# Wcag Compliance Check

`v0.6.1` · updated 2026-07-14

Runs a shallow accessibility structure check (tagged PDFs, document/slide metadata, alt text, and HTML heading structure) over PDF, Word, PowerPoint, and HTML files in a Kiteworks folder under WCAG, and saves a report. This is not a full WCAG conformance test.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/wcag-compliance-check)** — live examples, screenshots, and full detail.

## What's new

Checks a Kiteworks folder for the WCAG-relevant signals a file-sharing platform can actually see — sensitive content and external sharing — and saves a report, clearly flagging what falls outside its view.

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
