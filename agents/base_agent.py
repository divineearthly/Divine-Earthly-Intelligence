
from .message_protocol import Message
class BaseAgent:
    def __init__(self, role, model_connector=None, message_hub=None):
        self.role = role
        self.model_connector = model_connector
        self.message_hub = message_hub
    def receive_message(self, message: Message):
        pass
    def process_task(self, task, context=None):
        pass
