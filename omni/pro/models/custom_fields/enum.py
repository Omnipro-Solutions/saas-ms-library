from peewee import CharField


class EnumField(CharField):
    def __init__(self, enum_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.enum_type = enum_type

    def db_value(self, value):
        if isinstance(value, self.enum_type):
            return value.value
        elif isinstance(value, str):
            try:
                enum_value = self.enum_type(value)
                return enum_value.value
            except ValueError:
                raise ValueError(f"Invalid value for enum {self.enum_type.__name__}: {value}")
        else:
            return value

    def python_value(self, value):
        return self.enum_type(value) if value else None
