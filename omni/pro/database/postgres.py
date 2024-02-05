import ast
import operator

from omni.pro.protos.common import base_pb2
from sqlalchemy import and_, asc, create_engine, desc, not_, or_
from sqlalchemy.orm import aliased, scoped_session, sessionmaker
from sqlalchemy.sql import cast, operators
from sqlalchemy.sql.sqltypes import Enum, String


class SessionManager:
    def __init__(self, base_url):
        self.base_url = base_url
        self.engine = create_engine(self.base_url)
        self.session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(self.session_factory)

    def __enter__(self):
        # Esto dará una sesión específica para el hilo/contexto actual
        return self.Session()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Cuando el contexto se cierra, la sesión se cierra y elimina.
        if exc_tb is None:
            self.Session.commit()
        else:
            self.Session.rollback()
        self.Session.remove()


class PostgresDatabaseManager(SessionManager):
    """
    Handles database operations specific to Postgres using SQLAlchemy.
    Maneja operaciones de base de datos específicas para Postgres usando SQLAlchemy.

    Args:
    name (str): Name of the database.
                Nombre de la base de datos.
    host (str): Host of the database.
                Host de la base de datos.
    port (str): Port of the database.
                Puerto de la base de datos.
    user (str): User to connect to the database.
                Usuario para conectarse a la base de datos.
    password (str): Password to connect to the database.
                    Contraseña para conectarse a la base de datos.
    """

    DEFAULT_PAGE_SIZE = 10

    def __init__(self, name: str, host: str, port: str, user: str, password: str):
        """
        Initializes the PostgresDatabaseManager with the given database details.
        Inicializa el PostgresDatabaseManager con los detalles de base de datos proporcionados.

        Args:
        name (str): Name of the database.
                    Nombre de la base de datos.
        host (str): Host of the database.
                    Host de la base de datos.
        port (str): Port of the database.
                    Puerto de la base de datos.
        user (str): User to connect to the database.
                    Usuario para conectarse a la base de datos.
        password (str): Password to connect to the database.
                        Contraseña para conectarse a la base de datos.
        """
        self.name = name
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.base_url = f"postgresql://{user}:{password}@{host}:{port}/{name}"
        super().__init__(self.base_url)

    def get_db_connection(self):
        """
        Retrieves a connection to the Postgres database.
        Recupera una conexión a la base de datos Postgres.

        Returns:
        (obj): Database connection object.
               Objeto de conexión a la base de datos.
        """
        return self.engine.connect()

    def create_new_record(self, model, session, **kwargs):
        """
        Creates a new record in the database using the provided model and session.
        Crea un nuevo registro en la base de datos usando el modelo y la sesión proporcionados.

        Args:
        model (Base): The SQLAlchemy model where the record will be created.
                      El modelo SQLAlchemy donde se creará el registro.
        session (Session): An instance of the database session, likely from SQLAlchemy.
                           Una instancia de la sesión de base de datos, probablemente de SQLAlchemy.
        **kwargs: Attributes and values that will be used to initialize the new record of the model.
                  Atributos y valores que se utilizarán para inicializar el nuevo registro del modelo.

        Returns:
        (obj): The new model record after being added to the session.
               El nuevo registro del modelo después de ser añadido a la sesión.
        """
        record = model(**kwargs)
        record.create(session)
        return record

    def retrieve_record(self, model, session, filters: dict):
        """
        Retrieves a single database record based on provided filters.
        Recupera un único registro de la base de datos basado en los filtros proporcionados.

        Args:
        model (Base): The SQLAlchemy model to query.
                      El modelo SQLAlchemy a consultar.
        session (Session): An instance of the database session.
                           Una instancia de la sesión de base de datos.
        filters (dict): A dictionary of attributes to filter the records by.
                        Un diccionario de atributos para filtrar los registros.

        Returns:
        (obj): The first record that matches the filters, or None if not found.
               El primer registro que coincida con los filtros, o None si no se encuentra.
        """
        return session.query(model).filter_by(**filters).first()

    def retrieve_records(self, model, session, filters: dict):
        """
        Retrieves database records based on provided filters.

        Args:
        model (Base): The SQLAlchemy model to query.
        session (Session): An instance of the database session.
        filters (dict): A dictionary of attributes to filter the records by.

        Returns:
        (objs): List of records that match with filters, or empty list if not found.
        """
        return session.query(model).filter_by(**filters).all()

    def retrieve_record_by_id(self, model, session, id: int):
        """
        Retrieves a single database record by its ID.
        Recupera un único registro de la base de datos por su ID.

        Args:
        model (Base): The SQLAlchemy model to query.
                      El modelo SQLAlchemy a consultar.
        session (Session): An instance of the database session.
                           Una instancia de la sesión de base de datos.
        id (int): The ID of the record to retrieve.
                  El ID del registro a recuperar.

        Returns:
        (obj): The record with the given ID, or None if not found.
               El registro con el ID dado, o None si no se encuentra.
        """
        return session.query(model).get(id)

    def list_records(
        self,
        model,
        session,
        id: int,
        fields: base_pb2.Fields,
        filter: base_pb2.Filter,
        group_by: base_pb2.GroupBy,
        sort_by: base_pb2.SortBy,
        paginated: base_pb2.Paginated,
    ):
        """
        Lists database records based on provided parameters.
        Lista registros de la base de datos basados en los parámetros proporcionados.

        Args:
        model (Base): The SQLAlchemy model to query.
                      El modelo SQLAlchemy a consultar.
        session (Session): An instance of the database session.
                           Una instancia de la sesión de base de datos.
        id (int): The ID of a specific record to retrieve.
                  El ID de un registro específico para recuperar.
        fields (base_pb2.Fields): Fields to be returned in the response.
                                  Campos a ser devueltos en la respuesta.
        filter (base_pb2.Filter): Conditions to filter the list of records.
                                  Condiciones para filtrar la lista de registros.
        group_by (base_pb2.GroupBy): Conditions to group the list of records.
                                     Condiciones para agrupar la lista de registros.
        sort_by (base_pb2.SortBy): Conditions to sort the list of records.
                                   Condiciones para ordenar la lista de registros.
        paginated (base_pb2.Paginated): Conditions for pagination of the records.
                                        Condiciones para la paginación de los registros.

        Returns:
        (list): A list of records based on the provided parameters.
                Una lista de registros basados en los parámetros proporcionados.
        """
        # records = QueryBuilder.build_filter(model, session, id, fields, filter, group_by, sort_by, paginated)

        # Uso de la clase
        query = session.query(model)

        if filter.ListFields():
            # Uso de la clase
            expression = ast.literal_eval(filter.filter)  # Tu expresión en notación polaca inversa
            # converter = PolishNotationToSQLAlchemy(model, expression)
            # filter_condition, aliases = converter.convert()

            # Aplicar el filtro a la consulta
            # for alias in aliases.values():
            #     query = query.join(alias)

            query = self.parse_expression(expression, query, model)

        if id:
            query = query.filter(model.id == id)

        if fields.ListFields():
            query = query.with_entities(*[getattr(model, f) for f in fields.name_field])

        if sort_by.ListFields():
            order_by_fields = self.build_sort_by(model, sort_by)
            query = query.order_by(*order_by_fields)

        total = query.count()

        page = paginated.offset or 1
        limit = paginated.limit or self.DEFAULT_PAGE_SIZE
        offset = (page - 1) * limit
        query = query.offset(offset).limit(limit)

        return query.all(), total

    def build_sort_by(self, model, sort_by: base_pb2.SortBy):
        field = getattr(model, sort_by.name_field)
        if sort_by.type == sort_by.DESC:
            return [desc(field)]
        return [asc(field)]

    def update_record(self, model, session, model_id, update_dict):
        """
        Update a database record of the given model with the specified changes.
        Actualiza un registro de base de datos del modelo dado con los cambios especificados.

        Args:
        model (Base): The SQLAlchemy model to update.
                      El modelo SQLAlchemy a actualizar.
        session (Session): An instance of the database session.
                           Una instancia de la sesión de base de datos.
        model_id: The ID of the record to update.
                  El ID del registro a actualizar.
        update_dict (dict): A dictionary of attributes and their new values.
                            Un diccionario de atributos y sus nuevos valores.

        Returns:
        (obj): The updated record, or None if not found.
               El registro actualizado, o None si no se encuentra.
        """
        record = session.query(model).get(model_id)
        if not record:
            return None

        for key, value in update_dict.items():
            setattr(record, key, value)

        record.update(session)
        return record

    def delete_record_by_id(self, model, session, model_id):
        """
        Delete a database record of the given model by its ID.
        Elimina un registro de base de datos del modelo dado por su ID.

        Args:
        model (Base): The SQLAlchemy model to delete from.
                      El modelo SQLAlchemy del que eliminar.
        session (Session): An instance of the database session.
                           Una instancia de la sesión de base de datos.
        model_id: The ID of the record to delete.
                  El ID del registro a eliminar.

        Returns:
        (bool): True if the record was deleted, False otherwise.
                Verdadero si el registro fue eliminado, Falso en caso contrario.
        """
        record = session.query(model).filter_by(id=model_id).first()
        if record:
            success = record.delete(session)
            if success:
                return True
        return False

    def batch_upsert(self, model, session, data: list):
        """
        Batch upserts a list of records into the database.
        Actualiza por lotes una lista de registros en la base de datos.

        Args:
        model (Base): The SQLAlchemy model to upsert into.
                      El modelo SQLAlchemy para actualizar.
        session (Session): An instance of the database session.
                           Una instancia de la sesión de base de datos.
        data (list): A list of dictionaries containing the records to upsert.
                     Una lista de diccionarios que contienen los registros para actualizar.

        Returns:
        (list): A list of records that were upserted.
                Una lista de registros que fueron actualizados.
        """
        upsert_list = []
        for registro in data["models"]:
            registro = registro | {"tenant": data["context"]["tenant"], "updated_by": data["context"]["user"]}
            obj = session.query(model).filter_by(external_id=registro["external_id"]).first()
            if obj:
                for key, value in registro.items():
                    setattr(obj, key, value)
            else:
                obj = model(**registro)

            upsert_list.append(obj)

        session.bulk_save_objects(upsert_list, update_changed_only=True)
        session.commit()
        external_ids = [result.external_id for result in upsert_list]
        batch_upsert_process = session.query(model.external_id).filter(model.external_id.in_(external_ids)).all()
        batch_upsert_process = [id[0] for id in batch_upsert_process]

        session.close()

        return [obj for obj in upsert_list if obj.external_id not in batch_upsert_process]

    def get_sqlalchemy_operator(self, op):
        """
        Devuelve el operador de SQLAlchemy correspondiente al operador en string.

        :param op: El operador en formato de string.
        :return: Operador de SQLAlchemy.
        """
        operator_mapping = {
            "=": operators.eq,
            "!=": operators.ne,
            "<": operators.lt,
            "<=": operators.le,
            ">": operators.gt,
            ">=": operators.ge,
            "like": operators.like_op,
            "ilike": operators.ilike_op,
            "in": operators.in_op,
            "not in": operators.notin_op,
            # Agrega más operadores según sea necesario
        }
        return operator_mapping.get(op)

    def resolve_field_and_joins(self, base_model, field_path):
        """
        Resuelve el campo y construye los joins necesarios.

        :param base_model: El modelo base de SQLAlchemy.
        :param field_path: El camino al campo, que puede incluir '__' para relaciones.
        :return: El atributo del modelo SQLAlchemy correspondiente y una lista de joins.
        """
        fields = field_path.split("__")
        model = base_model
        joins = []
        for field in fields[:-1]:
            relationship_property = getattr(model, field)
            model = relationship_property.property.mapper.class_
            joins.append(relationship_property)
        return getattr(model, fields[-1]), joins

    def parse_expression(self, expression, query, base_model):
        stack = []
        joins = []
        for item in reversed(expression):
            if isinstance(item, tuple):
                field_path, op, value = item
                field, join_path = self.resolve_field_and_joins(base_model, field_path)

                joins.extend(join_path)

                operator_func = self.get_sqlalchemy_operator(op)

                if not operator_func:
                    raise ValueError(f"Operador desconocido: {op}")

                # Casting a texto si es necesario
                if isinstance(field.type, Enum) and op in ["like", "ilike"]:
                    field = cast(field, String)

                clause = operator_func(field, value)
                stack.append(clause)
            elif item in ["and", "or"]:
                right = stack.pop()
                left = stack.pop()
                if item == "and":
                    stack.append(and_(left, right))
                else:
                    stack.append(or_(left, right))

        if len(stack) != 1:
            raise ValueError("Expresión inválida")

        for join in joins:
            query = query.join(join)
        return query.filter(stack[0])


class PolishNotationToSQLAlchemy:
    def __init__(self, model, expression):
        self.model = model
        self.expression = expression
        self.aliases = {}

    def is_logical_operator(self, token):
        return token in ["and", "or", "not"]

    def is_comparison_operator(self, token):
        return token in ["=", "!=", "like", "!like", "in", "nin", ">", "<", ">=", "<="]

    def is_tuple(self, token):
        return isinstance(token, tuple) and len(token) == 3

    def get_field(self, model, field_path):
        fields = field_path.split("__")
        for field in fields[:-1]:  # process relationships
            relationship = getattr(model, field, None)
            if relationship is None:
                raise AttributeError(f"No such relationship {field} on {model}")
            if relationship in self.aliases:
                model = self.aliases[relationship]
            else:
                alias = aliased(relationship.property.mapper.class_)
                self.aliases[relationship] = alias
                model = alias
        return getattr(model, fields[-1], None), model

    def create_filter(self, model, field_path, operator, value):
        field, model = self.get_field(model, field_path)
        if operator == "=":
            return field == value
        elif operator == "!=":
            return field != value
        elif operator == "like":
            return field.like(value)
        elif operator == "!like":
            return not_(field.like(value))
        elif operator == "in":
            return field.in_(value)
        elif operator == "nin":
            return not_(field.in_(value))
        elif operator == ">":
            return field > value
        elif operator == "<":
            return field < value
        elif operator == ">=":
            return field >= value
        elif operator == "<=":
            return field <= value
        else:
            raise ValueError(f"Unknown operator: {operator}")

    def convert(self):
        operand_stack = []

        for token in reversed(self.expression):
            if self.is_logical_operator(token):
                operands = [operand_stack.pop() for _ in range(2)]
                if token == "and":
                    operand_stack.append(and_(*operands))
                elif token == "or":
                    operand_stack.append(or_(*operands))
                elif token == "not":
                    operand_stack.append(not_(operands[0]))
            elif self.is_tuple(token):
                field_path, operator, value = token
                operand_stack.append(self.create_filter(self.model, field_path, operator, value))
            else:
                raise ValueError(f"Unexpected token: {token}")

        if len(operand_stack) != 1:
            raise ValueError("The expression does not resolve to a single operand.")

        return operand_stack[0], self.aliases


class QueryBuilder:
    filter_ops = {
        "=": operator.eq,
        "<": operator.lt,
        "<=": operator.le,
        ">": operator.gt,
        ">=": operator.ge,
        "!=": operator.ne,
        "in": lambda x, y: x.in_(y),
        "and": operator.and_,
        "or": operator.or_,
        "not": lambda x: ~(x),
    }
    DEFAULT_PAGE_SIZE = 10

    @classmethod
    def pre_to_in(cls, filters: base_pb2.Filter) -> list:
        str_filter = filters.filter.replace("true", "True").replace("false", "False")
        expression = ast.literal_eval(str_filter)
        stack = []
        result = []
        for item in expression:
            if isinstance(item, tuple):
                if stack:
                    result.append(item)
                    result.append(stack.pop())
                else:
                    result.append(item)
            else:
                stack.append(item)
        return result

    @classmethod
    def build_filter(
        cls,
        model,
        session,
        id: int,
        fields: base_pb2.Fields,
        filter: base_pb2.Filter,
        group_by: base_pb2.GroupBy,
        sort_by: base_pb2.SortBy,
        paginated: base_pb2.Paginated,
    ):
        query = session.query(model)

        if id:
            query = query.filter(model.id == id)

        if fields.ListFields():
            query = query.with_entities(*[getattr(model, f) for f in fields.name_field])

        if filter.ListFields():
            filter_custom = cls.pre_to_in(filter)
            query_filter = cls.build_query(model, filter_custom)
            query = query.filter(query_filter)

        if group_by:
            group_by_fields = cls.build_group_by(model, group_by)
            query = query.group_by(*group_by_fields)

        if sort_by.ListFields():
            order_by_fields = cls.build_sort_by(model, sort_by)
            query = query.order_by(*order_by_fields)

        """
            Retrieves a paginated list from a given query.

            Args:
            
            query (obj): The query object that needs pagination.
            paginated (obj): Contains pagination parameters such as offset and limit.

            Returns:
            
            tuple: A tuple containing the paginated list and the total count.
            
        """

        total = query.count()

        if paginated.ListFields():
            page = paginated.offset or 1
            limit = paginated.limit or cls.DEFAULT_PAGE_SIZE
            offset = (page - 1) * limit
            query = query.offset(offset).limit(limit)

        return query.all(), total

    @classmethod
    def build_query(cls, model, filters: list):
        query = None

        filter_operator = None
        for item in filters:
            if isinstance(item, str):
                filter_operator = item.lower()
                if filter_operator not in cls.filter_ops:
                    raise ValueError(f"Invalid filter operator: {filter_operator}")
            elif isinstance(item, tuple) and len(item) == 3:
                field, op, value = item
                if "." in field:
                    related, field = field.split(".")
                    related_model = getattr(model, related).property.argument
                    related_field = getattr(related_model, field)
                    related_query = cls.filter_ops[op](related_field, value)
                    query = cls.filter_ops[op](query, related_query) if query else related_query
                else:
                    field = getattr(model, field)
                    field_query = cls.filter_ops[op](field, value)
                    query = cls.filter_ops[filter_operator](query, field_query) if filter_operator else field_query
            else:
                raise ValueError(f"Invalid filter item: {item}")

        return query

    @classmethod
    def build_sort_by(cls, model, sort_by: base_pb2.SortBy):
        field = getattr(model, sort_by.name_field)
        if sort_by.type == sort_by.DESC:
            return [desc(field)]
        return [asc(field)]
