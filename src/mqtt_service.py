class MQTTService():
    def __init__(self, address: str, topic: str):
        self.address = address
        self.topic = topic

    def publish(self, message: dict):
        print(f"Published: \n  {message }")
