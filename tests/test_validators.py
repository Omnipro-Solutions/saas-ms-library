import unittest
from unittest.mock import MagicMock, patch

from bson import ObjectId
from marshmallow import ValidationError
from omni.pro.validators import (
    ContextSchema,
    MicroServicePathValidator,
    ObjectIdField,
    PostgresBaseSchema,
    ensure_objid_type,
    oid_isval,
)


class TestSchemas(unittest.TestCase):

    def test_context_schema_validation(self):
        schema = ContextSchema()
        valid_data = {"tenant": "tenant_id", "user": "user_id"}
        result = schema.load(valid_data)
        self.assertEqual(result["tenant"], "tenant_id")
        self.assertEqual(result["user"], "user_id")

        invalid_data = {"tenant": "tenant_id"}
        with self.assertRaises(ValidationError):
            schema.load(invalid_data)

    def test_postgres_base_schema(self):
        schema = PostgresBaseSchema()
        data = {
            "active": True,
            "context": {"tenant": "tenant_id", "user": "user_id"},
        }
        result = schema.load(data)
        self.assertEqual(result["tenant"], "tenant_id")
        self.assertEqual(result["updated_by"], "user_id")

    def test_oid_isval_valid(self):
        oid = ObjectId()
        self.assertTrue(oid_isval(oid))

    def test_oid_isval_invalid(self):
        self.assertFalse(oid_isval("invalid_oid"))

    def test_ensure_objid_type_valid(self):
        oid = ObjectId()
        self.assertEqual(ensure_objid_type(oid), oid)

        oid_str = str(oid)
        self.assertEqual(ensure_objid_type(oid_str), oid)

    def test_ensure_objid_type_invalid(self):
        with self.assertRaises(ValidationError):
            ensure_objid_type("invalid_oid")

    def test_object_id_field_serialize(self):
        field = ObjectIdField()
        oid = ObjectId()
        result = field._serialize(oid, "oid", None)
        self.assertEqual(result, oid)

    def test_object_id_field_deserialize_valid(self):
        field = ObjectIdField()
        oid_str = str(ObjectId())
        result = field._deserialize(oid_str, "oid", None)
        self.assertTrue(isinstance(result, ObjectId))

    def test_object_id_field_deserialize_invalid(self):
        field = ObjectIdField()
        with self.assertRaises(ValidationError):
            field._deserialize("invalid_oid", "oid", None)


class TestMicroServicePathValidator(unittest.TestCase):

    @patch("pathlib.Path.exists")
    def test_validate_data_success(self, mock_exists):
        mock_exists.return_value = True
        base_app = MagicMock()
        schema = MicroServicePathValidator(base_app)

        data = {
            "name": "Test Service",
            "code": "test_service",
            "sumary": "Test Summary",
            "description": "Test Description",
            "version": "1.0.0",
            "author": "Test Author",
            "category": "Test Category",
            "context": {"tenant": "test_tenant", "user": "test_user"},
            "data": ["path1", "path2"],
        }

        schema.load(data)

    @patch("pathlib.Path.exists")
    def test_validate_data_file_not_found(self, mock_exists):
        mock_exists.side_effect = [True, False]
        base_app = MagicMock()
        schema = MicroServicePathValidator(base_app)

        data = {"data": ["path1", "path2"]}
        with self.assertRaises(ValidationError):
            schema.load(data)

    def test_validate_duplicate_elements(self):
        base_app = MagicMock()
        schema = MicroServicePathValidator(base_app)

        data = ["path1", "path2", "path1"]
        duplicates = schema._duplicate_elements(data)
        self.assertEqual(duplicates, ["path1"])

    def test_load_micro_service_data_and_settings(self):
        base_app = MagicMock()
        schema = MicroServicePathValidator(base_app)

        micro_settings = [{"code": "setting1", "value": "default"}]
        micro_data = [{"path": "path1"}]
        data = {
            "name": "Test Service",
            "code": "test_service",
            "sumary": "Test Summary",
            "description": "Test Description",
            "version": "1.0.0",
            "author": "Test Author",
            "category": "Test Category",
            "context": {"tenant": "test_tenant", "user": "test_user"},
            "data": ["path1", "path2"],
            "settings": [{"code": "setting1"}, {"code": "setting2"}],
        }

        result = schema.load(data, micro_settings=micro_settings, micro_data=micro_data)

        expected_data = [
            {"path": "path1"},
            {"path": "path2", "load": False},
        ]
        self.assertEqual(result["data"], expected_data)
        self.assertEqual(len(result["settings"]), 2)


if __name__ == "__main__":
    unittest.main()
