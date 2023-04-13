import typing

from marshmallow import Schema, fields, types


class ContextSchema(Schema):
    tenant = fields.String(required=True)
    user = fields.String(required=True)
    countryCode = fields.String(required=True)

    def load(
        self,
        data: (typing.Mapping[str, typing.Any] | typing.Iterable[typing.Mapping[str, typing.Any]]),
        *,
        many: bool | None = None,
        partial: bool | types.StrSequenceOrSet | None = None,
        unknown: str | None = None
    ):
        data = super().load(data, many=many, partial=partial, unknown=unknown)
        data["country_code"] = data.pop("countryCode")
        return data


class BaseObjectSchema(Schema):
    code = fields.String(required=True)
    name = fields.String(required=True)


class BaseSchema(Schema):
    context = fields.Nested(ContextSchema, required=True)
