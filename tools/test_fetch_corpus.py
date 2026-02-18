
import unittest
from unittest.mock import MagicMock, patch
import os
import sys

# Add the tools directory to the path so we can import fetch_corpus
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fetch_corpus import CorpusManager, CorpusFetcher

class TestCorpusFetcher(unittest.TestCase):
    def setUp(self):
        self.mock_manager = MagicMock(spec=CorpusManager)
        self.mock_manager.is_fetched.return_value = False
        self.fetcher = CorpusFetcher(self.mock_manager)

    @patch('fetch_corpus.CorpusFetcher.fetch_url')
    @patch('fetch_corpus.CorpusFetcher._parse_and_save_article')
    def test_process_substack_filtering(self, mock_save, mock_fetch):
        # Setup mock sitemap
        sitemap_content = """
        <?xml version="1.0" encoding="UTF-8"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
            <url><loc>https://eigenhector.substack.com/p/valid-post</loc></url>
            <url><loc>https://eigenhector.substack.com/about</loc></url>
            <url><loc>https://eigenhector.substack.com/p/another-valid-post</loc></url>
            <url><loc>https://eigenhector.substack.com/archive</loc></url>
        </urlset>
        """
        
        # Configure mock_fetch to return sitemap first, then html content for posts
        def side_effect(url, **kwargs):
            if url == "https://eigenhector.substack.com/sitemap.xml":
                return sitemap_content
            return "<html><body>Mock Content</body></html>"
            
        mock_fetch.side_effect = side_effect

        # Run the method
        self.fetcher.process_substack("https://eigenhector.substack.com/sitemap.xml", limit=10)

        # Verification
        # process_substack calls fetch_url for the sitemap (1) and for each valid post (2)
        # It should NOT call fetch_url for 'about' or 'archive'
        
        # Check calls to fetch_url
        fetched_urls = [call.args[0] for call in mock_fetch.call_args_list]
        self.assertIn("https://eigenhector.substack.com/sitemap.xml", fetched_urls)
        self.assertIn("https://eigenhector.substack.com/p/valid-post", fetched_urls)
        self.assertIn("https://eigenhector.substack.com/p/another-valid-post", fetched_urls)
        self.assertNotIn("https://eigenhector.substack.com/about", fetched_urls)
        self.assertNotIn("https://eigenhector.substack.com/archive", fetched_urls)

        # Check that save was called twice
        self.assertEqual(mock_save.call_count, 2)

if __name__ == '__main__':
    unittest.main()
