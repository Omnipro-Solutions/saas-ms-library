from google.protobuf import json_format
from omni.pro.airflow.call_register_models import RegisterModels
from omni.pro.celery.call_register_models import RegisterModels
from omni.pro.config import Config
from omni.pro.database import PersistenceTypeEnum
from omni.pro.descriptor import Descriptor
from omni.pro.logger import configure_logger
from omni.pro.redis import RedisManager
from omni.pro.topology import Topology
from omni.pro.user.access import INTERNAL_USER
from omni.pro.util import generate_hash
from omni_pro_grpc.grpc_function import ModelRPCFucntion

logger = configure_logger(name=__name__)


class RegisterModel(object):
    def __init__(self, models_path, microservice: str):
        self.models_path = models_path
        self.microservice = microservice

    def get_rpc_model_func_class(self):
        return ModelRPCFucntion

    def get_topology_class(self) -> Topology:
        return Topology

    def register_mongo_model(self):
        """
        Register MongoDB models.

        Registrar modelos MongoDB.
        """
        self._register("describe_mongo_model", PersistenceTypeEnum.NO_SQL)

    def register_sqlalchemy_model(self):
        """
        Register SQLAlchemy models.

        Registrar modelos SQLAlchemy.
        """
        self._register("describe_sqlalchemy_model", PersistenceTypeEnum.SQL)

    def _register(self, method: str, persistence_type: PersistenceTypeEnum):
        """
        Generic method to register models based on persistence type and descriptor method.

        Método genérico para registrar modelos basados en el tipo de persistencia y el método de descriptor.

        Parameters:
        ----------
        method : str
            Method name from Descriptor class to describe the model.
            Nombre del método de la clase Descriptor para describir el modelo.

        persistence_type : PersistenceTypeEnum
            Type of the persistence either "NO_SQL" or "SQL".
            Tipo de persistencia ya sea "NO_SQL" o "SQL".
        """
        logger.info(f"Running Registering models with persistence type {persistence_type}")
        logger.info(f"RedisManager: {Config.REDIS_HOST}:{Config.REDIS_PORT}/{Config.REDIS_DB}")
        redis_manager = RedisManager(
            host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, redis_ssl=Config.REDIS_SSL
        )
        logger.info(f"Running redis_manager.get_tenant_codes()")
        tenans = redis_manager.get_tenant_codes()
        logger.info(f"Running Topology().get_models_from_libs()")

        TopologyClass: Topology = self.get_topology_class()
        if isinstance(self.models_path, str):
            models_libs = TopologyClass(path_models=self.models_path).get_models_from_libs()
        else:
            models_libs = TopologyClass().get_models_from_libs()
        logger.info(f"Running for loop")
        for tenant in tenans:
            context = {
                "tenant": tenant,
                "user": INTERNAL_USER,
            }
            register_model = RegisterModels(tenant)
            for model in models_libs:
                desc = getattr(Descriptor, method)(model)
                desc = {"persistence_type": str(persistence_type), "microservice": self.microservice} | desc
                desc["hash_code"] = generate_hash(desc)
                params = desc
                request = {"grpc_params": params, "context": context, "microservice": self.microservice}
                response = register_model.register_model(request)

                getattr(logger, "warning" if not response else "info")(
                    f"Model {desc['class_name']} state {response.state} status {response.status} with id {response.id}"
                )

    def transform_model_desc(self, model):
        """
        Transform model description from proto message to dictionary.

        Transformar la descripción del modelo de mensaje proto a diccionario.

        Parameters:
        ----------
        model : object
            Proto message model description.
            Descripción del modelo de mensaje proto.

        Returns:
        -------
        dict
            Dictionary representation of the model description.
            Representación en diccionario de la descripción del modelo.
        """
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
        """
        Transform field description from dictionary to specific format.

        Transformar la descripción del campo de diccionario a un formato específico.

        Parameters:
        ----------
        field : dict
            Dictionary representation of the field.
            Representación en diccionario del campo.

        Returns:
        -------
        dict
            Dictionary in the desired format for the field description.
            Diccionario en el formato deseado para la descripción del campo.
        """
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
