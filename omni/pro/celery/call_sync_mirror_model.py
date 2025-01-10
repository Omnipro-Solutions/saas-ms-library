from omni.pro.celery.celery_redis import OmniCelery


class SynchronizedMirrorModel(OmniCelery):
    def __init__(self, tenant) -> None:
        super().__init__(tenant)
        self.task_name = "tasks.utilities.sync_mirror_model.sync_mirror_model"
        self.tenant = tenant
        self.queue = "low"
        self.celery_app = OmniCelery(self.tenant)

    def sync_mirror_model(self, params: dict):
        return self.celery_app.send_task(name=self.task_name, args=[{"params": params}], queue=self.queue)
