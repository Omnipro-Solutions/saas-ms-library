import importlib
import inspect
import pkgutil

from mongoengine.document import Document
from omni.pro.logger import configure_logger
from omni.pro.models.base import BaseAuditEmbeddedDocument, BaseDocument, BaseModel

logger = configure_logger(__name__)


class Topology(object):
    def __init__(self, path_models: str = "models"):
        self.path_models = importlib.import_module(path_models)

    def get_model_classes_from_module(self, module_name_list: list) -> list:
        model_classes = []
        for module_name in module_name_list:
            # Importa el módulo
            module = None
            try:
                module = getattr(self.path_models, module_name)
            except AttributeError:
                module = importlib.import_module(f"models.{module_name}")

            # Encuentra todas las clases de modelos en el módulo
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and (
                    (issubclass(obj, BaseModel) and obj != BaseModel)
                    or (issubclass(obj, Document) and obj != BaseDocument)
                    or (issubclass(obj, BaseAuditEmbeddedDocument) and obj != BaseAuditEmbeddedDocument)
                ):
                    if obj not in model_classes:
                        model_classes.append(obj)

        return model_classes

    def get_model_libs(self: importlib) -> list[str]:
        return [name for _, name, _ in pkgutil.iter_modules(self.path_models.__path__)]

    def get_models_from_libs(self) -> list[str]:
        model_libs = self.get_model_libs()
        model_classes = self.get_model_classes_from_module(model_libs)
        return list(set(model_classes))
