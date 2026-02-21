---
name: Corpus Registry
description: Documentation for the corpus_registry.json file and user management.
---

# Corpus Registry

The `corpus_registry.json` file is the central database for all user aliases and their corresponding source configurations in the Mystic Corpus system.

## Location

The registry is located at the root of the corpus storage directory:
- **Project Location**: `reports/mystic_corpus/corpus_registry.json`

> [!WARNING]
> Since this file is located within the `reports/` directory, it is ignored by Git by default. This is intentional to protect sensitive source URLs and local configuration.

## Schema

The registry is a JSON object where keys are **user aliases** and values are **configuration objects**.

### Configuration Object Fields

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `type` | String | Yes | The source type. Supported values: `substack`, `github`, `html-links`. |
| `url` | String | Yes | The source URL (e.g., sitemap XML, GitHub repo URL). |
| `description` | String | No | A human-readable description of the corpus. |
| `is_default` | Boolean | No | If `true`, this corpus is treated as the primary or "self" mandala for the system. Only one entry should have this set to true. |

### Example

```json
{
    "eigenhector": {
        "type": "substack",
        "url": "https://eigenhector.substack.com/sitemap.xml",
        "description": "Eigenhector Substack",
        "is_default": true
    },
    "paul_litvak": {
        "type": "substack",
        "url": "https://www.paullitvak.com/sitemap.xml",
        "description": "Paul Litvak's Substack"
    }
}
```

## Managing Entries

### Adding a User
To add a new user, you can manually edit the JSON file or use a dedicated tool (if available). Ensure the `alias` is unique and the `url` is accessible.

### Setting the Default Mandala
The `is_default` flag designates the primary perspective for the system (the "Self" in the Martian Interviewer context). 
- **Usage**: Tools may use this flag to determine the default `--user` argument if none is provided.
- **Constraint**: It is recommended to have only one entry marked as `"is_default": true`.

## Usage in Tools

Tools like `fetch_corpus.py` and `index_corpus.py` read this registry to resolve user aliases to source URLs.

```bash
python tools/fetch_corpus.py --user eigenhector --limit 10
```
