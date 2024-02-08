from enum import Enum

from mongoengine import DictField, EnumField, StringField
from omni.pro.models.base import BaseDocument


class StateEnum(Enum):
    error = "error"
    done = "done"
    pending = "pending"


class Logger(BaseDocument):
    state = EnumField(StateEnum)
    model_code = StringField()
    data = DictField()

    meta = {
        "collection": "loggers",
    }
