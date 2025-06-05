import logging
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

from agent.domain.agent.output import Output
from agent.domain.entity.chain import EntityChain
from agent.infra.openai.gateway import GatewayOpenAi
from observability import tracer

logger = logging.getLogger(__name__)

class BaseAgentDetectEmotion(EntityChain):
    def llm(self):
        """
        Initialize the LLM (Language Model) with the API key and model name.
        """
        logger.info("Initializing LLM client.")
        llm_instance = GatewayOpenAi()
        return llm_instance.get_llm_client()

    def prompt(self):
        """
        Initialize the prompt template with the specified template.
        """
        logger.info("Creating prompt template.")
        parser = self.parser()
        instructions = parser.get_format_instructions()

        prompt = PromptTemplate(
            template = self.template,
            input_variables = self.input_variables,
            partial_variables = {
                "format_instructions": instructions,
            },
        )

        return prompt

    def parser(self):
        """
        Initialize the parser class.
        """
        logger.info("Initializing parser.")
        parser = PydanticOutputParser(pydantic_object=Output)

        return parser

    def chain(self):
        """
        Initialize the chain with the LLM and prompt.
        """
        logger.info("Building chain.")
        prompt = self.prompt()
        llm = self.llm()
        parser = self.parser()

        chain = prompt | llm | parser
        return chain

    def run(self, input):
        """
        Run the chain with the given input.
        """
        logger.info(f"Running chain with input: {input}")
        with tracer.start_as_current_span("detect_emotion") as span:
            span.set_attribute("input", str(input))
            chain = self.chain()
            result = chain.invoke(input)
            span.set_attribute("result", str(result))
        logger.info(f"Chain result: {result}")
        return result


agent = BaseAgentDetectEmotion()
