from google.protobuf import json_format
from omni.pro import redis
from omni.pro.descriptor import Descriptor
from omni.pro.logger import configure_logger
from omni.pro.protos.grpc_function import ModelRPCFucntion
from omni.pro.topology import Topology
from omni.pro.util import generate_hash

logger = configure_logger(name=__name__)


class RegisterModel(object):
    def __init__(self, models_path, microservice: str):
        self.models_path = models_path
        self.microservice = microservice

    def register_mongo_model(self):
        self._register("describe_mongo_model", "NO_SQL")

    def register_sqlalchemy_model(self):
        self._register("describe_sqlalchemy_model", "SQL")

    def _register(self, method: str, persistence_type: str):
        redis_manager = redis.get_redis_manager()
        tenans = redis_manager.get_tenant_codes()
        models_libs = Topology(self.models_path).get_models_from_libs()
        for tenant in tenans:
            user = redis_manager.get_user_admin(tenant)
            context = {
                "tenant": tenant,
                "user": user.get("id") or "admin",
            }
            rpc_func = ModelRPCFucntion(context)
            for model in models_libs:
                desc = getattr(Descriptor, method)(model)
                desc = {"persistence_type": persistence_type, "microservice": self.microservice} | desc
                hash_code = generate_hash(desc)
                params = {
                    "filter": {
                        "filter": f"['and', ('microservice','=','{self.microservice}'), ('class_name','=','{desc.get('class_name')}')]"
                    }
                }
                response, success, event = rpc_func.read_model(params)
                if not success:
                    logger.warning(f"{event.get('rpc_method')}: {str(response.response_standard)}")
                    continue

                model = response.models[0] if response.models else None
                if model:
                    model_dict = self.transform_model_desc(model)
                    model_id = model_dict.pop("id")
                    if generate_hash(model_dict) == hash_code:
                        logger.info(f"Model {desc['class_name']} no changes")
                        continue

                    desc["hash_code"] = hash_code
                    params = {"model": {"id": model_id} | desc}
                    response, success, event = rpc_func.updated_model(params)
                else:
                    desc["hash_code"] = hash_code
                    params = desc
                    response, success, event = rpc_func.register_model(params)

                getattr(logger, "warning" if not success else "info")(
                    f"Model {desc['class_name']} method {event.get('rpc_method')} {str(response.response_standard)}"
                )

    def transform_model_desc(self, model):
        model_dict = json_format.MessageToDict(model, preserving_proto_field_name=True)
        return {
            "id": model_dict["id"],
            "persistence_type": model_dict["persistence_type"],
            "microservice": model_dict["microservice"],
            "name": model_dict["name"],
            "class_name": model_dict["class_name"],
            "code": model_dict["code"],
            "fields": [self.transform_field_desc(x) for x in model_dict["fields"]],
        }

    def transform_field_desc(self, field):
        field_dict = {
            "name": field["name"],
            "code": field["code"],
            "type": field["type"],
            "required": field["required"],
            "relation": field["relation"],
        }
        if field.get("size"):
            field_dict["size"] = field["size"]
        if field.get("options"):
            field_dict["options"] = field["options"]
        return field_dict
