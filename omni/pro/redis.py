from omni.pro.cloudmap import CloudMap
from omni.pro.database import RedisManager
from omni.pro.config import Config


def get_redis_manager() -> RedisManager:
    if Config.DEBUG:
        return RedisManager(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB)

    # logger.info(f"Cloud Map: {cm_params}")
    redis = RedisManager(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB)

    return redis
