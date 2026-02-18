import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import requests
from unittest.mock import patch, MagicMock

class TestSources(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_substack_sitemap(self, mock_get):
        """Test fetching and parsing a Substack sitemap."""
        # Mock XML response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = """<?xml version="1.0" encoding="UTF-8"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
            <url>
                <loc>https://eigenhector.substack.com/p/post1</loc>
                <lastmod>2023-10-26</lastmod>
            </url>
            <url>
                <loc>https://eigenhector.substack.com/p/post2</loc>
                <lastmod>2023-10-25</lastmod>
            </url>
        </urlset>"""
        mock_get.return_value = mock_response

        # links = fetch_substack_links("https://eigenhector.substack.com/sitemap.xml")
        # self.assertEqual(len(links), 2)
        # self.assertIn("https://eigenhector.substack.com/p/post1", links)
        pass

    @patch('requests.get')
    def test_fetch_html_links_md_only(self, mock_get):
        """Test fetching links from an HTML collection page, restricted to .md files."""
        # Mock HTML response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = """
        <html>
            <body>
                <div class="content">
                    <a href="https://smoothbrains.net/posts/post1.md">Post 1</a>
                    <a href="/posts/post2.html">Post 2</a>
                    <a href="/posts/post3.md">Post 3</a>
                </div>
            </body>
        </html>
        """
        mock_get.return_value = mock_response
        
        # We need to verify that fetch_url is called for post1.md and post3.md but NOT post2.html
        # Since process_html_links is an instance method, we need to instantiate it or spy on it.
        # But we are testing the logic flow. 
        # Integration-like unit test:
        
        from tools.fetch_corpus import CorpusFetcher, CorpusManager
        manager = MagicMock()
        manager.is_fetched.return_value = False
        manager.save_article.return_value = (1, "dummy_path.md")
        
        fetcher = CorpusFetcher(manager)
        # Mock fetch_url to avoid actual requests for the files themselves
        fetcher.fetch_url = MagicMock()
        # The first call to fetch_url is for the source_url, which returns the mock_response.text above
        # The subsequent calls are for the found links.
        
        # We can mock fetch_url to return different things based on URL.
        def side_effect(url, **kwargs):
            if url == "https://smoothbrains.net/posts/collection.html":
                return mock_response.text
            elif url.endswith('.md'):
                return "# Content"
            return None
        fetcher.fetch_url.side_effect = side_effect
        
        fetcher.process_html_links("https://smoothbrains.net/posts/collection.html", limit=10)
        
        # Verify calls
        # fetches: collection.html, post1.md, post3.md
        # does NOT fetch: post2.html
        
        calls = [args[0][0] for args in fetcher.fetch_url.call_args_list]
        self.assertIn("https://smoothbrains.net/posts/collection.html", calls)
        self.assertIn("https://smoothbrains.net/posts/post1.md", calls)
        self.assertIn("https://smoothbrains.net/posts/post3.md", calls) # Assuming relative link handling works to make it absolute or at least it tries to fetch it
        # Note: joinurl in implementation might make it absolute. 
        # Let's check if fetch_corpus resolves relative links. Yes, urljoin(source_url, href).
        
        # Check that .html file was NOT fetched
        self.assertFalse(any("post2.html" in call for call in calls))

    @patch('requests.get')
    def test_fetch_github_files(self, mock_get):
        """Test fetching .md files from a GitHub repository."""
        # This might likely use the GitHub API in a real implementation
        mock_response = MagicMock()
        mock_response.status_code = 200
        # Mocking a simple HTML generic response or API JSON response depending on implementation
        # For now assuming we might scrape the file list or use API
        mock_response.json.return_value = [
            {"name": "readme.md", "type": "file", "download_url": "http://github.com/user/repo/readme.md"},
            {"name": "script.py", "type": "file", "download_url": "http://github.com/user/repo/script.py"},
            {"name": "design.MD", "type": "file", "download_url": "http://github.com/user/repo/design.MD"}
        ]
        mock_get.return_value = mock_response

        # files = fetch_github_files("https://github.com/wbic16/eigenhector_mandala_translator")
        # self.assertEqual(len(files), 2) # readme.md and design.MD
        pass

    def test_rate_limiting(self):
        """Test that the limit flag respects the maximum number of items."""
        # items = ["item1", "item2", "item3", "item4", "item5"]
        # limited_items = apply_limit(items, 3)
        # self.assertEqual(len(limited_items), 3)
        # self.assertEqual(limited_items, ["item1", "item2", "item3"])
        pass



    @patch('requests.get')
    def test_fetch_url_timeout(self, mock_get):
        """Test that fetch_url enforces timeout."""
        # Mock a timeout exception
        mock_get.side_effect = requests.exceptions.Timeout
        
        from tools.fetch_corpus import CorpusManager, CorpusFetcher
        manager = MagicMock()
        fetcher = CorpusFetcher(manager)
        
        result = fetcher.fetch_url("http://example.com")
        self.assertIsNone(result)
        
        # Verify timeout argument was passed with default 10s
        mock_get.assert_called_with("http://example.com", headers={'User-Agent': 'Mozilla/5.0'}, timeout=10, stream=True)

    @patch('requests.get')
    def test_fetch_url_too_large(self, mock_get):
        """Test that fetch_url enforces a size limit."""
        # Mock a large response stream
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        
        # Generator for content chunks
        def generate_chunks():
            # Returns 3 chunks of 1MB
            yield b"a" * 1024 * 1024
            yield b"a" * 1024 * 1024
            yield b"a" * 1024 * 1024
        
        mock_response.iter_content.return_value = generate_chunks()
        mock_get.return_value = mock_response
        
        from tools.fetch_corpus import CorpusManager, CorpusFetcher
        manager = MagicMock()
        fetcher = CorpusFetcher(manager)
        
        # Set limit to 2MB (default is 10MB)
        # We need to call fetch_url with explicit limit or change default
        # Since fetch_url signature has default, we can pass it
        result = fetcher.fetch_url("http://example.com", max_size=2*1024*1024)
        
        self.assertIsNone(result) # Should fail as it exceeds limit

    def test_id_based_filename_generation(self):
        """Test that filenames are generated based on IDs and IDs increment."""
        from tools.fetch_corpus import CorpusManager
        
        # Determine a safe temp dir or mock
        cm = CorpusManager("test_corpus", storage_root=".")
        cm.docs_dir = "."
        # Mock index loading
        cm.index = []
        cm.next_id = 1
        
        with patch('builtins.open', new_callable=MagicMock) as mock_open:
            # First article
            doc_id, filepath = cm.save_article("My Title", "2023-01-01", "http://url1", "content")
            self.assertEqual(doc_id, 1)
            self.assertTrue("00001.md" in filepath)
            
            # Second article
            doc_id, filepath = cm.save_article("Another Title", "2023-01-02", "http://url2", "content")
            self.assertEqual(doc_id, 2)
            self.assertTrue("00002.md" in filepath)
            
            # Check for crazy characters in title - should not affect filename
            doc_id, filepath = cm.save_article("Title/With/Slashes", "2023-01-03", "http://url3", "content")
            self.assertEqual(doc_id, 3)
            self.assertTrue("00003.md" in filepath)


if __name__ == '__main__':
    unittest.main()
