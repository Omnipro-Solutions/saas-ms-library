import hashlib
import json
import math
import secrets
import string
import unicodedata
import time
import logging
from functools import reduce, wraps

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
