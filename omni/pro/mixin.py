from omni.pro.locales import translator


class EnumBaseMixin(object):
    # FIXME: remove this method after invoke __str__ method in Enum class in all enums
    def get_message(self, context):
        return context._(str(self)) if hasattr(context, "_") else str(self)

    def __str__(self):
        return translator.gettext(self.value[1])
