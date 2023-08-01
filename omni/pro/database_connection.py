import mongoengine as mongo
from omni.pro.logger import configure_logger
from omni.pro import redis
from omni.pro.config import Config

logger = configure_logger(name=__name__)


def ms_register_connection():
    manager = redis.get_redis_manager()
    tenants = manager.get_tenant_codes()
    # Registrar todas las conexiones
    for idx, tenant in enumerate(tenants):
        logger.info(f"Register connection for tenant {tenant}")
        conn = manager.get_mongodb_config(Config.SERVICE_ID, tenant)
        eval_conn = conn.copy()
        if Config.DEBUG:
            del eval_conn["complement"]
        if not all(eval_conn.values()):
            continue

        mongo.register_connection(
            alias=f"{tenant}_{conn['name']}",
            name=conn["name"],
            host=conn["host"],
            port=int(conn["port"]),
            username=conn["user"],
            password=conn["password"],
            **conn["complement"],
        )

        if idx == 0:
            mongo.register_connection(
                alias=mongo.DEFAULT_CONNECTION_NAME,
                name=mongo.DEFAULT_CONNECTION_NAME,
                host=conn["host"],
                port=int(conn["port"]),
                username=conn["user"],
                password=conn["password"],
                **conn["complement"],
            )
