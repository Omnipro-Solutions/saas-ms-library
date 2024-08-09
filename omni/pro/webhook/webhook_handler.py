import threading
from typing import Dict, List, Set, Type
import time

from omni.pro.logger import configure_logger
from omni_pro_grpc.grpc_function import EventRPCFucntion, WebhookRPCFucntion

logger = configure_logger(name=__name__)


class WebhookHandler:

    @classmethod
    def start_thread(cls, crud_attrs: dict, context: dict):
        if crud_attrs.get("created_attrs") or crud_attrs.get("updated_attrs") or crud_attrs.get("deleted_attrs"):
            thread = threading.Thread(target=cls.filter_events, args=(crud_attrs, context))
            thread.start()

    @classmethod
    def filter_events(cls, crud_attrs: dict, context: dict):

        type_db = context.pop("type_db")
        rpc_event = EventRPCFucntion(context=context)
        # Lógica para filtrar eventos y webhooks
        # Aquí enviarías los eventos filtrados a microservicios internos y Airflow
        time.sleep(0.3)
        print(f"context: {context}\ncrud attrs: {crud_attrs}")
        created_attrs: Dict[str, List[int]] = crud_attrs.get("created_attrs", {})
        updated_attrs: Dict[str, Dict[str, Set[str]]] = crud_attrs.get("updated_attrs", {})
        deleted_attrs: Dict[str, List[int]] = crud_attrs.get("deleted_attrs", {})
        class_by_name: Dict[str, Type[object]] = cls._get_class_by_name(type_db)

        class_by_name: Dict[str, Type[object]] = cls._get_class_by_name(type_db)

        event_codes: list = cls._get_event_codes(created_attrs, updated_attrs, deleted_attrs)

        print(f"table_class_by_name: {class_by_name}")
        if event_codes:
            response, success, _e = rpc_event.read_event({"filter": {"filter": f"['and',('code','in',{event_codes})]"}})

    @classmethod
    def _get_event_codes(cls, created_attrs, updated_attrs, deleted_attrs) -> list[str]:
        event_codes: list = []
        for model_name in created_attrs.keys():
            event_codes.append(f"{model_name}_create")
        for model_name in updated_attrs.keys():
            event_codes.append(f"{model_name}_update")
        for model_name in deleted_attrs.keys():
            event_codes.append(f"{model_name}_delete")
        return event_codes

    @classmethod
    def _get_create_event_codes(cls, created_attrs: Dict[str, List[int]]) -> list[str]:
        create_event_codes: list = []
        for model_name, create_ids in created_attrs.items():
            create_ids: list
            action_code = f"{model_name}_create"
            create_event_codes.append(action_code)
        return create_event_codes

    @classmethod
    def _get_class_by_name(cls, type_db: str) -> Dict[str, Type[object]]:
        from omni.pro.models.base import BaseDocument
        from omni.pro.models.base import BaseModel

        class_by_name = {}
        if type_db == "document":
            class_by_name = {cls._get_collection_name(): cls for cls in BaseDocument.__subclasses__()}
        elif type_db == "sql":
            class_by_name = {
                cls.__tablename__: cls
                for cls in BaseModel.registry._class_registry.values()
                if hasattr(cls, "__tablename__")
            }
        return class_by_name
