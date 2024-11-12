from omni.pro.celery.celery_redis import OmniCelery


class RegisterModels(OmniCelery):
    def __init__(self, tenant) -> None:
        super().__init__(tenant)
        self.task_name = "tasks.utilities.register_models.register_model"
        self.tenant = tenant
        self.queue = "low"
        self.celery_app = OmniCelery(self.tenant)

    def register_model(self, params: dict):
        return self.celery_app.send_task(name=self.task_name, args=[{"params": params}], queue=self.queue)
