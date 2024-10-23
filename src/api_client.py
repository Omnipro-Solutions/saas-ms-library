import requests


def get_location(ip_address):
    """
    Get location information from IP address
    :type ip_address: str
    :param ip_address: IP address
    :rtype: dict
    :return: Location information
    Example:
        ip_address = "167.0.225.46"
        get_location(ip_address)
    """
    url = f"https://freeipapi.com/api/json/{ip_address}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    # import ipdb

    # ipdb.set_trace()
    return data
