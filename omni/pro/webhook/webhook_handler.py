import threading
from typing import Dict, List, Set
import time


class WebhookHandler:

    @classmethod
    def start_thread(cls, crud_attrs: dict, context: dict):
        thread = threading.Thread(target=cls.filter_events, args=(crud_attrs, context))
        thread.start()

    @classmethod
    def filter_events(cls, crud_attrs: dict, context: dict):
        # Lógica para filtrar eventos y webhooks
        # Aquí enviarías los eventos filtrados a microservicios internos y Airflow
        time.sleep(0.3)
        print(f"context: {context}\ncrud attrs: {crud_attrs}")
        created_attrs: Dict[str, List[int]] = crud_attrs.get("created_attrs", {})
        updated_attrs: Dict[str, Dict[str, Set[str]]] = crud_attrs.get("updated_attrs", {})
        deleted_attrs: Dict[str, List[int]] = crud_attrs.get("deleted_attrs", {})
        context: Dict[str, str] = context

        pass
