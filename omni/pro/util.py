import hashlib
import json
import logging
import math
import secrets
import string
import time
import unicodedata
from functools import reduce, wraps

from omni.pro.exceptions import AlreadyExistError, NotFoundError
from omni.pro.stack import ExitStackDocument

logger = logging.getLogger(__name__)

DEFAULT_RECORD_LIMIT = 10000


def generate_strong_password(length=12):
    if length < 8:
        raise ValueError("The password length must be at least 8 characters.")

    punctuation = "!#$%&()*?@[]}{"
    characters = string.ascii_letters + string.digits + punctuation

    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(punctuation),
    ]

    for _ in range(length - 4):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)
    password_str = "".join(password)

    return password_str


def nested(data: dict, keys: str, default=None):
    """
    Receives a dictionary and a list of keys, and returns the value associated with the keys in order,
    searching the dictionary to any depth, not including lists. in order, searching the dictionary to
    any depth, not including lists. If the key is not found, it returns the default value.
    """
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), data)


def deep_search(lst, key=None, value=None, default=None):
    """
    Searches an item in a list in depth by key or value.

    Args:
        lst (list): the list to search.
        key (str): The key to search for.
        value: The value to search for.

    Returns:
        The element found or None if it was not found.
    """
    if isinstance(lst, dict):
        if key in lst and lst[key] == value:
            return lst
        for v in lst.values():
            if isinstance(v, (dict, list)):
                result = deep_search(v, key=key, value=value)
                if result is not None:
                    return result
    elif isinstance(lst, list):
        for elem in lst:
            if isinstance(elem, (dict, list)):
                result = deep_search(elem, key=key, value=value)
                if result is not None:
                    return result
            elif key is None and elem == value:
                return elem
            elif isinstance(elem, dict) and key in elem and elem[key] == value:
                return elem
    return default


def load_file_module(file_path: str, class_name: str):
    """
    Loads a module from a file.

    Args:
        file_path (str): The path to the file.
        class_name (str): The name of the class.

    Returns:
        The module loaded.
    """
    import importlib.util

    spec = importlib.util.spec_from_file_location(class_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def paginate_list(objects_list, page_num, per_page, filters=None):
    filtered_list = objects_list
    if filters:
        filtered_list = [o for o in objects_list if o.attr == filters["attr"]]
    start = (page_num - 1) * per_page
    end = start + per_page
    paginated_list = filtered_list[start:end]
    total_pages = int(math.ceil(len(filtered_list) / per_page))
    return paginated_list, total_pages


def parse_bool(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.lower() in ("yes", "true", "t", "1", "y")
    return bool(value)


def to_camel_case(text: str):
    # Divide el texto por guiones bajos y une cada palabra con la primera letra en mayúsculas
    return "".join(word.capitalize() for word in text.split("_"))


def normalize(value):
    return unicodedata.normalize("NFKD", str(value).strip()).encode("ascii", "ignore").decode("UTF-8")


class HTTPStatus(object):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    CONFLICT = 409
    UNPROCESSABLE_ENTITY = 422
    INTERNAL_SERVER_ERROR = 500


class Resource(object):
    AWS_COGNITO = "cognito"
    MONGODB = "mongodb"
    POSTGRES = "postgres"


def generate_hash(obj):
    # Convertir el objeto a una cadena con claves ordenadas
    obj_str = json.dumps(obj, sort_keys=True)

    # Generar un hash SHA-256
    return hashlib.sha256(obj_str.encode()).hexdigest()


def merge_and_remove_key(data_dict, key_to_remove):
    """
    Merge and remove key from a dictionary.
    Fusiona y elimina una clave de un diccionario.

    Args:
    data_dict (dict): The original dictionary. El diccionario original.
    key_to_remove (str): The key to be removed and merged. La clave a eliminar y fusionar.

    Returns:
    dict: A dictionary with the key removed and its values merged. Un diccionario con la clave eliminada y sus valores fusionados.
    """
    extracted_data = data_dict.pop(key_to_remove, {})
    return {**extracted_data, **data_dict}


def measure_time(function):
    """
    Decorator to measure the execution time of a function.
    Decorador para medir el tiempo de ejecución de una función.

    Args:
    function (callable): The function to be measured.
    función (callable): La función a medir.

    Returns:
    callable: The wrapped function that measures its execution time.
    callable: La función envuelta que mide su tiempo de ejecución.
    """

    @wraps(function)
    def measured_function(*args, **kwargs):
        """
        The wrapped function that calculates the time taken to execute the original function.
        La función envuelta que calcula el tiempo que tarda en ejecutarse la función original.

        Args:
        *args: Variable length argument list for the original function.
        *args: Lista de argumentos de longitud variable para la función original.

        **kwargs: Arbitrary keyword arguments for the original function.
        **kwargs: Argumentos de palabras clave arbitrarias para la función original.

        Returns:
        The result of the original function.
        El resultado de la función original.
        """
        start = time.time()
        result = function(*args, **kwargs)
        elapsed_time = time.time() - start
        logger.info(f"Func: {function.__qualname__} - Time: {elapsed_time:.2f} seconds")
        return result

    return measured_function


def add_or_remove_document_relations(
    context,
    document,
    exsitent_relations_list,
    new_relations_list,
    attribute_search,
    request_context,
    element_name,
    element_relation_name,
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

    Returns:
    The list of relations process.
    La lista de relaciones procesadas.
    """

    relations_list = set([x.__getattribute__(attribute_search) for x in exsitent_relations_list])
    new_relations_list = set(new_relations_list)

    remove_relations_list = list(relations_list - new_relations_list)
    add_relations_list = list(new_relations_list - relations_list)

    result_list = []

    result_list = remove_document_relations(
        context,
        document,
        remove_relations_list,
        exsitent_relations_list,
        attribute_search,
        request_context,
        element_name,
        element_relation_name,
    )
    result_list = add_document_relations(
        context,
        document,
        add_relations_list,
        result_list,
        attribute_search,
        request_context,
        element_name,
        element_relation_name,
    )
    return result_list


def remove_document_relations(
    context,
    document,
    list_elements,
    list_registers,
    attribute_search,
    request_context,
    element_name,
    element_relation_name,
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

    Returns:
    The list of relations process.
    La lista de relaciones procesadas.
    """
    with ExitStackDocument(document_classes=document.reference_list(), db_alias=context.db_name):
        for element in list_elements:
            register = get_register(attribute_search, context, document, element, request_context)
            if register not in list_registers:
                raise NotFoundError(message=f"{element_name} {element} not defined in {element_relation_name}")
            list_registers.remove(register)

        return list_registers


def add_document_relations(
    context,
    document,
    list_elements,
    list_registers,
    attribute_search,
    request_context,
    element_name,
    element_relation_name,
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

    Returns:
    The list of relations process.
    La lista de relaciones procesadas.
    """
    with ExitStackDocument(document_classes=document.reference_list(), db_alias=context.db_name):
        for element in list_elements:
            register = get_register(attribute_search, context, document, element, request_context)
            if not register:
                raise NotFoundError(message=f"{element_name} {element} not found")
            if register in list_registers:
                raise AlreadyExistError(message=f"{element_name} {element} already added in {element_relation_name}")
            list_registers.append(register)

        return list_registers


def get_register(attribute_search, context, document, element, request_context):
    """
    The get_register function get resgister from diferent type search by id or get_or_sync.
    La función get_register obtiene el registro de la búsqueda de diferentes tipos por id o get_or_sync.

    Args:
    attribute_search: Attribute to search. Atributo a buscar.
    context: Context of the request. Contexto de la petición.
    document: Class document to validate. Clase documento a validar.
    element: Element to search. Elemento a buscar.
    request_context: Context of the request. Contexto de la petición.

    Returns:
    Object of the register.
    Objeto del registro.
    """
    if attribute_search == "id":
        return context.db_manager.get_document(
            context.db_name, request_context.get("tenant"), document, **{attribute_search: element}
        )

    return document.get_or_sync(request_context, **{attribute_search: element})


def objects_to_integer(data, fields):
    """
    Transform dictionary keys and values according to specified fields.

    Args:
    data (dict): The input dictionary to transform. El diccionario de entrada para transformar.
    fields (set): A set of field names to consider for transformation. Una conjunto de nombres de campo a considerar para la transformación.

    Returns:
    dict: A transformed dictionary with modified keys and values. Un diccionario transformado con claves y valores modificados.
    """
    transformed_data = {}
    for key, value in data.items():
        new_key = key
        if key in fields:
            new_key = key + "_id" if not key.endswith("_id") else key
            if isinstance(value, dict):
                # If any key in the inner dictionary ends with "_doc_id", use its value
                doc_id_key = next((k for k in value.keys() if k.endswith("_doc_id")), None)
                if doc_id_key:
                    transformed_data[new_key] = value[doc_id_key]
                elif "id" in value:
                    transformed_data[new_key] = value["id"]
            else:
                transformed_data[new_key] = value
        else:
            transformed_data[new_key] = value
    return transformed_data
