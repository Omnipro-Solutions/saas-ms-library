import mongoengine as mongo
from omni.pro.config import Config
from omni.pro.logger import configure_logger
from omni.pro.redis import RedisManager

logger = configure_logger(name=__name__)


def register_logger_connection(tenant, manager: RedisManager):
    conn = manager.get_mongodb_config(Config.LOGGER_ID, tenant)
    mongo.register_connection(
        alias=f"{tenant}_{conn['name']}",
        name=conn["name"],
        host=conn["host"],
        port=int(conn["port"]),
        username=conn["user"],
        password=conn["password"],
        **conn["complement"],
    )


def ms_register_connection(logger_oms=False):
    manager = RedisManager(
        host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, redis_ssl=Config.REDIS_SSL
    )
    tenants = manager.get_tenant_codes()
    # Registrar todas las conexiones
    for idx, tenant in enumerate(tenants):
        logger.info(f"Register connection for tenant {tenant}")
        conn = manager.get_mongodb_config(Config.SERVICE_ID, tenant)
        eval_conn = conn.copy()
        if Config.DEBUG or not eval_conn.get("complement"):
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

        if logger_oms:
            register_logger_connection(tenant, manager)

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
