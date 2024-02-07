from kafka import KafkaConsumer, KafkaProducer


class KafkaHandler:
    def __init__(self, bootstrap_servers, topic):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic

    class Producer:
        def __init__(self, parent):
            self.parent = parent
            self.producer = KafkaProducer(bootstrap_servers=parent.bootstrap_servers)

        def send_message(self, msg):
            self.producer.send(self.parent.topic, msg)
            self.producer.flush()

    class Consumer:
        def __init__(self, parent):
            self.consumer = KafkaConsumer(parent.topic, bootstrap_servers=parent.bootstrap_servers)

        def receive_message(self):
            for msg in self.consumer:
                print(msg)

        def close(self):
            self.consumer.close()
