from enum import Enum

from .mongo import DatabaseManager, DBUtil, MongoConnection, PolishNotationToMongoDB
from .postgres import PolishNotationToSQLAlchemy, PostgresDatabaseManager, QueryBuilder, SessionManager
from .redis import FakeRedisServer, RedisConnection, RedisManager


class PersistenceTypeEnum(Enum):
    SQL = "SQL"
    NO_SQL = "NO_SQL"
    REDIS = "REDIS"

    def __str__(self) -> str:
        return self.value
