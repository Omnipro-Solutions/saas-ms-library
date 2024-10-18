import re
from datetime import datetime
from decimal import Decimal
from enum import Enum

from bson import ObjectId
from google.protobuf.timestamp_pb2 import Timestamp
from mongoengine import (
    BooleanField,
    DateTimeField,
    Document,
    EmbeddedDocument,
    EmbeddedDocumentField,
    StringField,
    signals,
)
from omni.pro.airflow.actions import ActionToAirflow
from omni.pro.config import Config
from omni.pro.database.postgres import CustomSession
from omni.pro.database.sqlalchemy import mapped_column
from omni.pro.logger import configure_logger
from omni.pro.user.access import INTERNAL_USER
from omni.pro.util import measure_time
from omni_pro_grpc.common.base_pb2 import Context as ContextProto
from omni_pro_grpc.common.base_pb2 import Object as ObjectProto
from omni_pro_grpc.common.base_pb2 import ObjectAudit as AuditProto
from sqlalchemy import Boolean, DateTime, String, event, inspect
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, declared_attr
from sqlalchemy.orm.session import Session

_logger = configure_logger(__name__)


class BaseEmbeddedDocument(EmbeddedDocument):
    meta = {
        "abstract": True,
        "strict": False,
    }

    def to_proto(self, *args, **kwargs):
        raise NotImplementedError


class BaseObjectEmbeddedDocument(BaseEmbeddedDocument):
    code = StringField()
    code_name = StringField()
    meta = {
        "allow_inheritance": True,
    }

    def to_proto(self):
        return ObjectProto(
            code=self.code,
            code_name=self.code_name,
        )


class Audit(BaseEmbeddedDocument):
    created_at = DateTimeField(default=datetime.utcnow, is_importable=False)
    created_by = StringField(is_importable=False)
    updated_at = DateTimeField(default=datetime.utcnow, is_importable=False)
    updated_by = StringField(is_importable=False)
    deleted_at = DateTimeField(is_importable=False)
    deleted_by = StringField(is_importable=False)

    def to_proto(self) -> AuditProto:
        create_at_ts = Timestamp()
        create_at_ts.FromDatetime(self.created_at)
        update_at_ts = Timestamp()
        update_at_ts.FromDatetime(self.updated_at)
        return AuditProto(
            created_by=self.created_by,
            updated_by=self.updated_by,
            created_at=create_at_ts,
            updated_at=update_at_ts,
        )


class Context(BaseEmbeddedDocument):
    tenant = StringField(is_importable=False)
    user = StringField(is_importable=False)

    def to_proto(self) -> ContextProto:
        return ContextProto(
            tenant=self.tenant,
            user=self.user,
        )


class BaseDocument(Document):
    __is_replic_table__ = False

    context = EmbeddedDocumentField(Context)
    audit = EmbeddedDocumentField(Audit)
    active = BooleanField(default=True)
    external_id = StringField()

    meta = {
        "abstract": True,
        "strict": False,
    }

    def __init__(self, *args, **kwargs):
        super(BaseDocument, self).__init__(*args, **kwargs)
        if self.pk:
            self._initial_data = self.to_mongo().to_dict()
        else:
            self._initial_data = {}

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        signals.post_save.connect(cls.post_save, sender=cls)
        signals.post_delete.connect(cls.post_delete, sender=cls)

    @classmethod
    @property
    def db(cls):
        return cls._get_db()

    def generate_dict(self):
        result = self.to_mongo().to_dict()
        response = result.copy()
        for key, value in result.items():
            if isinstance(value, ObjectId):
                if key == "_id":
                    response.pop(key)
                    key = "id"
                response[key] = str(value)

        return response

    def save(self, *args, **kwargs):
        if not self.context:
            self.context = Context()
        if not self.audit:
            self.audit = Audit(created_by=self.context.user)
        self.audit.updated_by = self.context.user
        self.audit.updated_at = datetime.utcnow()
        return super().save(*args, **kwargs)

    def update(self, **kwargs):
        res = super().update(**kwargs)
        if kwargs and isinstance(kwargs, dict):
            self.validate_change_fields(set(kwargs.keys()))
        return res

    def to_proto(self, *args, **kwargs):
        raise NotImplementedError

    @classmethod
    def reference_list(cls):
        return [cls]

    @classmethod
    @measure_time
    def post_save(cls, sender, document, **kwargs):
        if Config.PROCESS_WEBHOOK:  # Ignore if the process webhook is disabled
            if document.__is_replic_table__:  # Ignore replic tables
                return
            # identify if the object is a new instance or an existing one
            if kwargs.get("created", False):
                document.assign_crud_attrs_to_stack("create")
            else:
                document.validate_change_fields()
        return

    @classmethod
    @measure_time
    def post_delete(cls, sender, document, **kwargs):
        if Config.PROCESS_WEBHOOK:  # Ignore if the process webhook is disabled
            if document.__is_replic_table__:  # Ignore replic tables
                return
            document.assign_crud_attrs_to_stack("delete")
            # ActionToAirflow.send_to_airflow(
            #     cls,
            #     document,
            #     action="delete",
            #     context={"tenant": document.context.tenant, "user": document.context.user},
            # )
        return

    @classmethod
    def transform_mirror(cls, data: object):
        """
        Transform the data for the model instance.

        This method should be overridden in subclasses.

        """
        pass

    def assign_crud_attrs_to_stack(self, action: str, changed_fields: set = None):
        if not self._get_collection_name():
            _logger.debug("Collection is empty")
            _logger.debug(f"Instance id = {str(self.id)}")
            return
        model_name = self._get_collection_name()
        instance = self
        instance_id = str(instance.id)

        if not self.context:
            _logger.error("Context is not defined and CRUD attributes cannot be assigned to the stack.")
            return

        if action == "update" and hasattr(instance, "updated_attrs"):
            if changed_fields:
                instance.updated_attrs["tenant"] = self.context.tenant
                if not model_name in instance.updated_attrs:
                    instance.updated_attrs[model_name] = {}
                if not instance_id in instance.updated_attrs[model_name]:
                    instance.updated_attrs[model_name][instance_id] = set()
                instance.updated_attrs[model_name][instance_id] = (
                    instance.updated_attrs[model_name][instance_id] | changed_fields
                )
        elif action == "create" and hasattr(instance, "created_attrs"):
            instance.created_attrs["tenant"] = self.context.tenant
            if not model_name in instance.created_attrs:
                instance.created_attrs[model_name] = []
            instance.created_attrs[model_name].append(instance_id)
        elif action == "delete" and hasattr(instance, "deleted_attrs"):
            instance.deleted_attrs["tenant"] = self.context.tenant
            if not model_name in instance.deleted_attrs:
                instance.deleted_attrs[model_name] = []
            instance.deleted_attrs[model_name].append(instance_id)

    def validate_change_fields(self, changed_fields_in_update={}):
        other_changed_fields = self._detect_other_changed_fields()
        changed_fields = set(self._changed_fields) | set(other_changed_fields) | set(changed_fields_in_update)
        if changed_fields:
            self.assign_crud_attrs_to_stack("update", changed_fields)

    def _detect_other_changed_fields(self):
        changes = []
        updated_data = self.to_mongo().to_dict()
        for field_name, field_type in self._fields.items():
            if field_name in ["context", "audit", "created_attrs", "updated_attrs", "deleted_attrs"]:
                continue
            original_value = self._initial_data.get(field_name)
            updated_value = updated_data.get(field_name)

            if isinstance(original_value, dict) and isinstance(updated_value, dict):
                changed_keys = {
                    key
                    for key in set(original_value) | set(updated_value)
                    if original_value.get(key) != updated_value.get(key)
                }
                for key in changed_keys:
                    changes.append(f"{field_name}.{key}")

        return set(changes)


class BaseAuditEmbeddedDocument(BaseEmbeddedDocument):
    context = EmbeddedDocumentField(Context)
    audit = EmbeddedDocumentField(Audit)
    active = BooleanField(default=True)
    external_id = StringField()

    meta = {
        "abstract": True,
        "strict": False,
    }

    # TODO: Add a method to update the audit fields
    def save(self, *args, **kwargs):
        if not self.context:
            self.context = Context()
        if not self.audit:
            self.audit = Audit(created_by=self.context.user)
        self.audit.updated_by = self.context.user
        self.audit.updated_at = datetime.utcnow()
        return super().save(*args, **kwargs)


BaseAuditContextEmbeddedDocument = BaseAuditEmbeddedDocument


def set_created_by(context):
    if hasattr(context, "get_current_parameters"):
        params = context.get_current_parameters()
        if params.get("created_by") is None:
            return params.get("updated_by")
        return params.get("created_by")
    return INTERNAL_USER


class Base:
    """
    Base class provides foundational attributes and methods for database models.
    It includes common attributes such as 'id', 'active', and timestamp fields.
    It also provides methods for converting the model to its proto representation.
    """

    __is_replic_table__ = False
    __max_depth__ = 0
    __properties__ = []

    @staticmethod
    def _camel_to_snake(name):
        """
        Convert a CamelCase string to snake_case.

        Args:
            name (str): The CamelCase string.

        Returns:
            str: The converted snake_case string.
        """
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()

    @declared_attr
    def __tablename__(cls):
        """
        Generate a table name based on the class name.

        Returns:
            str: The table name in snake_case format.
        """
        return cls._camel_to_snake(cls.__name__)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, is_importable=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    external_id: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    tenant: Mapped[str] = mapped_column(String(30), nullable=False, is_importable=False)
    created_by: Mapped[str] = mapped_column(String(50), default=set_created_by, nullable=False, is_importable=False)
    updated_by: Mapped[str] = mapped_column(String(50), nullable=False, is_importable=False)
    deleted_by: Mapped[str] = mapped_column(String(50), nullable=True, is_importable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now, nullable=False, is_importable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False, is_importable=False
    )
    deleted_at: Mapped[datetime] = mapped_column(DateTime(), nullable=True, is_importable=False)

    def model_to_dict(self, depth=None, properties=None):
        """
        Convierte un modelo SQLAlchemy a un dict, incluyendo propiedades y relaciones
        hasta un nivel de profundidad especificado.

        Parameters:
            depth: Nivel de profundidad para relaciones.
            properties: Lista de nombres de propiedades para incluir.

        Returns:
            Un diccionario que representa al modelo.
        """
        # Primero, obtenemos los campos simples
        data = {}
        for col in inspect(self).mapper.column_attrs:
            col_val = getattr(self, col.key)
            if isinstance(col_val, Enum):
                data[col.key] = col_val.name
            elif isinstance(col_val, Decimal):
                data[col.key] = float(col_val)
            else:
                data[col.key] = col_val

        depth = self.__max_depth__ if depth == None else depth
        properties = properties or self.__properties__
        if depth > 0:
            # Ahora manejamos las relaciones, si depth > 0
            for relation in inspect(self).mapper.relationships:
                value = getattr(self, relation.key)
                if value is None:
                    data[relation.key] = None
                elif relation.uselist:  # es una relación de tipo lista
                    data[relation.key] = [item.model_to_dict(depth=depth - 1) for item in value]
                else:  # es una relación de uno a uno
                    data[relation.key] = value.model_to_dict(depth=depth - 1)

        # Incluir propiedades si se especifica
        for prop_name in properties:
            if hasattr(self, prop_name):
                prop_value = getattr(self, prop_name)
                data[prop_name] = prop_value

        return data

    def create(self, session):
        """
        Add the current instance to the provided database session and flushes the session.

        Parameters:
        - session (Session): An instance of a database session, likely from SQLAlchemy.

        Returns:
        - self: Returns the instance after adding it to the session.

        Usage:
        instance = Base()
        instance.create(session)
        """
        session.add(self)
        session.flush()
        return self

    @classmethod
    def bulk_insert(cls, session: Session, items: list[dict], field_name: str = None, field_value=None):
        session.bulk_insert_mappings(cls, items)
        session.flush()
        if field_name and hasattr(cls, field_name):
            field_attr = getattr(cls, field_name)
            return session.query(cls).filter(field_attr == field_value).all()
        return []

    @classmethod
    def bulk_update(cls, session: Session, items: list[dict], field_name: str = None, field_value=None):
        session.bulk_update_mappings(cls, items)
        session.flush()
        if field_name and hasattr(cls, field_name):
            field_attr = getattr(cls, field_name)
            return session.query(cls).filter(field_attr == field_value).all()
        return []

    def update(self, session):
        """
        Flush the changes made to the current instance to the database through the provided session.

        This function assumes that the instance has been already added to the session or
        is being tracked by the session. The function will flush changes without committing them,
        allowing for further operations before a final commit.

        Parameters:
        - session (Session): An instance of a database session, likely from SQLAlchemy.

        Usage:
        instance.attribute = new_value
        instance.update(session)
        """
        session.flush()
        session.refresh(self)

    def delete(self, session):
        """
        Attempts to delete the current instance from the database using the provided session.
        Intenta eliminar la instancia actual de la base de datos usando la sesión proporcionada.

        Parameters:
        - session (Session): An instance of a database session, likely from SQLAlchemy.
        - sesión (Session): Una instancia de una sesión de base de datos, probablemente de SQLAlchemy.

        Returns:
        - bool: True if the instance is marked for deletion without errors, False otherwise.
        - bool: True si la instancia se marca para eliminación sin errores, False en caso contrario.

        Usage/Uso:
        success = instance.delete(session)
        éxito = instancia.delete(sesión)
        """
        try:
            session.delete(self)
            return True
        except SQLAlchemyError as e:
            return False

    def to_proto(self) -> AuditProto:
        """
        Convert the model instance to its proto representation.

        Returns:
            AuditProto: The proto representation of the model.
        """
        create_at_ts = Timestamp()
        create_at_ts.FromDatetime(self.created_at)
        update_at_ts = Timestamp()
        update_at_ts.FromDatetime(self.updated_at)
        audit_proto = AuditProto(
            created_by=self.created_by,
            updated_by=self.updated_by,
            created_at=create_at_ts,
            updated_at=update_at_ts,
        )
        if self.deleted_at:
            deleted_at_ts = Timestamp()
            deleted_at_ts.FromDatetime(self.deleted_at)
            audit_proto.deleted_at = deleted_at_ts

        return audit_proto

    def sync_data(self, *args, **kwargs):
        """
        Synchronize the data for the model instance.

        This method should be overridden in subclasses.

        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """
        raise NotImplementedError

    def get_or_sync(self, *args, **kwargs):
        """
        Retrieve or synchronize the data for the model instance.

        This method should be overridden in subclasses.

        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """
        raise NotImplementedError

    def get_document_info(self, *args, **kwargs):
        """
        Retrieve document-related information for the model instance.

        This method should be overridden in subclasses.

        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """
        raise NotImplementedError

    @classmethod
    def transform_mirror(cls, data: object):
        """
        Transform the data for the model instance.

        This method should be overridden in subclasses.

        """
        pass

    def assign_crud_attrs_to_session(self, action: str):
        """
        Assigns CRUD attributes to the current session based on the action performed on an instance.

        This method updates the `updated_attrs`, `created_attrs`, or `deleted_attrs` dictionaries in the
        current session based on the specified action (create, update, delete). It tracks the changes made
        to an instance and stores the modified fields or instance IDs in the appropriate attribute dictionary.

        Parameters:

            action (str): The CRUD action performed. It can be "create", "update", or "delete".
            **kwargs: Additional keyword arguments containing the fields that were modified during an update action.

        Behavior:
            - For "update" actions:
                - Identifies the modified fields using the instance's attribute history.
                - Updates the `updated_attrs` dictionary in the session with the modified fields for the instance.
            - For "create" actions:
                - Adds the instance ID to the `created_attrs` dictionary in the session.
            - For "delete" actions:
                - Adds the instance ID to the `deleted_attrs` dictionary in the session.

        Additional Details:
            - If the session's `context` is not set, it initializes the context with tenant and user information.
            - Uses SQLAlchemy's `inspect` function to access the instance's state and attribute history.


        """
        mapper = inspect(self).mapper
        instance = self
        model_name = mapper.mapped_table.name
        state = inspect(instance)
        instance_id = instance.id

        session: CustomSession = Session.object_session(instance)
        if hasattr(session, "context") and not session.context:
            session.context = {"tenant": instance.tenant, "user": instance.updated_by}

        if not self._can_write_crud_attrs(mapper):
            return

        if action == "update" and hasattr(session, "updated_attrs"):
            modified_fields = set([f"{attr.key}" for attr in state.attrs if attr.history.has_changes()])
            if modified_fields:
                if not model_name in session.updated_attrs:
                    session.updated_attrs[model_name] = {}
                if not instance_id in session.updated_attrs[model_name]:
                    session.updated_attrs[model_name][instance_id] = set()
                session.updated_attrs[model_name][instance_id] = (
                    session.updated_attrs[model_name][instance_id] | modified_fields
                )
        elif action == "create" and hasattr(session, "created_attrs"):
            if not model_name in session.created_attrs:
                session.created_attrs[model_name] = []
            session.created_attrs[model_name].append(instance_id)
        elif action == "delete" and hasattr(session, "deleted_attrs"):
            if not model_name in session.deleted_attrs:
                session.deleted_attrs[model_name] = []
            session.deleted_attrs[model_name].append(instance_id)

    def _can_write_crud_attrs(self, mapper) -> bool:
        table_name = mapper.mapped_table.name
        can_write = True
        if table_name == "sale" and hasattr(self, "client_id") and not self.client_id:
            can_write = False
        return can_write

    @classmethod
    def dt_to_ts(cls, dt) -> Timestamp:
        """
        Convert a datetime object to a Timestamp object.

        Parameters:
            dt (datetime): The datetime object to convert.

        Returns:
            Timestamp: The converted Timestamp object.
        """
        return (t := Timestamp(), t.FromDatetime(dt))[0] if dt else None


BaseModel = declarative_base(cls=Base)


# Definir un evento que escuche a todos los modelos que heredan de Base
@event.listens_for(BaseModel, "after_insert", propagate=True)
@measure_time
def post_save(mapper, connection, target):
    if Config.PROCESS_WEBHOOK:  # Ignore if the process webhook is disabled
        if target.__is_replic_table__:  # Ignore replic tables
            return
        target.assign_crud_attrs_to_session("create")
        # ActionToAirflow.send_to_airflow(
        #     mapper, target, "create", context={"tenant": target.tenant, "user": target.updated_by}
        # )
    return


@event.listens_for(BaseModel, "after_update", propagate=True)
@measure_time
def post_update(mapper, connection, target):
    if Config.PROCESS_WEBHOOK:  # Ignore if the process webhook is disabled
        if target.__is_replic_table__:  # Ignore replic tables
            return
        target.assign_crud_attrs_to_session("update")
        # ActionToAirflow.send_to_airflow(
        #     mapper, target, "update", context={"tenant": target.tenant, "user": target.updated_by}
        # )
    return


@event.listens_for(BaseModel, "after_delete", propagate=True)
@measure_time
def post_delete(mapper, connection, target):
    if Config.PROCESS_WEBHOOK:  # Ignore if the process webhook is disabled
        if target.__is_replic_table__:  # Ignore replic tables
            return
        target.assign_crud_attrs_to_session("delete")
        # ActionToAirflow.send_to_airflow(
        #     mapper, target, "delete", context={"tenant": target.tenant, "user": target.updated_by}
        # )
    return
