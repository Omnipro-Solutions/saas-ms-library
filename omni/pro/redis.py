from omni.pro.cloudmap import CloudMap
from omni.pro.database import RedisManager


def get_redis_manager() -> RedisManager:
    # logger.info(f"Cloud Map: {cm_params}")
    cloud_map = CloudMap()

    redis_params = cloud_map.get_redis_config()
    # logger.info(f"Redis params: {redis_params}")

    redis_manager = RedisManager(**redis_params)
    return redis_manager