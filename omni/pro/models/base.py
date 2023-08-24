import re

from datetime import datetime

from google.protobuf.timestamp_pb2 import Timestamp
from mongoengine import BooleanField, DateTimeField, Document, EmbeddedDocument, EmbeddedDocumentField, StringField
from omni.pro.protos.common.base_pb2 import Context as ContextProto
from omni.pro.protos.common.base_pb2 import Object as ObjectProto
from omni.pro.protos.common.base_pb2 import ObjectAudit as AuditProto
from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Mapped, declarative_mixin, declared_attr, mapped_column, relationship


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
    created_at = DateTimeField(default=datetime.utcnow)
    created_by = StringField()
    updated_at = DateTimeField()
    updated_by = StringField()
    deleted_at = DateTimeField()
    deleted_by = StringField()

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
    tenant = StringField()
    user = StringField()

    def to_proto(self) -> ContextProto:
        return ContextProto(
            tenant=self.tenant,
            user=self.user,
        )


class BaseDocument(Document):
    context = EmbeddedDocumentField(Context)
    audit = EmbeddedDocumentField(Audit)
    active = BooleanField(default=True)

    meta = {
        "abstract": True,
        "strict": False,
    }

    @classmethod
    @property
    def db(cls):
        return cls._get_db()

    def save(self, *args, **kwargs):
        if not self.context:
            self.context = Context()
        if not self.audit:
            self.audit = Audit(created_by=self.context.user)
        self.audit.updated_by = self.context.user
        self.audit.updated_at = datetime.utcnow()
        return super().save(*args, **kwargs)

    def to_proto(self, *args, **kwargs):
        raise NotImplementedError

    @classmethod
    def reference_list(cls):
        return [cls]


class BaseAuditEmbeddedDocument(BaseEmbeddedDocument):
    context = EmbeddedDocumentField(Context)
    audit = EmbeddedDocumentField(Audit)
    active = BooleanField(default=True)
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
    params = context.get_current_parameters()
    if params.get("created_by") is None:
        return params.get("updated_by")
    return params.get("created_by")


class Base:
    """
    Base class provides foundational attributes and methods for database models.
    It includes common attributes such as 'id', 'active', and timestamp fields.
    It also provides methods for converting the model to its proto representation.
    """

    @staticmethod
    def _camel_to_snake(name):
        """
        Convert a CamelCase string to snake_case.

        Args:
            name (str): The CamelCase string.

        Returns:
            str: The converted snake_case string.
        """
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    @declared_attr
    def __tablename__(cls):
        """
        Generate a table name based on the class name.

        Returns:
            str: The table name in snake_case format.
        """
        return cls._camel_to_snake(cls.__name__)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    tenant: Mapped[str] = mapped_column(String(30), nullable=False)
    created_by: Mapped[str] = mapped_column(String(50), default=set_created_by, nullable=False)
    updated_by: Mapped[str] = mapped_column(String(50), nullable=False)
    deleted_by: Mapped[str] = mapped_column(String(50), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False
    )
    deleted_at: Mapped[datetime] = mapped_column(DateTime(), nullable=True)

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


BaseModel = declarative_base(cls=Base)
