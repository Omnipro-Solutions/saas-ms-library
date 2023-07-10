from omni.pro.aws import AWSCloudMap
from omni.pro.config import Config


class CloudMap(AWSCloudMap):
    def __init__(self, service_name=Config.SERVICE_NAME, *args, **kwargs):
        cm_params = {
            "aws_access_key_id": Config.AWS_ACCESS_KEY_ID,
            "aws_secret_access_key": Config.AWS_SECRET_ACCESS_KEY,
            "region_name": Config.REGION_NAME,
            "service_name": service_name,
            "namespace_name": Config.NAMESPACE_NAME,
        }
        super().__init__(**cm_params, **kwargs)
