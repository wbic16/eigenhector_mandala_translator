# Adding Users to the Corpus Registry

This skill outlines the process for registering new user aliases in the corpus registry, enabling simplified command-line usage (e.g., `fetch-corpus --user <alias>`). It is based on the design in `design/CORPUS_FETCHING_DESIGN.MD`.

## Overview
The **Corpus Registry** is a JSON configuration file that maps short, user-friendly aliases to specific corpus sources and types. By adding an entry here, you can fetch from complex URLs using a single keyword.

## Configuration File Location
*   **Path:** `mystic_corpus/corpus_registry.json`
*   **Exact Location:** Inside the user's `mystic_corpus` directory (e.g., `%USERPROFILE%\Documents\mystic_corpus\` on Windows or `~/Documents/mystic_corpus/` on Linux).

## JSON Structure
The registry is a JSON object where update keys are aliases and values are source definitions.

### Entry Format
Each user entry requires the following fields:
*   `type`: The source type (`substack`, `github`, or `html-links`).
*   `url`: The full URL to the source (e.g., sitemap XML, GitHub repo URL).
*   `description`: A brief description of the corpus.

### Example Configuration
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

## Step-by-Step Instructions

1.  **Locate the File:** Navigate to your `mystic_corpus` directory. If `corpus_registry.json` does not exist, create it.
2.  **Open in Editor:** Open the file in a text editor or IDE.
3.  **Add Entry:** Insert a new key-value pair for the desired user alias. Ensure the JSON syntax is valid (commas between entries).
4.  **Save:** Save and close the file.

## Verification
To verify the new user has been added correctly, run the fetch tool with the new alias:

```bash
fetch-corpus --user <new_alias> --limit 1
```

If the tool starts fetching from the correct URL, the configuration is successful.
