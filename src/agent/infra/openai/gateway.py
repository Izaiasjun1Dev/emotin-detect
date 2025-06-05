from langchain_openai import ChatOpenAI

from configs.settings import settings
import logging
from observability import tracer


class GatewayOpenAi:
    """
    Gateway for OpenAI API.
    """

    def __init__(self):
        self.settings = settings
        self.logger = logging.getLogger(__name__)

    def get_llm_client(self):
        """
        Get the LLM client.
        """
        return self._get_llm_client()

    def _get_llm_client(self):
        """
        Create and return the LLM client.
        """
        # Initialize the LLM client with the settings
        self.logger.info("Creating OpenAI client")
        with tracer.start_as_current_span("openai_client"):
            llm = ChatOpenAI(
                api_key=settings.openai_api_key,
                model_name=settings.openai_model,
                temperature=0.5,
            )

        return llm
