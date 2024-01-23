import csv
from ast import literal_eval
from pathlib import Path

from google.protobuf import json_format
from omni.pro import redis, util
from omni.pro.config import Config
from omni.pro.database import DatabaseManager
from omni.pro.logger import LoggerTraceback, configure_logger
from omni.pro.microservice import MicroService
from omni.pro.protos.grpc_connector import Event, GRPClient
from omni.pro.protos.v1.users import user_pb2
from omni.pro.protos.v1.utilities.ms_pb2 import Microservice as MicroserviceProto
from omni.pro.stack import ExitStackDocument
from omni.pro.validators import MicroServicePathValidator

logger = configure_logger(name=__name__)


class LoadData(object):
    def __init__(self, base_app: Path):
        # self.redis_manager = redis.get_redis_manager()
        self.base_app = base_app
        # self.context = self._get_context()
        # self.microserivce = None

    def get_rpc_manifest_func_class(self):
        return ManifestRPCFunction

    def load_data(self):
        redis_manager = redis.get_redis_manager()
        tenans = redis_manager.get_tenant_codes()
        for tenant in tenans:
            user = redis_manager.get_user_admin(tenant)
            context = {
                "tenant": tenant,
                "user": user.get("id") or "admin",
            }
            db_params = redis_manager.get_mongodb_config(Config.SERVICE_ID, tenant)
            db_alias = f"{tenant}_{db_params.get('name')}"
            micro: MicroserviceProto = self.get_rpc_manifest_func_class()(context).get_micro(
                MicroService.SAAS_MS_UTILITIES.value
            )
            if micro:
                db_params["db"] = db_params.pop("name")
                db_manager = DatabaseManager(**db_params)
                self.load_data_micro(db_manager, json_format.MessageToDict(micro), context, db_alias)

    def create_user_admin(self, context, rc):
        values = self.load_data_dict(Path(__file__).parent / "data" / "models.user.csv")
        user = UserChannel(context)
        response, success = user.create_users(values)
        if success:
            rc.json().set(
                context.get("tenant"), "$.user_admin", {"id": response.user.id, "username": response.user.username}
            )
        return response, success

    def load_data_dict(self, name_file):
        try:
            with open(name_file, mode="r", encoding="utf-8-sig") as csv_file:
                reader = csv.DictReader(csv_file, delimiter=";")
                for row in reader:
                    yield row
                return reader
        except FileNotFoundError as e:
            LoggerTraceback.error("File not found exception", e, logger)
        except Exception as e:
            LoggerTraceback.error("An unexpected error has occurred", e, logger)

    def load_data_micro(self, db_manager: DatabaseManager, micro: dict, context: dict, db_alias):
        tenant = context.get("tenant")
        for idx, file in enumerate(micro.get("data") or []):
            if file.get("load"):
                continue
            name_file = self.base_app / file.get("path")
            reader = self.load_data_dict(name_file)
            models, file_py, model_str = file.get("path").split("/")[1].split(".")[:-1]
            model_str = util.to_camel_case(model_str)
            ruta_modulo = self.base_app / models / f"{file_py}.py"
            if not ruta_modulo.exists():
                logger.error(f"File not found {ruta_modulo}")
                continue
            modulo = util.load_file_module(ruta_modulo, model_str)
            if not hasattr(modulo, model_str):
                logger.error(f"Class not found {model_str} in {ruta_modulo}")
                continue
            load = False
            with ExitStackDocument(
                (doc_class := getattr(modulo, model_str)).reference_list(),
                db_alias=db_alias,
                use_doc_classes=True,
            ):
                for row in reader:
                    row = row | {"context": context}
                    db_manager.create_document(db_name=None, document_class=doc_class, **row)
                    if not load:
                        load = True
                attr_data = [{f"set__data__{idx}__load": load}]
                # self.db_manager.update(micro, **attr_data)
                self.get_rpc_manifest_func_class()(context).update_micro(
                    {"microservice": {"id": micro.get("id"), "settings": micro.get("settings"), "data": attr_data}}
                )
                if load:
                    logger.info(f"Load data {micro.get('code')} - {tenant} - {file.get('path')}")


class Manifest(object):
    def __init__(self, base_app: Path):
        self.base_app = base_app

    def get_rpc_manifest_func_class(self):
        return ManifestRPCFunction

    def get_manifest(self):
        file_name = self.base_app / "__manifest__.py"
        if not file_name.exists():
            logger.warning(f"Manifest file not found {file_name}")
            return {}
        with open(file_name, "r") as f:
            data = f.read()
        manifest = literal_eval(data)
        return manifest

    def validate_manifest(
        self, context: dict, manifest: dict = {}, micro_data: [dict] = [], micro_settings: [dict] = []
    ):
        manifest = manifest or self.get_manifest()
        data_validated = MicroServicePathValidator(self.base_app).load(
            manifest | {"context": context}, micro_data=micro_data, micro_settings=micro_settings
        )
        return data_validated

    def load_manifest(self):
        manifest = self.get_manifest()
        if not manifest:
            return
        redis_manager = redis.get_redis_manager()
        tenans = redis_manager.get_tenant_codes()
        for tenant in tenans:
            user = redis_manager.get_user_admin(tenant)
            context = {
                "tenant": tenant,
                "user": user.get("id") or "admin",
            }
            rpc_func: ManifestRPCFunction = self.get_rpc_manifest_func_class()(context)
            try:
                micro = rpc_func.get_micro(manifest.get("code"))
                manifest_data = self.validate_manifest(
                    context=context,
                    manifest=manifest,
                    micro_data=json_format.MessageToDict(micro.data),
                    micro_settings=json_format.MessageToDict(micro.settings),
                )
                rpc_func.load_manifest(manifest_data)
            except Exception as e:
                LoggerTraceback.error("Load manifest exception", e, logger)


class ManifestRPCFunction(object):
    def __init__(self, context: dict) -> None:
        self.context = context
        self.service_id = MicroService.SAAS_MS_UTILITIES.value
        self.microservice_module_grpc = "v1.utilities.ms_pb2_grpc"
        self.microservice_stub_classname = "MicroserviceServiceStub"
        self.microservice_module_pb2 = "v1.utilities.ms_pb2"

        self.event = Event(
            module_grpc=self.microservice_module_grpc,
            stub_classname=self.microservice_stub_classname,
            rpc_method="",
            module_pb2=self.microservice_module_pb2,
            request_class="",
            params={},
        )

    def load_manifest(self, params):
        self.event.update(
            rpc_method="MicroserviceCreate",
            request_class="MicroserviceCreateRequest",
            params=params | {"context": self.context},
        )
        response, success = GRPClient(service_id=self.service_id).call_rpc_fuction(self.event)
        logger.info(f"Load manifest {response.microservice.code} - status: {success}")
        return response

    def get_micro(self, code: str) -> MicroserviceProto:
        self.event.update(
            rpc_method="MicroserviceRead",
            request_class="MicroserviceReadRequest",
            params={"filter": {"filter": f"[('code','=','{code}')]"}} | {"context": self.context},
        )
        response, _s = GRPClient(service_id=self.service_id).call_rpc_fuction(self.event)
        micro: MicroserviceProto = response.microservices[0] if response.microservices else MicroserviceProto()
        return micro

    def update_micro(self, params: dict):
        self.event.update(
            rpc_method="MicroserviceUpdate",
            request_class="MicroserviceUpdateRequest",
            params=params | {"context": self.context},
        )
        response, success = GRPClient(service_id=self.service_id).call_rpc_fuction(self.event)
        logger.info(f"Update manifest {response.microservice.code} - status: {success}")
        return response


class UserChannel(object):
    def __init__(self, context: dict) -> None:
        self.context = context
        self.service_id = MicroService.SAAS_MS_USER.value
        self.user_module_grpc = "v1.users.user_pb2_grpc"
        self.user_stub_classname = "UsersServiceStub"
        self.user_module_pb2 = "v1.users.user_pb2"

        self.event = Event(
            module_grpc=self.user_module_grpc,
            stub_classname=self.user_stub_classname,
            rpc_method="",
            module_pb2=self.user_module_pb2,
            request_class="",
            params={},
        )

    def create_users(self, list_value):
        response = user_pb2.UserCreateResponse(), False
        for value in list_value:
            self.context["user"] = self.context.get("user") or value.get("sub")
            self.event.update(
                rpc_method="UserCreate",
                request_class="UserCreateRequest",
                params={
                    "context": self.context,
                    "email": value.get("email"),
                    "email_confirm": value.get("email"),
                    "language": {"code": "01", "code_name": "CO"},
                    "name": value.get("name"),
                    "password": value.get("password"),
                    "password_confirm": value.get("password"),
                    "timezone": {"code": "01", "code_name": "CO"},
                    "username": value.get("username"),
                    "is_superuser": True,
                },
            )
            response = GRPClient(service_id=self.service_id).call_rpc_fuction(self.event)
        return response
