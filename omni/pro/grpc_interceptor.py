import grpc


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
