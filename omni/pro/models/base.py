from datetime import datetime

from google.protobuf.timestamp_pb2 import Timestamp
from mongoengine import BooleanField, DateTimeField, Document, EmbeddedDocument, EmbeddedDocumentField, StringField
from omni.pro.protos.common.base_pb2 import Context as ContextProto
from omni.pro.protos.common.base_pb2 import ObjectAudit as AuditProto


class BaseEmbeddedDocument(EmbeddedDocument):
    active = BooleanField(default=True)
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


class Context(EmbeddedDocument):
    tenant = StringField()
    user = StringField()

    def to_proto(self):
        return ContextProto(
            tenant=self.tenant,
            user=self.user,
        )


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


class BaseDocument(Document):
    audit = EmbeddedDocumentField(Audit)
    context = EmbeddedDocumentField(Context)
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
