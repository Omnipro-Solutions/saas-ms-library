from importlib import import_module
from itertools import groupby
from pathlib import Path
from datetime import datetime
import newrelic.agent
from bson import ObjectId
from marshmallow import ValidationError
from omni.pro.database import DBUtil
from omni.pro.decorators import resources_decorator
from omni.pro.exceptions import handle_error
from omni.pro.logger import LoggerTraceback, configure_logger
from omni.pro.redis import RedisManager
from omni.pro.response import MessageResponse
from omni.pro.stack import ExitStackDocument
from omni.pro.util import Resource, convert_model_alchemy_to_struct, convert_model_mongo_to_struct
from omni_pro_base.config import Config
from omni_pro_base.microservice import MicroService as MicroServiceEnum
from omni_pro_base.util import nested
from omni_pro_grpc.grpc_function import EventRPCFucntion, MethodRPCFunction, ModelRPCFucntion, WebhookRPCFucntion
from omni_pro_grpc.util import MessageToDict, to_list_value
from omni_pro_grpc.v1.utilities import mirror_model_pb2, mirror_model_pb2_grpc
from pymongo import DeleteOne, InsertOne, UpdateOne
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError, OperationalError

logger = configure_logger(__name__)


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

    def __init__(self, context: dict, model_path: str, tenant: str, user: str):
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
        self.tenant = tenant
        self.user = user

    def create_mirror_model(self, data):
        """
        Creates a new record in the mirror model using the provided data.

        Args:
            model (str): The name of the mirror model.
            data (dict): The data to be used for creating the new record.

        Returns:
            object: The newly created record.

        """
        mapper = inspect(self.model)
        filters = {}
        for column in mapper.columns:
            if column.unique and hasattr(column, "field_aliasing") and column.name in data["model_data"]:
                filters[column.name] = data["model_data"][column.name]
        if filters and (
            mdl := self.context.pg_manager.retrieve_record(self.model, self.context.pg_manager.Session, filters)
        ):
            return mdl
        self.model.transform_mirror(data["model_data"])
        audit = {"tenant": nested(data, "context.tenant"), "updated_by": nested(data, "context.user")}
        return self.context.pg_manager.create_new_record(
            self.model, self.context.pg_manager.Session, **data["model_data"] | audit
        )

    def multi_create_mirror_model(self, items: list):
        """
        Creates a new record in the mirror model using the provided data.

        Args:
            model (str): The name of the mirror model.
            items (list): The data to be used for creating the new record.

        Returns:
            object: The newly created record.

        """
        bulk_create_items = []
        unique_field_aliasing = self._get_unique_field_aliasing()

        if self.tenant and unique_field_aliasing:
            instance_ids_by_unique_field_aliasing = self._get_doc_ids_by_unique_field_aliasing(
                items, unique_field_aliasing
            )

            for item in items:
                unique_field_aliasing_value = item.get(unique_field_aliasing)
                instance_id = instance_ids_by_unique_field_aliasing.get(unique_field_aliasing_value)
                if instance_id:
                    continue
                self.model.transform_mirror(item)
                bulk_create_items.append(item)

        if bulk_create_items:
            self.model.bulk_insert(session=self.context.pg_manager.Session, items=bulk_create_items)

    def update_mirror_model(self, data):
        """
        Updates the mirror model in the SQL database.

        Args:
            model (str): The name of the model to update.
            data (dict): The data to update the model with.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        mdl = self.context.pg_manager.retrieve_record_by_id(
            self.model, self.context.pg_manager.Session, data["model_data"]["id"] or 0
        )
        if not mdl:
            data["model_data"].pop("id")
            return self.create_mirror_model(data)
        self.model.transform_mirror(data["model_data"])
        audit = {"tenant": nested(data, "context.tenant"), "updated_by": nested(data, "context.user")}
        return self.context.pg_manager.update_record(
            self.model, self.context.pg_manager.Session, nested(data, "model_data.id"), data["model_data"] | audit
        )

    def multi_update_mirror_model(self, items: list):
        """
        Updates the mirror model in the SQL database.

        Args:
            model (str): The name of the model to update.
            items (list): The data to update the model with.

        Returns:
            bool: True if the update was successful, False otherwise.
        """

        bulk_update_items = []
        bulk_create_items = []
        unique_field_aliasing = self._get_unique_field_aliasing()

        if self.tenant and unique_field_aliasing:
            instance_ids_by_unique_field_aliasing = self._get_doc_ids_by_unique_field_aliasing(
                items, unique_field_aliasing
            )
            self._convert_fields_to_db_types(items)
            for item in items:
                unique_field_aliasing_value = item.get(unique_field_aliasing)
                instance_id = instance_ids_by_unique_field_aliasing.get(unique_field_aliasing_value)
                self.model.transform_mirror(item)
                if not instance_id:
                    if "id" in item:
                        item.pop("id")
                    bulk_create_items.append(item)
                else:
                    item["id"] = instance_id
                    bulk_update_items.append(item)

            if bulk_update_items:
                self.model.bulk_update(self.context.pg_manager.Session, items=bulk_update_items)

            if bulk_create_items:
                self.model.bulk_insert(session=self.context.pg_manager.Session, items=bulk_create_items)

        else:
            raise Exception(f"tenant or unique_field_aliasing is not defined")

    def _convert_fields_to_db_types(self, items: list[dict]):
        field_type_by_name = {}
        mapper = inspect(self.model)
        for column in mapper.columns:
            column_type = str(column.type)
            if column_type in ["INTEGER"]:
                field_type_by_name[column.name] = column_type
        for item in items:
            for field_name, field_type in field_type_by_name.items():
                if field_name in item and field_type == "INTEGER":
                    field_value = item[field_name]
                    item[field_name] = int(field_value)

    def _get_doc_ids_by_unique_field_aliasing(self, items: list[dict], unique_field_aliasing: str):
        unique_field_aliasing_ids = [
            item.get(unique_field_aliasing) for item in items if item.get(unique_field_aliasing)
        ]
        if unique_field_aliasing_ids:
            instances = (
                self.context.pg_manager.Session.query(self.model)
                .filter(
                    self.model.tenant == self.tenant,
                    getattr(self.model, unique_field_aliasing).in_(unique_field_aliasing_ids),
                )
                .all()
            )
            return {
                getattr(instance, unique_field_aliasing): instance.id
                for instance in instances
                if hasattr(instance, unique_field_aliasing)
            }
        return {}

    def _get_unique_field_aliasing(self):
        code_field_aliasing = None
        mapper = inspect(self.model)
        for column in mapper.columns:
            if column.unique and hasattr(column, "field_aliasing") and column.name:
                if column.field_aliasing == "id":
                    return column.name
                elif column.field_aliasing == "code":
                    code_field_aliasing = column.name

        return code_field_aliasing

    def read_mirror_model(self, data):
        """
        Reads the mirror model from the SQL database.

        Args:
            model (str): The name of the model to read.
            data (dict): The data to read the model with.

        Returns:
            bool: True if the read was successful, False otherwise.
        """
        return self.context.pg_manager.list_records(
            self.model,
            self.context.pg_manager.Session,
            data.id,
            data.fields,
            data.filter,
            data.group_by,
            data.sort_by,
            data.paginated,
        )


class MirrorModelNoSQL(MirrorModelBase):
    def __init__(self, context: dict, model_path: str, tenant: str, user: str):
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
        self.tenant = tenant
        self.user = user

    def create_mirror_model(self, data):
        """
        Creates a mirror model using NO_SQL.

        Args:
            model (str): The model name.
            data (dict): The data to be used for creating the mirror model.

        Returns:
            object: The created mirror model.

        """
        filters = {}
        for field_key, field in self.model._fields.items():
            if field.unique and hasattr(field, "field_aliasing") and field.db_field in data["model_data"]:
                filters[field_key] = data["model_data"][field_key]
        if filters and (
            doc := self.context.db_manager.get_document(None, data["context"]["tenant"], self.model, **filters)
        ):
            return doc
        self.model.transform_mirror(data["model_data"])
        data["model_data"]["context"] = data["context"]
        return self.context.db_manager.create_document(None, self.model, **data["model_data"])

    def multi_create_mirror_model(self, items: list):
        """
        Creates a mirror model using NO_SQL.

        Args:
            model (str): The model name.
            items (list): The data to be used for creating the mirror model.

        Returns:
            object: The created mirror model.

        """
        bulk_create_items = []
        doc_ids_by_unique_field_aliasing = {}

        unique_field_aliasing = self._get_unique_field_aliasing()

        if self.tenant and unique_field_aliasing:
            doc_ids_by_unique_field_aliasing = self._get_doc_ids_by_unique_field_aliasing(items, unique_field_aliasing)

            for item in items:
                item: dict
                unique_field_aliasing_value = item.get(unique_field_aliasing)
                doc_id = doc_ids_by_unique_field_aliasing.get(unique_field_aliasing_value)
                if doc_id:
                    continue
                self.model.transform_mirror(item)
                bulk_create_items.append(InsertOne(item))

            if bulk_create_items:
                self.model._get_collection().bulk_write(bulk_create_items, ordered=False)
        else:
            raise Exception(f"tenant or unique_field_aliasing is not defined")

    def update_mirror_model(self, data):
        """
        Update the mirror model using NO_SQL.

        Args:
            model (str): The name of the model.
            data (dict): The data to update the model with.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        data["model_data"]["context"] = data["context"]
        doc = self.context.db_manager.get_document(
            None, data["context"]["tenant"], self.model, id=data["model_data"]["id"]
        )
        if not doc:
            data["model_data"].pop("id")
            return self.create_mirror_model(data)
        logger.info(f"Updating mirror model {self.model} with data {data['model_data']}")
        self.model.transform_mirror(data["model_data"])
        return self.context.db_manager.update_document(None, self.model, **data["model_data"])

    def multi_update_mirror_model(self, items: list):
        """
        Update the mirror model using NO_SQL.

        Args:
            model (str): The name of the model.
            items (list): The data to update the model with.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        bulk_write_items = []
        bulk_create_items = []
        items_create = []
        unique_field_aliasing = self._get_unique_field_aliasing()

        if self.tenant and unique_field_aliasing:
            doc_ids_by_unique_field_aliasing = self._get_doc_ids_by_unique_field_aliasing(items, unique_field_aliasing)
            self._convert_fields_to_db_types(items)
            for item in items:
                item: dict
                unique_field_aliasing_value = item.get(unique_field_aliasing)
                doc_id = doc_ids_by_unique_field_aliasing.get(unique_field_aliasing_value)
                self.model.transform_mirror(item)
                utcnow = datetime.utcnow
                item["audit"] = {
                    "created_at": datetime.utcnow(),
                    "created_by": self.user,
                    "updated_at": datetime.utcnow(),
                    "updated_by": self.user,
                }

                if not doc_id:
                    if "id" in item:
                        item.pop("id")
                    bulk_create_items.append(InsertOne(item))
                else:
                    bulk_write_items.append(UpdateOne({"_id": doc_id}, {"$set": item}))

            if bulk_write_items:
                result = self.model._get_collection().bulk_write(bulk_write_items, ordered=False)

            if bulk_create_items:
                self.model._get_collection().bulk_write(bulk_create_items, ordered=False)
        else:
            raise Exception(f"tenant or unique_field_aliasing is not defined")

    def _convert_fields_to_db_types(self, items: list[dict]):
        field_type_by_name = {}
        for field_name in self.model._fields:
            field = self.model._fields.get(field_name)
            field_type = field.__class__.__name__
            if field_type in ["ReferenceField", "IntField"]:
                field_type_by_name[field_name] = field_type

        for item in items:
            for field_name, field_type in field_type_by_name.items():
                if field_name in item:
                    field_value = item[field_name]
                    if field_type == "ReferenceField":
                        item[field_name] = ObjectId(field_value)
                    elif field_type == "IntField":
                        item[field_name] = int(field_value)

    def _get_doc_ids_by_unique_field_aliasing(self, items: list[dict], unique_field_aliasing: str):
        unique_field_aliasing_ids = [
            item.get(unique_field_aliasing) for item in items if item.get(unique_field_aliasing)
        ]
        if unique_field_aliasing_ids:
            filter_criteria = {f"{unique_field_aliasing}__in": unique_field_aliasing_ids}
            return {
                getattr(doc, unique_field_aliasing): doc.id
                for doc in self.model.objects(**filter_criteria, context__tenant=self.tenant)
                if hasattr(doc, unique_field_aliasing)
            }
        return {}

    def _get_unique_field_aliasing(self):
        code_field_aliasing = None
        for field_key, field in self.model._fields.items():
            if field.unique and hasattr(field, "field_aliasing") and field.db_field:
                if field.field_aliasing == "id":
                    return field.db_field
                elif field.field_aliasing == "code":
                    code_field_aliasing = field.db_field
        return code_field_aliasing

    def read_mirror_model(self, tenant, data):
        """
        Reads the mirror model using SQL.

        Args:
            model (str): The name of the model.
            data (dict): The data to read the model with.

        Returns:
            bool: True if the read was successful, False otherwise.
        """

        return self.context.db_manager.list_documents(None, tenant, self.model, **data)

    def delete_mirror_model(self, data):
        """
        Deletes the mirror model without using SQL.

        Args:
            model (str): The name of the model.
            data (dict): The data to delete the model with.

        Returns:
            bool: True if the delete was successful, False otherwise.
        """
        return self.context.db_manager.delete_document(None, self.model, **data["model_data"])

    def multi_delete_mirror_model(self, items: list):
        """
        Deletes the mirror model without using SQL.

        Args:
            model (str): The name of the model.
            data (dict): The data to delete the model with.

        Returns:
            bool: True if the delete was successful, False otherwise.
        """
        bulk_operations = []
        for data in items:
            bulk_operations.append(DeleteOne({"_id": ObjectId(data["id"])}))

        if bulk_operations:
            result = self.model._get_collection().bulk_write(bulk_operations, ordered=False)
            return result
        return None


def mirror_factory(context, model_path: str, tenant: str = "", user: str = ""):
    return (
        MirrorModelNoSQL(context, model_path, tenant, user)
        if not hasattr(context, "pg_manager")
        else MirrorModelSQL(context, model_path, tenant, user)
    )


class MirrorModelServiceMongo(mirror_model_pb2_grpc.MirrorModelServiceServicer):
    def __init__(self, path: Path):
        localdir = path / "locales"
        # self._ = set_language(localedir=localdir)
        super().__init__()

    @newrelic.agent.function_trace()
    @resources_decorator([Resource.MONGODB])
    def CreateMirrorModel(
        self, request: mirror_model_pb2.CreateOrUpdateMirrorModelRequest, context
    ) -> mirror_model_pb2.CreateOrUpdateCreateMirrorResponse:
        message_response = MessageResponse(mirror_model_pb2.CreateOrUpdateCreateMirrorResponse)
        try:
            data = MessageToDict(request)
            base = mirror_factory(context, data.pop("model_path"))
            with ExitStackDocument(
                document_classes=base.model.reference_list(),
                db_alias=context.db_name,
            ):
                data = MessageToDict(request)
                result = base.create_mirror_model(data)

                return message_response.created_response(
                    message="Mirror model created successfully", model_data=convert_model_mongo_to_struct(result)
                )

        except Exception as e:
            LoggerTraceback.error("Mirro model create exception", e, logger)
            return message_response.internal_response(message="Mirror model not created")

    @newrelic.agent.function_trace()
    @resources_decorator([Resource.MONGODB])
    def UpdateMirrorModel(
        self, request: mirror_model_pb2.CreateOrUpdateMirrorModelRequest, context
    ) -> mirror_model_pb2.CreateOrUpdateCreateMirrorResponse:
        message_response = MessageResponse(mirror_model_pb2.CreateOrUpdateCreateMirrorResponse)
        try:
            data = MessageToDict(request)
            base = mirror_factory(context, data.pop("model_path"))
            with ExitStackDocument(
                document_classes=base.model.reference_list(),
                db_alias=context.db_name,
            ):
                result = base.update_mirror_model(data)

                return message_response.updated_response(
                    message="Mirror updated successfully",
                    model_data=convert_model_mongo_to_struct(result),
                )

        except Exception as e:
            LoggerTraceback.error("Mirror model update exception", e, logger)
            return message_response.internal_response(message="Mirror model not updated")

    @newrelic.agent.function_trace()
    @resources_decorator([Resource.MONGODB])
    def ReadMirrorModel(
        self, request: mirror_model_pb2.ReadMirrorModelRequest, context
    ) -> mirror_model_pb2.ReadMirrorModelResponse:
        message_response = MessageResponse(mirror_model_pb2.ReadMirrorModelResponse)
        try:

            base = mirror_factory(context, request.model_path)
            with ExitStackDocument(
                document_classes=base.model.reference_list(),
                db_alias=context.db_name,
            ):
                data = DBUtil.db_prepared_statement(
                    request.id, request.fields, request.filter, request.paginated, None, request.sort_by
                )
                result = base.read_mirror_model(request.context.tenant, data)
                return message_response.created_response(
                    message="Mirror model read successfully",
                    mirror_models=to_list_value([mirror_model.generate_dict() for mirror_model in result[0]]),
                )

        except Exception as e:
            LoggerTraceback.error("Mirror model read exception", e, logger)
            return message_response.internal_response(message="Mirror model not read")

    @newrelic.agent.function_trace()
    @resources_decorator([Resource.MONGODB])
    def MultiCreateMirrorModel(
        self, request: mirror_model_pb2.MultiCreateOrMultiUpdateMirrorModelRequest, context
    ) -> mirror_model_pb2.MultiCreateOrMultiUpdateMirrorModelResponse:
        message_response = MessageResponse(mirror_model_pb2.MultiCreateOrMultiUpdateMirrorModelResponse)
        try:
            data = MessageToDict(request)
            base = mirror_factory(context, data.pop("model_path"), request.context.tenant, request.context.user)
            with ExitStackDocument(
                document_classes=base.model.reference_list(),
                db_alias=context.db_name,
            ):

                result = base.multi_create_mirror_model(data.get("data"))

                return message_response.created_response(
                    message="Mirror model created successfully", model_data=convert_model_mongo_to_struct(result)
                )

        except Exception as e:
            LoggerTraceback.error("Mirror model create exception", e, logger)
            return message_response.internal_response(message="Mirror model not created")

    @newrelic.agent.function_trace()
    @resources_decorator([Resource.MONGODB])
    def MultiUpdateMirrorModel(
        self, request: mirror_model_pb2.MultiCreateOrMultiUpdateMirrorModelRequest, context
    ) -> mirror_model_pb2.MultiCreateOrMultiUpdateMirrorModelResponse:
        message_response = MessageResponse(mirror_model_pb2.MultiCreateOrMultiUpdateMirrorModelResponse)
        try:
            data = MessageToDict(request)
            base = mirror_factory(context, data.pop("model_path"), request.context.tenant, request.context.user)
            with ExitStackDocument(
                document_classes=base.model.reference_list(),
                db_alias=context.db_name,
            ):

                result = base.multi_update_mirror_model(data.get("data"))

                return message_response.updated_response(
                    message="Mirror updated successfully",
                    # model_data=convert_model_mongo_to_struct(result),
                )

        except Exception as e:
            LoggerTraceback.error("Mirror model update exception", e, logger)
            return message_response.internal_response(message="Mirror model not updated")

    @newrelic.agent.function_trace()
    @resources_decorator([Resource.MONGODB])
    def MultiDeleteMirrorModel(
        self, request: mirror_model_pb2.MultiDeleteMirrorModelRequest, context
    ) -> mirror_model_pb2.CreateOrUpdateCreateMirrorResponse:
        message_response = MessageResponse(mirror_model_pb2.CreateOrUpdateCreateMirrorResponse)
        try:
            data = MessageToDict(request)
            base = mirror_factory(context, data.pop("model_path"), request.context.tenant, request.context.user)
            with ExitStackDocument(
                document_classes=base.model.reference_list(),
                db_alias=context.db_name,
            ):
                result = base.multi_delete_mirror_model(data)

                return message_response.updated_response(
                    message="Mirror updated successfully",
                    # model_data=convert_model_mongo_to_struct(result),
                )

        except Exception as e:
            LoggerTraceback.error("Mirror model update exception", e, logger)
            return message_response.internal_response(message="Mirror model not updated")


class MirrorModelServicePostgres(mirror_model_pb2_grpc.MirrorModelServiceServicer):

    def __init__(self, path: Path):
        localdir = path / "locales"
        # self._ = set_language(localedir=localdir)
        super().__init__()

    @newrelic.agent.function_trace()
    @resources_decorator([Resource.POSTGRES])
    def CreateMirrorModel(
        self, request: mirror_model_pb2.CreateOrUpdateMirrorModelRequest, context
    ) -> mirror_model_pb2.CreateOrUpdateCreateMirrorResponse:
        message_response = MessageResponse(mirror_model_pb2.CreateOrUpdateCreateMirrorResponse)
        try:
            with context.pg_manager as session:
                data = MessageToDict(request)
                result = mirror_factory(context, data.pop("model_path")).create_mirror_model(data)

                return message_response.created_response(
                    message="Mirror model created successfully", model_data=convert_model_alchemy_to_struct(result)
                )

        except (IntegrityError, ValidationError, OperationalError, Exception) as e:
            return handle_error("Mirror model", "Created", logger, e, message_response)

    @newrelic.agent.function_trace()
    @resources_decorator([Resource.POSTGRES])
    def UpdateMirrorModel(
        self, request: mirror_model_pb2.CreateOrUpdateMirrorModelRequest, context
    ) -> mirror_model_pb2.CreateOrUpdateCreateMirrorResponse:
        message_response = MessageResponse(mirror_model_pb2.CreateOrUpdateCreateMirrorResponse)
        try:
            with context.pg_manager as session:
                data = MessageToDict(request)
                result = mirror_factory(context, data.pop("model_path")).update_mirror_model(data)

                return message_response.updated_response(
                    message="Mirror updated successfully",
                    model_data=convert_model_alchemy_to_struct(result),
                )

        except (IntegrityError, ValidationError, OperationalError, Exception) as e:
            return handle_error("Mirror model", "Updated", logger, e, message_response)

    @newrelic.agent.function_trace()
    @resources_decorator([Resource.POSTGRES])
    def ReadMirrorModel(
        self, request: mirror_model_pb2.ReadMirrorModelRequest, context
    ) -> mirror_model_pb2.ReadMirrorModelResponse:
        message_response = MessageResponse(mirror_model_pb2.ReadMirrorModelResponse)
        try:
            with context.pg_manager as session:
                data = MessageToDict(request)
                result = mirror_factory(context, data.pop("model_path")).read_mirror_model(request)
                return message_response.created_response(
                    message="Mirror model read successfully",
                    mirror_models=to_list_value([mirror_model.model_to_dict() for mirror_model in result[0]]),
                )

        except (IntegrityError, ValidationError, OperationalError, Exception) as e:
            return handle_error("Mirror model", "Read", logger, e, message_response)

    @newrelic.agent.function_trace()
    @resources_decorator([Resource.POSTGRES])
    def MultiCreateMirrorModel(
        self, request: mirror_model_pb2.MultiCreateOrMultiUpdateMirrorModelRequest, context
    ) -> mirror_model_pb2.MultiCreateOrMultiUpdateMirrorModelResponse:
        message_response = MessageResponse(mirror_model_pb2.MultiCreateOrMultiUpdateMirrorModelResponse)
        try:
            with context.pg_manager as session:
                data = MessageToDict(request)
                result = mirror_factory(
                    context, data.pop("model_path"), request.context.tenant, request.context.user
                ).multi_create_mirror_model(data.get("data"))

                return message_response.created_response(
                    message="Mirror model created successfully",
                    # model_data=convert_model_alchemy_to_struct(result)
                )

        except (IntegrityError, ValidationError, OperationalError, Exception) as e:
            return handle_error("Mirror model", "Created", logger, e, message_response)

    @newrelic.agent.function_trace()
    @resources_decorator([Resource.POSTGRES])
    def MultiUpdateMirrorModel(
        self, request: mirror_model_pb2.MultiCreateOrMultiUpdateMirrorModelRequest, context
    ) -> mirror_model_pb2.MultiCreateOrMultiUpdateMirrorModelResponse:
        message_response = MessageResponse(mirror_model_pb2.MultiCreateOrMultiUpdateMirrorModelResponse)
        try:
            with context.pg_manager as session:
                data = MessageToDict(request)

                result = mirror_factory(
                    context, data.pop("model_path"), request.context.tenant, request.context.user
                ).multi_update_mirror_model(data.get("data"))

                return message_response.updated_response(
                    message="Mirror updated successfully",
                    # model_data=convert_model_alchemy_to_struct(result),
                )

        except (IntegrityError, ValidationError, OperationalError, Exception) as e:
            return handle_error("Mirror model", "Updated", logger, e, message_response)


class MirroModelWebhookRegister(object):

    @classmethod
    def create_or_update_webhook_by_mirror(cls, context: dict, params: dict):
        """
        Create or update a webhook based on the mirror model.

        Args:
            context (dict): The context dictionary.
            params (dict): The parameters dictionary.

        Returns:
            tuple: A tuple containing the response, success flag, and event.
        """
        rpc = WebhookRPCFucntion(context=context)
        filters = params.pop("filter", {})
        resp, success, _e = rpc.read_webhook(filters)
        if success:
            data = params.pop("data")
            if resp.webhooks:
                if len(resp.webhooks) == 1:
                    webhook = resp.webhooks[0]
                    data["events"] = [{"id": x for x in data.pop("event_ids")}]
                    data["method_grpc"] = {"id": data.pop("method_grpc_id")}
                    return rpc.update_webhook({"webhook": data | {"id": webhook.id}})
            else:
                return rpc.create_webhook(data)
        return resp, success, _e

    @classmethod
    def register(cls, context: dict):
        """
        Register method that processes mirror models and creates webhooks for events.

        Args:
            cls: The class object.
            context (dict): The context dictionary.

        Returns:
            None

        Raises:
            Exception: If there is an error creating the webhook.

        """
        dags = {
            "picking": "Signal_Event_Picking",
            "quant": "Signal_Event_Quants",
            MicroServiceEnum.SAAS_MS_CATALOG.value: "Signal_Event_Catalog",
            MicroServiceEnum.SAAS_MS_SALE.value: "Signal_Event_Sale",
        }
        all_models_resp = ModelRPCFucntion(context=context).read_model(
            params={
                "paginated": {
                    "offset": 1,
                    "limit": 1000,
                },
                "sort_by": {"name_field": "code", "type": "ASC"},
            }
        )

        grouped_by_code = {key: list(group) for key, group in groupby(all_models_resp[0].models, key=lambda x: x.code)}
        method_index = {
            "create": "MirrorModelService.CreateMirrorModel",
            "update": "MirrorModelService.UpdateMirrorModel",
            "delete": "MirrorModelService.DeleteMirrorModel",
        }
        method_resp = MethodRPCFunction(context=context).read_method_rpc(
            params={"filter": {"filter": f"[('class_name', '=','MirrorModelServiceStub')]"}}
        )
        # Procesar cada grupo
        method_micro_op_idx = {}
        for method in method_resp[0].method_grpcs:
            action = None
            for key, value in method_index.items():
                if value in method.code:
                    action = key
                    break
            if action:
                # key = f"{method.microservice.code}-{action}"
                method_micro_op_idx[action] = method.id

        for code, models in grouped_by_code.items():
            original = next((model for model in models if model.is_replic.value == False), None)
            replicas = [model for model in models if model.is_replic.value == True]

            if not replicas or not original:
                continue

            trigger_fields = set(
                [
                    f"{code}-{field.field_aliasing}"
                    for model in replicas
                    for field in model.fields
                    if field.field_aliasing
                ]
            )
            if not trigger_fields:
                continue

            event_resp = EventRPCFucntion(context=context).read_event(
                params={
                    "filter": {"filter": f"[('code', 'in', {[code + '_create', code + '_update', code + '_delete']})]"}
                }
            )
            dag_id = dags.get(code)
            if not dag_id:
                dag_id = dags.get(original.microservice) or "Signal_Event"

            for event in event_resp[0].events:
                # if not (method_grpc := method_micro_op_idx.get(f"{original.microservice}-{event.operation}")):
                #     continue
                method_grpc = method_micro_op_idx.get(event.operation)
                name = event.name + "-Mirror"
                data = {
                    "name": name,
                    "method": "post",
                    "format": "json",
                    "type_webhook": "internal",
                    "protocol": "grpc",
                    "python_code": "__result__ = True",
                    "trigger_fields": list(trigger_fields),
                    "dag_id": dag_id,
                    "headers": {},
                    "event_ids": [event.id],
                    "method_grpc_id": method_grpc,
                    "auth_type": "no_auth",
                }
                resp = cls.create_or_update_webhook_by_mirror(
                    context=context,
                    params={
                        "filter": {"filter": {"filter": f"[('name', '=', '{name}')]"}},
                        "data": data,
                    },
                )
                if not resp[1]:
                    raise Exception(f"{resp[0]}-{resp[2]}")

    @classmethod
    def run(cls, pattern="*", exlcudes_keys=["SETTINGS"]) -> None:
        redis_manager = RedisManager(
            host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, redis_ssl=Config.REDIS_SSL
        )
        tenans = redis_manager.get_tenant_codes(pattern=pattern, exlcudes_keys=exlcudes_keys)
        for tenant in tenans:
            user = redis_manager.get_user_admin(tenant)
            context = {
                "tenant": tenant,
                "user": user.get("id") or "admin",
            }
            cls.register(context=context)
