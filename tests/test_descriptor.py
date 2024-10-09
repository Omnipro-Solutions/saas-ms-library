import unittest
from unittest.mock import MagicMock, patch

import mongomock
from mongoengine import (
    Document,
    EmbeddedDocument,
    EmbeddedDocumentField,
    ReferenceField,
    StringField,
    connect,
    disconnect,
)
from omni.pro.descriptor import Descriptor
from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class EmbeddedDoc(EmbeddedDocument):
    embedded_field = StringField()


class MongoModel(Document):
    field1 = StringField(required=True)
    field2 = ReferenceField("self", required=False)
    field3 = EmbeddedDocumentField(EmbeddedDoc)

    __is_replic_table__ = True


Base = declarative_base()


class SQLAlchemyModel(Base):
    __tablename__ = "test_table"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200))
    status = Column(Enum("ACTIVE", "INACTIVE", name="status_enum"))

    @property
    def __is_replic_table__(self):
        return True


class TestDescriptor(unittest.TestCase):

    def setUp(self):
        connect("mongoenginetest", host="localhost", mongo_client_class=mongomock.MongoClient)

    def tearDown(self):
        disconnect()

    @patch("omni.pro.descriptor.Descriptor.get_equivalent_field", return_value="String")
    @patch("omni.pro.descriptor.inspect")
    def test_describe_sqlalchemy_model(self, mock_inspect, mock_get_equivalent_field):
        model = SQLAlchemyModel
        descriptor = Descriptor()

        mapper_mock = MagicMock()
        mapper_mock.columns = [
            Column("id", Integer),
            Column("name", String),
            Column("description", String),
        ]
        mapper_mock.relationships = {}

        mock_inspect.return_value = mapper_mock

        result = descriptor.describe_sqlalchemy_model(model)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["name"], "SQLAlchemyModel")
        self.assertIn("fields", result)
        self.assertEqual(len(result["fields"]), 3)

        field_names = [field["name"] for field in result["fields"]]
        self.assertIn("Id", field_names)
        self.assertIn("Name", field_names)
        self.assertIn("Description", field_names)

    def test_get_equivalent_field(self):
        descriptor = Descriptor()

        self.assertEqual(descriptor.get_equivalent_field("StringField"), "string")
        self.assertEqual(descriptor.get_equivalent_field("ReferenceField"), "reference")

        self.assertEqual(descriptor.get_equivalent_field("String"), "string")
        self.assertEqual(descriptor.get_equivalent_field("Enum"), "enum")

    @patch("omni.pro.descriptor.BaseModel")
    def test_set_extra_attribute(self, mock_base_model):
        descriptor = Descriptor()

        column_mock = MagicMock()
        column_mock.name = "test_column"

        mock_base_model.__annotations__ = {"test_column": MagicMock()}
        mock_base_model.test_column.column.is_filterable = True

        descriptor.set_extra_attribute(column_mock, "is_filterable")
        self.assertTrue(column_mock.is_filterable)


if __name__ == "__main__":
    unittest.main()
