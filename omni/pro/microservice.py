from enum import Enum, unique
from pathlib import Path

from omni.pro import redis
from omni.pro.descriptor import Descriptor
from omni.pro.protos.grpc_function import ModelRPCFucntion
from omni.pro.topology import Topology
from omni.pro.util import generate_hash


@unique
class MicroService(Enum):
    SAAS_MS_USER = "saas-ms-user"
    SAAS_MS_CATALOG = "saas-ms-catalog"
    SAAS_MS_UTILITIES = "saas-ms-utilities"
    SAAS_MS_STOCK = "saas-ms-stock"
    SAAS_MS_CLIENT = "saas-ms-client"


class MicroServiceDocument(object):
    pass


class RegisterModel(object):
    def __init__(self, path_models: Path) -> None:
        self.path_models = path_models

    def register_model(self):
        l = Topology(path_models=self.path_models).get_models_from_libs()
        redis_manager = redis.get_redis_manager()
        tenans = redis_manager.get_tenant_codes()
        for tenant in tenans:
            user = redis_manager.get_json(tenant, "$.user_admin", "id")
            for model in l:
                desc = Descriptor.describe_mongo_model(model)
                hash_code = generate_hash(desc)
                context = {
                    "tenant": tenant,
                    "user": user,
                }
                ModelRPCFucntion(context=context).register_model(model, hash_code)
