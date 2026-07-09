---
name: kw-binary-file-bridge
description: >
  Use this skill whenever a task needs the actual content of a binary file (.docx, .pdf, .pptx, .xlsx, .doc, .ppt, .xls, images, archives) that lives on Kiteworks — or any other MCP-connected source whose tools can only download files to a local filesystem path rather than returning raw bytes directly in a tool result. This is a plumbing/infrastructure skill invoked by other skills (like kw-document-summarizer), not something a user asks for by name. Triggers include: a binary-read MCP tool (e.g. read_file_contents) rejecting a file as "not supported" or "binary not allowed"; another skill's workflow needing to get a binary file from an external source into Claude's own sandbox for processing (pandoc, pdf extraction, python-pptx, python-docx, etc.). This skill is surface-aware — it only requires the separate Filesystem extension in standard Chat; in Cowork sessions, native local file access already covers this and the skill skips the extension requirement entirely. Do NOT use this for text-based files (txt, csv, json, xml, md, log) — try the source's native text-read tool first; only fall back to this bridge when that is rejected or absent.
---

# Kiteworks / MCP Binary File Bridge

## Step 0 — Detect the runtime surface first

This skill's whole reason for existing is that **standard Chat has no native bridge to a local filesystem** — Claude's environment there is a remote sandbox with no connection to the user's computer, which is exactly why the separate Filesystem extension/connector exists as a workaround.

**Cowork is different and does not need this workaround.** In a Cowork session, Claude already has direct, native local file read/write access as a core product capability — the Claude Desktop app grants this for the session's connected workspace folder(s), with no separate connector involved. If you're running in Cowork, using the Filesystem extension bridge below is redundant and adds an unnecessary permission ask.

**How to tell which surface you're in:** check what's already in your available tool list before assuming anything.
- If native local file tools (read/write/edit a real path on the user's machine) are already present *without* being namespaced under a separate connector like `Filesystem:...` — you're in Cowork (or an equivalent surface with native local access). **Skip straight to the Cowork path below.** Do not search for or ask the user to install the Filesystem extension; it isn't needed.
- If no native local file tools are present at all, and the only way to reach a local path is a distinct `Filesystem:` — namespaced connector that must be separately searched for and connected — you're in standard Chat. **Use the Prerequisites and Procedure sections below.**
- If genuinely unsure, look at how the Kiteworks download tool's target path resolves: in Cowork it should land inside the session's connected workspace folder where your native tools can already see it, with no bridging step needed at all — try reading it directly first before reaching for anything else.

### Cowork path (native local access already available)

1. Pick a location inside the session's connected workspace folder (not an arbitrary system path) as the download target.
2. Download the file there using the source MCP's "download to path" tool.
3. Read it directly with your native file tools — no `copy_file_user_to_claude` step, no Filesystem extension involved.
4. Process it with the appropriate format skill (docx, pdf, pptx, xlsx, etc.).
5. If the workspace is meant to stay clean, remove the temp file with your native delete/file-management capability once done — Cowork's tools aren't limited the way the Chat-side extension is (see the known limitation below), so real deletion is possible here.

Everything from here down (Prerequisites, Procedure, Known limitation) applies **only** to the standard-Chat path, where the Filesystem extension bridge is actually necessary.

## Why this exists

Some MCP servers (Kiteworks included) expose exactly two ways to get file content:

1. A text-only read tool (e.g. `read_file_contents`) that explicitly rejects binary formats.
2. A `download_file_to_path` — style tool that writes bytes to **a filesystem path**, not into the conversation.

There is currently no tool that returns base64-encoded binary bytes directly in a tool result (the way `create_file_from_content` accepts base64 for *uploads*). Until the source MCP server adds that, the only way to get binary bytes into Claude's own sandbox is to bounce them through a filesystem the Filesystem extension can reach — which today means the user's local machine, not Claude's sandbox directly.

**Treat this skill as a workaround, not a permanent design.** If the source MCP server later adds a base64/binary-capable read tool, skip this entire skill and read the file directly.

## Prerequisites — check before doing anything else

1. Check whether a `Filesystem:list_allowed_directories` tool is even available (search for it if it hasn't been loaded yet). Two distinct failure modes need two distinct messages:
   - **No such tool exists at all** → the Filesystem extension isn't installed. Tell the user this binary file needs the Filesystem extension added first, and that without it only text-based files (txt, csv, json, xml, md) can be summarized.
   - **The tool exists but `list_allowed_directories` errors or returns no directories** → the extension is installed but not connected/configured for this conversation. Tell the user to connect it (or check its folder configuration) before retrying.
   - Never guess at behavior in either case — the message the user needs differs (add the extension vs. reconnect it), so don't collapse them into one generic "something's wrong" response.
2. Do not silently fall back to guessing a sandbox path (`/home/claude/...`, `/tmp/...`) as the download target — the download tool writes wherever the MCP server process runs, which is the user's machine, not Claude's sandbox. Passing a sandbox-style path will fail with a filesystem error (e.g. "system cannot find the path specified").
3. Confirm the source MCP actually can't return the content another way (re-check: is this genuinely a binary format, and does the source lack a base64 option?). Don't invoke this bridge for anything a native text tool can already serve.

## Procedure

1. **Pick an allowed directory** from step 1 above — use the first one unless the user has specified otherwise.
2. **Generate a unique temp filename** to avoid collisions with concurrent runs or repeated calls on the same file name: `claude-bridge-<unix_timestamp>-<original_filename>`. Never reuse a bare original filename as the temp name.
3. **Download** the file from the source MCP's "download to path" tool, with `target` = `<allowed_directory>\<temp_filename>` (respect the OS path style the Filesystem extension reports — Windows paths use backslashes and a drive letter, as in the example above).
4. **Copy into Claude's sandbox** using `copy_file_user_to_claude` on that same temp path. This lands the file under `/mnt/user-data/uploads/` where Claude's normal file-processing tools (bash, view, skills for docx/pdf/pptx/xlsx) can work with it.
5. **Process the file** using the appropriate format skill (docx, pdf, pptx, xlsx, etc.) from the sandbox copy — never try to parse the file directly on the user's machine.
6. **Scrub the temp file** when done: overwrite it with empty content via `write_file` (content: `""`) at the same path used in step 3.

## Known limitation — read before promising "cleanup" to a user

The Filesystem extension currently has no delete capability. Step 6 overwrites the temp file's *content* so no sensitive bytes remain on disk, but the empty file itself stays at that path with its `claude-bridge-...` name until the user deletes it manually. Say this plainly if a user asks about cleanup — don't imply the file is fully removed when it isn't. Mentioning the exact leftover path is more useful than a vague "it's cleaned up."

## Reusing this skill in other plugins

This SKILL.md has no dependency on the document-summarizer skill in this plugin — it's self-contained. To reuse it in another plugin, copy this entire `skills/kw-binary-file-bridge/` directory into the new plugin's `skills/` folder unchanged. There is no cross-plugin import mechanism in this plugin system, so copying the file is the supported pattern — keep this copy as the canonical source and propagate updates manually to other plugins that include it.
