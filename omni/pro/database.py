import ast
import json
import time

import mongoengine as mongo
import redis
from bson import ObjectId
from mongoengine import register_connection
from mongoengine.context_managers import switch_db
from omni.pro.logger import configure_logger
from omni.pro.protos.common import base_pb2
from omni.pro.util import nested
from peewee import PostgresqlDatabase

logger = configure_logger(name=__name__)


def measure_time(function):
    def measured_function(*args, **kwargs):
        start = time.time()
        c = function(*args, **kwargs)
        logger.info(f"Func: {str(function.__qualname__)} - Time: {time.time() - start}")
        return c

    return measured_function


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

    @measure_time
    def create_document(self, db_name: str, document_class, **kwargs) -> object:
        # with self.get_connection() as cnn:
        document = document_class(**kwargs)
        document.save()
        return document

    @measure_time
    def get_document(self, db_name: str, tenant: str, document_class, **kwargs) -> object:
        # with self.get_connection() as cnn:
        document = document_class.objects(**kwargs, context__tenant=tenant).first()
        # document.to_proto()
        return document

    @measure_time
    def update_document(self, db_name: str, document_class, id: str, **kwargs) -> object:
        # with self.get_connection() as cnn:
        document = document_class.objects(id=id).first()
        document_class.objects(id=document.id).update_one(**kwargs)
        document.reload()
        return document

    @measure_time
    def update(self, document_instance, **kwargs):
        # with self.get_connection() as cnn:
        document_instance.update(**kwargs)
        document_instance.reload()
        return document_instance

    @measure_time
    def delete(self, document_instance):
        # with self.get_connection() as cnn:
        document_instance.delete()
        return document_instance

    @measure_time
    def delete_document(self, db_name: str, document_class, id: str) -> object:
        # with self.get_connection() as cnn:
        document = document_class.objects(id=id).first()
        document.delete()
        return document

    @measure_time
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
        # with self.get_connection() as cnn:
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

    @measure_time
    def delete_documents(self, db_name, document_class, **kwargs):
        # with self.get_connection() as cnn:
        document = document_class.objects(**kwargs).delete()
        return document

    @measure_time
    def update_embeded_document(
        self, db_name: str, document_class, filters: dict, update: dict, many: bool = False
    ) -> object:
        # with self.get_connection() as cnn:
        if many:
            document_class.objects(**filters).update(**update)
            document = document_class.objects(**filters)
        else:
            document_class.objects(**filters).update_one(**update)
            document = document_class.objects(**filters).first()
        return document


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
        self.host = f"mongodb://{host}:{port}/?{'&'.join([f'{k}={v}' for (k,v) in complement.items()])}"
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


class PostgresDatabaseManager:
    def __init__(self, name: str, host: str, port: str, user: str, password: str):
        self.name = name
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.connection = PostgresqlDatabase(
            database=self.name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )

    def get_db_connection(self):
        return self.connection

    def create_new_record(self, model, **kwargs):
        model._meta.database = self.connection
        with self.connection.atomic():
            if not model.table_exists():
                self.connection.create_tables([model])
            new_record = model(**kwargs)
            new_record.bind(self.connection)
            new_record.save()
        return new_record

    def retrieve_record(self, model, filters):
        model._meta.database = self.connection
        with self.connection.atomic():
            model.bind(self.connection)
            query = model.get_or_none(**filters)
        return query

    def retrieve_record_by_id(self, model, id):
        model._meta.database = self.connection
        with self.connection.atomic():
            model.bind(self.connection)
            query = model.get_by_id(id)
        return query

    def update_record(self, model, model_id, update_dict):
        model._meta.database = self.connection
        with self.connection.atomic():
            model.bind(self.connection)
            record = model.get_by_id(model_id)
            record.update(**update_dict).where(model.id == model_id).execute()
        return model.get_by_id(model_id)

    def delete_record_by_id(self, model, model_id):
        model._meta.database = self.connection
        with self.connection.atomic():
            model.bind(self.connection)
            record = model.get_by_id(model_id)
            query = record.delete_instance()
        return query


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

    def get_postgres_config(self, service_id: str, tenant_code: str) -> dict:
        config = self.get_resource_config(service_id, tenant_code)
        return {
            "host": nested(config, "dbs.postgres.host"),
            "port": nested(config, "dbs.postgres.port"),
            "user": nested(config, "dbs.postgres.user"),
            "password": nested(config, "dbs.postgres.pass"),
            "name": nested(config, "dbs.postgres.name"),
        }


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
            expression = [("_id", "=", cls.generate_object_id(id))]
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

    @classmethod
    def generate_object_id(cls, id=None):
        try:
            return ObjectId(id)
        except:
            return ObjectId(None)
