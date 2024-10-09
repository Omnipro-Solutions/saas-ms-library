import unittest
from unittest.mock import MagicMock, patch

from omni.pro.decorators import FunctionThreadController, Resource, resources_decorator


class TestResourcesDecorator(unittest.TestCase):

    @patch("omni.pro.decorators.RedisManager")
    @patch("omni.pro.decorators.AWSCognitoClient")
    @patch("omni.pro.decorators.AWSS3Client")
    @patch("omni.pro.decorators.DatabaseManager")
    @patch("omni.pro.decorators.PostgresDatabaseManager")
    @patch("omni.pro.response.MessageResponse.internal_response", return_value="response")
    def test_resources_decorator(
        self,
        mock_internal_response,
        mock_pg_db_manager,
        mock_db_manager,
        mock_s3_client,
        mock_cognito_client,
        mock_redis_manager,
    ):
        mock_redis_instance = MagicMock()
        mock_redis_manager.return_value = mock_redis_instance

        mock_redis_instance.get_aws_cognito_config.return_value = {"region": "us-west-1"}
        mock_redis_instance.get_aws_s3_config.return_value = {"bucket": "test-bucket"}
        mock_redis_instance.get_mongodb_config.return_value = {"name": "test_db", "host": "localhost"}
        mock_redis_instance.get_postgres_config.return_value = {"name": "test_pg_db", "host": "localhost"}

        resource_list = [Resource.AWS_COGNITO, Resource.AWS_S3, Resource.MONGODB, Resource.POSTGRES]

        @resources_decorator(resource_list)
        def dummy_func(instance, request, context):
            return "success"

        request = MagicMock()
        request.context.user = "test_user"
        request.context.tenant = "test_tenant"
        context = MagicMock()

        result = dummy_func(None, request, context)

        mock_cognito_client.assert_called_once_with(region="us-west-1")
        mock_s3_client.assert_called_once_with(bucket="test-bucket")

        self.assertEqual(context.db_name, "test_pg_db")
        mock_pg_db_manager.assert_called_once_with(name="test_pg_db", host="localhost")


class TestFunctionThreadController(unittest.TestCase):

    def setUp(self):
        self.controller = FunctionThreadController(timeout=1)

    @patch("threading.Thread")
    def test_run_thread_controller(self, mock_thread):
        def dummy_function(arg1, arg2):
            pass

        wrapped_func = self.controller.run_thread_controller(dummy_function)

        wrapped_func(1, 2)

        self.assertIn("dummy_function", self.controller.function_threads)
        self.assertTrue(mock_thread.called)
        thread_instance = self.controller.function_threads["dummy_function"]["thread"]
        self.assertIsNotNone(thread_instance)
        thread_instance.start.assert_called_once()

    @patch("queue.Queue")
    def test_function_queue(self, mock_queue):
        def dummy_function(arg1, arg2):
            pass

        mock_queue_instance = MagicMock()
        mock_queue.return_value = mock_queue_instance

        wrapped_func = self.controller.run_thread_controller(dummy_function)

        wrapped_func(1, 2)


if __name__ == "__main__":
    unittest.main()
