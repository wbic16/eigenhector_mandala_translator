# Substack Bulk Add Skill

This skill allows for the bulk addition of Substack users to the corpus registry and auto-fetching of their content. It streamlines the process of setting up multiple corpora at once.

## Usage

Use the `tools/bulk_add_substack.py` script to add users.

### Command Structure
```bash
python tools/bulk_add_substack.py <alias1> <url1> <alias2> <url2> ... [--limit <number>]
```

### Parameters
- **`alias`**: The short name for the user (e.g., `ari`).
- **`url`**: The Substack URL (e.g., `https://ari.substack.com/`). The script will automatically append `sitemap.xml` if needed.
- **`--limit`**: (Optional) Number of articles to fetch per user (default: 20).

### Example
To add Ari and Eigenhector and fetch 20 articles for each:

```bash
python tools/bulk_add_substack.py ari https://ari.substack.com/ eigenhector https://eigenhector.substack.com/
```

To add Paul Litvak and fetch only 5 articles:

```bash
python tools/bulk_add_substack.py paul_litvak https://www.paullitvak.com/ --limit 5
```

## Related Skills
- **@[skills/ADD_CORPUS_USER.MD]**: For adding single users manually.
- **@[skills/CORPUS_FETCHING.MD]**: For details on the fetching process.
