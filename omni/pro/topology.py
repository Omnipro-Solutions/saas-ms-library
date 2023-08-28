import importlib
import inspect
import pathlib

import networkx as nx
import peewee
from mongoengine.document import Document
from omni.pro.logger import configure_logger
from omni.pro.models.base import BaseDocument, BaseModel
from peewee import ForeignKeyField

logger = configure_logger(__name__)


class Topology(object):
    def __init__(self, path_models):
        self.path_models = path_models

    def sort_models_topologically(self, models: list) -> list:
        graph = nx.DiGraph()

        # Agrega todos los modelos como nodos en el gráfico.
        for model in models:
            graph.add_node(model)

        # Agrega aristas para todas las relaciones de clave foránea.
        for model in models:
            for field in model._meta.sorted_fields:
                if isinstance(field, ForeignKeyField):
                    # Ignora las relaciones recursivas
                    if field.rel_model != model:
                        graph.add_edge(model, field.rel_model)

        # Intenta encontrar y eliminar ciclos
        while not nx.is_directed_acyclic_graph(graph):
            try:
                # Encuentra un ciclo
                cycle = nx.find_cycle(graph, orientation="original")

                # Imprime los nodos que forman un ciclo y sus dependencias
                logger.warning("# Found a cycle:")
                for edge in cycle:
                    logger.warning(f"# {edge[0]} -> {edge[1]}")

                # Elimina una arista del ciclo
                graph.remove_edge(cycle[0][0], cycle[0][1])
            except:
                break

        # Devuelve los modelos en un orden topológico.
        return list(nx.topological_sort(graph))

    def get_model_classes_from_module(self, module_name_list: list) -> list:
        model_classes = []
        for module_name in module_name_list:
            # Importa el módulo
            module = importlib.import_module(module_name)

            # Encuentra todas las clases de modelos en el módulo
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and (
                    (issubclass(obj, BaseModel) and obj != BaseModel)
                    or (issubclass(obj, Document) and obj != BaseDocument)
                ):
                    model_classes.append(obj)

        return model_classes

    def get_model_libs(self: pathlib.Path) -> list[str]:
        return [
            f"models.{path.stem}" for path in pathlib.Path(self.path_models).glob("**/*.py") if path.stem != "__init__"
        ]

    def get_models_from_libs(self) -> list[str]:
        model_libs = self.get_model_libs()
        model_classes = self.get_model_classes_from_module(model_libs)
        return list(set(model_classes))

    def logger_to_imports(self):
        # Ejemplo de uso
        model_libs = self.get_model_libs()
        model_classes = self.get_model_classes_from_module(model_libs)

        # Esto imprimirá los nombres de todas las clases de modelos en el módulo
        # for model_class in model_classes:
        #     print(model_class.__name__)

        model_top = self.sort_models_topologically(model_classes)
        model_top.reverse()
        for x in model_top:
            logger.info(f"from {x.__module__} import {x.__name__}")

        for x in model_top:
            logger.info(f"migrator.create_model({x.__name__})")
