from airflow_client.client.configuration import Configuration
from airflow_client.client.api_client import ApiClient
from airflow_client.client.api import dag_run_api
from airflow_client.client.model.dag_run import DAGRun
from airflow_client.client import ApiException

from omni_pro_base.logger import configure_logger
from omni_pro_base.config import Config
from omni_pro_base.microservice import MicroService
from omni_pro_redis.redis import RedisManager

logger = configure_logger(name=__name__)


class AirflowClientBase:
    def __init__(self, tenant) -> None:
        self.configuration = Configuration(**self.get_config(tenant))
        self.api_client = ApiClient(configuration=self.configuration)

    def get_config(self, tennat):
        redis = RedisManager(
            host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, redis_ssl=Config.REDIS_SSL
        )
        return redis.get_airflow_config(MicroService.SAAS_AIRFLOW_OMS.value, tennat)

    def run_dag(self, dag_id: str, params: dict):
        with self.api_client as api_client:
            api_instance = dag_run_api.DAGRunApi(api_client)
            try:
                api_reponse = api_instance.post_dag_run(
                    dag_id=dag_id,
                    dag_run=DAGRun(
                        conf=params,
                    ),
                )
            except ApiException as e:
                logger.info("Exception when calling DAGRunApi->post_dag_run: %s\n" % e)
            else:
                return api_reponse
