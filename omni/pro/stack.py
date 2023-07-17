import importlib
import inspect
import pkgutil
from contextlib import ExitStack

from mongoengine import Document
from mongoengine import context_managers as ctx_mgr
from mongoengine import fields
from omni.pro.models.base import BaseDocument


class ExitStackDocument(ExitStack):
    """
    Context manager for dynamic management of an outbound callback stack for Documents.

    For example:
        with ExitStackDocument([DocumentClass1, DocumentClass2], "db_alias") as stack:
            DocumentClass1.objects.all()
            # All documents are swiched to their respective aliases.
    """

    def __init__(self, document_classes: list = [], db_alias="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.document_classes = document_classes
        self.db_alias = db_alias
        self.model_classes = []

    def __enter__(self):
        for document_class in self.document_classes:
            self.model_classes = self.enter_context(ctx_mgr.switch_db(document_class, self.db_alias))
        return super().__enter__()


class ExitStackDocumentMicro(ExitStackDocument):
    """
    Context manager for dynamic management of an outbound callback stack for user microservice documents.

    For example:
        with ExitStackDocumentMicro("db_alias") as stack:
            pass
            # All documents in models package are swiched to their respective db_alias.
    """

    def __init__(self, db_alias=None, *args, **kwargs):
        super().__init__(document_classes=[], db_alias=db_alias, *args, **kwargs)

    def __enter__(self):
        self.document_classes = self.get_document_classes()
        return super().__enter__()

    def get_document_classes(self):
        # El nombre de tu paquete (la carpeta que contiene los módulos)
        package_name = "models"

        # Busca todos los módulos en el paquete
        package = importlib.import_module(package_name)
        modules = [name for _, name, _ in pkgutil.iter_modules(package.__path__)]

        document_classes = []
        # Importa cada módulo y busca las clases de tipo Document
        for module_name in modules:
            module = importlib.import_module(f"{package_name}.{module_name}")

            for name, obj in inspect.getmembers(module):
                if (
                    inspect.isclass(obj)
                    and issubclass(obj, Document)
                    and obj != Document
                    and obj != BaseDocument
                    and obj not in document_classes
                ):
                    document_classes.append(obj)
                    for field in self.get_reference_fields_and_classes(obj):
                        if field not in document_classes:
                            document_classes.append(field)

        return document_classes

    def get_reference_fields_and_classes(self, doc):
        ref_fields = []
        for name, field in doc._fields.items():
            if isinstance(field, fields.ReferenceField):
                ref_fields.append(field.document_type)
            elif isinstance(field, fields.ListField) and isinstance(field.field, fields.ReferenceField):
                ref_fields.append(field.field.document_type)
        return ref_fields
