import unittest
from src.attention_r2_retry_budget import resolve_attention_retry_budget
class RetryBudgetTests(unittest.TestCase):
    def test_zero(self): self.assertEqual(resolve_attention_retry_budget(0, 4), 0)
    def test_negative(self):
        with self.assertRaises(ValueError): resolve_attention_retry_budget(-1)
if __name__ == "__main__": unittest.main()
