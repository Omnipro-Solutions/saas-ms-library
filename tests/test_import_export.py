import unittest
from datetime import datetime
from unittest.mock import MagicMock, patch

from omni.pro.import_export import BatchUpsert, ImportExportBase, QueryExport


class TestImportExportBase(unittest.TestCase):

    @patch("omni.pro.import_export.import_module")
    def test_get_model(self, mock_import_module):
        mock_class = MagicMock()
        mock_module = MagicMock()
        mock_import_module.return_value = mock_module
        mock_module.SomeClass = mock_class

        base = ImportExportBase()
        result = base.get_model("some.module.SomeClass")

        mock_import_module.assert_called_once_with("some.module")
        self.assertEqual(result, mock_class)


class TestQueryExport(unittest.TestCase):

    def setUp(self):
        self.context = MagicMock()
        self.query_export = QueryExport(self.context)
        self.model = MagicMock()
        self.model.__tablename__ = "test_table"

    @patch.object(QueryExport, "get_model")
    @patch.object(QueryExport, "get_data_no_sql")
    def test_get_data_no_sql(self, mock_get_data_no_sql, mock_get_model):
        mock_model = MagicMock()
        mock_get_model.return_value = mock_model
        mock_get_data_no_sql.return_value = [{"data": "test"}]

        result = self.query_export.get_data(
            "some.module.SomeModel", ["field1", "field2"], "2024-01-01", "2024-12-31", self.context
        )

        mock_get_model.assert_called_once_with("some.module.SomeModel")
        mock_get_data_no_sql.assert_called_once_with(
            mock_model, "some.module.SomeModel", ["field1", "field2"], "2024-01-01", "2024-12-31", self.context
        )
        self.assertEqual(result, [{"data": "test"}])

    @patch.object(QueryExport, "parse_date")
    def test_parse_date(self, mock_parse_date):
        mock_parse_date.side_effect = [datetime(2024, 1, 1, 0, 0, 0), datetime(2024, 12, 31, 0, 0, 0)]

        start_date = self.query_export.parse_date("2024-01-01T00:00:00Z")
        end_date = self.query_export.parse_date("2024-12-31T00:00:00.000Z")

        self.assertEqual(start_date, datetime(2024, 1, 1, 0, 0, 0))
        self.assertEqual(end_date, datetime(2024, 12, 31, 0, 0, 0))

    @patch.object(QueryExport, "parse_date")
    def test_get_data_no_sql(self, mock_parse_date):
        mock_model = MagicMock()
        mock_model._fields.keys.return_value = {"field1", "field2", "id"}

        mock_db = MagicMock()
        mock_model.db = mock_db

        expected_result = [{"field1": "value1"}]
        mock_db.__getitem__.return_value.find.return_value = expected_result

        mock_parse_date.side_effect = [datetime(2024, 1, 1), datetime(2024, 12, 31)]

        result = self.query_export.get_data_no_sql(
            mock_model, "some.module.SomeModel", ["field1"], "2024-01-01", "2024-12-31", {"tenant": "test_tenant"}
        )

        mock_db.__getitem__.assert_called_with("somemodel")
        mock_db.__getitem__.return_value.find.assert_called_once_with(
            {
                "context.tenant": "test_tenant",
                "audit.created_at": {"$gte": datetime(2024, 1, 1), "$lte": datetime(2024, 12, 31)},
            },
            projection={"_id": False, "field2": False},
        )

        self.assertEqual(result, expected_result)

    @patch("omni.pro.import_export.inspect")
    @patch("omni.pro.import_export.text")
    @patch.object(QueryExport, "_serialize_query_result")
    def test_get_data_sql(self, mock_serialize_query_result, mock_text, mock_inspect):
        mock_inspect.return_value.columns = [
            MagicMock(name="id", foreign_keys=[]),
            MagicMock(name="field1", foreign_keys=[]),
            MagicMock(name="field2", foreign_keys=[]),
            MagicMock(
                name="related_id", foreign_keys=[MagicMock(column=MagicMock(table=MagicMock(name="related_table")))]
            ),
        ]

        mock_text.return_value = MagicMock()
        mock_result = MagicMock()
        self.context.pg_manager.Session.execute.return_value = mock_result

        result = self.query_export.get_data_sql(
            self.model,
            "some.module.SomeModel",
            ["field1", "related_id"],
            datetime(2024, 1, 1),
            datetime(2024, 12, 31),
            {"tenant": "test_tenant"},
        )

        mock_text.assert_called_once()
        self.context.pg_manager.Session.execute.assert_called_once_with(
            mock_text.return_value,
            {"tenant": "test_tenant", "start_date": datetime(2024, 1, 1), "end_date": datetime(2024, 12, 31)},
        )

        mock_serialize_query_result.assert_called_once_with(mock_result)

    def test_serialize_query_result(self):
        mock_result = MagicMock()
        mock_result.cursor.description = [("id",), ("field1",), ("created_at",)]
        mock_result.fetchall.return_value = [(1, "value1", datetime(2024, 1, 1))]

        result = self.query_export._serialize_query_result(mock_result)

        expected_result = [
            {
                "id": 1,
                "field1": "value1",
                "created_at": "2024-01-01T00:00:00",
            }
        ]
        self.assertEqual(result, expected_result)

    def test_datetime_to_string(self):
        dt = datetime(2024, 1, 1, 10, 30, 45)
        result = self.query_export.datetime_to_string(dt)
        self.assertEqual(result, "2024-01-01T10:30:45")

        result = self.query_export.datetime_to_string("not a datetime")
        self.assertEqual(result, "not a datetime")


class TestBatchUpsert(unittest.TestCase):

    def setUp(self):
        self.context_sql = MagicMock()
        self.context_sql.pg_manager = MagicMock()
        self.context_no_sql = MagicMock()
        self.context_no_sql.db_manager = MagicMock()

        self.batch_upsert_sql = BatchUpsert(context=self.context_sql)
        self.batch_upsert_no_sql = BatchUpsert(context=self.context_no_sql)

    @patch.object(BatchUpsert, "get_model")
    def test_upsert_data_sql(self, mock_get_model):
        mock_model = MagicMock()
        mock_get_model.return_value = mock_model

        data = {"model_path": "some.module.SomeModel", "upsert_data": [{"id": 1, "field1": "value1"}]}

        result = self.batch_upsert_sql.upsert_data(data)

        self.context_sql.pg_manager.batch_upsert.assert_called_once_with(
            mock_model, self.context_sql.pg_manager.Session, data
        )


if __name__ == "__main__":
    unittest.main()
