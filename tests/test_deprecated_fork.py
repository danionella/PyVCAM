import importlib
import pathlib
import sys
import unittest
import warnings


SRC_DIR = pathlib.Path(__file__).resolve().parents[1] / "src"


class DeprecatedForkTests(unittest.TestCase):
    def test_import_warns_to_use_upstream_release(self):
        sys.path.insert(0, str(SRC_DIR))
        try:
            sys.modules.pop("pyvcam", None)
            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter("always")
                importlib.import_module("pyvcam")
        finally:
            sys.modules.pop("pyvcam", None)
            sys.path.remove(str(SRC_DIR))

        self.assertTrue(caught)
        self.assertIn("Photometrics release from PyPI", str(caught[0].message))
