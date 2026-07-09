# 📊 Storage Visualizer Lite

**Version 0.3.0**

Best-effort direct-MCP storage summary over Kiteworks folder metadata - totals, largest folders/files, cleanup candidates. Productivity-grade and host-instruction-driven, not the audited compliance runtime.

> **Productivity-grade helper. This is a best-effort assistant that calls Kiteworks directly through a host connector. It is NOT the audited Kiteworks compliance runtime: its output is not deterministic, not audit-defensible, and must not be relied on for compliance, legal, or regulatory decisions.**

## Workflows

Each workflow is a bundled skill that fires automatically when your request matches it. Just ask in natural language. Where the surface supports invoking a skill by name, you can also run `/kiteworks-storage-viz-lite:<workflow>`:

- **scan** (`/kiteworks-storage-viz-lite:scan`) — Scan my Kiteworks storage and tell me the totals.
- **report** (`/kiteworks-storage-viz-lite:report`) — Build a storage dashboard for my Kiteworks files and save it.

## Setup

This plugin calls Kiteworks through a remote MCP connector named `Kiteworks`. See `skills/SETUP.md` to connect your tenant. No connector URL is bundled — your Kiteworks admin provides the tenant-specific link.

See `SECURITY.md` for this package's full security profile (allowed tools, enforcement status).
