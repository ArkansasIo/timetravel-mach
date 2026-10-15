import unittest
from etps.catalog_complete import load_systems

class CompleteCatalogTests(unittest.TestCase):
    def test_catalog_has_all_ids_once(self):
        systems = load_systems()
        self.assertEqual(len(systems), 175)
        self.assertEqual([s["id"] for s in systems], list(range(226, 401)))
    def test_records_have_required_fields(self):
        for system in load_systems():
            with self.subTest(system_id=system["id"]):
                self.assertTrue(system["title"])
                self.assertIn(system["volume"], {"III", "IV"})
                self.assertTrue(system["status"])
                self.assertTrue(system["summary"])
    def test_volume_boundary(self):
        systems = load_systems()
        self.assertTrue(all(s["volume"] == "III" for s in systems if s["id"] <= 300))
        self.assertTrue(all(s["volume"] == "IV" for s in systems if s["id"] >= 301))

if __name__ == "__main__":
    unittest.main()
