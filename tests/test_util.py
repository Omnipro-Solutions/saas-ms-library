import unittest
from unittest.mock import MagicMock, patch

import pkg_resources
from google.protobuf import struct_pb2
from omni.pro.util import convert_model_alchemy_to_struct, convert_model_mongo_to_struct, libraries_versions_installed


class TestUtilities(unittest.TestCase):

    @patch("pkg_resources.get_distribution")
    def test_libraries_versions_installed(self, mock_get_distribution):
        mock_get_distribution.side_effect = [
            MagicMock(version="1.0.0"),
            MagicMock(version="2.0.0"),
            MagicMock(version="3.0.0"),
            MagicMock(version="4.0.0"),
        ]

        result = libraries_versions_installed()

        expected_result = {
            "omni_pro": "1.0.0",
            "omni_pro_base": "2.0.0",
            "omni_pro_redis": "3.0.0",
            "omni_pro_grpc": "4.0.0",
        }

        self.assertEqual(result, expected_result)
        mock_get_distribution.assert_any_call("omni-pro")
        mock_get_distribution.assert_any_call("omni-pro-base")
        mock_get_distribution.assert_any_call("omni-pro-redis")
        mock_get_distribution.assert_any_call("omni-pro-grpc")

    @patch("pkg_resources.get_distribution")
    def test_libraries_versions_not_installed(self, mock_get_distribution):
        mock_get_distribution.side_effect = [
            MagicMock(version="1.0.0"),
            pkg_resources.DistributionNotFound,
            pkg_resources.DistributionNotFound,
            MagicMock(version="4.0.0"),
        ]

        result = libraries_versions_installed()

        expected_result = {
            "omni_pro": "1.0.0",
            "omni_pro_base": "Not installed",
            "omni_pro_redis": "Not installed",
            "omni_pro_grpc": "4.0.0",
        }

        self.assertEqual(result, expected_result)

    @patch("omni.pro.util.convert_to_serializable")
    @patch("omni.pro.util.json_format.ParseDict")
    def test_convert_model_alchemy_to_struct(self, mock_parse_dict, mock_convert_to_serializable):
        mock_model = MagicMock()
        mock_model.model_to_dict.return_value = {"field": "value"}
        mock_convert_to_serializable.return_value = {"field": "value"}
        mock_struct = MagicMock()
        mock_parse_dict.return_value = mock_struct

        result = convert_model_alchemy_to_struct(mock_model)

        mock_model.model_to_dict.assert_called_once()
        mock_convert_to_serializable.assert_called_once_with({"field": "value"})
        mock_parse_dict.assert_called_once_with({"field": "value"}, struct_pb2.Struct())
        self.assertEqual(result, mock_struct)

    @patch("omni.pro.util.convert_to_serializable")
    @patch("omni.pro.util.json_format.ParseDict")
    def test_convert_model_mongo_to_struct(self, mock_parse_dict, mock_convert_to_serializable):
        mock_model = MagicMock()
        mock_model.generate_dict.return_value = {"field": "value"}
        mock_convert_to_serializable.return_value = {"field": "value"}
        mock_struct = MagicMock()
        mock_parse_dict.return_value = mock_struct

        result = convert_model_mongo_to_struct(mock_model)

        mock_model.generate_dict.assert_called_once()
        mock_convert_to_serializable.assert_called_once_with({"field": "value"})
        mock_parse_dict.assert_called_once_with({"field": "value"}, struct_pb2.Struct())
        self.assertEqual(result, mock_struct)


if __name__ == "__main__":
    unittest.main()
