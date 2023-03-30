import logging
import traceback


def configure_logger(name) -> logging.Logger:
    logger = logging.getLogger(name=name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


def write_exception_msg(msg: str, e: Exception, logger: logging.Logger) -> None:
    msg_error = "{msg} - {ex}".format(msg=msg, ex=e.__class__)
    tb = traceback.format_exc()
    logger.error(f"{msg_error}: {tb}")
    return msg_error
