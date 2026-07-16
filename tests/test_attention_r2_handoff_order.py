import unittest
from src.attention_r2_handoff_order import order_handoff_rows
class OrderTests(unittest.TestCase):
    def test_named(self):
        rows=[{"severity":"high","owner":"zeta"},{"severity":"critical","owner":"beta"},{"severity":"high","owner":"alpha"}]
        self.assertEqual([r["owner"] for r in order_handoff_rows(rows)],["beta","alpha","zeta"])
if __name__ == "__main__": unittest.main()
