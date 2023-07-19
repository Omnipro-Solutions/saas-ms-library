from datetime import datetime

from google.protobuf.timestamp_pb2 import Timestamp
from mongoengine import BooleanField, DateTimeField, Document, EmbeddedDocument, EmbeddedDocumentField, StringField
from omni.pro.protos.common.base_pb2 import Context as ContextProto
from omni.pro.protos.common.base_pb2 import Object as ObjectProto
from omni.pro.protos.common.base_pb2 import ObjectAudit as AuditProto
from peewee import BooleanField as BooleanFieldPeewee
from peewee import CharField as CharFieldPeewee
from peewee import DateTimeField as DateTimeFieldPeewee
from peewee import IntegerField as IntegerFieldPeewee
from peewee import Model


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

    def to_proto(self):
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

    def to_proto(self):
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


class AuditPeewee(Model):
    created_by = IntegerFieldPeewee(null=True, default=None)
    updated_by = IntegerFieldPeewee(null=True, default=None)
    deleted_by = IntegerFieldPeewee(null=True, default=None)
    created_at = DateTimeFieldPeewee(null=True, default=None)
    updated_at = DateTimeFieldPeewee(null=True, default=None)
    deleted_at = DateTimeFieldPeewee(null=True, default=None)

    def to_proto(self) -> AuditProto:
        return AuditProto(
            created_by=self.created_by,
            updated_by=self.updated_by,
            deleted_by=self.deleted_by,
            created_at=self.created_at,
            updated_at=self.updated_at,
            deleted_at=self.deleted_at,
        )


class ContextPeewee(Model):
    tenant = CharFieldPeewee()
    user = CharFieldPeewee()

    def to_proto(self) -> ContextProto:
        return ContextProto(
            tenant=self.tenant,
            user=self.user,
        )


class BaseModel(Model):
    created_by = CharFieldPeewee(null=True, default=None)
    updated_by = CharFieldPeewee(null=True, default=None)
    deleted_by = CharFieldPeewee(null=True, default=None)
    created_at = DateTimeFieldPeewee(default=datetime.now())
    updated_at = DateTimeFieldPeewee(null=True, default=None)
    deleted_at = DateTimeFieldPeewee(null=True, default=None)
    active = BooleanFieldPeewee(null=False, default=True)

    class Meta:
        abstract = True
        database = None

    def get_audit_proto(self) -> AuditProto:
        created_at_ts = Timestamp()
        created_at_ts.FromDatetime(self.created_at)
        updated_at_ts = Timestamp()
        updated_at_ts.FromDatetime(self.updated_at)
        audit_proto = AuditProto(
            created_by=self.created_by,
            updated_by=self.updated_by,
            deleted_by=self.deleted_by,
            created_at=created_at_ts,
            updated_at=updated_at_ts,
        )
        if self.deleted_at:
            deleted_at_ts = Timestamp()
            deleted_at_ts.FromDatetime(self.deleted_at)
            audit_proto.deleted_at = deleted_at_ts
        return audit_proto

    def get_context_proto(self) -> ContextProto:
        return ContextProto(
            tenant=self.context["tenant"],
            user=self.context["user"],
        )

    # TODO add a method to update the audit fields in update and delete
    def save(self, *args, **kwargs):
        if self.created_by is None:
            self.created_by = self.context["user"]
        if self.created_at is None:
            self.created_at = datetime.now()
        self.updated_by = self.context["user"]
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)

    def to_proto(self, *args, **kwargs):
        raise NotImplementedError

    def sync_data(self, *args, **kwargs):
        raise NotImplementedError

    def get_document_info(self, *args, **kwargs):
        raise NotImplementedError
