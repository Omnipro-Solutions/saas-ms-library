from omni.pro.aws.client import AWSClient


class AWSCloudMap(AWSClient):
    def __init__(
        self,
        region_name: str,
        namespace_name: str,
        service_name: str,
        aws_access_key_id: str,
        aws_secret_access_key: str,
        **kwargs,
    ):
        super().__init__(
            service_name="servicediscovery",
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            **kwargs,
        )
        self.namespace_name = namespace_name
        self.service_name = service_name

    def discover_instances(self):
        response = self.client.discover_instances(
            NamespaceName=self.namespace_name,
            ServiceName=self.service_name,
        )
        if not response.get("Instances"):
            raise Exception("No instances found")

        return response.get("Instances")

    def get_redis_config(self):
        instances = self.discover_instances()
        instance = instances[0]
        return {
            "host": instance.get("Attributes").get("host"),
            "port": int(instance.get("Attributes").get("port") or 6379),
            "db": int(instance.get("Attributes").get("db") or 0),
        }
