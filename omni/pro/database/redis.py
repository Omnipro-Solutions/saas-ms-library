from omni_pro_base.config import Config
from omni_pro_redis.redis import RedisConnection


class RedisCache(object):
    def __init__(self, host: str, port: int, db: int, redis_ssl: bool) -> None:
        self.host = host
        self.port = int(port)
        self.db = db
        self.redis_ssl = redis_ssl
        self._connection = RedisConnection(host=self.host, port=self.port, db=self.db, redis_ssl=self.redis_ssl)

    def get_connection(self) -> RedisConnection:
        # if Config.TESTING:
        #     return fakeredis.FakeStrictRedis(
        #         server=FakeRedisServer.get_instance(),
        #         charset="utf-8",
        #         decode_responses=True,
        #     )
        return self._connection

    def set_connection(self, connection: RedisConnection) -> None:
        self._connection = connection

    def save_cache(self, hash_key: str, data: dict) -> bool:
        """
        Save data to the Redis cache.

        Args:
            hash_key (str): The key to store the data in the cache.
            data (dict): The data to be stored in the cache.

        Returns:
            bool: True if the data was successfully saved to the cache, False otherwise.
        """
        with self.get_connection() as rc:
            response = rc.json().set(hash_key, "$", obj=data)
            rc.expire(hash_key, Config.EXPIRE_CACHE)
            return response

    def get_cache(self, hash_key: str) -> dict:
        """
        Retrieves the value associated with the given hash key from the cache.

        Args:
            hash_key (str): The key used to retrieve the value from the cache.

        Returns:
            dict: The value associated with the hash key, or None if the key is not found in the cache.
        """
        with self.get_connection() as rc:
            result = rc.json().get(hash_key)
            if result is None:
                return None
            return result
