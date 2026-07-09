# Kiteworks Document Summarizer

Find and summarize documents stored in Kiteworks — Word docs, PDFs, PowerPoint, Excel, and plain text — directly in chat, without leaving the conversation to open the file yourself.

## What it does

Ask things like:

- "Summarize TestDocx.docx in Kiteworks"
- "What's in the file at My Folder/Reports/Q3 update.pdf?"
- "Give me the gist of the deployment plan on Kiteworks"

The plugin finds the file, checks it's clean (antivirus/DLP status) and notes any sensitivity label, retrieves its content, and returns a right-sized summary with the source path and last-modified date so it's traceable.

## Prerequisites

- **A Kiteworks MCP connector**, connected and enabled for the conversation.
- **The Filesystem extension**, connected with at least one allowed directory — required for binary formats (`.docx`, `.pdf`, `.pptx`, `.xlsx`, etc.). Without it, only text-based files (`.txt`, `.csv`, `.json`, `.xml`, `.md`) can be summarized.

## Why the Filesystem extension is needed

The current Kiteworks MCP server exposes only two ways to read file content: a text-only tool that rejects binary formats, and a "download to path" tool that writes to a filesystem rather than returning bytes directly. Until the server adds a base64-capable read tool (mirroring how it already accepts base64 on *upload*), binary files have to be bridged through a local filesystem the Filesystem extension can reach. See `skills/kw-binary-file-bridge/SKILL.md` for the exact mechanism and its one known limitation (the extension can't delete files — a leftover empty placeholder stays on disk after content is scrubbed).

## Components

| Component | Purpose |
|---|---|
| `skills/kw-document-summarizer` | The user-facing workflow: find the file, check it, read it, summarize it, optionally save the summary back. |
| `skills/kw-binary-file-bridge` | Reusable infrastructure skill that bridges binary file content into Claude's sandbox via the Filesystem extension. Self-contained — copy this folder as-is into any other plugin that needs the same capability. |

## Reusing `kw-binary-file-bridge` elsewhere

This skill has no dependency on the summarizer skill. To use it in a different plugin, copy `skills/kw-binary-file-bridge/` into that plugin's `skills/` directory unchanged. There's no cross-plugin import in this plugin system, so this copy is the canonical source — if you improve it, propagate the change manually to other plugins that carry a copy.

## Known limitations

- Binary files can't be read without the Filesystem extension (see above).
- Cleanup of temporary local files is content-only (overwritten empty), not deletion — the extension has no delete tool today.
- If a file search matches more than one result, the skill will ask which one rather than guessing.
- Encrypted files and image-only (non-OCR'd) scans aren't supported.

## Suggested longer-term fix

Feed back to whoever owns the Kiteworks MCP server roadmap: add a `read_file_contents` option (or an equivalent) that supports `encoding: base64` for binary files, symmetric with how `create_file_from_content` already accepts base64 on upload. That would remove the need for this bridge — and the Filesystem extension prerequisite — entirely.
