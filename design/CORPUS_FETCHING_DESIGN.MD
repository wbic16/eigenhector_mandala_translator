# Corpus Fetching Tool Design

## Overview
This document outlines the design for a tool to fetch and preprocess text articles from various online sources into a standardized Markdown format suitable for corpus analysis.

## Core Features

1.  **Source Handling:**
    *   **Substack XML sitemaps:** e.g., `https://eigenhector.substack.com/sitemap.xml`
        *   **Filtering:** Only fetch URLs matching specific patterns (e.g., `/p/` for posts) to avoid fetching non-article pages.
    *   **Link Collection Pages:** e.g., `https://example.com/posts/` (Fetches `.md` files linked from the page)
    *   **GitHub Repositories:** e.g., `https://github.com/wbic16/eigenhector_mandala_translator/` (Fetches `.md` files)

2.  **Content Processing:**
    *   Parse HTML/XML content.
    *   Extract relevant text, metadata (title, date, author).
    *   Convert content into clean Markdown.

3.  **Rate Limiting / Quantity Control:**
    *   Implement a flag to limit the number of posts fetched (e.g., `--limit <number>`).

4.  **Integration:**
    *   Output files must be in Markdown format to be directly usable by `skills/CORPUS_ANALYSIS.MD`.

## Usage Examples

### Substack Example
**Target:** `https://eigenhector.substack.com/sitemap.xml`

**Command:**
```bash
fetch-corpus --source "https://eigenhector.substack.com/sitemap.xml" --type substack --limit 10 --name eigenhector
# Automatically filters for /p/ links by default for Substack type
# Stores in reports/mystic_corpus/eigenhector/
```

### Link Collection Example
**Target:** `https://smoothbrains.net/posts/index.html` (containing links to `.md` files)

**Command:**
```bash
fetch-corpus --source "https://smoothbrains.net/posts/index.html" --type html-links --limit 5 --name smoothbrains
# Stores in reports/mystic_corpus/smoothbrains/
# Fetches only .md files
```

### GitHub Repository Example
**Target:** `https://github.com/wbic16/eigenhector_mandala_translator`

**Command:**
```bash
fetch-corpus --source "https://github.com/wbic16/eigenhector_mandala_translator" --type github --limit 20 --name eigenhector_translator
# Stores in reports/mystic_corpus/eigenhector_translator/
# Fetches only .md files
```

## Output Format
Each fetched article should be saved as a separate Markdown file.

**File format:**
Files are named with a 5-digit index (e.g., `00001.md`). The mapping between the ID and the original metadata is stored in `index.json`.
```markdown
---
title: [Article Title]
date: [YYYY-MM-DD]
url: [Original URL]
---

# [Article Title]

[Content converted to Markdown...]
```

## Integration with Corpus Analysis
The generated Markdown files are the input for the process described in `skills/CORPUS_ANALYSIS.MD`. The analysis tools expect clean Markdown with metadata headers.

## Security & Safety

### Injection Attack Prevention
*   **Filename Generation:** Strict 5-digit numeric filenames (e.g., `00001.md`) are used to prevent filesystem injection attacks. The original title is stored in metadata, not the filename.
*   **URL Validation:**
    *   Ensure URLs use `http` or `https` schemes.
    *   Validate domains against expected sources if possible (e.g., only `substack.com` subdomains for substack type).
*   **Content Sanitization:**
    *   **HTML:** Strip `<script>`, `<object>`, `<embed>`, `<iframe>`, and `style` tags before conversion to Markdown.
    *   **Markdown:** Maintain standard Markdown syntax but be wary of raw HTML embedding.

### User Data Safety
*   **Size Limits:**
    *   **Max File Size:** Enforce a hard limit (e.g., 10MB) on individual article downloads to prevent memory exhaustion or disk filling.
    *   **MIME Type Check:** Verify `Content-Type` headers before downloading large bodies (text/html, application/xml, text/plain only).
*   **Network Safety:**
    *   **Timeouts:** Enforce connection and read timeouts (e.g., 10 seconds) on all requests to prevent hanging processes.
    *   **Retries:** limited retries with exponential backoff for transient errors.
*   **Rate Limiting:**
    *   Implement delays between requests (e.g., 1 second) to be a polite crawler and avoid IP bans.

## Storage & Deduplication

### Default Storage Location
*   **Path:** Project root under `reports/mystic_corpus`.
    *   **Project Root:** `reports/mystic_corpus/`
*   **Structure:**
    *   `mystic_corpus/`
        *   `<corpus_name>/` (Subdirectory for the specific corpus)
            *   `docs/` (Actual markdown files, named `00001.md`, `00002.md`, etc.)
            *   `index.json` (Index of fetched documents, mapping IDs to metadata)

### Deduplication
*   **Index File:** Verify against `index.json` in the corpus directory before fetching.
*   **Check:** If a URL or Title already exists in the index, skip fetching unless a `--force` flag is used.
*   **Update:** Upon successful fetch, append the new article's metadata (URL, Title, Date, Local Path) to `index.json`.

### Flags
*   `--name <corpus_name>`: Name of the corpus (creates directory).
*   `--storage-root <path>`: Override the default `mystic_corpus` location.
*   `--force`: Force re-fetch even if present in the index.
*   `--limit <number>`: Limit the number of articles fetched.



## User Directory & Configuration

To simplify usage, a JSON-based user directory allows mapping short user names to corpus hosting information.

### Configuration File
*   **Location:** `mystic_corpus/corpus_registry.json` (inside the user's `mystic_corpus` directory)
*   **Purpose:** Maps short aliases (e.g., "ari") to source details.

### JSON Structure
```json
{
  "ari": {
    "type": "substack",
    "url": "https://ari.substack.com/sitemap.xml",
    "description": "Ari's Substack"
  },
  "hector": {
    "type": "github",
    "url": "https://github.com/hectorgon/eigenhector_mandala_translator",
    "description": "Hector's GitHub Repo"
  }
}
```

### Usage
When the `--user` flag is used, the tool looks up the alias in `corpus_registry.json` to determine the `source` and `type`.

**Example Command:**
```bash
fetch-corpus --user ari --limit 5
# Equivalent to:
# fetch-corpus --source "https://ari.substack.com/sitemap.xml" --type substack --limit 5 --name ari
```

## Environment Setup

### Virtual Environment
This project uses a Python 3 virtual environment to manage dependencies locally.
*   **Location:** `%USERPROFILE%\.virtualenvs\eigenhector` (Windows)
*   **Activation:** Run `.virtualenvs\eigenhector\Scripts\activate` (or specify absolute path to python/pip).

### Dependencies
*   **File:** `requirements.txt` (in repository root)
*   **Install:**
    ```bash
    %USERPROFILE%\.virtualenvs\eigenhector\Scripts\pip install -r requirements.txt
    ```

### Usage for Agents

When running Python scripts (e.g., `check_requests.py` or new tools), **ALWAYS** use the python executable from the virtual environment.

#### Windows
**Command Prompt (cmd):**
```cmd
%USERPROFILE%\.virtualenvs\eigenhector\Scripts\python <script_name>.py
```

**PowerShell:**
```powershell
& "$env:USERPROFILE\.virtualenvs\eigenhector\Scripts\python" <script_name>.py
```

#### Linux / macOS
```bash
# Standard location
~/.virtualenvs/eigenhector/bin/python <script_name>.py
```

This ensures all installed packages (like `requests`) are available.
