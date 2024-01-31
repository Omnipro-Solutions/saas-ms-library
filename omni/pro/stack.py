import importlib
import inspect
import pkgutil
from contextlib import ExitStack

from mongoengine import Document
from mongoengine import context_managers as ctx_mgr
from mongoengine import fields
from omni.pro.models.base import BaseDocument
from omni.pro.topology import Topology


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
            self.__create_collection(document_class)
            self.model_classes = self.enter_context(ctx_mgr.switch_db(document_class, self.db_alias))
        return super().__enter__()

    def __create_collection(self, document_class):
        document_class._meta["db_alias"] = self.db_alias
        db = document_class.db
        collection_name = document_class._get_collection_name()
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)


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
        self.document_classes = self.__reference_models_services()
        return super().__enter__()

    @staticmethod
    def __reference_models_services():
        return Topology().get_models_from_libs()
