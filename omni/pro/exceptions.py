import traceback
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError, OperationalError, ProgrammingError

from omni.pro.logger import LoggerTraceback


def handle_error(logger, error, message_response):
    """
    Handle and log errors, returning appropriate response messages.
    Maneja y registra errores, devolviendo mensajes de respuesta apropiados.

    Args:
    logger (Logger object): Logger instance to record the errors.
    Instancia de Logger para registrar los errores.

    error (Exception): The error or exception instance to be handled.
    La instancia de error o excepción a manejar.

    message_response (Response object): Object for creating responses.
    Objeto para crear respuestas.

    Returns:
    Response object: An appropriate error message response.
    Un objeto de respuesta con un mensaje de error apropiado.
    """

    tb = traceback.format_exc()
    logger.error(f"Error: {str(error)}\n\nTraceback:\n\n {tb}")

    error_handlers = {
        IntegrityError: (
            "Location create integrity error",
            lambda error: f"pgerror: {error.orig.pgerror}",
        ),
        ValidationError: (
            "Location create validation error",
            lambda error: str(error.messages),
        ),
        OperationalError: (
            "Location create operational error",
            lambda _: "Error with connection",
        ),
        Exception: (
            "Location create exception",
            lambda _: "Location create Exception",
        ),
        AttributeError: (
            "Location attribute error",
            lambda error: str(error),
        ),
        ProgrammingError: (
            "Location programming error",
            lambda error: str(error),
        ),
        NotFoundError: (
            "Model not found error",
            lambda error: str(error),
        ),
        ValueError: (
            "Value error",
            lambda error: str(error),
        )
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
