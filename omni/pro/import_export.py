from datetime import datetime
from importlib import import_module

from dateutil import parser
from sqlalchemy import inspect, text


class ImportExportBase:
    def get_model(self, model_path):
        """
        Dynamically imports and returns a class from a given module path.
        Parameters:
            model_path (str): The dot-separated path to the module and class (e.g., "module.submodule.ClassName").
        Returns: The class object referred to by model_path
        """
        module_path, class_name = model_path.rsplit(".", 1)
        module = import_module(module_path)
        return getattr(module, class_name)


class QueryExport(ImportExportBase):
    def __init__(self, context: dict):
        """
        Initializes the QueryExport instance.
        Parameters:
        context (dict): The context containing database connection information and other relevant settings.
        """
        self.context = context
        self.db_types = {
            "SQL": self.get_data_sql,
            "NO_SQL": self.get_data_no_sql,
        }
        self.db_type = "NO_SQL" if not hasattr(self.context, "pg_manager") else "SQL"

    def get_data(self, model_path, fields, date_init, date_finish, context):
        """
        Fetches data from the database (SQL or NoSQL) based on the provided model path, fields, and context.
        Parameters:
        model_path (str): The path to the model class.
        fields (list): A list of field names to be fetched.
        date_init(datetime): The start date for the query.
        date_finish(datetime): The end date for the query.
        context (dict): The context for the database operation.
        Returns: The fetched data.
        """
        model = self.get_model(model_path)
        return self.db_types[self.db_type](model, model_path, fields, date_init, date_finish, context)

    def parse_date(self, date):
        result = None
        try:
            result = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            result = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
        return parser.parse(result.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00"))

    def get_data_no_sql(self, model, model_path, fields, start_date, end_date, context):
        """
        Fetches data from a NoSQL database.
        Parameters:
        model: The model class for the NoSQL operation.
        model_path (str): The path to the model class.
        fields (list): A list of field names to be fetched.
        date_init(datetime): The start date for the query.
        date_finish(datetime): The end date for the query.
        context (dict): The context for the NoSQL database operation.
        Returns: Data retrieved from the NoSQL database.
        """
        exclude = {"_id" if key == "id" else key: False for key in set(model._fields.keys()) - set(fields)}
        db = model.db
        query_filter = {
            "context.tenant": context["tenant"],
            "audit.created_at": {
                "$gte": self.parse_date(start_date),
                "$lte": self.parse_date(end_date),
            },
        }
        cursor = db[model_path.split(".")[2].lower()].find(
            query_filter,
            projection=exclude,
        )
        result = list(cursor)
        return result

    def get_data_sql(self, model, model_path, fields, start_date, end_date, context):
        """
        Fetches data from a SQL database.
        Parameters:
        model (Type[Any]): The model class for the SQL operation.
        fields (List[str]): A list of field names to be fetched.
        start_date (datetime): The start date for the query.
        end_date (datetime): The end date for the query.
        context (Dict[str, Any]): The context for the SQL database operation.

        Returns:
        List[Dict[str, Any]]: Data retrieved from the SQL database.
        """

        inspector = inspect(model)
        foreign_keys = []
        related_fields = ["id", "name"]
        main_table = model.__tablename__
        main_table_fields = ", ".join([f"{main_table}.{field}" for field in fields])
        join_clauses = []
        related_table_fields = []

        for column in inspector.columns:
            if column.name in fields:
                for fk in column.foreign_keys:
                    target_class = fk.column.table.name.capitalize()
                    foreign_keys.append(
                        {
                            "column": column.name,
                            "target_class": str(target_class).lower(),
                        }
                    )

        # Create join clauses and related fields for foreign keys
        for fk in foreign_keys:
            related_table = fk["target_class"]
            join_clauses.append(f'LEFT JOIN "{related_table}" ON {main_table}.{fk["column"]} = {related_table}.id')
            for field in related_fields:
                alias = f"{related_table}_{field}"
                related_table_fields.append(f"{related_table}.{field} AS {alias}")

        # Build the SQL query
        sql_query = text(
            f"""
            SELECT {main_table_fields}{","+", ".join(related_table_fields ) if related_table_fields else ""}
            FROM "{main_table}"
            {" ".join(join_clauses)}
            WHERE {main_table}.tenant = :tenant
            AND {main_table}.created_at BETWEEN :start_date AND :end_date
            """
        )

        # Execute the query with parameters to avoid SQL injection
        result = self.context.pg_manager.Session.execute(
            sql_query,
            {
                "tenant": context["tenant"],
                "start_date": start_date,
                "end_date": end_date,
            },
        )

        return self._serialize_query_result(result)

    def _serialize_query_result(self, result):
        """
        Converts the result of a database query to a list of dictionaries.
        Parameters:
        result: The result object from the database query.
        Returns: A list of dictionaries representing the rows fetched from the database.
        """
        columns = [column[0] for column in result.cursor.description]

        fetched_results = result.fetchall()
        rows = [dict(zip(columns, row)) for row in fetched_results]
        if rows:
            for row in rows:
                for key, value in row.items():
                    if isinstance(value, datetime):
                        row[key] = self.datetime_to_string(value)
        return rows

    def datetime_to_string(self, o):
        """
        Converts a datetime object to an ISO formatted string.
        Parameters:
        o: The object to be converted.
        Returns: ISO formatted string if o is a datetime object; otherwise, returns o.
        """
        if isinstance(o, datetime):
            return o.isoformat()

        return o


class BatchUpsert(ImportExportBase):
    def __init__(self, context: dict):
        """
        Initializes the BatchUpsert instance.
        Parameters:
        context (dict): The context containing database connection information and other relevant settings.
        """
        self.context = context
        self.db_types = {
            "SQL": self.upsert_data_sql,
            "NO_SQL": self.upsert_data_no_sql,
        }
        self.db_type = "NO_SQL" if not hasattr(self.context, "pg_manager") else "SQL"

    def upsert_data(self, data):
        """
        Performs a batch upsert operation using the appropriate database method based on the context.
        Parameters:
        data (dict): The data to be upserted.
        Returns: The result of the upsert operation.
        """
        model = self.get_model(data["model_path"])
        return self.db_types[self.db_type](model, data)

    def upsert_data_no_sql(self, model, data):
        """
        Handles the batch upsert operation in a NoSQL database.
        Parameters:
        model: The model class for the NoSQL operation.
        data (dict): The data to be upserted.
        Returns: The result of the NoSQL upsert operation.
        """
        return self.context.db_manager.batch_upsert(model, data)

    def upsert_data_sql(self, model, data):
        """
        Handles the batch upsert operation in a SQL database.
        Parameters:
        model: The model class for the SQL operation.
        data (dict): The data to be upserted.
        Returns: The result of the SQL upsert operation.
        """
        return self.context.pg_manager.batch_upsert(model, self.context.pg_manager.Session, data)
