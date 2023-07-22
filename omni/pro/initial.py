import csv
from pathlib import Path

import grpc
from google.protobuf import wrappers_pb2
from omni.pro import redis, util
from omni.pro.cloudmap import CloudMap
from omni.pro.config import Config
from omni.pro.database import DatabaseManager
from omni.pro.logger import LoggerTraceback, configure_logger
from omni.pro.models.common.ms import MicroService
from omni.pro.protos.v1.users import user_pb2, user_pb2_grpc
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
                with self.db_manager.get_connection():
                    if not self.manifest:
                        continue
                    micro = self.load_manifest(context=context)
                    self.load_data_micro(micro, context)
                list_contexts.append(context)
        return list_contexts

    def create_user_admin(self, context, rc):
        values = self.load_data_dict(Path(__file__).parent / "data" / "models.user.csv")
        user = UserStub()
        response = user.create_users(context, values)
        success = response.response_standard.status_code in range(200, 300)
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

    def load_manifest(self, context: dict):
        tenant = context.get("tenant")
        filters = {"code": self.manifest.get("code"), "tenant_code": tenant}
        micro: MicroService = self.db_manager.get_document(
            db_name=None, tenant=tenant, document_class=MicroService, **filters
        )
        self.manifest["tenant_code"] = tenant
        data_validated = MicroServiceValidator(self.base_app, micro.data if micro else []).load(
            self.manifest | {"context": context}
        )
        if not micro:
            micro = self.db_manager.create_document(db_name=None, document_class=MicroService, **data_validated)
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

    def load_data_micro(self, micro: MicroService, context: dict):
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
            for row in reader:
                row = row | {"context": context}
                self.db_manager.create_document(db_name=None, document_class=getattr(modulo, model_str), **row)
                if not load:
                    load = True
            attr_data = {f"set__data__{idx}__load": load}
            self.db_manager.update(micro, **attr_data)
            if load:
                logger.info(f"Load data {micro.code} - {tenant} - {file.get('path')}")


class UserStub(object):
    def __init__(self):
        cloud_map = CloudMap(service_name=Config.SERVICE_NAME_BALANCER)
        response = cloud_map.discover_instances()
        self.port = None
        self.host = None
        for instance in response:
            if instance.get("InstanceId") == Config.SAAS_MS_USER:
                self.host = instance.get("Attributes").get("host")
                self.port = instance.get("Attributes").get("port")
                break

    def create_users(self, context: dict, list_value: list) -> user_pb2.UserCreateResponse:
        credentials = grpc.ssl_channel_credentials()
        with grpc.secure_channel(
            f"{self.host}:{self.port}",
            credentials,
            options=[("grpc.ssl_target_name_override", "omni.pro")],
        ) as channel:
            stub = user_pb2_grpc.UsersServiceStub(channel)
            response = user_pb2.UserCreateResponse()
            for value in list_value:
                context["user"] = context.get("user") or value.get("username")
                response = self._create_user(context, value, stub)
                if response.response_standard.status_code in range(200, 300):
                    logger.info(f"User created {response.user.username}")
                else:
                    logger.error(f"User not created {context.get('user')}")
            return response

    def _create_user(self, context: dict, value: dict, stub) -> user_pb2.UserCreateResponse:
        user = user_pb2.UserCreateRequest(
            **{
                "context": context,
                "email": value.get("email"),
                "email_confirm": value.get("email"),
                "language": {"code": "01", "code_name": "CO"},
                "name": value.get("name"),
                "password": value.get("password"),
                "password_confirm": value.get("password"),
                "timezone": {"code": "01", "code_name": "CO"},
                "username": value.get("username"),
                "is_superuser": wrappers_pb2.BoolValue(value=util.parse_bool(value.get("is_superuser") or False)),
            }
        )
        return stub.UserCreate(user)
