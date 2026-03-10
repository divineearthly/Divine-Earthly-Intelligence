
from .openai_connector import OpenAIConnector
from .huggingface_connector import HuggingFaceConnector
from .local_llm_connector import LocalLLMConnector

class ConnectorFactory:
    @staticmethod
    def get_connector(provider, **kwargs):
        provider = provider.lower()
        if provider == 'openai':
            return OpenAIConnector(**kwargs)
        elif provider == 'hf':
            return HuggingFaceConnector(**kwargs)
        elif provider == 'local':
            return LocalLLMConnector(**kwargs)
        else:
            raise ValueError(f'Unknown provider: {provider}')
