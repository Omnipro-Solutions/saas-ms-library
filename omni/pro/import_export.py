from importlib import import_module


class QueryExport:
    def __init__(self, context: dict, db_type):
        self.context = context
        self.db_types = {
            "mongo": self.get_data_no_sql,
            "sql": self.get_data_sql,
        }
        self.db_type = db_type

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
        pass

    def get_model(self, model_path):
        module_path, class_name = model_path.rsplit(".", 1)
        module = import_module(module_path)
        return getattr(module, class_name)
