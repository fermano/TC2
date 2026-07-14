import unittest
from datetime import datetime, timezone
from src.attention_r2_release_window import within_release_window
class ReleaseWindowTests(unittest.TestCase):
    def test_includes_end(self):
        start=datetime(2026,7,1,tzinfo=timezone.utc); end=datetime(2026,7,2,tzinfo=timezone.utc)
        self.assertTrue(within_release_window(end,start,end))
if __name__ == "__main__": unittest.main()
