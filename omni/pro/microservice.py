from enum import Enum, unique


@unique
class MicroService(Enum):
    SAAS_MS_USER = "saas-ms-user"
    SAAS_MS_CATALOG = "saas-ms-catalog"
    SAAS_MS_UTILITIES = "saas-ms-utilities"
    SAAS_MS_STOCK = "saas-ms-stock"
    SAAS_MS_CLIENT = "saas-ms-client"
    SAAS_MS_SALE = "saas-ms-sale"
    SAAS_MS_RULE = "saas-ms-rule"

    @classmethod
    def valid_value(cls, value: str) -> bool:
        return value in cls._value2member_map_
class MicroServiceDocument(object):
    pass
