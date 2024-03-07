from datetime import datetime
from dateutil import parser
from sqlalchemy import text
from importlib import import_module


class MirrorModel(ImportExportBase):
    def __init__(self, context: dict):
        """
        Initializes a new instance of the MirrorModel class.

        Args:
            context (dict): The context dictionary containing the necessary information.

        Attributes:
            context (dict): The context dictionary containing the necessary information.
            db_type (str): The type of database, either "NO_SQL" or "SQL".
        """
        self.context = context
        self.db_type = "NO_SQL" if not hasattr(self.context, "pg_manager") else "SQL"

    def create_mirror_model(self, data):
        """
        Creates a mirror model based on the specified data.

        Args:
            data (dict): The data used to create the mirror model.

        Returns:
            The created mirror model.
        """
        db_types = {
            "SQL": self.create_mirror_model_sql,
            "NO_SQL": self.create_mirror_model_no_sql,
        }
        model = self.get_model(data["model_path"])
        return db_types[self.db_type](model, data)

    def update_mirror_model(self, data):
        """
        Updates the mirror model based on the provided data.

        Args:
            data (dict): The data containing the model path and other necessary information.

        Returns:
            The result of the update operation.

        Raises:
            KeyError: If the provided database type is not supported.
        """
        db_types = {
            "SQL": self.update_mirror_model_sql,
            "NO_SQL": self.update_mirror_model_no_sql,
        }
        model = self.get_model(data["model_path"])
        return db_types[self.db_type](model, data)

    def create_mirror_model_no_sql(self, model, data):
        """
        Creates a mirror model without using SQL.

        Args:
            model (str): The model name.
            data (dict): The data to be used for creating the mirror model.

        Returns:
            object: The created mirror model.

        """
        return self.context.db_manager.create_document(None, model, **data)

    def create_mirror_model_sql(self, model, data):
        """
        Creates a new record in the mirror model using the provided data.

        Args:
            model (str): The name of the mirror model.
            data (dict): The data to be used for creating the new record.

        Returns:
            object: The newly created record.

        """
        return self.context.pg_manager.create_new_record(model, self.context.pg_manager.Session, data)

    def update_mirror_model_no_sql(self, model, data):
        """
        Update the mirror model without using SQL.

        Args:
            model (str): The name of the model.
            data (dict): The data to update the model with.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        return self.context.db_manager.update_document(None, model, **data)

    def update_mirror_model_sql(self, model, data):
        """
        Updates the mirror model in the SQL database.

        Args:
            model (str): The name of the model to update.
            data (dict): The data to update the model with.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        return self.context.pg_manager.update_record(model, self.context.pg_manager.Session, data.pop("id"), data)
