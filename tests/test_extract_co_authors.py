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


class TestExtractCoAuthors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_aval_module()

    def test_extrai_coautores_de_commit(self):
        e = self.mod.extract_co_authors_from_commit
        msg = (
            "Fix thing\n\n"
            "Co-authored-by: Alice <alice@example.com>\n"
            "Co-authored-by: bob <bob@users.noreply.github.com>"
        )

        authors = e(msg)

        self.assertIn("alice", authors)
        self.assertIn("bob", authors)
