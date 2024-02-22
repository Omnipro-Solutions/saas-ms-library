from omni.pro.airflow.airflow_client_base import AirflowClientBase


class RegisterModels(AirflowClientBase):
    def __init__(self, tenant) -> None:
        super().__init__(tenant)
        self.dag_id = "RegisterModels"

    def register_model(self, params):
        return self.run_dag(self.dag_id, params)
