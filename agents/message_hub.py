
class MessageHub:
    def __init__(self):
        self.registry = {}
    def register_agent(self, name, instance):
        self.registry[name.lower()] = instance
    def send_direct_message(self, message):
        pass
