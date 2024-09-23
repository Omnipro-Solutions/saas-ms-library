from contextlib import ExitStack
from mongoengine import context_managers as ctx_mgr
from omni.pro.topology import Topology
from typing import Dict, List, Set
from omni.pro.webhook.webhook_handler import WebhookHandler


class ExitStackDocument(ExitStack):
    """
    Context manager for dynamic management of an outbound callback stack for Documents.

    For example:
        with ExitStackDocument([DocumentClass1, DocumentClass2], "db_alias") as stack:
            DocumentClass1.objects.all()
            # All documents are swiched to their respective aliases.
    """

    def __init__(self, document_classes: list = [], db_alias="", context={}, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.document_classes = document_classes
        self.db_alias = db_alias
        self.model_classes = []
        self.created_attrs: Dict[str, List[int]] = {}
        self.updated_attrs: Dict[str, Dict[str, Set[str]]] = {}
        self.deleted_attrs: Dict[str, List[int]] = {}
        self.context: Dict[str, str] = context

    def __enter__(self):
        for document_class in self.document_classes:
            self.__create_collection(document_class)
            self.model_classes = self.enter_context(ctx_mgr.switch_db(document_class, self.db_alias))
            document_class.created_attrs = self.created_attrs
            document_class.updated_attrs = self.updated_attrs
            document_class.deleted_attrs = self.deleted_attrs
        return super().__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self._pull_crud_attrs()
        return super().__exit__(exc_type, exc_value, traceback)

    def __create_collection(self, document_class):
        document_class._meta["db_alias"] = self.db_alias
        db = document_class.db
        collection_name = document_class._get_collection_name()
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)

    def _pull_crud_attrs(self):
        """
        Extracts CRUD attributes from the context and initiates a new thread to handle webhooks.

        This method constructs a dictionary containing the `context` and CRUD attributes (created,
        updated, deleted) from the `ExitStackDocument` instance. It then calls
        `WebhookHandler.start_thread` to process these attributes in a separate thread.

        Attributes Extracted:
            - `context`: A dictionary containing the context, as provided during initialization.
            - `created_attrs`: A dictionary of attributes for created documents.
            - `updated_attrs`: A dictionary of attributes for updated documents.
            - `deleted_attrs`: A dictionary of attributes for deleted documents.

        Calls:
            - `WebhookHandler.start_thread(crud_attrs, context)`: Initiates a new thread to filter events
              and webhooks based on the extracted CRUD attributes and context.
        """

        crud_attrs = dict(
            created_attrs=self.created_attrs,
            updated_attrs=self.updated_attrs,
            deleted_attrs=self.deleted_attrs,
        )
        self.context["type_db"] = "document"
        WebhookHandler.start_thread(crud_attrs=crud_attrs, context=self.context)


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
