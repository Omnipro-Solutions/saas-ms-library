import os


class Config(object):
    DEBUG = False
    TESTING = False

    GRPC_PORT = os.environ.get("GRPC_PORT") or 50051
    GRPC_MAX_WORKERS = int(os.environ.get("GRPC_MAX_WORKERS") or 10)
    SERVICE_ID = os.environ["SERVICE_ID"]
    REDIS_HOST = os.environ["REDIS_HOST"]
    REDIS_PORT = int(os.environ.get("REDIS_PORT") or 6379)
    REDIS_DB = int(os.environ.get("REDIS_DB") or 0)
