import os

from omni.pro.util import parse_bool


class Config(object):
    DEBUG = parse_bool(os.environ.get("DEBUG")) or False
    API_REFLECTION = parse_bool(os.environ.get("API_REFLECTION")) or False
    TESTING = parse_bool(os.environ.get("TESTING")) or False

    GRPC_PORT = os.environ.get("GRPC_PORT") or 50051
    GRPC_MAX_WORKERS = int(os.environ.get("GRPC_MAX_WORKERS") or 10)
    SERVICE_ID = os.environ.get("SERVICE_ID")
    REDIS_HOST = os.environ.get("REDIS_HOST") or "localhost"
    REDIS_PORT = int(os.environ.get("REDIS_PORT") or 6379)
    REDIS_DB = int(os.environ.get("REDIS_DB") or 0)
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_KEY")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET")
    REGION_NAME = os.environ.get("REGION_NAME") or "us-east-1"
    NAMESPACE_NAME = os.environ.get("NAMESPACE_NAME")
    SERVICE_NAME = os.environ.get("SERVICE_NAME")
    USER_MS_PORT = os.environ.get("USER_MS_PORT") or 50052
    USER_MS_HOST = os.environ.get("USER_MS_HOST") or "localhost"
    SERVICE_NAME_BALANCER = os.environ.get("SERVICE_NAME_BALANCER")
    SAAS_MS_USER = os.environ.get("SAAS_MS_USER")
    SAAS_MS_CATALOG = os.environ.get("SAAS_MS_CATALOG")
    SAAS_MS_UTILITIES = os.environ.get("SAAS_MS_UTILITIES")
    SAAS_MS_STOCK = os.environ.get("SAAS_MS_STOCK")
    SAAS_MS_CLIENT = os.environ.get("SAAS_MS_CLIENT")
    TENANT_POSTGRESQL_URL = os.environ.get("TENANT_POSTGRESQL_URL")
