import logging

import pkg_resources
import pytz
from google.protobuf import json_format, struct_pb2, timestamp_pb2
from omni.pro.database.mongo import DatabaseManager
from omni_pro_base.util import *

logger = logging.getLogger(__name__)


def libraries_versions_installed():
    """
    Returns a dictionary with the installed versions of the libraries.
    """
    libraries = ["omni-pro", "omni-pro-base", "omni-pro-redis", "omni-pro-grpc"]
    versions = {}
    for library in libraries:
        try:
            version = pkg_resources.get_distribution(library).version
            versions[library.replace("-", "_")] = version
        except pkg_resources.DistributionNotFound:
            versions[library.replace("-", "_")] = "Not installed"
    return versions


def convert_model_alchemy_to_struct(model):
    return json_format.ParseDict(convert_to_serializable(model.model_to_dict()), struct_pb2.Struct())


def convert_model_mongo_to_struct(model):
    return json_format.ParseDict(convert_to_serializable(model.generate_dict()), struct_pb2.Struct())


def transform_timezone(date, context, return_as_string=False) -> datetime:
    """
    Transforms a given date to the user's timezone based on the provided context.

    Parameters:
    - date (str | datetime): The date to transform. It can be a string in the format "YYYY-MM-DD" or "YYYY-MM-DD HH:MM:SS", or a datetime object.
    - context (dict): A dictionary containing contextual information, including the user's identifier under the key "user".
    - return_as_string (bool): Indicates whether the transformed date should be returned as a string (True) or as a protobuf Timestamp object (False). Default is False.

    Returns:
    - datetime | str: The date transformed to the user's timezone. The return format depends on the value of `return_as_string`. If True, it returns a string in the format "YYYY-MM-DD HH:MM:SS". If False, it returns a protobuf Timestamp object.

    Exceptions:
    - ValueError: If the user is not found in the context or if the date format is invalid.

    Example usage:
    ```python
    from datetime import datetime

    context = {
        "user": "some_user_id"
    }
    date = "2024-06-06 12:34:56"
    transformed_date = transform_timezone(date, context, return_as_string=True)
    print(transformed_date)  # Output: "2024-06-06 08:34:56" (depending on the user's timezone)
    ```

    Implementation details:
    - The function uses the `UserChannel` class from the `omni.pro.initial` module to get user information.
    - If the user does not have a defined timezone, "UTC" is assumed by default.
    - The date is converted to a UTC-aware datetime object.
    - Then, the date is adjusted to the user's timezone.
    - Depending on the `return_as_string` parameter, the adjusted date is returned as a string or as a protobuf Timestamp object.

    """
    from omni.pro.initial import UserChannel

    user = UserChannel(context).get_user_by_sub(context.get("user"))
    if not user:
        raise ValueError("User not found")

    time_zone = user.timezone.code_name if user.timezone else "UTC"

    if isinstance(date, str):
        date_format = "%Y-%m-%d %H:%M:%S" if " " in date else "%Y-%m-%d"
        naive_date = datetime.strptime(date, date_format)
    elif isinstance(date, datetime):
        naive_date = date
    else:
        raise ValueError("Invalid date format. Must be a string or datetime object.")

    utc_date = naive_date.replace(tzinfo=pytz.utc)

    target_timezone = pytz.timezone(time_zone)

    transformed_date = utc_date.astimezone(target_timezone)

    if return_as_string:
        return transformed_date.strftime("%Y-%m-%d %H:%M:%S")
    else:
        timestamp = timestamp_pb2.Timestamp()
        timestamp.FromDatetime(transformed_date)
        return timestamp
