# Corpus Analysis Guidelines

## Corpus Acquisition

Before starting analysis, ensure you have the target corpus available.

1.  **Fetch Content:** Use the **@[skills/CORPUS_FETCHING.MD]** skill to download the corpus.
    -   Example: `fetch-corpus --source "https://example.com/sitemap.xml" --type substack --name example_corpus`
2.  **User Shortcuts:** If analyzing a known user, check **@[skills/ADD_CORPUS_USER.MD]** for aliases.
    -   Example: `fetch-corpus --user ari --limit 10`

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

The Dream Interview Method (DIM) is a specific technique for comparing metaphors across parallel corpora. It treats text segments as "dream images" to reveal unique, culturally specific meanings.

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

## Output Instructions

When collecting this analysis, formatted output is required.
Refer to `skills/DREAM_BRIDGE_TEMPLATE.MD` for the exact expected output structure.