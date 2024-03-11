from importlib import import_module
from omni_pro_base.util import nested


class MirrorModelBase:
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

    def create_mirror_model(self, data):
        """
        Creates a mirror model based on the specified data.

        Args:
            data (dict): The data used to create the mirror model.

        Returns:
            The created mirror model.
        """
        raise NotImplementedError

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
        raise NotImplementedError

    def read_mirror_model(self, data):
        """
        Reads the mirror model based on the provided data.

        Args:
            data (dict): The data containing the model path and other necessary information.

        Returns:
            The result of the read operation.

        Raises:
            KeyError: If the provided database type is not supported.
        """
        raise NotImplementedError

    def delete_mirror_model(self, data):
        """
        Deletes the mirror model based on the provided data.

        Args:
            data (dict): The data containing the model path and other necessary information.

        Returns:
            The result of the delete operation.

        Raises:
            KeyError: If the provided database type is not supported.
        """
        raise NotImplementedError


class MirrorModelSQL(MirrorModelBase):

    def __init__(self, context: dict, model_path: str):
        """
        Initializes a new instance of the MirrorModel class.

        Args:
            context (dict): The context dictionary containing the necessary information.

        Attributes:
            context (dict): The context dictionary containing the necessary information.
            db_type (str): The type of database, either "NO_SQL" or "SQL".
        """
        self.context = context
        self.model = self.get_model(model_path)

    def create_mirror_model(self, data):
        """
        Creates a new record in the mirror model using the provided data.

        Args:
            model (str): The name of the mirror model.
            data (dict): The data to be used for creating the new record.

        Returns:
            object: The newly created record.

        """
        return self.context.pg_manager.create_new_record(self.model, self.context.pg_manager.Session, **data)

    def update_mirror_model(self, data):
        """
        Updates the mirror model in the SQL database.

        Args:
            model (str): The name of the model to update.
            data (dict): The data to update the model with.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        return self.context.pg_manager.update_record(self.model, self.context.pg_manager.Session, data.pop("id"), data)

    def read_mirror_model(self, data):
        """
        Reads the mirror model from the SQL database.

        Args:
            model (str): The name of the model to read.
            data (dict): The data to read the model with.

        Returns:
            bool: True if the read was successful, False otherwise.
        """
        return self.context.pg_manager.retrieve_record(
            self.model,
            self.context.pg_manager.Session,
            filters=data.get("filter"),
        )


class MirrorModelNoSQL(MirrorModelBase):
    def __init__(self, context: dict, model_path: str):
        """
        Initializes a new instance of the MirrorModel class.

        Args:
            context (dict): The context dictionary containing the necessary information.

        Attributes:
            context (dict): The context dictionary containing the necessary information.
            db_type (str): The type of database, either "NO_SQL" or "SQL".
        """
        self.context = context
        self.model = self.get_model(model_path)

    def create_mirror_model(self, data):
        """
        Creates a mirror model without using SQL.

        Args:
            model (str): The model name.
            data (dict): The data to be used for creating the mirror model.

        Returns:
            object: The created mirror model.

        """
        return self.context.db_manager.create_document(None, self.model, **data)

    def update_mirror_model(sel, data):
        """
        Update the mirror model without using SQL.

        Args:
            model (str): The name of the model.
            data (dict): The data to update the model with.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        return self.context.db_manager.update_document(None, self.model, **data)

    def read_mirror_model(self, data):
        """
        Reads the mirror model without using SQL.

        Args:
            model (str): The name of the model.
            data (dict): The data to read the model with.

        Returns:
            bool: True if the read was successful, False otherwise.
        """

        return self.context.db_manager.get_document(
            None, nested(data, "context.tenant"), self.model, data.get("filter")
        )

    def delete_mirror_model(self, data):
        """
        Deletes the mirror model without using SQL.

        Args:
            model (str): The name of the model.
            data (dict): The data to delete the model with.

        Returns:
            bool: True if the delete was successful, False otherwise.
        """
        return self.context.db_manager.delete_document(None, self.model, **data)


def mirror_factory(context, model_path: str):
    return (
        MirrorModelNoSQL(context, model_path)
        if not hasattr(context, "pg_manager")
        else MirrorModelSQL(context, model_path)
    )
