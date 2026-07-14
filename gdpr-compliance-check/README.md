# Gdpr Compliance Check

`v0.5.1` · updated 2026-07-14

Scans a Kiteworks folder for personal data, external sharing, and files older than your retention policy under GDPR, and saves a report. Covers the same ground GDPR's storage-limitation and exposure concerns care about.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/gdpr-compliance-check)** — live examples, screenshots, and full detail.

## What's new

Checks a Kiteworks folder for the GDPR-relevant signals a file-sharing platform can actually see — sensitive content and external sharing — and saves a report, clearly flagging what falls outside its view.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install gdpr-compliance-check@kiteworks-lite
```

**Claude Desktop:** download `gdpr-compliance-check.plugin` (or the identical `gdpr-compliance-check.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Check the Vendor Share folder for GDPR exposure risks”
- “Summarize this folder's GDPR exposure and save a report”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
