from omni.pro.decorators import custom_decorator
from omni_pro_base.logger import configure_logger

logger = configure_logger(name=__name__)


@custom_decorator
def test_weebhook(ex=False):
    if ex:
        logger.error("Webhook is not working")
    return {"status": "success", "message": "Webhook is working fine"}
