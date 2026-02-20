---
name: Local Corpus Builder
description: Transforms a local directory of documents into a structured Mystic Corpus with Martian Interviewer onboarding.
---

# Local Corpus Builder

This skill guides the creation of a local "Mystic Corpus" from a folder of documents. It combines narrative inquiry with technical indexing.

## Phase 1: The Martian Appraisal
Adopt the **Martian Interviewer** persona (see [DIM.MD](DreamBridge/DIM.MD)).

1.  **Direct the User**: Ask the user to provide the absolute path to their document folder.
2.  **The Appraisal**:
    > "I come from a world of sterile data. I see you have brought a collection of 'scrolls'. Before we catalog them, I must understand their soul. If I were to touch these documents without reading them, what would they feel like? Are they brittle and ancient? Are they humming with electricity? What is the 'Vibe' of this collection?"
3.  **Alias Assignment**: Based on the description, suggest a unique `corpus_name` alias (e.g., `the_shattering_chronicles` or `circuit_board_sutras`).

## Phase 2: Technical Transmutation
Once the "Vibe" is established, proceed with the transmutation (indexing).

1.  **Inventory**: List the files found in the target directory.
2.  **Conversion**: For any non-Markdown files (`.pdf`, `.docx`, `.txt`), use appropriate conversion scripts to move them into the `mystic_corpus/[alias]/docs/` folder as `00001.md`, `00002.md`, etc.
3.  **Frontmatter Synthesis**: Each file must have frontmatter generated:
    ```markdown
    ---
    id: [number]
    title: [filename or inferred title]
    date: [file date]
    url: local://[original_path]
    ---
    ```
4.  **Index Generation**: Create `index.json` in the corpus root following [CORPUS_STRUCTURE.MD](CORPUS_STRUCTURE.MD).

## Phase 3: Verification & Ritual
1.  **Verify**: Run the verification tool:
    ```powershell
    python tools/verify_corpus.py --name [alias]
    ```
2.  **Visual Synthesis**: Generate a DALL-E prompt for the corpus "cover art" based on the Martian Interviewer's findings.
    *   *Example*: "A thangka painting of a digital library where the books are made of glowing fiber optics and the ink is liquid starlight."

## Phase 4: Integration
Add the new corpus to the `mystic_corpus/corpus_registry.json`.
