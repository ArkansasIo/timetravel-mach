import unittest
from examples.causal_graph import is_acyclic

class CausalGraphTests(unittest.TestCase):
    def test_linear_graph_is_acyclic(self):
        self.assertTrue(is_acyclic([("past","present"),("present","future")]))
    def test_cycle_is_detected(self):
        self.assertFalse(is_acyclic([("a","b"),("b","c"),("c","a")]))
    def test_disconnected_nodes(self):
        self.assertTrue(is_acyclic([("a","b"),("x","y")]))
    def test_empty_graph(self):
        self.assertTrue(is_acyclic([]))

if __name__ == "__main__":
    unittest.main()
