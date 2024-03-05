from omni_pro_base.logger import configure_logger
from omni.pro.newrelic import register_event_new_relic

logger = configure_logger(name=__name__)


def test_weebhook(tenant):
    logger.info(f"Send data to newrelic")
    register_event_new_relic(
        "TEST_WEBHOOK", {"status": "success", "message": "Webhook is working fine", "tenant": tenant}
    )
    return {"status": "success", "message": "Webhook is working fine"}
