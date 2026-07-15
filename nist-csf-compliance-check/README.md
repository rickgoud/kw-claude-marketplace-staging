# NIST CSF Compliance Check

`v0.5.2` · updated 2026-07-15

Checks a Kiteworks folder for external sharing exposure, the one sliver of NIST CSF's Protect function a file-sharing platform can see, and saves a report. Most of NIST CSF is outside what this can check; it says so.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/nist-csf-compliance-check)** — live examples, screenshots, and full detail.

## What's new

Refined the NIST CSF checks and PII term matching; refreshed the branded report and safety pre-check.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install nist-csf-compliance-check@kiteworks-lite
```

**Claude Desktop:** download `nist-csf-compliance-check.plugin` (or the identical `nist-csf-compliance-check.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Check the Vendor Share folder for the NIST CSF exposure risks”
- “Summarize this folder's the NIST CSF exposure and save a report”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
