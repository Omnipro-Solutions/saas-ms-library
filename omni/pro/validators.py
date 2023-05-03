from marshmallow import Schema, fields


class ContextSchema(Schema):
    tenant = fields.String(required=True)
    user = fields.String(required=True)


class BaseObjectSchema(Schema):
    code = fields.String(required=True)
    code_name = fields.String(required=True)


class BaseSchema(Schema):
    context = fields.Nested(ContextSchema, required=True)
