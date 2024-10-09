import unittest
from unittest.mock import MagicMock, patch

from omni.pro.mirror_model import MirroModelWebhookRegister, MirrorModelNoSQL, MirrorModelSQL
from pymongo.operations import InsertOne, UpdateOne


class TestMirrorModelSQL(unittest.TestCase):

    def setUp(self):
        self.context = MagicMock()
        self.context.pg_manager = MagicMock()
        self.context.pg_manager.Session = MagicMock()
        self.tenant = "test_tenant"
        self.user = "test_user"
        self.model_path = "omni.pro.mirror_model.MirrorModelSQL"

        self.mirror_model_sql = MirrorModelSQL(self.context, self.model_path, self.tenant, self.user)
        self.mirror_model_sql.model = MagicMock()
        self.mirror_model_sql.model.transform_mirror = MagicMock()

    @patch("omni.pro.mirror_model.inspect")
    def test_create_mirror_model(self, mock_inspect):
        mock_mapper = MagicMock()
        mock_column = MagicMock()
        mock_column.unique = True
        mock_column.name = "unique_field"
        mock_column.field_aliasing = "code"
        mock_mapper.columns = [mock_column]
        mock_inspect.return_value = mock_mapper

        data = {
            "model_data": {"unique_field": "value1", "other_field": "value2"},
            "context": {"tenant": self.tenant, "user": self.user},
        }

        self.context.pg_manager.retrieve_record.return_value = None

        result = self.mirror_model_sql.create_mirror_model(data)

        self.mirror_model_sql.model.transform_mirror.assert_called_once_with(data["model_data"])

        self.context.pg_manager.create_new_record.assert_called_once_with(
            self.mirror_model_sql.model,
            self.context.pg_manager.Session,
            **data["model_data"],
            tenant=self.tenant,
            updated_by=self.user
        )

    @patch("omni.pro.mirror_model.inspect")
    def test_update_mirror_model(self, mock_inspect):
        mock_mapper = MagicMock()
        mock_column = MagicMock()
        mock_column.unique = True
        mock_column.name = "id"
        mock_mapper.columns = [mock_column]
        mock_inspect.return_value = mock_mapper

        data = {
            "model_data": {"id": 1, "other_field": "value2"},
            "context": {"tenant": self.tenant, "user": self.user},
        }

        self.context.pg_manager.retrieve_record_by_id.return_value = MagicMock()

        result = self.mirror_model_sql.update_mirror_model(data)

        self.mirror_model_sql.model.transform_mirror.assert_called_once_with(data["model_data"])

        self.context.pg_manager.update_record.assert_called_once_with(
            self.mirror_model_sql.model,
            self.context.pg_manager.Session,
            1,
            data["model_data"] | {"tenant": self.tenant, "updated_by": self.user},
        )

    @patch("omni.pro.mirror_model.inspect")
    def test_multi_create_mirror_model(self, mock_inspect):
        mock_mapper = MagicMock()
        mock_column = MagicMock()
        mock_column.unique = True
        mock_column.name = "unique_field"
        mock_column.field_aliasing = "code"
        mock_mapper.columns = [mock_column]
        mock_inspect.return_value = mock_mapper

        items = [
            {"unique_field": "value1", "other_field": "value2"},
            {"unique_field": "value2", "other_field": "value3"},
        ]

        self.mirror_model_sql._get_doc_ids_by_unique_field_aliasing = MagicMock(return_value={})

        self.mirror_model_sql.multi_create_mirror_model(items)

        self.mirror_model_sql.model.transform_mirror.assert_any_call(items[0])
        self.mirror_model_sql.model.transform_mirror.assert_any_call(items[1])

        self.mirror_model_sql.model.bulk_insert.assert_called_once_with(
            session=self.context.pg_manager.Session, items=items
        )

    def test_read_mirror_model(self):
        data = MagicMock()
        data.id = 1
        data.fields = ["field1", "field2"]
        data.filter = {"field1": "value1"}
        data.group_by = []
        data.sort_by = []
        data.paginated = False

        result = self.mirror_model_sql.read_mirror_model(data)

        self.context.pg_manager.list_records.assert_called_once_with(
            self.mirror_model_sql.model,
            self.context.pg_manager.Session,
            data.id,
            data.fields,
            data.filter,
            data.group_by,
            data.sort_by,
            data.paginated,
        )


class TestMirrorModelNoSQL(unittest.TestCase):

    def setUp(self):
        self.context = MagicMock()
        self.context.db_manager = MagicMock()
        self.tenant = "test_tenant"
        self.user = "test_user"
        self.model_path = "omni.pro.mirror_model.MirrorModelNoSQL"

        self.mirror_model_nosql = MirrorModelNoSQL(self.context, self.model_path, self.tenant, self.user)
        self.mirror_model_nosql.model = MagicMock()
        self.mirror_model_nosql.model.transform_mirror = MagicMock()

        self.mirror_model_nosql._get_unique_field_aliasing = MagicMock(return_value="unique_field")
        self.mirror_model_nosql._get_doc_ids_by_unique_field_aliasing = MagicMock(return_value={})

    def test_create_mirror_model(self):
        data = {
            "model_data": {"unique_field": "value1", "other_field": "value2"},
            "context": {"tenant": self.tenant, "user": self.user},
        }

        self.context.db_manager.get_document.return_value = None

        result = self.mirror_model_nosql.create_mirror_model(data)

        self.mirror_model_nosql.model.transform_mirror.assert_called_once_with(data["model_data"])

        self.context.db_manager.create_document.assert_called_once_with(
            None, self.mirror_model_nosql.model, **data["model_data"]
        )

    def test_multi_create_mirror_model(self):
        items = [
            {"unique_field": "value1", "other_field": "value2"},
            {"unique_field": "value2", "other_field": "value3"},
        ]

        self.mirror_model_nosql._get_doc_ids_by_unique_field_aliasing = MagicMock(return_value={})

        self.mirror_model_nosql.multi_create_mirror_model(items)

        self.mirror_model_nosql.model.transform_mirror.assert_any_call(items[0])
        self.mirror_model_nosql.model.transform_mirror.assert_any_call(items[1])

        self.mirror_model_nosql.model._get_collection().bulk_write.assert_called_once_with(
            [InsertOne(items[0]), InsertOne(items[1])], ordered=False
        )

    def test_update_mirror_model(self):
        data = {
            "model_data": {"id": "existing_doc_id", "other_field": "value2"},
            "context": {"tenant": self.tenant, "user": self.user},
        }

        self.context.db_manager.get_document.return_value = MagicMock()

        result = self.mirror_model_nosql.update_mirror_model(data)

        self.mirror_model_nosql.model.transform_mirror.assert_called_once_with(data["model_data"])

        self.context.db_manager.update_document.assert_called_once_with(
            None, self.mirror_model_nosql.model, **data["model_data"]
        )

    def test_multi_update_mirror_model(self):
        items = [
            {"unique_field": "value1", "other_field": "value2", "id": "doc_id_1"},
            {"unique_field": "value2", "other_field": "value3", "id": "doc_id_2"},
        ]

        self.mirror_model_nosql._get_doc_ids_by_unique_field_aliasing = MagicMock(
            return_value={"value1": "doc_id_1", "value2": "doc_id_2"}
        )

        self.mirror_model_nosql.multi_update_mirror_model(items)

        self.mirror_model_nosql.model.transform_mirror.assert_any_call(items[0])
        self.mirror_model_nosql.model.transform_mirror.assert_any_call(items[1])

        self.mirror_model_nosql.model._get_collection().bulk_write.assert_called_once_with(
            [UpdateOne({"_id": "doc_id_1"}, {"$set": items[0]}), UpdateOne({"_id": "doc_id_2"}, {"$set": items[1]})],
            ordered=False,
        )


class TestMirroModelWebhookRegister(unittest.TestCase):

    def setUp(self):
        self.context = {
            "tenant": "test_tenant",
            "user": "test_user",
        }

        self.params = {
            "filter": {"filter": "[('name', '=', 'test_webhook')]"},
            "data": {
                "name": "Test Webhook",
                "event_ids": [1, 2, 3],
                "method_grpc_id": 123,
            },
        }

    @patch("omni.pro.mirror_model.RedisManager")
    @patch.object(MirroModelWebhookRegister, "register")
    def test_run(self, mock_register, mock_redis_manager):
        mock_redis_instance = mock_redis_manager.return_value
        mock_redis_instance.get_tenant_codes.return_value = ["tenant1", "tenant2"]
        mock_redis_instance.get_user_admin.side_effect = [{"id": "user1"}, {"id": "user2"}]

        MirroModelWebhookRegister.run()

        self.assertEqual(mock_register.call_count, 2)

        expected_context_1 = {"tenant": "tenant1", "user": "user1"}
        expected_context_2 = {"tenant": "tenant2", "user": "user2"}

        mock_register.assert_any_call(context=expected_context_1)
        mock_register.assert_any_call(context=expected_context_2)


if __name__ == "__main__":
    unittest.main()
