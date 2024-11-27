import grpc
from omni.pro.locales import set_language
from omni_pro_grpc.util import MessageToDict


class LoggingInterceptor(grpc.ServerInterceptor):
    """
    Interceptor to log the gRPC method calls.
    Interceptor para registrar las llamadas de métodos gRPC.
    """

    def __init__(self, logger):
        """
        Initializes the LoggingInterceptor with a logger.
        Inicializa el LoggingInterceptor con un registrador.

        Args:
        logger (object): The logger instance used for logging.
                         Instancia de registrador utilizada para registrar.
        """
        self.logger = logger

    def intercept_service(self, continuation, handler_call_details):
        """
        Intercept the gRPC service call and log the method being called.
        Intercepta la llamada de servicio gRPC y registra el método que se está llamando.

        Args:
        continuation (function): A function that proceeds to the next interceptor or the service handler.
                                 Una función que procede al siguiente interceptor o al manejador del servicio.
        handler_call_details (obj): A named tuple with the attributes 'method' and 'invocation_metadata'.
                                    Una tupla nombrada con los atributos 'method' y 'invocation_metadata'.

        Returns:
        (obj): The result of the continuation function.
               El resultado de la función continuation.

        Raises:
        Exception: Propagates any exception raised during the gRPC service invocation.
                   Propaga cualquier excepción generada durante la invocación del servicio gRPC.
        """
        try:
            # Optional: Log the source of the call. Remove if not needed.
            # client_ip = handler_call_details.invocation_metadata["client_ip"]
            # self.logger.info("Received call from %s to %s", client_ip, handler_call_details.method)
            if handler_call_details.method != "/AWS.ALB/healthcheck":
                self.logger.info("Received call to %s", handler_call_details.method)
                return continuation(handler_call_details)
        except Exception as e:
            self.logger.error("Error while invoking method %s: %s", handler_call_details.method, str(e))
            raise


class LanguageInterceptor(grpc.ServerInterceptor):
    def __init__(self, base_localedir):
        self.base_localedir = base_localedir

    def intercept_service(self, continuation, handler_call_details):
        rpc_method_handler = continuation(handler_call_details)

        def new_unary_unary_handler(request, context):
            if hasattr(request, "context"):
                user_context = getattr(request, "context", None)
                if user_context and hasattr(user_context, "locale"):
                    locale_struct = user_context.locale
                    locale_dict = MessageToDict(locale_struct)
                    language_code = locale_dict.get("fields", {}).get("language", {}).get("stringValue", "es")
                    gettext_function = set_language(language_code=language_code, localedir=self.base_localedir)
                    context._ = gettext_function
            return rpc_method_handler.unary_unary(request, context)

        if rpc_method_handler.unary_unary:
            return grpc.unary_unary_rpc_method_handler(
                new_unary_unary_handler,
                request_deserializer=rpc_method_handler.request_deserializer,
                response_serializer=rpc_method_handler.response_serializer,
            )

        return rpc_method_handler
