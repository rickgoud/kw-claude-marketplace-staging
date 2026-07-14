# Nist 800 53 Compliance Check

`v0.5.1` · updated 2026-07-14

Scans a Kiteworks folder for CUI/PII-shaped content and external sharing under NIST SP 800-53, and saves a report. Most of the control catalog is outside what this can check; it says so.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/nist-800-53-compliance-check)** — live examples, screenshots, and full detail.

## What's new

Checks a Kiteworks folder for the NIST 800-53-relevant signals a file-sharing platform can actually see — sensitive content and external sharing — and saves a report, clearly flagging what falls outside its view.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install nist-800-53-compliance-check@kiteworks-lite
```

**Claude Desktop:** download `nist-800-53-compliance-check.plugin` (or the identical `nist-800-53-compliance-check.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Check the Vendor Share folder for NIST 800-53 exposure risks”
- “Summarize this folder's NIST 800-53 exposure and save a report”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
