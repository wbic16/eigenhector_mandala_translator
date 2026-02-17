# Corpus Fetching Skill

This skill outlines the procedure for fetching and preparing text corpora for analysis, based on the design specifications in `design/CORPUS_FETCHING_DESIGN.MD`.

## Usage Instructions

### 1. Identify Source Type
Determine if your source is a Substack blog (XML sitemap) or a generic HTML page with a list of links.

### 2. Fetch Content
Use the corpus fetching tool (or equivalent method) to download articles.

**Command Structure:**
`fetch-corpus --source [URL] --type [substack|html-links] --limit [number]`

**Examples:**

*   **Substack:**
    ```bash
    fetch-corpus --source "https://eigenhector.substack.com/sitemap.xml" --type substack --limit 10
    ```

*   **Link Collection:**
    ```bash
    fetch-corpus --source "https://smoothbrains.net/posts/2025-10-18-three-year-retrospective.html#sequences" --type html-links --limit 5
    ```

### 3. Markdown Conversion
Ensure all fetched content is converted to Markdown format. This is critical for the next stage of the pipeline.

**Required Format:**
*   Frontmatter with metadata (title, date, url).
*   Body content in standard Markdown.

### 4. Integration with Analysis
Once the corpus is fetched and converted to Markdown, proceed to **@[skills/CORPUS_ANALYSIS.MD]**. The analysis tools and prompts are designed to ingest this specific Markdown format.
