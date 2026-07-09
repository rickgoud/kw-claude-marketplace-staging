# 🗂️ Duplicate Finder Lite

**Version 0.1.0**

Best-effort direct-MCP duplicate report over Kiteworks folder metadata - groups files whose content fingerprint and size both match and shows the reclaimable space. Report only; nothing is moved or deleted. Productivity-grade and host-instruction-driven, not the audited compliance runtime.

> **Productivity-grade helper. This is a best-effort assistant that calls Kiteworks directly through a host connector. It is NOT the audited Kiteworks compliance runtime: its output is not deterministic, not audit-defensible, and must not be relied on for compliance, legal, or regulatory decisions.**

## Workflows

Each workflow is a bundled skill that fires automatically when your request matches it. Just ask in natural language. Where the surface supports invoking a skill by name, you can also run `/kiteworks-duplicate-finder-lite:<workflow>`:

- **scan** (`/kiteworks-duplicate-finder-lite:scan`) — Find duplicate files in my Projects folder and show what space I could reclaim.

## Setup

This plugin calls Kiteworks through a remote MCP connector named `Kiteworks`. See `skills/SETUP.md` to connect your tenant. No connector URL is bundled — your Kiteworks admin provides the tenant-specific link.

See `SECURITY.md` for this package's full security profile (allowed tools, enforcement status).
