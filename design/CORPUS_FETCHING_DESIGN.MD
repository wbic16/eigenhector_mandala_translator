# Corpus Fetching Tool Design

## Overview
This document outlines the design for a tool to fetch and preprocess text articles from various online sources into a standardized Markdown format suitable for corpus analysis.

## Core Features

1.  **Source Handling:**
    *   **Substack XML sitemaps:** e.g., `https://eigenhector.substack.com/sitemap.xml`
    *   **Link Collection Pages:** e.g., `https://smoothbrains.net/posts/2025-10-18-three-year-retrospective.html#sequences`
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
# Stores in ~/Documents/mystic_corpus/eigenhector/
```

### Link Collection Example
**Target:** `https://smoothbrains.net/posts/2025-10-18-three-year-retrospective.html#sequences`

**Command:**
```bash
fetch-corpus --source "https://smoothbrains.net/posts/2025-10-18-three-year-retrospective.html#sequences" --type html-links --limit 5 --name smoothbrains
# Stores in ~/Documents/mystic_corpus/smoothbrains/
```

### GitHub Repository Example
**Target:** `https://github.com/wbic16/eigenhector_mandala_translator`

**Command:**
```bash
fetch-corpus --source "https://github.com/wbic16/eigenhector_mandala_translator" --type github --limit 20 --name eigenhector_translator
# Stores in ~/Documents/mystic_corpus/eigenhector_translator/
# Fetches only .md files
```

## Output Format
Each fetched article should be saved as a separate Markdown file.

**File format:**
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

## Storage & Deduplication

### Default Storage Location
*   **Path:** User's documents directory under `mystic_corpus`.
    *   **Windows:** `%USERPROFILE%\Documents\mystic_corpus\`
    *   **Linux:** `~/Documents/mystic_corpus/`
*   **Structure:**
    *   `mystic_corpus/`
        *   `<corpus_name>/` (Subdirectory for the specific corpus)
            *   `docs/` (Actual markdown files)
            *   `index.json` (Index of fetched documents)

### Deduplication
*   **Index File:** Verify against `index.json` in the corpus directory before fetching.
*   **Check:** If a URL or Title already exists in the index, skip fetching unless a `--force` flag is used.
*   **Update:** Upon successful fetch, append the new article's metadata (URL, Title, Date, Local Path) to `index.json`.

### Flags
*   `--name <corpus_name>`: Name of the corpus (creates directory).
*   `--storage-root <path>`: Override the default `mystic_corpus` location.
*   `--force`: Force re-fetch even if present in the index.
*   `--limit <number>`: Limit the number of articles fetched.

