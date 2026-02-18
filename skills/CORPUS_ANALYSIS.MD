# Corpus Analysis Guidelines

## Corpus Acquisition

Before starting analysis, ensure you have the target corpus available.

1.  **Fetch Content:** Use the **@[skills/CORPUS_FETCHING.MD]** skill to download the corpus.
    -   Example: `fetch-corpus --source "https://example.com/sitemap.xml" --type substack --name example_corpus`

2.  **User Shortcuts:** If analyzing a known user, check **@[skills/ADD_CORPUS_USER.MD]** for aliases.
    -   Example: `fetch-corpus --user ari --limit 10`

3.  **Verify Integrity:** Run the verification tool to ensure the corpus is complete and valid.
    -   Command: `python tools/verify_corpus.py --name <corpus_name>`
    -   Example: `python tools/verify_corpus.py --name eigenhector`

### Corpus Location
The fetched corpus will be stored in:
`mystic_corpus/<corpus_name>/docs` (e.g., `mystic_corpus/eigenhector/docs`)
Each file will be a Markdown document containing a single post or article.


## General Corpus Patterns
When analyzing a corpus, you should look for the following patterns to generate a full synthesis including:

- The top 10-15 major recurring metaphors with characteristic adjectives, feelings, and exact quotes for each
- The overall emotional texture
- Lineages drawn upon
- Recurring themes
- Key concepts
- Important terms
- Relationships between concepts
- Evolution of ideas over time
- Connections to other fields or traditions
- Unique insights or perspectives
- Any patterns that seem particularly interesting or relevant to the task at hand

## Dream Bridge Analysis Method (DIM)

The Dream Interview Method (DIM) is a specific technique for comparing metaphors across parallel corpora. It accepts the **structured JSON analysis** of two target corpora as input and synthesizes them. It treats text segments as "dream images" to reveal unique, culturally specific meanings.

### Phase 1: The Setup (Martian Perspective)
Adopt the persona of a **Martian Interviewer** who knows nothing about Earth customs or symbols. Prevent projecting your own definitions onto the text. Elicit meaning entirely from the text's own descriptions.

### Phase 2: The Interview Process
For each target metaphor in each corpus:

1.  **Description (The "Alien" Inquiry):**
    - Ask: "What is [Metaphor] like?"
    - Elicit 3-4 specific adjectives and feelings distinct to this text (e.g., is the "Forest" *dark/suffocating* or *green/resource-rich*?).

2.  **Recapitulation (Mirroring):**
    - Summarize the description back using **only the text's exact words**.
    - Confirm the specific tone.

3.  **Reflective Bridge (Contextualization):**
    - Ask: "Is there any situation, argument, or theme in this text that is **like** [Recapitulation]?"
    - Connect the image to the broader reality or argument of the text (the "waking life" of the corpus).

### Phase 3: Crossing the Dream Bridge
Compare the findings from Corpus A and Corpus B:
-   **Compare Adjectives/Feelings:** How do the specific textures differ?
-   **Compare Bridges:** How do the functional metaphors differ? (e.g., Internal state vs. External event).

## Structural Comparison Dimensions

In addition to metaphor analysis, compare the corpora along these structural dimensions:

1.  **Rhetorical Mode:** Style, tone, genre, typical references.
2.  **Emotional Register:** Dominant mood, feeling-tone, emotional signature.
3.  **Direction of Attention:** Inward/Outward, Up/Down, Micro/Macro.
4.  **Relationship to the Reader:** Teacher, friend, oracle, diarist, etc.
5.  **Core Verb:** One word that captures the central activity of the corpus.

## Output Standards

To ensure the analysis is both human-readable and machine-processable for downstream tasks (like the Dream Bridge), you must generate **two** output files for every analysis.

### 1. Human-Readable Output (HTML)
**Purpose:** For human review and simplified reading.
**Location:** `mystic_corpus/<corpus_name>/analysis/<corpus_name>_analysis_<YYYYMMDD>.html`
**Format:**
-   **Structure:** Standard HTML5.
-   **Style:** Clean, minimal CSS (e.g., sans-serif fonts, clear headers, distinct sections for metaphors).
-   **Content:**
    -   **Metadata Header:** Corpus name, author, date.
    -   **Executive Summary:** High-level synthesis.
    -   **Metaphors Section:** Each metaphor clearly displayed with its description, recapitulation, and bridge.
    -   **Structural Dimensions:** Formatted as a readable list or table.
    -   **Key Concepts:** Definitions list.
    -   **Evolution of Ideas:** Narrative text.

### 2. Machine-Readable Output (JSON)
**Purpose:** To serve as input for `skills/DREAM_BRIDGE_TEMPLATE.MD` and other agentic tasks.
**Location:** `mystic_corpus/<corpus_name>/analysis/<corpus_name>_analysis_<YYYYMMDD>.json`
**Format:**
-   **Strict Schema:** Must strictly follow the structure defined in `skills/ANALYSIS_JSON_TEMPLATE.json`.
-   **Fields Required:**
    -   `corpus_metadata` (including `local_corpus_path`)
    -   `major_recurring_metaphors` (Array of objects, must include `occurrences` list with quotes and `source_document` paths)
    -   `structural_dimensions`
    -   `key_concepts` (Array of objects, must include `occurrences` list with `source_document` paths)
    -   `evolution_of_ideas`
