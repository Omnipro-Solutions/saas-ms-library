from datetime import datetime

from google.protobuf.timestamp_pb2 import Timestamp
from mongoengine import BooleanField, DateTimeField, Document, EmbeddedDocument, EmbeddedDocumentField, StringField
from peewee import BooleanField as BooleanFieldPeewee
from peewee import CharField as CharFieldPeewee
from peewee import DateTimeField as DateTimeFieldPeewee
from peewee import ForeignKeyField
from peewee import IntegerField as IntegerFieldPeewee
from peewee import Model

from omni.pro.protos.common.base_pb2 import Context as ContextProto
from omni.pro.protos.common.base_pb2 import ObjectAudit as AuditProto


class BaseEmbeddedDocument(EmbeddedDocument):
    meta = {
        "abstract": True,
        "strict": False,
    }

    def to_proto(self):
        raise NotImplementedError


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

    def to_proto(self):
        raise NotImplementedError


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
    created_at = DateTimeFieldPeewee(default=datetime.now())
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
    object_audit = ForeignKeyField(AuditPeewee, null=True)
    context = ForeignKeyField(ContextPeewee, null=True)
    active = BooleanFieldPeewee(default=True)

    class Meta:
        database = None

    def save(self, *args, **kwargs):
        if self.object_audit is None:
            self.object_audit = AuditPeewee()
        if self._get_pk_value() is None:
            self.object_audit.created_by = self.context.user
            self.object_audit.created_at = datetime.now()
        self.object_audit.updated_by = self.context.user
        self.object_audit.updated_at = datetime.now()
        return super().save(*args, **kwargs)

    def to_proto(self, proto_model):
        proto_model.active = self.active
        proto_model.tenant = self.context.tenant
        proto_model.user = self.context.user
        proto_model.object_audit.CopyFrom(self.object_audit.to_proto())
        return proto_model
