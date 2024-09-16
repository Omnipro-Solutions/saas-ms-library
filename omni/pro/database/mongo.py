import ast

import mongoengine as mongo
from bson import ObjectId
from omni.pro.airflow.actions import ActionToAirflow
from omni.pro.exceptions import AlreadyExistError, NotFoundError
from omni.pro.response import MessageResponse
from omni_pro_base.logger import LoggerTraceback, configure_logger
from omni_pro_grpc.common import base_pb2
from pymongo import UpdateOne
import ast
import time

logger = configure_logger(name=__name__)


class DatabaseManager(object):
    def __init__(self, host: str, port: int, db: str, user: str, password: str, complement: dict) -> None:
        """
        :param db_object: Database object
        Example:
            db_object = {
                "host":"mongo",
                "port":"27017",
                "user":"root",
                "password":"123456",
                "type":"write | read",
                "no_sql":"true",
                "complement":""
            }
        """
        self.db = db
        self.host = host
        self.port = port
        self.username = user
        self.password = password
        self.complement = complement
        # self.get_connection().connect()

    def get_connection(self):
        return MongoConnection(
            db=self.db,
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            complement=self.complement,
        )

    def create_document(self, db_name: str, document_class, **kwargs) -> object:
        document = document_class(**kwargs)
        document.save()
        return document

    def get_document(self, db_name: str, tenant: str, document_class, **kwargs) -> object:
        document = document_class.objects(**kwargs, context__tenant=tenant).first()
        # document.to_proto()
        return document

    def update_document(self, db_name: str, document_class, id: str, **kwargs) -> object:
        document = document_class.objects(id=id).first()
        document_class.objects(id=document.id).first().update(**kwargs)
        document.reload()
        if not document.__is_replic_table__:
            ActionToAirflow.send_to_airflow(
                document_class,
                document,
                action="update",
                context={"tenant": document.context.tenant, "user": document.context.user},
                **kwargs,
            )
        return document

    def update(self, document_instance, **kwargs):
        document_instance.update(**kwargs)
        document_instance.reload()
        if not document_instance.__is_replic_table__:
            ActionToAirflow.send_to_airflow(
                document_instance.__class__,
                document_instance,
                action="update",
                context={"tenant": document_instance.context.tenant, "user": document_instance.context.user},
                **kwargs,
            )
        return document_instance

    def delete(self, document_instance):
        document_instance.delete()
        return document_instance

    def delete_document(self, db_name: str, document_class, id: str) -> object:
        document = document_class.objects(id=id).first()
        document.delete()
        return document

    def list_documents(
        self,
        db_name: str,
        tenant: str,
        document_class,
        fields: list = None,
        filter: dict = None,
        group_by: str = None,
        paginated: dict = None,
        sort_by: list = None,
        str_filter: str = None,
    ) -> tuple[list, int]:
        """
        Recupera una lista de documentos basada en los filtros y la paginación proporcionados.

        Parameters:
        fields (list): Lista opcional de campos a recuperar.
        filter (dict): Diccionario opcional con criterios de filtrado.
        group_by (str): Campo opcional para agrupar resultados.
        paginated (dict): Diccionario opcional con información de paginación.
        sort_by (list): Lista opcional de campos para ordenar resultados.

        Returns:
        tuple: Una lista de documentos que coinciden con los criterios especificados y el conteo total.
        """
        start_time = time.time()
        
        documents = []
        total_count = 0

        # Convertir filtro de string a diccionario si está presente
        str_filter = str(str_filter).replace("true", "True").replace("false", "False")
        filter_conditions = ast.literal_eval(str_filter) if str_filter else {}
        
        # Agregar el filtro por tenant
        filter_cursor = {"context.tenant": tenant}

        # Verificar si el filtro contiene referencias y si se debe usar _list_documents
        if filter_conditions and self._is_reference_in_filter(document_class=document_class, filter_conditions=filter_conditions):
            # Si hay referencias, llamar a _list_documents
            query_set = self._list_documents(tenant, filter_conditions, None, document_class, paginated, sort_by)
            return query_set, len(query_set)

        # Manejar el filtro si está presente
        collection = document_class._get_collection()
        with collection.database.client.start_session() as session:
            try:
                # Si no hay filtros complejos, trabajar con el cursor de PyMongo
                if filter:
                    query_set = document_class.objects(context__tenant=tenant).filter(__raw__=filter)
                else:
                    query_set = collection.find(filter_cursor, session=session, no_cursor_timeout=True).batch_size(100)

                # Aplicar los campos especificados si existen
                if fields:
                    query_set = query_set.only(*fields)
                    
                if group_by:
                    query_set = query_set.only(*fields)
                    
                # Aplicar paginación si está presente
                if paginated:
                    page = int(paginated.get("page") or 1)
                    per_page = int(paginated.get("per_page") or 10)
                    start = (page - 1) * per_page
                    end = start + per_page
                    query_set = query_set[start:end]

                # Aplicar ordenamiento si está presente
                if sort_by:
                    query_set = query_set.order_by(*sort_by)

                # Procesar los documentos del cursor si es PyMongo
                if not isinstance(query_set, list) and not hasattr(query_set, 'count'):
                    for doc in query_set:
                        documents.append(document_class._from_son(doc))

                    total_count = collection.count_documents(filter_cursor, session=session)
                    # # Usar agregación para contar el total de documentos coincidentes
                    # pipeline = [
                    #     {"$match": filter_cursor}, 
                    #     {"$count": "total"}  
                    # ]
                    # result = list(collection.aggregate(pipeline, session=session))
                    # total_count = result[0]["total"] if result else 0
                    # total_count = collection.count_documents(filter_conditions, session=session)
                else:
                    documents = list(query_set)
                    total_count = query_set.count()

            except Exception as e:
                print(f"Error occurred during query execution: {e}")
            finally:
                elapsed_time = time.time() - start_time
                print(f"Elapsed time: {elapsed_time}")

        return documents, total_count
    
    def _is_reference_in_filter(self, document_class, filter_conditions: list):
        for condition in filter_conditions:
            if isinstance(condition, tuple):
                field, operator, value = condition
                if "__" in field or "." in field:
                    if any(
                        map(
                            lambda x: (
                                isinstance(getattr(document_class, x), mongo.fields.ReferenceField)
                                if hasattr(document_class, x)
                                else {}
                            ),
                            field.replace("__", ".").split(".")[:-1],
                        )
                    ):
                        return True
        return False

    def _list_documents(
        self, tenant: str, filter_conditions: list, id: str, document_class, paginated: dict, sort: list = None
    ) -> list:
        # filter = ["or", ("active","=",True), "and", ("appointment__id", "=", "65e1e7c1379356701b5f6b59"), ("context.tenant.value","=","TEST")]
        pipeline = self.parse_expression_to_pipeline(
            document_class=document_class,
            filter_conditions=filter_conditions,
            id=id,
            paginated=paginated,
            sort=sort,
        )

        query_set = []
        for item in document_class._get_collection().aggregate(pipeline):
            inst = document_class._from_son(item)
            inst.reload()
            query_set.append(inst)
        return query_set

    def parse_expression_to_pipeline(
        self, document_class, filter_conditions: list, id: str, sort: list = None, paginated: dict = None
    ) -> list:
        pipeline = []
        operator_mapping = {
            "=": "$eq",
            ">": "$gt",
            "<": "$lt",
            ">=": "$gte",
            "<=": "$lte",
            "in": "$in",
            "nin": "$nin",
            "!=": "$ne",
            "!like": "$not",
            "like": "$regex",
            "ilike": "$regex",
        }
        # Agregar filtro por _id si está presente
        if id:
            pipeline.append({"$match": {"_id": ObjectId(id)}})

        # Preparar para condiciones de filtro
        else:
            stack = []
            for condition in reversed(filter_conditions):
                if isinstance(condition, tuple):
                    field, operator, value = condition
                    mongo_operator = operator_mapping.get(operator)
                    parts = field.split("__") if "__" in field else field.split(".")

                    # Construir referencia para campos de múltiples niveles
                    ref_field = ""
                    for i, part in enumerate(parts[:-1]):
                        if i > 0:
                            ref_field += "."
                        ref_field += part

                        # Determinar si el campo actual es un campo de referencia
                        field_obj = getattr(document_class, parts[0], None)
                        for sub_part in parts[1 : i + 1]:
                            field_obj = (
                                getattr(field_obj.document_type, sub_part, None)
                                if field_obj and hasattr(field_obj, "document_type")
                                else None
                            )

                        if field_obj and isinstance(field_obj, mongo.fields.ReferenceField):
                            pipeline.append(
                                {
                                    "$lookup": {
                                        "from": field_obj.document_type._meta["collection"],
                                        "localField": f"{ref_field}",
                                        "foreignField": "_id",
                                        "as": ref_field,
                                    }
                                }
                            )
                            pipeline.append({"$unwind": f"${ref_field}"})

                    if parts[-1] == "id":
                        value = ObjectId(value)
                        parts[-1] = "_id"

                    # condition = {".".join(parts): value}
                    # Manejo especial para 'like' y '!like', asumiendo que usas expresiones regulares
                    if operator in ["like", "ilike"]:
                        condition = {".".join(parts): {"$regex": value, "$options": "i"}}
                    elif operator == "!like":
                        condition = {".".join(parts): {"$not": {"$regex": value, "$options": "i"}}}
                    else:
                        # Asegurar el mapeo correcto para otros operadores
                        if mongo_operator:
                            condition = {".".join(parts): {mongo_operator: value}}
                        else:
                            raise ValueError(f"Operador no soportado: {operator}")
                    stack.append(condition)
                else:
                    # Combinar condiciones usando el operador
                    conditions = {f"${condition}": stack}
                    stack = [conditions]

            if stack:
                pipeline.append({"$match": stack[0]})

        # Añadir ordenamiento si está presente
        if sort:
            pipeline.append({"$sort": {item[1:]: 1 if item.startswith("+") else -1 for item in sort}})

        # Añadir paginación si está presente
        if paginated:
            page = max(paginated.get("page", 1), 1)  # Asegurar que la página sea al menos 1
            per_page = max(paginated.get("per_page", 10), 1)  # Asegurar que per_page sea positivo
            skip_amount = (page - 1) * per_page
            if skip_amount >= 0:  # Añadir skip solo si es no negativo
                pipeline.append({"$skip": skip_amount})
            pipeline.append({"$limit": per_page})

        return pipeline

    def delete_documents(self, db_name, document_class, **kwargs):
        # with self.get_connection() as cnn:
        document = document_class.objects(**kwargs).delete()
        return document

    def update_embeded_document(
        self,
        db_name: str,
        document_class,
        filters: dict,
        update: dict,
        many: bool = False,
    ) -> object:
        # with self.get_connection() as cnn:
        if many:
            document_class.objects(**filters).update(**update)
            document = document_class.objects(**filters)
        else:
            document_class.objects(**filters).update_one(**update)
            document = document_class.objects(**filters).first()
        return document

    def batch_upsert(self, document_isntance, data):
        """
        Batch upserts a list of records into the database.
        Actualiza por lotes una lista de registros en la base de datos.

        Args:
            document_isntance(mongoengine.Document): The MongoEngine model to upsert into.
            data (list): A list of dictionaries containing the records to upsert.
        """

        bulk_operations = [
            UpdateOne(
                {"external_id": obj["external_id"]},
                {"$set": obj | {"tenant": data["context"]["tenant"], "updated_by": data["context"]["user"]}},
                upsert=True,
            )
            for obj in data["models"]
        ]
        result = document_isntance._get_collection().bulk_write(bulk_operations, ordered=False)
        return result

    def add_or_remove_document_relations(
        self,
        context,
        document,
        exsitent_relations_list,
        new_relations_list,
        attribute_search,
        request_context,
        element_name,
        element_relation_name,
        multiple_params=False,
        params_multiple: tuple = None,
    ):
        """
        The add_or_remove_document_relations function process and get registers to remove and add, to apply changes and return a list of result.
        La función add_or_remove_document_relations procesa y obtiene registros para eliminar y agregar, para aplicar cambios y devolver una lista de resultados.

        Args:
        context: Context of the request. Contexto de la petición.
        document: Class document to validate. Clase documento a validar.
        tenant: Tenant of request. Tenant de la petición.
        exsitent_relations_list: List of realtion to validate. Lista de relaciones a validar.
        new_relations_list: List to add or remove. Lista a agregar o eliminar.
        attribute_search: Attribute to search. Atributo a buscar.
        request_context: Context of the request. Contexto de la petición.
        element_name: Model name. Nombre del modelo.
        element_relation_name: Relation name. Nombre de la relación.
        multiple_params: If the search is by multiple params. Si la búsqueda es por múltiples parámetros.

        Returns:
        The list of relations process.
        La lista de relaciones procesadas.
        """

        relations_list = set([x.__getattribute__(attribute_search) for x in exsitent_relations_list])
        set_new_relations_list = set(
            new_relations_list if multiple_params is False else [x["code"] for x in new_relations_list]
        )

        if multiple_params:
            add_relations_list = [item for item in new_relations_list if item["code"] not in relations_list]
            remove_relations_list = [
                item for item in exsitent_relations_list if item.code not in set_new_relations_list
            ]
            remove_relations_list = [
                {key: getattr(item, key) for key in params_multiple} for item in remove_relations_list
            ]
        else:
            add_relations_list = list(set_new_relations_list - relations_list)
            remove_relations_list = list(relations_list - set_new_relations_list)
        result_list = []

        result_list = self.remove_document_relations(
            context,
            document,
            remove_relations_list,
            exsitent_relations_list,
            attribute_search,
            request_context,
            element_name,
            element_relation_name,
            multiple_params,
        )
        result_list = self.add_document_relations(
            context,
            document,
            add_relations_list,
            result_list,
            attribute_search,
            request_context,
            element_name,
            element_relation_name,
            multiple_params,
        )
        return result_list

    def remove_document_relations(
        self,
        context,
        document,
        list_elements,
        list_registers,
        attribute_search,
        request_context,
        element_name,
        element_relation_name,
        multiple_params=False,
    ):
        """
        The remove_document_relations function remove resgisters of list_registers the elements defined on list_elements.
        La función remove_document_relations elimina registros de list_registers los elementos definidos en list_elements.

        Args:
        context: Context of the request. Contexto de la petición.
        document: Class document to validate. Clase documento a validar.
        list_elements: List of realtion to remove. Lista de relaciones a eliminar.
        list_registers: List to add or remove. Lista a agregar o eliminar.
        attribute_search: Attribute to search. Atributo a buscar.
        request_context: Context of the request. Contexto de la petición.
        element_name: Model name. Nombre del modelo.
        element_relation_name: Relation name. Nombre de la relación.
        multiple_params: If the search is by multiple params. Si la búsqueda es por múltiples parámetros.

        Returns:
        The list of relations process.
        La lista de relaciones procesadas.
        """
        for element in list_elements:
            register = self.get_register(attribute_search, context, document, element, request_context, multiple_params)
            if register not in list_registers:
                raise NotFoundError(message=f"{element_name} {element} not defined in {element_relation_name}")
            list_registers.remove(register)

        return list_registers

    def add_document_relations(
        self,
        context,
        document,
        list_elements,
        list_registers,
        attribute_search,
        request_context,
        element_name,
        element_relation_name,
        multiple_params=False,
    ):
        """
        The add_document_relations function add resgisters to list_registers from elements defined on list_elements.
        La función add_document_relations agrega registros a list_registers de elementos definidos en list_elements.

        Args:
        context: Context of the request. Contexto de la petición.
        document: Class document to validate. Clase documento a validar.
        list_elements: List of realtion to add. Lista de relaciones a agregar.
        list_registers: List to add or remove. Lista a agregar o eliminar.
        attribute_search: Attribute to search. Atributo a buscar.
        request_context: Context of the request. Contexto de la petición.
        element_name: Model name. Nombre del modelo.
        element_relation_name: Relation name. Nombre de la relación.
        multiple_params: If the search is by multiple params. Si la búsqueda es por múltiples parámetros.

        Returns:
        The list of relations process.
        La lista de relaciones procesadas.
        """
        for element in list_elements:
            register = self.get_register(attribute_search, context, document, element, request_context, multiple_params)
            if not register:
                raise NotFoundError(message=f"{element_name} {element} not found")
            if register in list_registers:
                raise AlreadyExistError(message=f"{element_name} {element} already added in {element_relation_name}")
            list_registers.append(register)

        return list_registers

    def get_register(self, attribute_search, context, document, element, request_context, multiple_params):
        """
        The get_register function get resgister from diferent type search by id or get_or_sync.
        La función get_register obtiene el registro de la búsqueda de diferentes tipos por id o get_or_sync.

        Args:
        attribute_search: Attribute to search. Atributo a buscar.
        context: Context of the request. Contexto de la petición.
        document: Class document to validate. Clase documento a validar.
        element: Element to search. Elemento a buscar.
        request_context: Context of the request. Contexto de la petición.
        multiple_params: If the search is by multiple params. Si la búsqueda es por múltiples parámetros.

        Returns:
        Object of the register.
        Objeto del registro.
        """
        if attribute_search == "id":
            return context.db_manager.get_document(
                context.db_name, request_context.get("tenant"), document, **{attribute_search: element}
            )
        if multiple_params:
            return document.get_or_sync(request_context, **element)
        return document.get_or_sync(request_context, **{attribute_search: element})

    def read_response(
        self,
        request,
        context,
        document_class,
        message_response: MessageResponse,
        msg_success: str,
        msg_exception: str,
        entry_field_name: str,
        **kwargs,
    ):
        """
        :param request: request is a Message grpc\n
        :param context: context is a Message grpc with db_manager, db_name field\n
        :param document_class: document_class is a Document class\n
        :param reference_list: reference_list is a list of Document class\n
        :param message_response: message_response is a MessageResponse instance\n
        :param msg_success: msg_success is a success message\n
        :param msg_exception: msg_exception is a exception message\n
        :return: MessageResponse cls param
        """
        try:
            data = DBUtil.db_prepared_statement(
                request.id,
                request.fields,
                request.filter,
                request.paginated,
                None,
                request.sort_by,
            )
            list_docs, total = self.list_documents(
                context.db_name,
                request.context.tenant,
                document_class,
                **data,
            )
            kwargs_return = {
                f"{entry_field_name}": [doc.to_proto() for doc in list_docs],
            } | kwargs
            return message_response.fetched_response(
                message=msg_success,
                total=total,
                count=len(list_docs),
                id=request.id,
                paginated=request.paginated,
                **kwargs_return,
            )
        except ValueError as e:
            LoggerTraceback.error("Input request data validation error", e, logger)
            return message_response.input_validator_response(message=str(e))
        except Exception as e:
            LoggerTraceback.error(msg_exception, e, logger)
            return message_response.internal_response(message=msg_exception)


class MongoConnection(object):
    """A MongoConnection class that can dynamically connect to a MongoDB database with MongoEngine and close the connection after each query.

    Args:
        host (str): The hostname or IP address of the MongoDB server.
        port (int): The port number of the MongoDB server.
        username (str): The username for the MongoDB database.
        password (str): The password for the MongoDB database.
        database (str): The name of the MongoDB database.
    """

    def __init__(self, host, port, db, username, password, complement):
        self.host = f"mongodb://{host}:{port}/?{'&'.join([f'{k}={v}' for (k, v) in complement.items()])}"
        self.port = port
        self.username = username
        self.password = password
        self.db = db

    def connect(self):
        """Connects to the MongoDB database.

        Returns:
            A MongoEngine connection object.
        """
        self.connection = mongo.connect(
            db=self.db,
            username=self.username,
            password=self.password,
            host=self.host,
        )
        return self.connection

    def close(self):
        """Closes the connection to the MongoDB database."""
        # self.connection.close()
        mongo.disconnect()

    def __enter__(self):
        """Enters a context manager.

        Returns:
            A MongoConnection object.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exits a context manager."""
        self.close()


class PolishNotationToMongoDB:
    def __init__(self, expression):
        self.expression = expression
        self.operators_logical = {
            "and": "$and",
            "or": "$or",
            "nor": "$nor",
            "not": "$not",
        }
        self.operators_comparison = {
            "=": "$eq",
            ">": "$gt",
            "<": "$lt",
            ">=": "$gte",
            "<=": "$lte",
            "in": "$in",
            "nin": "$nin",
            "!=": "$ne",
            "not_like": "$not",
            "!like": "$not",
            "not_ilike": "$not",
            "!ilike": "$not",
            "like": "$regex",
            "ilike": "$regex",
        }

    def is_logical_operator(self, token):
        if not isinstance(token, str):
            return False
        return token in self.operators_logical

    def is_comparison_operator(self, token):
        if not isinstance(token, str):
            return False
        return token in self.operators_comparison

    def is_tuple(self, token):
        return isinstance(token, tuple) and len(token) == 3

    def convert(self):
        operand_stack = []
        operator_stack = []

        for token in reversed(self.expression):
            if self.is_logical_operator(token):
                operator_stack.append(token)
            elif self.is_comparison_operator(token):
                operator_stack.append(token)
            elif self.is_tuple(token):
                field, old_operator, value = token
                if old_operator in self.operators_comparison:
                    options = {}
                    if old_operator in ["like", "ilike"]:
                        options = {"$options": "i"}
                    elif old_operator in ["not_like", "!like", "not_ilike", "!ilike"]:
                        options = {
                            self.operators_comparison[old_operator]: {
                                "$regex": value,
                                "$options": "i",
                            }
                        }
                    operand_stack.append({field: {self.operators_comparison[old_operator]: value} | options})
                else:
                    raise ValueError(f"Unexpected operator: {old_operator}")
            else:
                raise ValueError(f"Unexpected token: {token}")

        while operator_stack:
            operator = operator_stack.pop()
            if operator in self.operators_logical:
                operands = []
                for _ in range(2):
                    operands.append(operand_stack.pop())
                operand_stack.append({self.operators_logical[operator]: operands})
            else:
                raise ValueError(f"Unexpected operator: {operator}")

        return operand_stack.pop()


class DBUtil(object):
    @classmethod
    def db_prepared_statement(
        cls,
        id: str,
        fields: base_pb2.Fields,
        filter: base_pb2.Filter,
        paginated: base_pb2.Paginated,
        group_by: base_pb2.GroupBy,
        sort_by: base_pb2.SortBy,
    ) -> dict:
        prepared_statement = {}
        prepared_statement["paginated"] = {
            "page": paginated.offset,
            "per_page": paginated.limit or 10,
        }
        if (ft := filter.ListFields()) or id:
            expression = [("_id", "=", cls.generate_object_id(id))]
            if ft:
                str_filter = filter.filter.replace("true", "True").replace("false", "False").replace("__", ".")
                expression = ast.literal_eval(str_filter)
                # reemplace filter id by _id and convert to ObjectId
                for idx, exp in enumerate(expression):
                    if isinstance(exp, tuple) and len(exp) == 3 and exp[0] == "id":
                        if type(exp[2]) == list:
                            expression[idx] = (
                                "_id",
                                exp[1],
                                [cls.generate_object_id(x) for x in exp[2]],
                            )
                            continue
                        expression[idx] = (
                            "_id",
                            exp[1],
                            cls.generate_object_id(exp[2]),
                        )
            filter_custom = PolishNotationToMongoDB(expression=expression).convert()
            prepared_statement["filter"] = filter_custom
        if group_by:
            prepared_statement["group_by"] = [x.name_field for x in group_by]
        if sort_by.ListFields():
            prepared_statement["sort_by"] = [cls.db_trans_sort(sort_by)]
        if fields:
            prepared_statement["fields"] = fields.name_field
        return prepared_statement | {"str_filter": filter.filter}

    @classmethod
    def db_trans_sort(cls, sort_by: base_pb2.SortBy) -> str:
        if not sort_by.name_field:
            return None
        return f"{'-' if sort_by.type == sort_by.DESC else '+'}{sort_by.name_field}"

    @classmethod
    def generate_object_id(cls, id=None):
        try:
            return ObjectId(id)
        except:
            return ObjectId(None)
