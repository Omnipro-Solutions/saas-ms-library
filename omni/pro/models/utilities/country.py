from mongoengine import BooleanField, EmbeddedDocumentField, FloatField, IntField, ListField, MapField, StringField
from omni.pro.models.base import Audit, BaseAuditEmbeddedDocument, BaseDocument, BaseEmbeddedDocument
from omni.pro.protos.common.base_pb2 import Object as CurrencyProto
from omni.pro.protos.v1.utilities.country_pb2 import Country as CountryProto
from omni.pro.protos.v1.utilities.document_type_pb2 import DocumentType as DocumentTypeProto
from omni.pro.protos.v1.utilities.language_pb2 import Language as LanguageProto
from omni.pro.protos.v1.utilities.payment_method_pb2 import PaymentMethod as PaymentMethodProto
from omni.pro.protos.v1.utilities.tax_pb2 import Tax as TaxProto
from omni.pro.protos.v1.utilities.territory_matrix_pb2 import TerritoryMatrix as TerritoryMatrixProto
from omni.pro.protos.v1.utilities.timezone_pb2 import Timezone as TimezoneProto


class Timezone(BaseAuditEmbeddedDocument):
    name = StringField()
    code = StringField()
    utc_offset = StringField()
    active = BooleanField(default=True)

    def to_proto(self) -> TimezoneProto:
        return TimezoneProto(
            name=self.name,
            code=self.code,
            utc_offset=self.utc_offset,
            active=self.active,
            object_audit=self.audit.to_proto(),
        )


class Language(BaseAuditEmbeddedDocument):
    name = StringField()
    code = StringField()
    active = BooleanField(default=True)

    def to_proto(self) -> LanguageProto:
        return LanguageProto(
            name=self.name,
            code=self.code,
            active=self.active,
            object_audit=self.audit.to_proto(),
        )


class Currency(BaseAuditEmbeddedDocument):
    name = StringField()
    code = StringField()
    currency_unit_label = StringField()
    currency_subunit_label = StringField()
    rate = IntField()
    rounding = FloatField()
    decimal_places = IntField()
    symbol = StringField()
    position = StringField()

    def to_proto(self) -> CurrencyProto:
        return CurrencyProto(
            name=self.name,
            code=self.code,
            currency_unit_label=self.currency_unit_label,
            currency_subunit_label=self.currency_subunit_label,
            rate=self.rate,
            rounding=self.rounding,
            decimal_places=self.decimal_places,
            symbol=self.symbol,
            position=self.position,
            active=self.active,
            # object_audit=self.audit.to_proto(),
        )


class Tax(BaseAuditEmbeddedDocument):
    name = StringField()
    code = StringField()
    rate = FloatField()
    rounding = FloatField()
    decimal_places = IntField()
    position = StringField()

    def to_proto(self) -> TaxProto:
        if not self.audit:
            self.audit = Audit()
        return TaxProto(
            name=self.name,
            code=self.code,
            rate=self.rate,
            rounding=self.rounding,
            decimal_places=self.decimal_places,
            position=self.position,
            active=self.active,
            # object_audit=self.audit.to_proto(),
        )


class DocumentType(BaseAuditEmbeddedDocument):
    name = StringField()
    code = StringField()
    size = IntField()

    def to_proto(self) -> DocumentTypeProto:
        return DocumentTypeProto(
            name=self.name,
            code=self.code,
            size=self.size,
            active=self.active,
            # object_audit=self.audit.to_proto(),
        )


class PaymentMethod(BaseAuditEmbeddedDocument):
    name = StringField()
    code = StringField()
    description = StringField()

    def to_proto(self) -> PaymentMethodProto:
        return PaymentMethodProto(
            name=self.name,
            code=self.code,
            description=self.description,
            active=self.active,
            # object_audit=self.audit.to_proto(),
        )


class TerritoryMatrix(BaseAuditEmbeddedDocument):
    sequence = IntField()
    name = StringField()
    code = StringField()

    def to_proto(self) -> TerritoryMatrixProto:
        return TerritoryMatrixProto(
            sequence=self.sequence,
            name=self.name,
            code=self.code,
            active=self.active,
            # object_audit=self.audit.to_proto(),
        )


class Country(BaseDocument):
    code = StringField()
    name = StringField()
    phone_number_size = IntField()
    phone_prefix = StringField()
    require_zipcode = BooleanField()
    currency = EmbeddedDocumentField(Currency)
    taxes = ListField(EmbeddedDocumentField(Tax))
    document_types = ListField(EmbeddedDocumentField(DocumentType))
    payment_methods = ListField(EmbeddedDocumentField(PaymentMethod))
    territory_matrixes = ListField(EmbeddedDocumentField(TerritoryMatrix))
    low_level = StringField()
    timezones = ListField(EmbeddedDocumentField(Timezone))
    languages = ListField(EmbeddedDocumentField(Language))

    def to_proto(self) -> CountryProto:
        return CountryProto(
            id=str(self.id),
            code=self.code,
            name=self.name,
            phone_number_size=self.phone_number_size,
            phone_prefix=self.phone_prefix,
            require_zipcode=self.require_zipcode,
            currency=self.currency.to_proto() if self.currency else None,
            taxes=[tax.to_proto() for tax in self.taxes],
            document_types=[document_type.to_proto() for document_type in self.document_types],
            payment_methods=[payment_method.to_proto() for payment_method in self.payment_methods],
            territory_matrixes=[territory_matrix.to_proto() for territory_matrix in self.territory_matrixes],
            timezones=[timezone.to_proto() for timezone in self.timezones],
            languages=[language.to_proto() for language in self.languages],
            active=self.active,
            object_audit=self.audit.to_proto(),
        )
