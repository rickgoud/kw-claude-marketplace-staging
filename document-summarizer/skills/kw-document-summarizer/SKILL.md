---
name: kw-document-summarizer
description: >
  Use this skill whenever the user asks to summarize, review, or explain what's in a file stored in Kiteworks — triggers include "summarize this Kiteworks file", "what's in X.docx on Kiteworks", "give me the gist of that file", "what does the file in My Folder say", "can you summarize this filename", or any request to find and summarize a named document, spreadsheet, or presentation that lives in Kiteworks rather than being pasted or uploaded directly into the conversation. Do NOT use this for files already uploaded/attached directly to the conversation — those can be read without any of the Kiteworks lookup or bridging steps below.
---

# Kiteworks Document Summarizer

## Step 1 — Find the file

Search Kiteworks with `search_files` (or `search` for a broader name/content match) using the name or description the user gave.

- **Exactly one match:** proceed.
- **Multiple matches:** list the candidate paths (folder + filename + last modified date) and ask which one, rather than guessing. Don't silently pick the most recent or first result.
- **No matches:** say so plainly and ask for a more specific name or folder — don't invent a result.

## Step 2 — Check the file before reading it

Call `get_file_metadata` on the matched file and look at:

- **`avStatus`** — if it's still `scanning` or shows an infected/blocked result, tell the user and stop. Don't summarize a file that hasn't cleared antivirus scanning.
- **`dlpStatus`** — if DLP has flagged or blocked the file, surface that to the user rather than proceeding silently.
- **Sensitivity/classification label**, if the metadata exposes one (e.g. MSIP label) — mention it in your eventual summary output rather than omitting it. A summary of a "Confidential — Restricted" file should say so.

## Step 3 — Get the content

Route by extension:

- **Text-based** (`.txt`, `.csv`, `.json`, `.xml`, `.md`, `.log`): call `read_file_contents` directly. No bridging needed.
- **Binary** (`.docx`, `.pdf`, `.pptx`, `.xlsx`, `.doc`, `.ppt`, `.xls`): use the **kw-binary-file-bridge** skill to get the file into Claude's sandbox, then extract text with the matching format skill/tool:
  - `.docx` / `.doc` → the docx skill (`pandoc -t markdown` for reading)
  - `.pdf` → the pdf-reading skill
  - `.pptx` → the pptx skill's read path
  - `.xlsx` / `.xls` → the xlsx skill's read path
- **Anything else** (encrypted files, image-only scans without OCR, unrecognized formats): tell the user clearly that this format isn't supported yet rather than attempting a partial read.

## Step 4 — Write the summary

- **Length:** default to something proportional to the source — a sentence or two for a short file, a short paragraph plus a few key-point bullets for a longer one. Don't ask the user to specify a length up front; deliver a sensible default, then offer to go shorter/longer or more detailed afterward.
- **PII and sensitive identifiers:** never reproduce government IDs, full financial account numbers, credentials, or similarly sensitive strings verbatim in the summary — describe generically instead (e.g. "a sample BSN value" rather than the digits). This applies even if the source file is explicitly a test/sample file.
- **Traceability:** name the file's path and last-modified date in your response so the summary is traceable back to its source.
- **Classification:** if Step 2 surfaced a sensitivity label or a DLP/AV flag, restate it alongside the summary rather than only in an internal check.

## Step 5 — Optional: save the summary back to Kiteworks

If the user asks to save the summary as a file:

- **Plain text (.txt):** `create_file_from_content` with UTF-8 encoding — no extra steps needed.
- **Word document (.docx):** follow the docx skill's full creation process, **including its render-and-verify step** (`soffice.py --headless --convert-to pdf` → `pdftoppm` → look at the rendered pages) before uploading. Only after visual verification, base64-encode the file and upload with `create_file_from_content` (`encoding: "base64"`) directly to the target Kiteworks folder — do not round-trip a generated output file through the user's local machine; that's only needed for the read path in kw-binary-file-bridge, not for writes.
- Confirm the destination folder with the user if it's not obvious (e.g. default to the same folder as the source file, but say so).
