import unittest
from src.attention_r2_release_marker import parse_release_marker
class MarkerTests(unittest.TestCase):
    def test_explicit(self): self.assertEqual(parse_release_marker("ga:4.7"),("ga","4.7"))
    def test_omitted(self):
        with self.assertRaises(ValueError): parse_release_marker("4.7")
if __name__ == "__main__": unittest.main()
