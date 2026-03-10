
class OpenAIConnector:
    def __init__(self, api_key='mock_key'):
        self.api_key = api_key

    def generate_text(self, prompt, model='gpt-3.5-turbo'):
        return f'[OpenAI {model} Response] to: {prompt}'
