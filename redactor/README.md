# Redactor

`v0.5.0` · updated 2026-07-14

Finds and replaces specific text -- like a name or other sensitive information -- across documents in a Kiteworks folder, and creates redacted copies once you approve. Originals are never changed.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/redactor)** — live examples, screenshots, and full detail.

## What's new

Improved content extraction and the redaction apply step; refreshed report export.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install redactor@kiteworks-lite
```

**Claude Desktop:** download `redactor.plugin` (or the identical `redactor.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Redact the name 'Jane Smith' from documents in the Case Files folder”
- “Create the redacted copies”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
