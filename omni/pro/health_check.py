from time import time

from omni.pro.config import Config
from omni_pro_grpc.v1.util import health_check_pb2
from pymongo import MongoClient
from sqlalchemy import text


class HealthCheck:

    def _check_service(self, connect_fn, success_message, failure_message):
        start_time = time()
        try:
            connect = connect_fn
            end_time = time()
            time_ms = round((end_time - start_time) * 1000, 2)

            if connect is not None:
                return (
                    health_check_pb2.ServiceStatus(status="SUCCESS", detail=success_message, time_ms=time_ms),
                    time_ms,
                )

            return health_check_pb2.ServiceStatus(status="FAILURE", detail=failure_message, time_ms=time_ms), time_ms
        except Exception:
            end_time = time()
            time_ms = (end_time - start_time) * 1000
            return health_check_pb2.ServiceStatus(status="FAILURE", detail=failure_message, time_ms=time_ms), time_ms

    def _get_mongo_client(self, db_manager):
        mongo_uri = f"mongodb://{db_manager.username}:{db_manager.password}@{db_manager.host}:{db_manager.port}/{db_manager.db}?authSource=admin"
        return MongoClient(mongo_uri)

    def _execute_check_query(self, engine):
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

    def check_mongo(self, db_manager):
        try:
            mongo_client = self._get_mongo_client(db_manager)
            return self._check_service(
                mongo_client.server_info(), "MongoDB connection established", "MongoDB connection failed"
            )
        except Exception:
            return health_check_pb2.ServiceStatus(status="FAILURE", detail="MongoDB connection failed", time_ms=0), 0

    def check_postgres(self, engine):
        return self._check_service(
            lambda: self._execute_check_query(engine),
            "Postgres connection established",
            "Postgres connection failed",
        )

    def check_redis(self, redis_client):
        try:
            return self._check_service(redis_client.ping(), "Redis connection established", "Redis connection failed")
        except Exception:
            return health_check_pb2.ServiceStatus(status="FAILURE", detail="Redis connection failed", time_ms=0), 0
