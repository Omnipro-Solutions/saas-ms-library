import ast
import json

import redis
from bson import ObjectId
from mongoengine import register_connection
from mongoengine.context_managers import switch_db
from omni.pro.logger import configure_logger
from omni.pro.protos.common import base_pb2
from omni.pro.util import nested

logger = configure_logger(name=__name__)


class DatabaseManager(object):
    def __init__(self, host: str, port: int, user: str, password: str, complement: dict) -> None:
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
        register_connection(
            alias="default",
            db="default",
            host=host,
            port=int(port),
            username=user,
            password=password,
            **complement,
        )
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.complement = complement
        self.connections = {}

    def get_db_alias(self, db_name: str) -> str:
        return f"db_{db_name}"

    def connect_to_database(self, db_name: str) -> str:
        db_alias = self.get_db_alias(db_name)

        if db_alias not in self.connections:
            register_connection(
                alias=db_alias,
                db=db_name,
                host=self.host,
                port=int(self.port),
                username=self.user,
                password=self.password,
                **self.complement,
            )
            self.connections[db_alias] = True

        return db_alias

    def create_document(self, db_name: str, document_class, **kwargs) -> object:
        db_alias = self.connect_to_database(db_name)

        with switch_db(document_class, db_alias) as DocumentAlias:
            document = DocumentAlias(**kwargs)
            document.save()

        return document

    def get_document(self, db_name: str, tenant: str, document_class, **kwargs) -> object:
        db_alias = self.connect_to_database(db_name)

        with switch_db(document_class, db_alias) as DocumentAlias:
            document = DocumentAlias.objects(**kwargs, context__tenant=tenant).first()

        return document

    def update_document(self, db_name: str, document_class, id: str, **kwargs) -> object:
        db_alias = self.connect_to_database(db_name)

        with switch_db(document_class, db_alias) as DocumentAlias:
            document = DocumentAlias.objects(id=id).first()
            DocumentAlias.objects(id=document.id).update_one(**kwargs)
            document.reload()

        return document

    def delete_document(self, db_name: str, document_class, id: str) -> object:
        db_alias = self.connect_to_database(db_name)

        with switch_db(document_class, db_alias) as DocumentAlias:
            document = DocumentAlias.objects(id=id).first()
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
        db_alias = self.connect_to_database(db_name)

        with switch_db(document_class, db_alias) as DocumentAlias:
            # Filter documents based on criteria provided
            if filter:
                query_set = DocumentAlias.objects(context__tenant=tenant).filter(__raw__=filter)
            else:
                query_set = DocumentAlias.objects(context__tenant=tenant)

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
        db_alias = self.connect_to_database(db_name)
        with switch_db(document_class, db_alias) as DocumentAlias:
            document = DocumentAlias.objects(**kwargs).delete()

        return document

    def update_list_element(
        self, db_name: str, document_class, filters: dict, update: dict, many: bool = False
    ) -> object:
        db_alias = self.connect_to_database(db_name)
        with switch_db(document_class, db_alias) as DocumentAlias:
            if many:
                document = DocumentAlias.objects(**filters).update_many(**update)
            document = DocumentAlias.objects(**filters).update_one(**update)

        return document


class RedisConnection:
    def __init__(self, host: str, port: int, db: int) -> None:
        self.host = host
        self.port = int(port)
        self.db = db

    def __enter__(self) -> redis.StrictRedis:
        self.redis_client = redis.StrictRedis(host=self.host, port=self.port, db=self.db, decode_responses=True)
        return self.redis_client

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.redis_client.close()


class RedisManager(object):
    def __init__(self, host: str, port: int, db: int) -> None:
        self.host = host
        self.port = int(port)
        self.db = db
        self._connection = RedisConnection(host=self.host, port=self.port, db=self.db)

    def get_connection(self) -> RedisConnection:
        return self._connection

    def set_connection(self, connection: RedisConnection) -> None:
        self._connection = connection

    def set_json(self, key, json_obj):
        with self.get_connection() as rc:
            if isinstance(json_obj, str):
                json_obj = json.loads(json_obj)
            return rc.json().set(key, "$", json_obj)

    def get_json(self, key):
        with self.get_connection() as rc:
            return rc.json().get(key)

    def get_resource_config(self, service_id: str, tenant_code: str) -> dict:
        config = self.get_json(tenant_code)
        logger.info(f"Redis config", extra={"deb_config": config})
        return {
            **nested(config, f"resources.{service_id}", {}),
            **nested(config, "aws", {}),
        }

    def get_aws_cognito_config(self, service_id: str, tenant_code: str) -> dict:
        config = self.get_resource_config(service_id, tenant_code)
        return {
            "region_name": nested(config, "aws.cognito.region"),
            "aws_access_key_id": config.get("aws_access_key_id"),
            "aws_secret_access_key": config.get("aws_secret_access_key"),
            "user_pool_id": nested(config, "aws.cognito.user_pool_id"),
        }

    def get_mongodb_config(self, service_id: str, tenant_code: str) -> dict:
        config = self.get_resource_config(service_id, tenant_code)
        return {
            "host": nested(config, "dbs.mongodb.host"),
            "port": nested(config, "dbs.mongodb.port"),
            "user": nested(config, "dbs.mongodb.user"),
            "password": nested(config, "dbs.mongodb.pass"),
            "name": nested(config, "dbs.mongodb.name"),
            "complement": nested(config, "dbs.mongodb.complement"),
        }

    connection = property(get_connection, set_connection)


class PolishNotationToMongoDB:
    def __init__(self, expression):
        self.expression = expression
        self.operators_logical = {"and": "$and", "or": "$or", "nor": "$nor", "not": "$not"}
        self.operators_comparison = {
            "=": "$eq",
            ">": "$gt",
            "<": "$lt",
            ">=": "$gte",
            "<=": "$lte",
            "in": "$in",
            "nin": "$nin",
            "!=": "$ne",
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
                    operand_stack.append({field: {self.operators_comparison[old_operator]: value}})
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
        prepared_statement["paginated"] = {"page": paginated.offset, "per_page": paginated.limit or 10}
        if (ft := filter.ListFields()) or id:
            expression = [("_id", "=", ObjectId(id or None))]
            if ft:
                str_filter = filter.filter.replace("true", "True").replace("false", "False")
                expression = ast.literal_eval(str_filter)
            filter_custom = PolishNotationToMongoDB(expression=expression).convert()
            prepared_statement["filter"] = filter_custom
        if group_by:
            prepared_statement["group_by"] = [x.name_field for x in group_by]
        if sort_by.ListFields():
            prepared_statement["sort_by"] = [cls.db_trans_sort(sort_by)]
        return prepared_statement

    @classmethod
    def db_trans_sort(cls, sort_by: base_pb2.SortBy) -> str:
        if not sort_by.name_field:
            return None
        return f"{'-' if sort_by.type == sort_by.DESC else '+'}{sort_by.name_field}"
