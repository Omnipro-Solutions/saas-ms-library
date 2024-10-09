import unittest
from unittest.mock import ANY, MagicMock, patch

from bson import ObjectId
from omni.pro.database.mongo import DatabaseManager, DBUtil, MongoConnection, PolishNotationToMongoDB
from omni.pro.exceptions import AlreadyExistError
from omni_pro_grpc.common import base_pb2


class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        self.db_manager = DatabaseManager(
            host="localhost", port=27017, db="test_db", user="root", password="123456", complement={}
        )

    def test_create_document(self):
        mock_document_class = MagicMock()

        document_instance = self.db_manager.create_document(
            "test_db", mock_document_class, field1="value1", field2="value2"
        )

        mock_document_class.assert_called_once_with(field1="value1", field2="value2")
        document_instance.save.assert_called_once()

    def test_get_document(self):
        mock_document_class = MagicMock()

        mock_document_instance = MagicMock()
        mock_document_class.objects.return_value.first.return_value = mock_document_instance

        result = self.db_manager.get_document("test_db", "tenant_code", mock_document_class, field="value")

        mock_document_class.objects.assert_called_once_with(field="value", context__tenant="tenant_code")
        self.assertEqual(result, mock_document_instance)

    def test_update_document(self):
        mock_document_class = MagicMock()

        mock_document_instance = MagicMock()
        mock_document_instance.id = "12345"
        mock_document_class.objects.return_value.first.return_value = mock_document_instance

        result = self.db_manager.update_document("test_db", mock_document_class, id="12345", field="new_value")
        mock_document_class.objects.assert_called_with(id="12345")
        mock_document_instance.update.assert_called_once_with(field="new_value")
        mock_document_instance.reload.assert_called_once()
        self.assertEqual(result, mock_document_instance)

    def test_delete(self):
        mock_document_instance = MagicMock()

        deleted_document = self.db_manager.delete(mock_document_instance)

        mock_document_instance.delete.assert_called_once()
        self.assertEqual(deleted_document, mock_document_instance)

    def test_delete_document(self):
        mock_document_class = MagicMock()

        mock_document_instance = MagicMock()
        mock_document_class.objects.return_value.first.return_value = mock_document_instance

        deleted_document = self.db_manager.delete_document("test_db", mock_document_class, id="12345")

        mock_document_class.objects.assert_called_with(id="12345")
        mock_document_instance.delete.assert_called_once()

        self.assertEqual(deleted_document, mock_document_instance)

    @patch("time.time", side_effect=[0, 1])
    def test_list_documents(self, mock_time):
        mock_document_class = MagicMock()

        mock_query_set = MagicMock()

        mock_query_set.count.return_value = 5

        mock_document_class.objects.return_value = mock_query_set
        mock_query_set.only.return_value = mock_query_set
        mock_query_set.order_by.return_value = mock_query_set
        mock_query_set.limit.return_value = mock_query_set
        mock_query_set.skip.return_value = mock_query_set
        mock_query_set.__getitem__.return_value = mock_query_set

        documents, total_count = self.db_manager.list_documents(
            db_name="test_db",
            tenant="tenant_code",
            document_class=mock_document_class,
            fields=["field1", "field2"],
            paginated={"page": 1, "per_page": 10},
            sort_by=["-field1"],
        )

        mock_document_class.objects.assert_called_once_with(context__tenant="tenant_code")

        mock_query_set.only.assert_called_once_with("field1", "field2")

        print(f"documents: {documents}, total_count: {total_count}")

        self.assertEqual(documents, list(mock_query_set))
        self.assertEqual(total_count, 5)

    @patch("omni.pro.database.mongo.MongoConnection")
    def test_list_documents(self, mock_mongo_connection):
        mock_document_class = MagicMock()

        mock_collection = mock_document_class._get_collection.return_value
        mock_aggregate_result = [
            {"_id": "1", "name": "document1"},
            {"_id": "2", "name": "document2"},
        ]
        mock_collection.aggregate.return_value = mock_aggregate_result

        filter_conditions = [("name", "=", "document1")]
        query_set = self.db_manager._list_documents(
            tenant="tenant_code",
            filter_conditions=filter_conditions,
            id=None,
            document_class=mock_document_class,
            paginated={"page": 1, "per_page": 10},
            sort=["+name"],
        )

        mock_collection.aggregate.assert_called_once()
        called_pipeline = mock_collection.aggregate.call_args[0][0]

        self.assertIn({"$match": {"name": {"$eq": "document1"}}}, called_pipeline)
        self.assertIn({"$sort": {"name": 1}}, called_pipeline)

        self.assertEqual(query_set, [mock_document_class._from_son(item) for item in mock_aggregate_result])

    def test_parse_expression_to_pipeline(self):
        mock_document_class = MagicMock()

        filter_conditions = [("name", "like", "doc")]

        pipeline = self.db_manager.parse_expression_to_pipeline(
            document_class=mock_document_class,
            filter_conditions=filter_conditions,
            id=None,
            sort=["+name"],
            paginated={"page": 1, "per_page": 10},
        )

        expected_match = {"$match": {"name": {"$regex": "doc", "$options": "i"}}}
        expected_sort = {"$sort": {"name": 1}}
        expected_skip = {"$skip": 0}
        expected_limit = {"$limit": 10}

        self.assertIn(expected_match, pipeline)
        self.assertIn(expected_sort, pipeline)
        self.assertIn(expected_skip, pipeline)
        self.assertIn(expected_limit, pipeline)

    def test_delete_documents(self):
        mock_document_class = MagicMock()
        mock_delete_result = MagicMock()
        mock_document_class.objects.return_value.delete.return_value = mock_delete_result

        result = self.db_manager.delete_documents(
            db_name="test_db", document_class=mock_document_class, some_field="some_value"
        )

        mock_document_class.objects.assert_called_once_with(some_field="some_value")

        mock_document_class.objects().delete.assert_called_once()

        self.assertEqual(result, mock_delete_result)

    def test_update_embeded_document_single(self):
        mock_document_class = MagicMock()

        mock_update_result = MagicMock()
        mock_document_class.objects.return_value.update_one.return_value = mock_update_result
        mock_document_class.objects.return_value.first.return_value = "updated_document"

        result = self.db_manager.update_embeded_document(
            db_name="test_db",
            document_class=mock_document_class,
            filters={"_id": "123"},
            update={"$set": {"field": "value"}},
            many=False,
        )

        self.assertEqual(mock_document_class.objects.call_count, 2)
        mock_document_class.objects.assert_any_call(_id="123")
        mock_document_class.objects().update_one.assert_called_once_with(**{"$set": {"field": "value"}})
        mock_document_class.objects().first.assert_called_once()

        self.assertEqual(result, "updated_document")

    def test_update_embeded_document_many(self):
        mock_document_class = MagicMock()

        mock_update_result = MagicMock()
        mock_document_class.objects.return_value.update.return_value = mock_update_result
        mock_document_class.objects.return_value.return_value = ["updated_doc1", "updated_doc2"]

        result = self.db_manager.update_embeded_document(
            db_name="test_db",
            document_class=mock_document_class,
            filters={"_id": "123"},
            update={"$set": {"field": "value"}},
            many=True,
        )

        self.assertEqual(mock_document_class.objects.call_count, 2)
        mock_document_class.objects.assert_any_call(_id="123")
        mock_document_class.objects().update.assert_called_once_with(**{"$set": {"field": "value"}})

        self.assertEqual(result, mock_document_class.objects())

    @patch("omni.pro.database.mongo.UpdateOne")
    def test_batch_upsert(self, mock_update_one):
        mock_document_instance = MagicMock()
        mock_collection = mock_document_instance._get_collection.return_value

        data = {
            "context": {"tenant": "tenant_code", "user": "user_name"},
            "models": [{"external_id": "1", "field": "value1"}, {"external_id": "2", "field": "value2"}],
        }

        self.db_manager.batch_upsert(mock_document_instance, data)

        mock_update_one.assert_any_call(
            {"external_id": "1"},
            {"$set": {"external_id": "1", "field": "value1", "tenant": "tenant_code", "updated_by": "user_name"}},
            upsert=True,
        )
        mock_update_one.assert_any_call(
            {"external_id": "2"},
            {"$set": {"external_id": "2", "field": "value2", "tenant": "tenant_code", "updated_by": "user_name"}},
            upsert=True,
        )

        mock_collection.bulk_write.assert_called_once()

    @patch.object(DatabaseManager, "remove_document_relations")
    @patch.object(DatabaseManager, "add_document_relations")
    def test_add_or_remove_document_relations(self, mock_add_relations, mock_remove_relations):
        existent_relations = [MagicMock(code="relation1"), MagicMock(code="relation2")]
        new_relations = [{"code": "relation2"}, {"code": "relation3"}]

        result = self.db_manager.add_or_remove_document_relations(
            context={},
            document=MagicMock(),
            exsitent_relations_list=existent_relations,
            new_relations_list=new_relations,
            attribute_search="code",
            request_context={},
            element_name="Element",
            element_relation_name="Relation",
            multiple_params=False,
        )

        mock_remove_relations.assert_called_once_with(
            ANY,
            ANY,
            ["relation1"],
            existent_relations,
            "code",
            {},
            "Element",
            "Relation",
            False,
        )

        mock_add_relations.assert_called_once_with(
            ANY,
            ANY,
            ["relation3"],
            ANY,
            "code",
            {},
            "Element",
            "Relation",
            False,
        )

    @patch.object(DatabaseManager, "get_register")
    def test_remove_document_relations(self, mock_get_register):
        existent_relations = [MagicMock(code="relation1")]

        mock_get_register.return_value = existent_relations[0]

        result = self.db_manager.remove_document_relations(
            context={},
            document=MagicMock(),
            list_elements=["relation1"],
            list_registers=existent_relations,
            attribute_search="code",
            request_context={},
            element_name="Element",
            element_relation_name="Relation",
            multiple_params=False,
        )

        self.assertEqual(result, [])

        mock_get_register.assert_called_once_with("code", {}, ANY, "relation1", {}, False)

    @patch.object(DatabaseManager, "get_register")
    def test_add_document_relations(self, mock_get_register):
        mock_register1 = MagicMock()
        mock_register2 = MagicMock()

        def side_effect_func(attribute_search, context, document, element, request_context, multiple_params):
            if element == "relation1":
                return mock_register1
            elif element == "relation2":
                return mock_register2
            return None

        mock_get_register.side_effect = side_effect_func

        existent_relations = [mock_register1]

        new_relations = ["relation2"]

        result = self.db_manager.add_document_relations(
            context={},
            document=MagicMock(),
            list_elements=new_relations,
            list_registers=existent_relations,
            attribute_search="id",
            request_context={},
            element_name="Element",
            element_relation_name="Relation",
            multiple_params=False,
        )

        self.assertIn(mock_register2, result)
        mock_get_register.assert_any_call("id", {}, ANY, "relation2", {}, False)

    @patch.object(DatabaseManager, "get_register")
    def test_add_document_relations_already_exists(self, mock_get_register):
        mock_register = MagicMock()
        mock_get_register.return_value = mock_register

        existent_relations = [mock_register]

        with self.assertRaises(AlreadyExistError):
            self.db_manager.add_document_relations(
                context={},
                document=MagicMock(),
                list_elements=["relation1"],
                list_registers=existent_relations,
                attribute_search="id",
                request_context={},
                element_name="Element",
                element_relation_name="Relation",
                multiple_params=False,
            )

    @patch.object(DatabaseManager, "get_register")
    def test_get_register(self, mock_get_register):
        mock_document = MagicMock()

        result = self.db_manager.get_register(
            attribute_search="id",
            context={},
            document=mock_document,
            element="relation1",
            request_context={"tenant": "tenant1"},
            multiple_params=False,
        )

        mock_get_register.assert_called_once_with(
            attribute_search="id",
            context={},
            document=mock_document,
            element="relation1",
            request_context={"tenant": "tenant1"},
            multiple_params=False,
        )


class TestMongoConnection(unittest.TestCase):

    @patch("mongoengine.connect")
    def test_connect(self, mock_connect):
        host = "localhost"
        port = 27017
        db = "test_db"
        username = "user"
        password = "password"
        complement = {"authSource": "admin"}

        mongo_conn = MongoConnection(host, port, db, username, password, complement)

        connection = mongo_conn.connect()

        mock_connect.assert_called_once_with(
            db=db, username=username, password=password, host="mongodb://localhost:27017/?authSource=admin"
        )

        self.assertEqual(connection, mock_connect.return_value)

    @patch("mongoengine.disconnect")
    def test_close(self, mock_disconnect):
        host = "localhost"
        port = 27017
        db = "test_db"
        username = "user"
        password = "password"
        complement = {"authSource": "admin"}

        mongo_conn = MongoConnection(host, port, db, username, password, complement)

        mongo_conn.close()

        mock_disconnect.assert_called_once()

    @patch("mongoengine.connect")
    @patch("mongoengine.disconnect")
    def test_context_manager(self, mock_disconnect, mock_connect):
        host = "localhost"
        port = 27017
        db = "test_db"
        username = "user"
        password = "password"
        complement = {"authSource": "admin"}

        with MongoConnection(host, port, db, username, password, complement) as mongo_conn:
            mock_connect.assert_called_once_with(
                db=db, username=username, password=password, host="mongodb://localhost:27017/?authSource=admin"
            )
            self.assertEqual(mongo_conn.db, db)

        mock_disconnect.assert_called_once()


class TestPolishNotationToMongoDB(unittest.TestCase):

    def test_single_comparison_operator(self):
        expression = [("age", "=", 30)]
        converter = PolishNotationToMongoDB(expression)
        result = converter.convert()
        expected = {"age": {"$eq": 30}}
        self.assertEqual(result, expected)

    def test_multiple_comparison_operator(self):
        expression = [("age", ">", 20), ("salary", "<", 5000)]
        converter = PolishNotationToMongoDB(expression)
        result = converter.convert()
        expected = {"$and": [{"salary": {"$lt": 5000}}, {"age": {"$gt": 20}}]}
        self.assertEqual(result, expected)

    def test_logical_operator_and(self):
        expression = ["and", ("age", ">", 20), ("salary", "<", 5000)]
        converter = PolishNotationToMongoDB(expression)
        result = converter.convert()
        expected = {"$and": [{"age": {"$gt": 20}}, {"salary": {"$lt": 5000}}]}
        self.assertEqual(result, expected)

    def test_logical_operator_or(self):
        expression = ["or", ("age", ">", 20), ("salary", "<", 5000)]
        converter = PolishNotationToMongoDB(expression)
        result = converter.convert()
        expected = {"$or": [{"age": {"$gt": 20}}, {"salary": {"$lt": 5000}}]}
        self.assertEqual(result, expected)

    def test_like_operator(self):
        expression = [("name", "like", "John")]
        converter = PolishNotationToMongoDB(expression)
        result = converter.convert()
        expected = {"name": {"$regex": "John", "$options": "i"}}
        self.assertEqual(result, expected)

    def test_nested_logical_operators(self):
        expression = ["or", ("age", ">", 30), ["and", ("name", "=", "John"), ("salary", ">", 5000)]]
        converter = PolishNotationToMongoDB(expression)
        result = converter.convert()
        expected = {"$or": [{"age": {"$gt": 30}}, {"$and": [{"name": {"$eq": "John"}}, {"salary": {"$gt": 5000}}]}]}
        self.assertEqual(result, expected)

    def test_invalid_operator(self):
        expression = [("age", "invalid_op", 30)]
        converter = PolishNotationToMongoDB(expression)
        with self.assertRaises(ValueError) as context:
            converter.convert()
        self.assertTrue("Unexpected operator: invalid_op" in str(context.exception))

    def test_invalid_token(self):
        expression = ["invalid_token"]
        converter = PolishNotationToMongoDB(expression)
        with self.assertRaises(ValueError) as context:
            converter.convert()
        self.assertTrue("Unexpected token: invalid_token" in str(context.exception))


class TestDBUtil(unittest.TestCase):

    def setUp(self):
        self.fields = MagicMock()
        self.fields.name_field = ["name", "age"]

        self.filter = MagicMock()
        self.filter.ListFields.return_value = [("some_field",)]
        self.filter.filter = '[("name", "=", "John")]'

        self.paginated = MagicMock()
        self.paginated.offset = 1
        self.paginated.limit = 20

        self.group_by = MagicMock()
        self.group_by.name_field = ["name"]

        self.sort_by = MagicMock()
        self.sort_by.name_field = "age"
        self.sort_by.type = base_pb2.SortBy.ASC

    def test_db_prepared_statement_with_id(self):
        id = "507f1f77bcf86cd799439011"
        self.filter.ListFields.return_value = [("id", "=", id)]
        self.filter.filter = f'[("id", "=", "{id}")]'

        result = DBUtil.db_prepared_statement(id, self.fields, self.filter, self.paginated, self.group_by, self.sort_by)

        expected_result = {
            "paginated": {"page": 1, "per_page": 20},
            "filter": {"_id": {"$eq": ObjectId(id)}},
            "group_by": ["name"],
            "sort_by": ["+age"],
            "fields": ["name", "age"],
            "str_filter": f'[("id", "=", "{id}")]',
        }

        self.assertEqual(result, expected_result)

    def test_db_prepared_statement_without_filters(self):
        id = None

        self.filter.ListFields.return_value = [("name", "=", "John")]
        self.filter.filter = '[("name", "=", "John")]'

        result = DBUtil.db_prepared_statement(id, self.fields, self.filter, self.paginated, self.group_by, self.sort_by)

        expected_result = {
            "paginated": {"page": 1, "per_page": 20},
            "filter": {"name": {"$eq": "John"}},
            "group_by": ["name"],
            "sort_by": ["+age"],
            "fields": ["name", "age"],
            "str_filter": '[("name", "=", "John")]',
        }

        self.assertEqual(result, expected_result)

    def test_db_prepared_statement_without_id(self):
        id = None
        result = DBUtil.db_prepared_statement(id, self.fields, self.filter, self.paginated, self.group_by, self.sort_by)

        expected_result = {
            "paginated": {"page": 1, "per_page": 20},
            "filter": {"name": {"$eq": "John"}},
            "group_by": ["name"],
            "sort_by": ["+age"],
            "fields": ["name", "age"],
            "str_filter": '[("name", "=", "John")]',
        }

        self.assertEqual(result, expected_result)

    def test_db_trans_sort_asc(self):
        result = DBUtil.db_trans_sort(self.sort_by)
        self.assertEqual(result, "+age")

    def test_db_trans_sort_desc(self):
        self.sort_by.type = base_pb2.SortBy.DESC
        result = DBUtil.db_trans_sort(self.sort_by)
        self.assertEqual(result, "-age")


if __name__ == "__main__":
    unittest.main()
