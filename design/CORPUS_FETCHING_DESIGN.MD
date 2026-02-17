# Corpus Fetching Tool Design

## Overview
This document outlines the design for a tool to fetch and preprocess text articles from various online sources into a standardized Markdown format suitable for corpus analysis.

## Core Features

1.  **Source Handling:**
    *   **Substack XML sitemaps:** e.g., `https://eigenhector.substack.com/sitemap.xml`
    *   **Link Collection Pages:** e.g., `https://smoothbrains.net/posts/2025-10-18-three-year-retrospective.html#sequences`

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
fetch-corpus --source "https://eigenhector.substack.com/sitemap.xml" --type substack --limit 10 --output-dir corpus/eigenhector
```

### Link Collection Example
**Target:** `https://smoothbrains.net/posts/2025-10-18-three-year-retrospective.html#sequences`

**Command:**
```bash
fetch-corpus --source "https://smoothbrains.net/posts/2025-10-18-three-year-retrospective.html#sequences" --type html-links --limit 5 --output-dir corpus/smoothbrains
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
