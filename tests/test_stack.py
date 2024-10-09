import unittest
from unittest.mock import MagicMock, patch

from omni.pro.stack import ExitStackDocument, ExitStackDocumentMicro


class TestExitStackDocument(unittest.TestCase):

    def setUp(self):
        self.document_class_1 = MagicMock()
        self.document_class_2 = MagicMock()
        self.document_classes = [self.document_class_1, self.document_class_2]
        self.db_alias = "test_db"
        self.context = {"user": "test_user", "tenant": "test_tenant"}

    @patch("omni.pro.stack.ctx_mgr.switch_db")
    def test_enter_creates_collections_and_switches_db(self, mock_switch_db):
        with ExitStackDocument(self.document_classes, self.db_alias, self.context) as stack:
            mock_switch_db.assert_any_call(self.document_class_1, self.db_alias)
            mock_switch_db.assert_any_call(self.document_class_2, self.db_alias)
            self.document_class_1._meta.__setitem__.assert_called_with("db_alias", self.db_alias)
            self.document_class_1.db.list_collection_names.assert_called_once()
            self.document_class_1.db.create_collection.assert_called_once()

    @patch("omni.pro.stack.WebhookHandler.start_thread")
    def test_exit_pulls_crud_attrs_and_starts_webhook_thread(self, mock_start_thread):
        with ExitStackDocument(self.document_classes, self.db_alias, self.context) as stack:
            stack.created_attrs = {"doc1": [1, 2, 3]}
            stack.updated_attrs = {"doc1": {"field1": {"value1"}}}
            stack.deleted_attrs = {"doc1": [4, 5, 6]}

        expected_crud_attrs = {
            "created_attrs": {"doc1": [1, 2, 3]},
            "updated_attrs": {"doc1": {"field1": {"value1"}}},
            "deleted_attrs": {"doc1": [4, 5, 6]},
        }
        self.context["type_db"] = "document"
        mock_start_thread.assert_called_once_with(crud_attrs=expected_crud_attrs, context=self.context)


class TestExitStackDocumentMicro(unittest.TestCase):

    @patch("omni.pro.stack.Topology.get_models_from_libs", return_value=[MagicMock(), MagicMock()])
    @patch("omni.pro.stack.ctx_mgr.switch_db")
    @patch("importlib.import_module")
    def test_enter_switches_to_all_models_in_services(self, mock_import_module, mock_switch_db, mock_get_models):
        mock_import_module.return_value = MagicMock()

        db_alias = "microservice_db"
        with ExitStackDocumentMicro(db_alias) as stack:
            mock_switch_db.assert_any_call(mock_get_models.return_value[0], db_alias)
            mock_switch_db.assert_any_call(mock_get_models.return_value[1], db_alias)

    @patch("omni.pro.stack.Topology.get_models_from_libs", return_value=[MagicMock(), MagicMock()])
    @patch("omni.pro.stack.ctx_mgr.switch_db")
    @patch("omni.pro.stack.WebhookHandler.start_thread")
    @patch("importlib.import_module")
    def test_exit_with_models_from_services(
        self, mock_import_module, mock_start_thread, mock_switch_db, mock_get_models
    ):
        mock_import_module.return_value = MagicMock()

        context = {"tenant": "test_tenant", "user": "test_user"}
        with ExitStackDocumentMicro("microservice_db", context=context) as stack:
            stack.created_attrs = {"model_1": [1, 2]}
            stack.updated_attrs = {"model_2": {"field1": {"value1"}}}
            stack.deleted_attrs = {"model_1": [3, 4]}

        expected_crud_attrs = {
            "created_attrs": {"model_1": [1, 2]},
            "updated_attrs": {"model_2": {"field1": {"value1"}}},
            "deleted_attrs": {"model_1": [3, 4]},
        }
        context["type_db"] = "document"
        mock_start_thread.assert_called_once_with(crud_attrs=expected_crud_attrs, context=context)


if __name__ == "__main__":
    unittest.main()
