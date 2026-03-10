
class LocalLLMConnector:
    def __init__(self, host='http://localhost:11434'):
        self.host = host

    def generate_text(self, prompt, model='llama3'):
        return f'[Local LLM {model} @ {self.host}] output for: {prompt}'
