# import unittest
# from unittest.mock import MagicMock, patch

# from omni.pro.airflow.actions import ActionToAirflow  # Reemplaza con el nombre de tu módulo y clase


# class TestSendToAirflow(unittest.TestCase):

#     @patch("omni_pro_redis.redis.RedisManager.get_json")
#     @patch("omni_pro_redis.redis.RedisManager.get_load_balancer_name")
#     @patch("omni.pro.airflow.airflow_client_base.AirflowClientBase")  # Mock del cliente Airflow
#     @patch("omni_pro_grpc.grpc_function.WebhookRPCFucntion")  # Mock de WebhookRPCFucntion
#     @patch("omni_pro_grpc.grpc_function.EventRPCFucntion")  # Mock de EventRPCFucntion
#     @patch("omni_pro_grpc.util.MessageToDict")  # Mock de MessageToDict
#     @patch("omni_pro_base.util.eval_condition")  # Mock de eval_condition
#     @patch("sqlalchemy.inspection.inspect")  # Mock de inspect
#     def test_send_to_airflow(
#         self,
#         mock_inspect,
#         mock_eval_condition,
#         mock_message_to_dict,
#         mock_event_rpc,
#         mock_webhook_rpc,
#         mock_airflow_client,
#         mock_get_load_balancer_name,
#         mock_get_json,
#     ):
#         mock_get_load_balancer_name.return_value = "mocked_load_balancer_name"
#         mock_get_json.return_value = {"tenant_code": "mocked_tenant_code"}  # Simulamos que existe tenant_code en Redis

#         # Mocks de los parámetros de entrada
#         cls_name = MagicMock()
#         cls_name._collection.name = "mock_model"  # Simulando un Document
#         instance = MagicMock()
#         instance.generate_dict.return_value = {"field": "value"}
#         instance.__is_replic_table__ = True
#         action = "update"
#         context = {"tenant": "tenant_code", "user": "user_name"}

#         # Mock de la respuesta del RPC para EventRPCFucntion
#         mock_event_rpc_instance = mock_event_rpc.return_value
#         mock_event_rpc_instance.read_event.return_value = (
#             MagicMock(events=[{"operation": "update", "id": 1}]),
#             True,
#             None,
#         )

#         # Mock de la respuesta del RPC para WebhookRPCFucntion
#         mock_webhook_rpc_instance = mock_webhook_rpc.return_value
#         mock_webhook_rpc_instance.read_webhook.return_value = (
#             MagicMock(
#                 webhooks=[
#                     {
#                         "dag_id": "dag_test",
#                         "trigger_fields": ["mock_model-field"],
#                         "type_webhook": "external",
#                         "python_code": "",
#                     }
#                 ]
#             ),
#             True,
#             None,
#         )

#         # Mock de inspect y eval_condition
#         mock_inspect.return_value.attrs = [
#             MagicMock(key="field", history=MagicMock(has_changes=MagicMock(return_value=True)))
#         ]
#         mock_eval_condition.return_value = True  # Siempre pasar la condición

#         print(f"cls_name: {cls_name}, instance: {instance}, action: {action}, context: {context}")
#         # Ejecuta el método que se está probando
#         ActionToAirflow.send_to_airflow(cls_name, instance, action, context)

#         self.assertTrue(mock_airflow_client.called, "AirflowClientBase no fue llamado")

#         # Verificar que se llamó a AirflowClientBase con los parámetros correctos
#         mock_airflow_client.assert_called_once_with(context["tenant"])
#         mock_airflow_client_instance = mock_airflow_client.return_value
#         mock_airflow_client_instance.run_dag.assert_called_once_with(
#             dag_id="dag_test",
#             params={
#                 "instance": {"field": "value"},  # Lo que genera generate_dict
#                 "action_code": "mock_model_update",
#                 "context": context,
#                 "webhook": {
#                     "dag_id": "dag_test",
#                     "trigger_fields": ["mock_model-field"],
#                     "type_webhook": "external",
#                     "python_code": "",
#                 },
#             },
#         )

#         # Verificar que se llamaron las funciones auxiliares como eval_condition
#         mock_eval_condition.assert_called_once_with({"field": "value"}, "")
#         mock_inspect.assert_called_once_with(instance)


# if __name__ == "__main__":
#     unittest.main()
