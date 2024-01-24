import ast

import mongoengine as mongo
from bson import ObjectId
from omni.pro.protos.common import base_pb2
from pymongo import UpdateOne


class DatabaseManager(object):
    def __init__(self, host: str, port: int, db: str, user: str, password: str, complement: dict) -> None:
        """
        :param db_object: Database object
        Example:
            db_object = {
                "host":"mongo",
                "port":"27017",
                "user":"root",
                "password":"123456",
                "type":"write | read",
                "no_sql":"true",
                "complement":""
            }
        """
        self.db = db
        self.host = host
        self.port = port
        self.username = user
        self.password = password
        self.complement = complement
        # self.get_connection().connect()

    def get_connection(self):
        return MongoConnection(
            db=self.db,
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            complement=self.complement,
        )

    def create_document(self, db_name: str, document_class, **kwargs) -> object:
        document = document_class(**kwargs)
        document.save()
        return document

    def get_document(self, db_name: str, tenant: str, document_class, **kwargs) -> object:
        document = document_class.objects(**kwargs, context__tenant=tenant).first()
        # document.to_proto()
        return document

    def update_document(self, db_name: str, document_class, id: str, **kwargs) -> object:
        document = document_class.objects(id=id).first()
        document_class.objects(id=document.id).first().update(**kwargs)
        document.reload()
        return document

    def update(self, document_instance, **kwargs):
        document_instance.update(**kwargs)
        document_instance.reload()
        return document_instance

    def delete(self, document_instance):
        document_instance.delete()
        return document_instance

    def delete_document(self, db_name: str, document_class, id: str) -> object:
        document = document_class.objects(id=id).first()
        document.delete()
        return document

    def list_documents(
        self,
        db_name: str,
        tenant: str,
        document_class,
        fields: list = None,
        filter: dict = None,
        group_by: str = None,
        paginated: dict = None,
        sort_by: list = None,
    ) -> tuple[list, int]:
        """
        Parameters:
        fields (list): Optional list of fields to retrieve from the documents.
        filter (dict): Optional dictionary containing filter criteria for the query.
        group_by (str): Optional field to group results by.
        paginated (dict): Optional dictionary containing pagination information.
        sort_by (list): Optional list of fields to sort results by.

        Returns:
        list: A list of documents matching the specified criteria.
        """
        # Filter documents based on criteria provided

        if filter:
            query_set = document_class.objects(context__tenant=tenant).filter(__raw__=filter)
        else:
            query_set = document_class.objects(context__tenant=tenant)

        # Only retrieve specified fields
        if fields:
            query_set = query_set.only(*fields)

        # Group results by specified field
        if group_by:
            query_set = query_set.group_by(group_by)

        # Paginate results based on criteria provided
        if paginated:
            page = int(paginated.get("page") or 1)
            per_page = int(paginated.get("per_page") or 10)
            start = (page - 1) * per_page
            end = start + per_page
            query_set = query_set[start:end]

        # Sort results based on criteria provided
        if sort_by:
            query_set = query_set.order_by(*sort_by)

        # Return list of documents matching the specified criteria and total count of documents
        return list(query_set), query_set.count()

    def delete_documents(self, db_name, document_class, **kwargs):
        # with self.get_connection() as cnn:
        document = document_class.objects(**kwargs).delete()
        return document

    def update_embeded_document(
        self,
        db_name: str,
        document_class,
        filters: dict,
        update: dict,
        many: bool = False,
    ) -> object:
        # with self.get_connection() as cnn:
        if many:
            document_class.objects(**filters).update(**update)
            document = document_class.objects(**filters)
        else:
            document_class.objects(**filters).update_one(**update)
            document = document_class.objects(**filters).first()
        return document

    def batch_upsert(self, document_isntance, data):
        """
        Batch upserts a list of records into the database.
        Actualiza por lotes una lista de registros en la base de datos.

        Args:
            document_isntance(mongoengine.Document): The MongoEngine model to upsert into.
            data (list): A list of dictionaries containing the records to upsert.
        """

        bulk_operations = [
            UpdateOne(
                {"external_id": obj["external_id"]},
                {"$set": obj | {"tenant": data["context"]["tenant"], "updated_by": data["context"]["user"]}},
                upsert=True,
            )
            for obj in data["models"]
        ]

        result = document_isntance.bulk_write(bulk_operations)
        return result


class MongoConnection(object):
    """A MongoConnection class that can dynamically connect to a MongoDB database with MongoEngine and close the connection after each query.

    Args:
        host (str): The hostname or IP address of the MongoDB server.
        port (int): The port number of the MongoDB server.
        username (str): The username for the MongoDB database.
        password (str): The password for the MongoDB database.
        database (str): The name of the MongoDB database.
    """

    def __init__(self, host, port, db, username, password, complement):
        self.host = f"mongodb://{host}:{port}/?{'&'.join([f'{k}={v}' for (k, v) in complement.items()])}"
        self.port = port
        self.username = username
        self.password = password
        self.db = db

    def connect(self):
        """Connects to the MongoDB database.

        Returns:
            A MongoEngine connection object.
        """
        self.connection = mongo.connect(
            db=self.db,
            username=self.username,
            password=self.password,
            host=self.host,
        )
        return self.connection

    def close(self):
        """Closes the connection to the MongoDB database."""
        # self.connection.close()
        mongo.disconnect()

    def __enter__(self):
        """Enters a context manager.

        Returns:
            A MongoConnection object.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exits a context manager."""
        self.close()


class PolishNotationToMongoDB:
    def __init__(self, expression):
        self.expression = expression
        self.operators_logical = {
            "and": "$and",
            "or": "$or",
            "nor": "$nor",
            "not": "$not",
        }
        self.operators_comparison = {
            "=": "$eq",
            ">": "$gt",
            "<": "$lt",
            ">=": "$gte",
            "<=": "$lte",
            "in": "$in",
            "nin": "$nin",
            "!=": "$ne",
            "!like": "$not",
            "like": "$regex",
        }

    def is_logical_operator(self, token):
        if not isinstance(token, str):
            return False
        return token in self.operators_logical

    def is_comparison_operator(self, token):
        if not isinstance(token, str):
            return False
        return token in self.operators_comparison

    def is_tuple(self, token):
        return isinstance(token, tuple) and len(token) == 3

    def convert(self):
        operand_stack = []
        operator_stack = []

        for token in reversed(self.expression):
            if self.is_logical_operator(token):
                operator_stack.append(token)
            elif self.is_comparison_operator(token):
                operator_stack.append(token)
            elif self.is_tuple(token):
                field, old_operator, value = token
                if old_operator in self.operators_comparison:
                    options = {}
                    if old_operator == "like":
                        options = {"$options": "i"}
                    elif old_operator == "!like":
                        options = {
                            self.operators_comparison[old_operator]: {
                                "$regex": value,
                                "$options": "i",
                            }
                        }
                    operand_stack.append({field: {self.operators_comparison[old_operator]: value} | options})
                else:
                    raise ValueError(f"Unexpected operator: {old_operator}")
            else:
                raise ValueError(f"Unexpected token: {token}")

        while operator_stack:
            operator = operator_stack.pop()
            if operator in self.operators_logical:
                operands = []
                for _ in range(2):
                    operands.append(operand_stack.pop())
                operand_stack.append({self.operators_logical[operator]: operands})
            else:
                raise ValueError(f"Unexpected operator: {operator}")

        return operand_stack.pop()


class DBUtil(object):
    @classmethod
    def db_prepared_statement(
        cls,
        id: str,
        fields: base_pb2.Fields,
        filter: base_pb2.Filter,
        paginated: base_pb2.Paginated,
        group_by: base_pb2.GroupBy,
        sort_by: base_pb2.SortBy,
    ) -> dict:
        prepared_statement = {}
        prepared_statement["paginated"] = {
            "page": paginated.offset,
            "per_page": paginated.limit or 10,
        }
        if (ft := filter.ListFields()) or id:
            expression = [("_id", "=", cls.generate_object_id(id))]
            if ft:
                str_filter = filter.filter.replace("true", "True").replace("false", "False").replace("__", ".")
                expression = ast.literal_eval(str_filter)
                # reemplace filter id by _id and convert to ObjectId
                for idx, exp in enumerate(expression):
                    if isinstance(exp, tuple) and len(exp) == 3 and exp[0] == "id":
                        if type(exp[2]) == list:
                            expression[idx] = (
                                "_id",
                                exp[1],
                                [cls.generate_object_id(x) for x in exp[2]],
                            )
                            continue
                        expression[idx] = (
                            "_id",
                            exp[1],
                            cls.generate_object_id(exp[2]),
                        )
            filter_custom = PolishNotationToMongoDB(expression=expression).convert()
            prepared_statement["filter"] = filter_custom
        if group_by:
            prepared_statement["group_by"] = [x.name_field for x in group_by]
        if sort_by.ListFields():
            prepared_statement["sort_by"] = [cls.db_trans_sort(sort_by)]
        if fields:
            prepared_statement["fields"] = fields.name_field
        return prepared_statement

    @classmethod
    def db_trans_sort(cls, sort_by: base_pb2.SortBy) -> str:
        if not sort_by.name_field:
            return None
        return f"{'-' if sort_by.type == sort_by.DESC else '+'}{sort_by.name_field}"

    @classmethod
    def generate_object_id(cls, id=None):
        try:
            return ObjectId(id)
        except:
            return ObjectId(None)
