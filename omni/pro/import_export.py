from datetime import datetime
from sqlalchemy import text
from importlib import import_module


class ImportExportBase:
    def get_model(self, model_path):
        module_path, class_name = model_path.rsplit(".", 1)
        module = import_module(module_path)
        return getattr(module, class_name)


class QueryExport(ImportExportBase):
    def __init__(self, context: dict):
        self.context = context
        self.db_types = {
            "SQL": self.get_data_sql,
            "NO_SQL": self.get_data_no_sql,
        }
        self.db_type = "NO_SQL" if not hasattr(self.context, "pg_manager") else "SQL"

    def get_data(self, model_path, fields, context):
        model = self.get_model(model_path)
        return self.db_types[self.db_type](model, model_path, fields, context)

    def get_data_no_sql(self, model, model_path, fields, context):
        exclude = {"_id" if key == "id" else key: False for key in set(model._fields.keys()) - set(fields)}
        db = model.db
        cursor = db[model_path.split(".")[2].lower()].find({"tenant": context["tenant"]}, projection=exclude)
        result = list(cursor)
        return result

    def get_data_sql(self, model, model_path, fields, context):
        sql_query = text(f"SELECT {','.join(fields)} FROM {model.__tablename__} WHERE tenant = '{context['tenant']}'")
        result = self.context.pg_manager.Session.execute(sql_query)
        return self._serialize_query_result(result)

    def _serialize_query_result(self, result):
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
        if isinstance(o, datetime):
            return o.isoformat()

        return o


class BatchUpsert(ImportExportBase):
    def __init__(self, context: dict):
        self.context = context
        self.db_types = {
            "SQL": self.upsert_data_sql,
            "NO_SQL": self.upsert_data_no_sql,
        }
        self.db_type = "NO_SQL" if not hasattr(self.context, "pg_manager") else "SQL"

    def upsert_data(self, data):
        model = self.get_model(data["model_path"])
        return self.db_types[self.db_type](model, data)

    def upsert_data_no_sql(self, model, data):
        self.context.db_manager.batch_upsert(model, data)

    def upsert_data_sql(self, model, data):
        self.context.pg_manager.batch_upsert(model, self.context.pg_manager.Session, data)
