import argparse
import json
import os
import sys
from urllib.parse import urlparse

# Add current directory to sys.path to allow importing fetch_corpus
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    from fetch_corpus import CorpusManager, CorpusFetcher, load_registry
except ImportError:
    # If running from tools/ directly, this might fail if catch_corpus isn't in path correctly
    # But usually relative imports or sys.path modification works.
    # Fallback or error if strict structure is required.
    print("Error: Could not import fetch_corpus. Make sure you are running this from the project root or tools directory.")
    sys.exit(1)

def get_registry_path(storage_root=None):
    if storage_root:
        base_dir = storage_root
    else:
        if os.name == 'nt':
            base_dir = os.path.join(os.environ['USERPROFILE'], 'Documents', 'mystic_corpus')
        else:
            base_dir = os.path.join(os.path.expanduser('~'), 'Documents', 'mystic_corpus')
            
    return os.path.join(base_dir, 'corpus_registry.json'), base_dir

def ensure_sitemap_url(url):
    parsed = urlparse(url)
    if not parsed.scheme:
        url = 'https://' + url
        parsed = urlparse(url)
    
    if 'sitemap.xml' in url:
        return url
    
    # If it ends with slash, just append keys
    if url.endswith('/'):
        return url + 'sitemap.xml'
    else:
        return url + '/sitemap.xml'

def update_registry(registry_path, new_entries):
    registry = {}
    if os.path.exists(registry_path):
        with open(registry_path, 'r', encoding='utf-8') as f:
            try:
                registry = json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: Could not decode {registry_path}, starting fresh.")
                registry = {}
    
    updated = False
    for alias, url in new_entries.items():
        if alias not in registry:
            # Clean URL to ensuring sitemap
            sitemap_url = ensure_sitemap_url(url)
            registry[alias] = {
                "type": "substack",
                "url": sitemap_url,
                "description": f"{alias}'s Substack"
            }
            print(f"Added {alias} -> {sitemap_url}")
            updated = True
        else:
            print(f"Skipping {alias}: Already exists.")
            
    if updated:
        os.makedirs(os.path.dirname(registry_path), exist_ok=True)
        with open(registry_path, 'w', encoding='utf-8') as f:
            json.dump(registry, f, indent=4)
        print("Registry updated.")
    else:
        print("No new users added to registry.")

def main():
    parser = argparse.ArgumentParser(description="Bulk add Substack users and fetch initial content.")
    parser.add_argument('pairs', nargs='+', help="Pairs of 'alias url' (e.g. ari https://ari.substack.com/)")
    parser.add_argument('--limit', type=int, default=20, help="Number of articles to fetch per user (default: 20)")
    parser.add_argument('--storage-root', help="Override default storage root")
    
    args = parser.parse_args()
    
    if len(args.pairs) % 2 != 0:
        print("Error: Arguments must be in pairs of 'alias url'.")
        return

    # Parse pairs
    user_pairs = {}
    for i in range(0, len(args.pairs), 2):
        alias = args.pairs[i]
        url = args.pairs[i+1]
        user_pairs[alias] = url
        
    registry_path, base_dir = get_registry_path(args.storage_root)
    
    # Update Registry
    update_registry(registry_path, user_pairs)
    
    # Fetch Content
    for alias in user_pairs.keys():
        print(f"\n--- Fetching for {alias} ---")
        # We can reuse the main function from fetch_corpus if we want, or just instantiate classes.
        # Instantiating classes gives us more control and avoids re-parsing args.
        
        # Reload registry to get the correct URL (normalized)
        registry = load_registry(args.storage_root)
        if alias not in registry:
            print(f"Error: Could not find {alias} in registry after adding.")
            continue
            
        entry = registry[alias]
        source_url = entry['url']
        
        manager = CorpusManager(alias, args.storage_root)
        fetcher = CorpusFetcher(manager)
        fetcher.process_substack(source_url, args.limit)

if __name__ == "__main__":
    main()
