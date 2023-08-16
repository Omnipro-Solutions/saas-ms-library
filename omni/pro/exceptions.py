class NotFoundError(Exception):
    def __init__(
        self,
        message: str | list | dict,
        **kwargs,
    ):
        self.messages = [message] if isinstance(message, (str, bytes)) else message
        self.kwargs = kwargs
        super().__init__(message)
