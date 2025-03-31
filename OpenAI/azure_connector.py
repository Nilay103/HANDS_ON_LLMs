import os

from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()


class AzureOpenAIConnector:
    instance = None

    @classmethod
    def __get_config(cls):
        return {
            "api_key": os.getenv("OPENAPI_API_KEY"),
            "api_version": os.getenv("OPENAPI_API_VERSION"),
            "azure_endpoint": os.getenv("OPENAPI_API_BASE"),
        }

    def get_client(cls):
        if cls.instance is None:
            cls.instance = AzureOpenAI(**cls.__get_config())
        return cls.instance

    def send_message(self, messages, **model_params):
        return self.get_client().chat.completions.create(
            model=os.getenv("OPENAPI_ENGINE"),
            **model_params,
            messages=messages
        )


azure_openai_connector = AzureOpenAIConnector()
