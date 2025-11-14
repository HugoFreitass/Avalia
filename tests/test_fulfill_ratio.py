import unittest
import importlib.util
import os


def load_aval_module():
    base = os.path.dirname(__file__)
    path = os.path.abspath(os.path.join(base, "..", "aval_mds.py"))
    spec = importlib.util.spec_from_file_location("aval_mds", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestFulfillRatio(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_aval_module()

    def test_taxa_de_cumprimento(self):
        fr = self.mod.fulfill_ratio

        self.assertEqual(fr(10, 2, 5), 1.0)
        self.assertEqual(fr(0, 4, 1), 0.0)
        self.assertAlmostEqual(fr(3, 2, 2), 0.75)
