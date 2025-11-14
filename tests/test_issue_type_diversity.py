import unittest
import importlib.util
import os
from collections import Counter


def load_aval_module():
    base = os.path.dirname(__file__)
    path = os.path.abspath(os.path.join(base, "..", "aval_mds.py"))
    spec = importlib.util.spec_from_file_location("aval_mds", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestIssueTypeDiversity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_aval_module()

    def test_diversidade_tipo_issue(self):
        f = self.mod.issue_type_diversity_score
        c = Counter({"bug": 3, "feature": 1})
        self.assertAlmostEqual(f(c), 0.5)
