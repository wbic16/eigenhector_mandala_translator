import os
import time
import argparse
import requests
import json
import re
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import unicodedata
from markdownify import markdownify as md
import corpus_config

class CorpusManager:
    def __init__(self, corpus_name, storage_root=None):
        self.corpus_name = corpus_name
        if storage_root:
             self.base_dir = storage_root
        else:
            self.base_dir = corpus_config.get_base_dir()
        
        self.corpus_dir = os.path.join(self.base_dir, self.corpus_name)
        self.docs_dir = os.path.join(self.corpus_dir, 'docs')
        self.index_path = os.path.join(self.corpus_dir, 'index.json')
        
        self._ensure_directories()
        self.index = self._load_index()
        self.next_id = self._calculate_next_id()

    def _ensure_directories(self):
        os.makedirs(self.docs_dir, exist_ok=True)

    def _load_index(self):
        if os.path.exists(self.index_path):
            with open(self.index_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def _calculate_next_id(self):
        if not self.index:
            return 1
        ids = [entry.get('id', 0) for entry in self.index]
        return max(ids) + 1 if ids else 1

    def save_index(self):
        with open(self.index_path, 'w', encoding='utf-8') as f:
            json.dump(self.index, f, indent=4)

    def is_fetched(self, url):
        for entry in self.index:
            if entry['url'] == url:
                return True
        return False

    def add_entry(self, doc_id, title, url, date, filepath):
        entry = {
            'id': doc_id,
            'title': title,
            'url': url,
            'date': date,
            'filepath': filepath
        }
        self.index.append(entry)
        self.save_index()

    def save_article(self, title, date, url, content):
        doc_id = self.next_id
        self.next_id += 1
        
        filename = f"{doc_id:05d}.md"
        filepath = os.path.join(self.docs_dir, filename)
        
        # Create frontmatter
        markdown_content = f"---\nid: {doc_id}\ntitle: {title}\ndate: {date}\nurl: {url}\n---\n\n# {title}\n\n{content}"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
            
        print(f"Saved: {filepath}")
        return doc_id, filepath

    def _sanitize_filename(self, filename):
        # Normalize unicode
        filename = unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore').decode('ascii')
        
        # Replace unsafe characters
        filename = re.sub(r'[\\/*?:"<>|]', "", filename)
        
        # Windows reserved names
        reserved = {
            "CON", "PRN", "AUX", "NUL",
            "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
            "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
        }
        name_upper = filename.upper().split('.')[0]
        if name_upper in reserved:
            filename = "_" + filename
            
        # Truncate to avoid path length issues (255 max usually, leave room for ext and path)
        if len(filename) > 200:
            filename = filename[:200]
            
        # Ensure it's not empty or just dots
        if not filename or re.match(r'^\.+$', filename):
            filename = "untitled_doc"
            
        return f"{filename}.md"

class CorpusFetcher:
    def __init__(self, manager):
        self.manager = manager

    def fetch_url(self, url, timeout=10, max_size=10*1024*1024):
        time.sleep(2)
        try:
            # Stream response to check size
            with requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=timeout, stream=True) as response:
                response.raise_for_status()
                
                content = []
                downloaded = 0
                for chunk in response.iter_content(chunk_size=8192, decode_unicode=True):
                    if chunk:
                        downloaded += len(chunk)
                        if downloaded > max_size:
                            print(f"Error: Content at {url} exceeds size limit of {max_size} bytes")
                            return None
                        content.append(chunk)
                return "".join(content)
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def process_substack(self, source_url, limit):
        print(f"Fetching Substack sitemap: {source_url}")
        xml_content = self.fetch_url(source_url)
        if not xml_content:
            return

        soup = BeautifulSoup(xml_content, 'xml')
        urls = soup.find_all('url')
        
        count = 0
        for url_tag in urls:
            if limit and count >= limit:
                break
                
            loc = url_tag.find('loc').text
            if self.manager.is_fetched(loc):
                print(f"Skipping already fetched: {loc}")
                continue

            # Filter for Substack posts (usually contain /p/)
            if '/p/' not in loc:
                print(f"Skipping non-post URL: {loc}")
                continue
                
            # Basic validation to skip non-post pages if possible or fetch and check
            # For sitemaps, usually all LOCs are posts/pages.
            
            print(f"Processing: {loc}")
            html_content = self.fetch_url(loc)
            if html_content:
                self._parse_and_save_article(html_content, loc)
                count += 1

    def process_html_links(self, source_url, limit):
        print(f"Fetching link collection: {source_url}")
        html_content = self.fetch_url(source_url)
        if not html_content:
            return

        soup = BeautifulSoup(html_content, 'html.parser')
        # This is a heuristic; might need adjustment based on specific implementation
        links = soup.find_all('a', href=True)
        
        count = 0
        for link in links:
            if limit and count >= limit:
                break
            
            href = link['href']
            full_url = urljoin(source_url, href)
            
            # Filter for .md files
            if not full_url.endswith('.md'):
                # print(f"Skipping non-md file: {full_url}") # Optional, maybe too noisy
                continue

            if self.manager.is_fetched(full_url):
                print(f"Skipping already fetched: {full_url}")
                continue

            print(f"Processing: {full_url}")
            article_content = self.fetch_url(full_url)
            if article_content:
                # Use filename as title for .md files from links, similar to GitHub
                parsed_url = urlparse(full_url)
                filename = os.path.basename(parsed_url.path)
                title = filename.replace('.md', '')
                date = datetime.now().strftime('%Y-%m-%d')
                
                doc_id, filepath = self.manager.save_article(title, date, full_url, article_content)
                self.manager.add_entry(doc_id, title, full_url, date, filepath)
                count += 1

    def process_github(self, source_url, limit):
        print(f"Fetching GitHub repository: {source_url}")
        # Logic to fetch .md files from a GitHub repo URL
        # This is complex because we need to navigate the file structure or use the API.
        # For simplicity, let's assume raw file fetching if possible, or simple scraping of the file list.
        # Using GitHub API is better but requires rate limiting awareness.
        
        # Heuristic: convert standard URL to API URL
        # e.g. https://github.com/user/repo -> https://api.github.com/repos/user/repo/contents
        
        parsed = urlparse(source_url)
        path_parts = parsed.path.strip('/').split('/')
        if len(path_parts) < 2:
            print("Invalid GitHub URL")
            return
            
        user = path_parts[0]
        repo = path_parts[1]
        api_url = f"https://api.github.com/repos/{user}/{repo}/contents"
        
        # Recursive function to fetch files with depth limit
        self._fetch_github_dir(api_url, limit)

    def _fetch_github_dir(self, api_url, limit, current_count=0, depth=0, max_depth=10):
        if limit and current_count >= limit:
            return current_count
            
        if depth > max_depth:
            print(f"Recursion depth exceeded at {api_url}")
            return current_count

        try:
            time.sleep(2)
            response = requests.get(api_url, headers={'User-Agent': 'CorpusFetcher'})
            if response.status_code != 200:
                print(f"Error accessing GitHub API: {response.status_code}")
                return current_count
                
            items = response.json()
            if not isinstance(items, list): # It's a file or something else
                return current_count

            for item in items:
                if limit and current_count >= limit:
                    break
                    
                if item['type'] == 'file' and item['name'].endswith('.md'):
                    raw_url = item['download_url']
                    if self.manager.is_fetched(raw_url):
                        continue
                        
                    print(f"Fetching GitHub file: {item['name']}")
                    content = self.fetch_url(raw_url)
                    if content:
                        # For GitHub md files, they are already markdown. 
                        # We just need to wrap them with our metadata.
                        # Check if frontmatter exists?
                        # For now, just wrap it.
                        
                        # Use file date or current date? GitHub API has 'last modified' but requires extra call or header check.
                        # Use current date for simplicity or 'unknown'.
                        date = datetime.now().strftime('%Y-%m-%d')
                        title = item['name'].replace('.md', '')
                        doc_id, filepath = self.manager.save_article(title, date, raw_url, content)
                        self.manager.add_entry(doc_id, title, raw_url, date, filepath)
                        current_count += 1
                        
                elif item['type'] == 'dir':
                     current_count = self._fetch_github_dir(item['url'], limit, current_count, depth + 1, max_depth)
                     
            return current_count

        except Exception as e:
            print(f"GitHub Fetch Error: {e}")
            return current_count


    def _parse_and_save_article(self, html_content, url):
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # extract title
            title_tag = soup.find('title')
            title = title_tag.text.strip() if title_tag else "Untitled"
            
            # extract date (heuristics)
            date = datetime.now().strftime('%Y-%m-%d')
            # detailed date extraction can be added here (meta tags, time tags)
            
            # extract content
            # Remove scripts and styles
            for script in soup(["script", "style", "nav", "footer", "header"]):
                script.decompose()
                
            markdown = md(str(soup.find('body') or soup))
            
            # Cleaning up markdown (excessive newlines)
            markdown = re.sub(r'\n{3,}', '\n\n', markdown)
            
            doc_id, filepath = self.manager.save_article(title, date, url, markdown)
            self.manager.add_entry(doc_id, title, url, date, filepath)
            return True
        except Exception as e:
            print(f"Error parsing {url}: {e}")
            return False

def load_registry(storage_root=None):
    if storage_root:
        base_dir = storage_root
    else:
        base_dir = corpus_config.get_base_dir()
            
    registry_path = corpus_config.get_registry_path(base_dir)
    if os.path.exists(registry_path):
        with open(registry_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def main():
    parser = argparse.ArgumentParser(description="Fetch and process text corpora.")
    parser.add_argument('--source', help="Source URL (sitemap, page, or repo)")
    parser.add_argument('--type', choices=['substack', 'html-links', 'github'], help="Type of source")
    parser.add_argument('--limit', type=int, help="Limit number of items to fetch")
    parser.add_argument('--name', help="Name of the corpus")
    parser.add_argument('--user', help="User alias from corpus_registry.json")
    parser.add_argument('--storage-root', help="Override default storage root")
    parser.add_argument('--force', action='store_true', help="Force re-fetch")
    
    args = parser.parse_args()
    
    # Handle user alias
    if args.user:
        registry = load_registry(args.storage_root)
        if args.user not in registry:
            print(f"Error: User '{args.user}' not found in registry.")
            return
            
        entry = registry[args.user]
        args.source = entry['url']
        args.type = entry['type']
        # Use alias as corpus name by default if not provided, or maybe separate name in registry?
        # For now, alias seems appropriate as the corpus name.
        if not args.name:
            args.name = args.user
            
        print(f"Loaded config for user '{args.user}': Source={args.source}, Type={args.type}")

    # Validation
    if not args.source or not args.type or not args.name:
        parser.error("The following arguments are required: --source, --type, --name (or use --user)")
    
    manager = CorpusManager(args.name, args.storage_root)
    
    if args.force:
        # Monkey patch for this run
        manager.is_fetched = lambda x: False
        
    fetcher = CorpusFetcher(manager)
    
    if args.type == 'substack':
        fetcher.process_substack(args.source, args.limit)
    elif args.type == 'html-links':
        fetcher.process_html_links(args.source, args.limit)
    elif args.type == 'github':
        fetcher.process_github(args.source, args.limit)

if __name__ == "__main__":
    main()
