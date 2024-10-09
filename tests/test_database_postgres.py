import unittest
from datetime import datetime as DateTime
from unittest.mock import ANY, MagicMock, patch

from omni.pro.database.postgres import CustomSession, PostgresDatabaseManager, SessionManager
from sqlalchemy import Column, DateTime, Enum, String, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.sql import operators

Base = declarative_base()


class StatusEnum(Enum):
    FOO = "foo"
    BAR = "bar"


class TestCustomSession(unittest.TestCase):

    def setUp(self):
        self.session = CustomSession()

    def test_initialization(self):
        self.assertEqual(self.session.created_attrs, {}, "created_attrs debe inicializarse como un diccionario vacío.")
        self.assertEqual(self.session.updated_attrs, {}, "updated_attrs debe inicializarse como un diccionario vacío.")
        self.assertEqual(self.session.deleted_attrs, {}, "deleted_attrs debe inicializarse como un diccionario vacío.")
        self.assertEqual(self.session.context, {}, "context debe inicializarse como un diccionario vacío.")

    def test_created_attrs_update(self):
        model_name = "User"
        instance_id = 1
        self.session.created_attrs[model_name] = [instance_id]

        self.assertIn(model_name, self.session.created_attrs)
        self.assertEqual(self.session.created_attrs[model_name], [instance_id])

    def test_updated_attrs_update(self):
        model_name = "User"
        instance_id = "1"
        updated_fields = {"name", "email"}

        self.session.updated_attrs[model_name] = {instance_id: updated_fields}

        self.assertIn(model_name, self.session.updated_attrs)
        self.assertIn(instance_id, self.session.updated_attrs[model_name])
        self.assertEqual(self.session.updated_attrs[model_name][instance_id], updated_fields)

    def test_deleted_attrs_update(self):
        model_name = "User"
        instance_id = 1
        self.session.deleted_attrs[model_name] = [instance_id]

        self.assertIn(model_name, self.session.deleted_attrs)
        self.assertEqual(self.session.deleted_attrs[model_name], [instance_id])

    def test_context_update(self):
        context_key = "service_url"
        context_value = "http://example.com/api"
        self.session.context[context_key] = context_value

        self.assertIn(context_key, self.session.context)
        self.assertEqual(self.session.context[context_key], context_value)


class TestSessionManager(unittest.TestCase):

    @patch("omni.pro.database.postgres.create_engine")
    @patch("omni.pro.database.postgres.scoped_session")
    @patch("omni.pro.database.postgres.sessionmaker")
    def setUp(self, mock_sessionmaker, mock_scoped_session, mock_create_engine):
        self.base_url = "sqlite:///:memory:"
        self.session_manager = SessionManager(self.base_url)

        self.mock_session = MagicMock(spec=CustomSession)
        self.session_manager.Session.return_value = self.mock_session

    def test_session_creation(self):

        with self.session_manager as session:
            self.assertIs(session, self.mock_session)
            self.session_manager.Session.assert_called_once()

    def test_commit_on_exit(self):
        with self.session_manager:
            pass
        self.session_manager.Session.commit.assert_called_once()
        self.session_manager.Session.remove.assert_called_once()

    def test_rollback_on_exception(self):
        with self.assertRaises(Exception):
            with self.session_manager:
                raise Exception("Test exception")
        self.session_manager.Session.rollback.assert_called_once()
        self.session_manager.Session.remove.assert_called_once()

    @patch("omni.pro.database.postgres.WebhookHandler.start_thread")
    def test_pull_crud_attrs(self, mock_start_thread):
        self.mock_session.context = {"key": "value"}
        self.mock_session.created_attrs = {"User": [1]}
        self.mock_session.updated_attrs = {"User": {"1": {"name", "email"}}}
        self.mock_session.deleted_attrs = {"User": [2]}

        self.session_manager._pull_crud_attrs()

        expected_crud_attrs = {
            "created_attrs": {"User": [1]},
            "updated_attrs": {"User": {"1": {"name", "email"}}},
            "deleted_attrs": {"User": [2]},
        }
        expected_context = {"key": "value", "type_db": "sql"}

        mock_start_thread.assert_called_once_with(crud_attrs=expected_crud_attrs, context=expected_context)

    def test_session_commit_on_no_exception(self):
        with self.session_manager as session:
            session.commit.assert_not_called()

        self.session_manager.Session.commit.assert_called_once()

    def test_session_rollback_on_exception(self):
        with self.assertRaises(ValueError):
            with self.session_manager as session:
                raise ValueError("Test Error")

        self.session_manager.Session.rollback.assert_called_once()


class TestPostgresDatabaseManager(unittest.TestCase):

    @patch("omni.pro.database.postgres.create_engine")
    @patch("omni.pro.database.postgres.scoped_session")
    def setUp(self, mock_scoped_session, mock_create_engine):
        self.name = "test_db"
        self.host = "localhost"
        self.port = "5432"
        self.user = "test_user"
        self.password = "test_password"

        self.db_manager = PostgresDatabaseManager(self.name, self.host, self.port, self.user, self.password)

        self.mock_engine = MagicMock()
        mock_create_engine.return_value = self.mock_engine
        self.mock_session = MagicMock(spec=CustomSession)
        self.db_manager.Session.return_value = self.mock_session
        self.session = MagicMock(spec=Session)
        self.model = MagicMock()

        self.fields = MagicMock()
        self.filter = MagicMock()
        self.group_by = MagicMock()
        self.sort_by = MagicMock()
        self.paginated = MagicMock()

    def test_init(self):
        self.assertEqual(self.db_manager.name, self.name)
        self.assertEqual(self.db_manager.host, self.host)
        self.assertEqual(self.db_manager.port, self.port)
        self.assertEqual(self.db_manager.user, self.user)
        self.assertEqual(self.db_manager.password, self.password)
        self.assertEqual(
            self.db_manager.base_url, f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
        )

    @patch("omni.pro.database.postgres.create_engine")
    def test_get_db_connection(self, mock_create_engine):

        mock_connection = MagicMock()

        mock_create_engine.return_value.connect.return_value = mock_connection

        db_manager = PostgresDatabaseManager(
            name="test_db", host="localhost", port="5432", user="user", password="password"
        )

        connection = db_manager.get_db_connection()

        mock_create_engine.return_value.connect.assert_called_once()

        self.assertIs(connection, mock_connection)

    def test_create_new_record(self):
        mock_model = MagicMock()
        mock_session = MagicMock()

        record_data = {"name": "Test Record", "value": 100}
        new_record = self.db_manager.create_new_record(mock_model, mock_session, **record_data)

        mock_model.assert_called_once_with(**record_data)
        new_record.create.assert_called_once_with(mock_session)

        self.assertEqual(new_record, mock_model.return_value)

    def test_retrieve_record_by_id(self):
        mock_record = MagicMock()
        self.session.query(self.model).get.return_value = mock_record

        result = self.db_manager.retrieve_record_by_id(self.model, self.session, 1)

        self.session.query(self.model).get.assert_called_once_with(1)
        self.assertEqual(result, mock_record)

    def test_retrieve_record(self):
        mock_record = MagicMock()
        self.db_manager._retrieve_records = MagicMock(return_value=self.session.query(self.model))
        self.session.query(self.model).first.return_value = mock_record

        filters = {"name": "test"}
        result = self.db_manager.retrieve_record(self.model, self.session, filters)

        self.db_manager._retrieve_records.assert_called_once_with(self.model, self.session, filters)
        self.session.query(self.model).first.assert_called_once()
        self.assertEqual(result, mock_record)

    def test_retrieve_records(self):
        mock_records = [MagicMock(), MagicMock()]
        self.db_manager._retrieve_records = MagicMock(return_value=self.session.query(self.model))
        self.session.query(self.model).all.return_value = mock_records

        filters = {"name": "test"}
        result = self.db_manager.retrieve_records(self.model, self.session, filters)

        self.db_manager._retrieve_records.assert_called_once_with(self.model, self.session, filters)
        self.session.query(self.model).all.assert_called_once()
        self.assertEqual(result, mock_records)

    def test_retrieve_records_with_or_filters(self):
        mock_records = [MagicMock(), MagicMock()]
        self.session.query(self.model).filter.return_value = self.session.query(self.model)
        self.session.query(self.model).all.return_value = mock_records

        filters = [{"name": "test"}, {"age": 30}]
        result = self.db_manager._retrieve_records(self.model, self.session, filters)

        self.session.query(self.model).filter.assert_called_once_with(ANY)
        self.assertEqual(result.all(), mock_records)

    def test_retrieve_records_with_and_filters(self):
        mock_records = [MagicMock(), MagicMock()]
        self.session.query(self.model).filter_by.return_value = self.session.query(self.model)
        self.session.query(self.model).all.return_value = mock_records

        filters = {"name": "test", "age": 30}
        result = self.db_manager._retrieve_records(self.model, self.session, filters)

        self.session.query(self.model).filter_by.assert_called_once_with(**filters)
        self.assertEqual(result.all(), mock_records)

    def test_retrieve_records_with_invalid_filters(self):
        with self.assertRaises(ValueError):
            self.db_manager._retrieve_records(self.model, self.session, "invalid_filter")

    def test_retrieve_records_with_nested_or_conditions(self):
        with self.assertRaises(NotImplementedError):
            filters = [["name", "test"]]
            self.db_manager._retrieve_records(self.model, self.session, filters)

    def test_list_records_without_id(self):
        self.paginated.offset = 1
        self.paginated.limit = 10
        self.fields.ListFields.return_value = []
        self.filter.ListFields.return_value = []
        self.sort_by.ListFields.return_value = []

        records = [MagicMock(), MagicMock()]
        self.session.query.return_value.offset.return_value.limit.return_value.all.return_value = records
        self.session.query.return_value.count.return_value = 2

        result, total = self.db_manager.list_records(
            self.model, self.session, None, self.fields, self.filter, self.group_by, self.sort_by, self.paginated
        )

        self.session.query(self.model).offset.assert_called_once_with(0)
        self.session.query(self.model).offset().limit.assert_called_once_with(10)
        self.assertEqual(result, records)
        self.assertEqual(total, 2)

    def test_update_record(self):
        model_id = 1
        update_dict = {"name": "Updated Name", "age": 30}
        record = MagicMock()

        self.session.query(self.model).get.return_value = record

        result = self.db_manager.update_record(self.model, self.session, model_id, update_dict)

        self.session.query(self.model).get.assert_called_once_with(model_id)
        self.assertEqual(record.name, "Updated Name")
        self.assertEqual(record.age, 30)
        record.update.assert_called_once_with(self.session)
        self.assertEqual(result, record)

    def test_update_record_not_found(self):
        model_id = 1
        update_dict = {"name": "Updated Name"}

        self.session.query(self.model).get.return_value = None

        result = self.db_manager.update_record(self.model, self.session, model_id, update_dict)

        self.session.query(self.model).get.assert_called_once_with(model_id)
        self.assertIsNone(result)

    @patch("omni.pro.database.postgres.Session")
    def test_delete_record_by_id(self, mock_session):
        mock_record = MagicMock()
        mock_record.delete.return_value = True

        self.session.query(self.model).filter_by.return_value.first.return_value = mock_record

        result = self.db_manager.delete_record_by_id(self.model, self.session, 1)

        mock_record.delete.assert_called_once_with(self.session)
        self.assertTrue(result)

    @patch("omni.pro.database.postgres.Session")
    def test_delete_record_by_id_not_found(self, mock_session):
        self.session.query(self.model).filter_by.return_value.first.return_value = None

        result = self.db_manager.delete_record_by_id(self.model, self.session, 1)

        self.assertFalse(result)

    def test_get_sqlalchemy_operator(self):
        self.assertEqual(self.db_manager.get_sqlalchemy_operator("="), operators.eq)
        self.assertEqual(self.db_manager.get_sqlalchemy_operator("!="), operators.ne)
        self.assertEqual(self.db_manager.get_sqlalchemy_operator("like"), operators.ilike_op)

        self.assertIsNone(self.db_manager.get_sqlalchemy_operator("unknown_operator"))

    def test_resolve_field_and_joins(self):
        mock_base_model = MagicMock()
        mock_related_model = MagicMock()
        mock_relationship = MagicMock()

        mock_related_field = MagicMock()

        mock_base_model.field1 = mock_relationship
        mock_relationship.property.mapper.class_ = mock_related_model
        mock_related_model.field2 = mock_related_field

        field_path = "field1__field2"
        field, joins = self.db_manager.resolve_field_and_joins(mock_base_model, field_path)

        self.assertIs(field, mock_related_field)
        self.assertEqual(joins, [mock_relationship])

    def test_parse_expression_simple(self):
        mock_base_model = MagicMock()
        mock_base_model.field = Column(String)
        mock_query = MagicMock()

        self.db_manager.get_sqlalchemy_operator = MagicMock(return_value=operators.eq)

        expression = [("field", "=", "value")]

        result_query = self.db_manager.parse_expression(expression, mock_query, mock_base_model)

        self.db_manager.get_sqlalchemy_operator.assert_any_call("=")
        mock_query.filter.assert_called_once()

    def test_parse_expression_with_datetime(self):
        mock_base_model = MagicMock()
        mock_base_model.created_at = Column(DateTime)
        mock_query = MagicMock()

        self.db_manager.get_sqlalchemy_operator = MagicMock(return_value=operators.eq)

        expression = [("created_at", "=", "2024-01-01 12:00:00")]

        result_query = self.db_manager.parse_expression(expression, mock_query, mock_base_model)

        self.db_manager.get_sqlalchemy_operator.assert_called_with("=")
        mock_query.filter.assert_called_once()


if __name__ == "__main__":
    unittest.main()
