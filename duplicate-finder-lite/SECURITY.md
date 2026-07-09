# Security profile — Duplicate Finder Lite

> Generated from the package's KACS spec — do not edit by hand; changes will be overwritten on the next build.

- **Plugin:** `kiteworks-duplicate-finder-lite` — package version 0.1.0
- **Grade:** productivity (Lite)

> **Productivity-grade helper. This is a best-effort assistant that calls Kiteworks directly through a host connector. It is NOT the audited Kiteworks compliance runtime: its output is not deterministic, not audit-defensible, and must not be relied on for compliance, legal, or regulatory decisions.**

## Scope

This package exposes exactly 1 workflow(s), listed below, and nothing else. No connector URL, credential, or server is bundled in this package; Kiteworks is reached only through the tenant-configured `Kiteworks` connector.

### Workflow: scan — read-only, metadata-only

Example ask: Find duplicate files in my Projects folder and show what space I could reclaim.

**Allowed tools (read-only):** get_folder_children, get_top_folders, get_user_info_whoami, search_folders.
**Never call:** delete_file, delete_folder, download_file_to_path, move_file, move_folder, read_file_contents, upload_file_from_path.
Requires an explicit folder or path before scanning.
Bounded walk — do not exceed max_depth=25, max_pages=50, max_items=20000.

> NEVER include fingerprint or hash values in your output — identify each duplicate set by a neutral label and its file names/paths only.

## Enforcement status

| Surface | Enforcement |
| --- | --- |
| claude.ai web chat | Guidance only — tool restrictions are host instructions the agent asks the host to honor; they are not runtime-enforced on this surface. |
| Claude Desktop chat | Guidance only — tool restrictions are host instructions the agent asks the host to honor; they are not runtime-enforced on this surface. |
| Claude Cowork | Guidance only — tool restrictions are host instructions the agent asks the host to honor; they are not runtime-enforced on this surface. |
| Claude Code | Guidance only — tool restrictions are host instructions the agent asks the host to honor; they are not runtime-enforced on this surface. |

These tool restrictions are host-instruction guidance, not runtime-enforced; the agent relies on the host honoring them.

## Security contact

To disclose a security issue in this package or the Kiteworks connector, contact Kiteworks via https://kiteworks.com.
