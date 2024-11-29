from pathlib import Path

import grpc
from omni.pro.locales import set_language, translator


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
            # if handler_call_details.method != "/AWS.ALB/healthcheck":
            self.logger.info("Received call to %s", handler_call_details.method)
        except Exception as e:
            self.logger.error(
                "LoggingInterceptor Error while invoking method %s: %s", handler_call_details.method, str(e)
            )
        return continuation(handler_call_details)


class LanguageInterceptor(grpc.ServerInterceptor):
    def __init__(self, base_localedir):
        self.base_localedir = base_localedir

    def intercept_service(self, continuation, handler_call_details):
        rpc_method_handler = continuation(handler_call_details)

        def _unary_set_text_language_context(request, context):
            if hasattr(request, "context") and (ctx := request.context).HasField("locale"):
                locale_dict = dict(ctx.locale.items())
                language_code = locale_dict.get("language")
                mofile: Path = Path(str(self.base_localedir)) / str(language_code) / "LC_MESSAGES" / "messages.mo"
                if language_code and mofile.exists():
                    gettext_function = set_language(language_code=language_code, localedir=self.base_localedir)
                    context._ = gettext_function
                    translator.set_language(language_code, self.base_localedir)
                else:
                    # TODO: Remove this block after all services update to new translation method
                    context._ = set_language(language_code="es", localedir=self.base_localedir)
                    translator.set_language(language_code="es", localedir=self.base_localedir)
            else:
                # TODO: Remove this block after all services update to new translation method
                context._ = set_language(language_code="es", localedir=self.base_localedir)
                translator.set_language(language_code="es", localedir=self.base_localedir)
            return rpc_method_handler.unary_unary(request, context)

        if isinstance(rpc_method_handler, grpc.RpcMethodHandler) and rpc_method_handler.unary_unary:
            return grpc.unary_unary_rpc_method_handler(
                _unary_set_text_language_context,
                request_deserializer=rpc_method_handler.request_deserializer,
                response_serializer=rpc_method_handler.response_serializer,
            )

        return rpc_method_handler
