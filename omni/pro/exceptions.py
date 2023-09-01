import traceback

from marshmallow import ValidationError
from omni.pro.logger import LoggerTraceback
from sqlalchemy.exc import IntegrityError, OperationalError, ProgrammingError


def handle_error(service_model: str, service_method: str, logger, error: Exception, message_response):
    """
    Handles and logs different types of errors, returning appropriate response messages based on the error type.
    Maneja y registra diferentes tipos de errores, devolviendo mensajes de respuesta apropiados según el tipo de error.

    Args:
    - service_model (str): The name of the service model where the error occurred.
    - service_model (str): El nombre del modelo de servicio donde ocurrió el error.

    - service_method (str): The method of the service model where the error occurred.
    - service_method (str): El método del modelo de servicio donde ocurrió el error.

    - logger (Logger): Logger instance to record the errors.
    - logger (Logger): Instancia de Logger para registrar los errores.

    - error (Exception): The error or exception instance to be handled.
    - error (Exception): La instancia de error o excepción a manejar.

    - message_response (MessageResponse): Object for creating and returning response messages.
    - message_response (MessageResponse): Objeto para crear y devolver mensajes de respuesta.

    Returns:
    - MessageResponse: An appropriate error message response based on the error type.
    - MessageResponse: Una respuesta de mensaje de error apropiada según el tipo de error.

    Usage/Uso:
    response = handle_error(service_model, service_method, logger, error, message_response)
    respuesta = handle_error(service_model, service_method, logger, error, message_response)
    """
    tb = traceback.format_exc()
    logger.error(f"Error: {str(error)}\n\nTraceback:\n\n {tb}")

    error_handlers = {
        IntegrityError: (
            f"{service_model} {service_method} integrity error",
            lambda error: f"pgerror: {error.orig.pgerror}",
        ),
        ValidationError: (
            f"{service_model} {service_method} validation error",
            lambda error: str(error.messages),
        ),
        OperationalError: (
            f"{service_model} {service_method} operational error",
            lambda _: "Error with connection",
        ),
        Exception: (
            f"{service_model} {service_method} exception",
            lambda _: "{service_model} {service_method} Exception",
        ),
        AttributeError: (
            f"{service_model} attribute error",
            lambda error: str(error),
        ),
        ProgrammingError: (
            f"{service_model} programming error",
            lambda error: str(error),
        ),
        NotFoundError: (
            f"{service_model} not found error",
            lambda error: str(error),
        ),
        ValueError: (
            f"{service_model} Value error",
            lambda error: str(error),
        ),
        MoveLineBusinessLogicError: (
            f"{service_model} move line business logic error",
            lambda error: str(error),
        ),
        PickingBusinessLogicError: (
            f"{service_model} picking business logic error",
            lambda error: str(error),
        ),
    }

    error_message, error_response = error_handlers.get(type(error), ("Unknown error", None))

    LoggerTraceback.error(error_message, error, logger)

    message = f"{error_message}:\n\nTraceback:\n\n{tb}\n\nError Response:\n\n{error_response}"

    if isinstance(error, OperationalError):
        return message_response.internal_response(message=message)

    return message_response.bad_response(message=message)


class NotFoundError(Exception):
    def __init__(
        self,
        message: str | list | dict,
        **kwargs,
    ):
        self.messages = [message] if isinstance(message, (str, bytes)) else message
        self.kwargs = kwargs
        super().__init__(message)


class MoveLineBusinessLogicError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class PickingBusinessLogicError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class AlreadyExistError(Exception):
    def __init__(
        self,
        message: str | list | dict,
        **kwargs,
    ):
        self.messages = [message] if isinstance(message, (str, bytes)) else message
        self.kwargs = kwargs
        super().__init__(message)
