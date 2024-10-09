import unittest
from datetime import datetime
from decimal import Decimal
from unittest.mock import MagicMock, patch

from bson import ObjectId
from google.protobuf.timestamp_pb2 import Timestamp
from omni.pro.models.base import (
    Audit,
    Base,
    BaseAuditEmbeddedDocument,
    BaseDocument,
    BaseObjectEmbeddedDocument,
    Context,
)
from sqlalchemy import DECIMAL, Boolean, Column, Integer, String, create_engine, inspect
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, declarative_base, sessionmaker

BaseModel = declarative_base(cls=Base)


class TestModel(BaseModel):
    __tablename__ = "test_model"
    id = Column(Integer, primary_key=True)
    active = Column(Boolean, default=True)
    name = Column(String(50))
    price = Column(DECIMAL(10, 2))


class TestBaseObjectEmbeddedDocument(unittest.TestCase):
    def test_to_proto(self):
        obj = BaseObjectEmbeddedDocument(code="test_code", code_name="test_name")

        proto = obj.to_proto()

        self.assertEqual(proto.code, "test_code")
        self.assertEqual(proto.code_name, "test_name")


class TestAudit(unittest.TestCase):
    def test_to_proto(self):
        audit = Audit(
            created_by="user1", updated_by="user2", created_at=datetime(2023, 1, 1), updated_at=datetime(2023, 1, 2)
        )

        proto = audit.to_proto()

        self.assertEqual(proto.created_by, "user1")
        self.assertEqual(proto.updated_by, "user2")

        create_at_ts = Timestamp()
        create_at_ts.FromDatetime(datetime(2023, 1, 1))
        update_at_ts = Timestamp()
        update_at_ts.FromDatetime(datetime(2023, 1, 2))

        self.assertEqual(proto.created_at, create_at_ts)
        self.assertEqual(proto.updated_at, update_at_ts)


class TestContext(unittest.TestCase):
    def test_to_proto(self):
        context = Context(tenant="test_tenant", user="test_user")

        proto = context.to_proto()

        self.assertEqual(proto.tenant, "test_tenant")
        self.assertEqual(proto.user, "test_user")


class TestBaseDocument(unittest.TestCase):
    def setUp(self):
        self.context = Context(tenant="test_tenant", user="test_user")
        self.audit = Audit(created_by="test_user", updated_by="test_user")
        self.document = BaseDocument(context=self.context, audit=self.audit, active=True)
        self.document._collection = MagicMock()
        self.document._collection.name = "test_collection"
        self.document.id = ObjectId("507f1f77bcf86cd799439011")
        self.document._changed_fields = ["field1"]

    def test_generate_dict(self):
        self.document.id = ObjectId("507f1f77bcf86cd799439011")

        with patch.object(self.document, "to_mongo") as mock_to_mongo:
            mock_to_mongo.return_value.to_dict.return_value = {
                "_id": ObjectId("507f1f77bcf86cd799439011"),
                "context": {"tenant": "test_tenant", "user": "test_user"},
                "audit": {
                    "created_at": datetime(2024, 10, 8, 15, 4, 16),
                    "created_by": "test_user",
                    "updated_at": datetime(2024, 10, 8, 15, 4, 16),
                    "updated_by": "test_user",
                },
                "active": True,
            }

            generated_dict = self.document.generate_dict()

            self.assertIn("id", generated_dict)
            self.assertEqual(generated_dict["id"], "507f1f77bcf86cd799439011")

    @patch("omni.pro.models.base.Context")
    @patch("omni.pro.models.base.Audit")
    def test_save(self, mock_audit, mock_context):
        mock_audit.return_value = Audit(created_by="test_user")
        mock_context.return_value = self.context

        with patch.object(BaseDocument, "save", return_value=None) as mock_save:
            self.document.save()

            self.assertEqual(self.document.audit.updated_by, "test_user")
            self.assertIsNotNone(self.document.audit.updated_at)
            mock_save.assert_called_once()

    def test_update(self):
        with patch.object(BaseDocument, "update", return_value=None) as mock_update:
            self.document.update(name="New Name")
            mock_update.assert_called_once()

    @patch("omni.pro.models.base.BaseDocument.assign_crud_attrs_to_stack")
    @patch("omni.pro.models.base.Config")
    def test_post_save_create(self, mock_config, mock_crud_attrs):
        mock_config.PROCESS_WEBHOOK = True
        BaseDocument.post_save(sender=BaseDocument, document=self.document, created=True)

        mock_crud_attrs.assert_called_once_with("create")

    @patch("omni.pro.models.base.BaseDocument.assign_crud_attrs_to_stack")
    @patch("omni.pro.models.base.Config")
    def test_post_save_update(self, mock_config, mock_crud_attrs):
        mock_config.PROCESS_WEBHOOK = True
        BaseDocument.post_save(sender=BaseDocument, document=self.document, created=False)

        mock_crud_attrs.assert_called_once_with("update", {"field1"})

    @patch("omni.pro.models.base.BaseDocument.assign_crud_attrs_to_stack")
    @patch("omni.pro.models.base.Config")
    def test_post_delete(self, mock_config, mock_crud_attrs):
        mock_config.PROCESS_WEBHOOK = True
        BaseDocument.post_delete(sender=BaseDocument, document=self.document)

        mock_crud_attrs.assert_called_once_with("delete")

    def test_assign_crud_attrs_to_stack_create(self):
        self.document.created_attrs = {}
        self.document.assign_crud_attrs_to_stack(action="create")
        self.assertIn(self.document._collection.name, self.document.created_attrs)


class TestBaseAuditEmbeddedDocument(unittest.TestCase):

    def setUp(self):
        self.document = BaseAuditEmbeddedDocument(
            context=Context(tenant="test_tenant", user="test_user"), audit=Audit(created_by="initial_user")
        )

    @patch("omni.pro.models.base.datetime")
    def test_audit_fields_are_updated(self, mock_datetime):
        mock_datetime.utcnow.return_value = datetime(2024, 1, 1, 12, 0, 0)

        self.document.update_audit_fields()

        self.assertEqual(self.document.audit.created_by, "initial_user")
        self.assertEqual(self.document.audit.updated_by, "test_user")
        self.assertEqual(self.document.audit.updated_at, datetime(2024, 1, 1, 12, 0, 0))

    def test_context_is_set_if_not_present(self):
        document = BaseAuditEmbeddedDocument(audit=Audit(created_by="initial_user"))

        document.update_audit_fields()

        self.assertIsNotNone(document.context)
        self.assertIsNotNone(document.context.tenant)

    def test_context_is_set_if_not_present(self):
        document = BaseAuditEmbeddedDocument()

        document.context = Context(tenant="default_tenant", user="default_user")

        document.update_audit_fields()

        self.assertIsNotNone(document.context)
        self.assertEqual(document.context.tenant, "default_tenant")
        self.assertEqual(document.context.user, "default_user")

    def test_active_field_defaults_to_true(self):
        document = BaseAuditEmbeddedDocument()

        self.assertTrue(document.active)

    def test_external_id_can_be_set(self):
        document = BaseAuditEmbeddedDocument(external_id="test_external_id")

        self.assertEqual(document.external_id, "test_external_id")


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.engine = create_engine("sqlite:///:memory:")
        BaseModel.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        self.instance = TestModel(
            id=1,
            active=True,
            name="Test Item",
            price=Decimal("19.99"),
            external_id="ext_123",
            tenant="tenant_1",
            created_by="user_1",
            updated_by="user_2",
            created_at=datetime(2024, 1, 1, 10, 0),
            updated_at=datetime(2024, 1, 2, 10, 0),
        )
        self.session.add(self.instance)
        self.session.commit()

        self.session = MagicMock(spec=Session)

    def test_create_method(self):
        result = self.instance.create(self.session)
        self.session.add.assert_called_once_with(self.instance)
        self.session.flush.assert_called_once()
        self.assertEqual(result, self.instance)

    def test_bulk_insert_method(self):
        items = [{"field1": "value1"}, {"field1": "value2"}]
        Base.bulk_insert(self.session, items)
        self.session.bulk_insert_mappings.assert_called_once_with(Base, items)
        self.session.flush.assert_called_once()

    def test_bulk_update_method(self):
        items = [{"field1": "value1"}, {"field1": "value2"}]
        Base.bulk_update(self.session, items)
        self.session.bulk_update_mappings.assert_called_once_with(Base, items)
        self.session.flush.assert_called_once()

    def test_update_method(self):
        self.instance.update(self.session)
        self.session.flush.assert_called_once()
        self.session.refresh.assert_called_once_with(self.instance)

    def test_delete_method_success(self):
        result = self.instance.delete(self.session)
        self.session.delete.assert_called_once_with(self.instance)
        self.assertTrue(result)

    def test_delete_method_failure(self):
        self.session.delete.side_effect = SQLAlchemyError
        result = self.instance.delete(self.session)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
