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


class TestTextNontrivial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_aval_module()

    def test_texto_nao_trivial(self):
        t = self.mod.text_nontrivial
        self.assertTrue(t("This is non trivial"))
        self.assertFalse(t("short"))
