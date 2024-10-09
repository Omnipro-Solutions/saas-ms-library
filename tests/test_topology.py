import unittest
from unittest.mock import MagicMock, patch

from omni.pro.topology import Topology


class TestTopology(unittest.TestCase):

    @patch("importlib.import_module")
    def setUp(self, mock_import_module):
        self.mock_models = MagicMock()
        self.mock_models.__path__ = ["path_to_models"]
        mock_import_module.return_value = self.mock_models
        self.topology = Topology()

    @patch("pkgutil.iter_modules")
    def test_get_model_libs(self, mock_iter_modules):
        mock_iter_modules.return_value = [(None, "module1", None), (None, "module2", None)]

        result = self.topology.get_model_libs()

        self.assertEqual(result, ["module1", "module2"])


if __name__ == "__main__":
    unittest.main()
