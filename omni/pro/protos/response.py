from omni.pro.protos.common import base_pb2
from omni.pro.util import HTTPStatus


class MessageResponse(object):
    def __init__(self, cls):
        self.cls = cls

    def response(self, message: str, success: bool, status_code: int = HTTPStatus.OK, **kwargs):
        return self.cls(
            response_standard=base_pb2.ResponseStandard(success=success, message=message, status_code=status_code),
            **kwargs,
        )
