from peewee import CharField


class EnumField(CharField):
    def __init__(self, enum_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.enum_type = enum_type

    def db_value(self, value):
        return value.value if value else None

    def python_value(self, value):
        return self.enum_type(value) if value else None
