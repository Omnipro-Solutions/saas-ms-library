import newrelic.agent as agent
from omni.pro.logger import configure_logger

logger = configure_logger(name=__name__)


def register_event_new_relic(event_name: str, event_data: dict):
    """
    Registers a custom event in New Relic.

    Args:
        event_name (str): The name of the event.
        event_data (dict): The data associated with the event.

    Returns:
        None
    """
    agent.record_custom_event(event_name, event_data)
    logger.info(f"Register: {event_name}, in newrelic")
