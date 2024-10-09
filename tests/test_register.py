import unittest
from unittest.mock import patch

from omni.pro.register import RegisterModel


class TestRegisterModel(unittest.TestCase):

    def setUp(self):
        self.models_path = "path/to/models"
        self.microservice = "test_microservice"
        self.register_model = RegisterModel(self.models_path, self.microservice)

    def test_transform_field_desc(self):
        mock_field = {"name": "test_field", "code": "test_code", "type": "string", "required": True, "relation": {}}

        result = self.register_model.transform_field_desc(mock_field)

        self.assertEqual(result["name"], "test_field")
        self.assertEqual(result["code"], "test_code")
        self.assertEqual(result["type"], "string")
        self.assertEqual(result["required"], True)
        self.assertEqual(result["relation"], {})

    def test_transform_field_desc_with_options_and_size(self):
        mock_field = {
            "name": "test_field",
            "code": "test_code",
            "type": "string",
            "required": True,
            "relation": {},
            "size": 255,
            "options": ["option1", "option2"],
        }

        result = self.register_model.transform_field_desc(mock_field)

        self.assertEqual(result["size"], 255)
        self.assertEqual(result["options"], ["option1", "option2"])


if __name__ == "__main__":
    unittest.main()
