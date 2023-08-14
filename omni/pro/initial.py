import csv
from pathlib import Path

from omni.pro import redis, util
from omni.pro.config import Config
from omni.pro.database import DatabaseManager
from omni.pro.logger import LoggerTraceback, configure_logger
from omni.pro.microservice import MicroService, MicroServiceDocument
from omni.pro.protos.grpc_connector import Event, GRPClient
from omni.pro.protos.v1.users import user_pb2
from omni.pro.stack import ExitStackDocument
from omni.pro.validators import MicroServiceValidator

logger = configure_logger(name=__name__)


class LoadData(object):
    def __init__(self, base_app: Path):
        # self.redis_manager = redis.get_redis_manager()
        self.base_app = base_app
        self.manifest = self._get_manifest_ms()
        # self.context = self._get_context()
        self.microserivce = None

    def load_data(self, *args, **kwargs):
        self.redis_manager = redis.get_redis_manager()
        list_contexts = []
        with self.redis_manager.get_connection() as rc:
            tenant_codes = self.redis_manager.get_tenant_codes()
            for tenant in tenant_codes:
                user = rc.json().get(tenant, "$.user_admin")
                context = {"tenant": tenant, "user": user}
                if (not context.get("user")) or (context.get("user") and (not context.get("user")[0])):
                    context["user"] = None
                    response, success = self.create_user_admin(context, rc)
                    if not success:
                        # TODO: End process
                        continue
                    context["user"] = response.user.username
                else:
                    # TODO: Validate if user exists in database
                    context["user"] = user[0].get("username")
                db_params = self.redis_manager.get_mongodb_config(Config.SERVICE_ID, tenant)
                db_params["db"] = db_params.pop("name")
                self.db_manager = DatabaseManager(**db_params)
                db_alias = f"{tenant}_{db_params['db']}"
                if not self.manifest:
                    continue
                micro = self.load_manifest(context=context, db_alias=db_alias)
                self.load_data_micro(micro, context, db_alias)
                list_contexts.append(context)
        return list_contexts

    def create_user_admin(self, context, rc):
        values = self.load_data_dict(Path(__file__).parent / "data" / "models.user.csv")
        user = UserChannel(context)
        response, success = user.create_users(values)
        if success:
            rc.json().set(
                context.get("tenant"), "$.user_admin", {"id": response.user.id, "username": response.user.username}
            )
        return response, success

    def _get_manifest_ms(self):
        file_name = self.base_app / "__manifest__.py"
        if not file_name.exists():
            logger.warning(f"Manifest file not found {file_name}")
            return {}
        with open(file_name, "r") as f:
            data = f.read()
        return eval(data)

    def load_manifest(self, context: dict, db_alias: str):
        with ExitStackDocument(MicroServiceDocument.reference_list(), db_alias=db_alias):
            tenant = context.get("tenant")
            filters = {"code": self.manifest.get("code"), "tenant_code": tenant}
            micro: MicroServiceDocument = self.db_manager.get_document(
                db_name=None, tenant=tenant, document_class=MicroServiceDocument, **filters
            )
            self.manifest["tenant_code"] = tenant
            data_validated = MicroServiceValidator(self.base_app, micro.data if micro else []).load(
                self.manifest | {"context": context}
            )
            if not micro:
                micro = self.db_manager.create_document(
                    db_name=None, document_class=MicroServiceDocument, **data_validated
                )
            else:
                micro.data = data_validated.get("data")
                micro.save()
            self.microservice = micro
            return micro

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

    def load_data_micro(self, micro: MicroServiceDocument, context: dict, db_alias):
        tenant = context.get("tenant")
        for idx, file in enumerate(micro.data):
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
                (doc_class := getattr(modulo, model_str)).reference_list() + MicroServiceDocument.reference_list(),
                db_alias=db_alias,
            ):
                for row in reader:
                    row = row | {"context": context}
                    self.db_manager.create_document(db_name=None, document_class=doc_class, **row)
                    if not load:
                        load = True
                attr_data = {f"set__data__{idx}__load": load}
                self.db_manager.update(micro, **attr_data)
                if load:
                    logger.info(f"Load data {micro.code} - {tenant} - {file.get('path')}")


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
