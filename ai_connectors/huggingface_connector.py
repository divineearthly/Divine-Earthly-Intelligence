
class HuggingFaceConnector:
    def __init__(self, token='mock_token'):
        self.token = token

    def generate_text(self, prompt, model='gpt-2'):
        return f'[HuggingFace {model} Inference] result for: {prompt}'
