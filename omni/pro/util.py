import math
import secrets
import string
from functools import reduce


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


def paginate_list(objects_list, page_num, per_page, filters=None):
    filtered_list = objects_list
    if filters:
        filtered_list = [o for o in objects_list if o.attr == filters["attr"]]
    start = (page_num - 1) * per_page
    end = start + per_page
    paginated_list = filtered_list[start:end]
    total_pages = int(math.ceil(len(filtered_list) / per_page))
    return paginated_list, total_pages


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
