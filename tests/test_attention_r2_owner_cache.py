import unittest
from src.attention_r2_owner_cache import clear_owner_cache, normalized_owner
class OwnerCacheTests(unittest.TestCase):
    def setUp(self): clear_owner_cache()
    def test_spellings(self): self.assertEqual(normalized_owner(" Billing  Ops "),normalized_owner("billing ops"))
if __name__ == "__main__": unittest.main()
