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


class TestClamp01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_aval_module()

    def test_limitar_01(self):
        clamp01 = self.mod.clamp01
        self.assertEqual(clamp01(-0.5), 0.0)
        self.assertEqual(clamp01(0.3), 0.3)
        self.assertEqual(clamp01(2.0), 1.0)
