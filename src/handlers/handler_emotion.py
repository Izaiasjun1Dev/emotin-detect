import json
import logging
from agent.base_agent.base import agent
from agent.domain.handler_emotion.input import APIGatewayProxyRequestEvent
from agent.domain.handler_emotion.output import APIGatewayProxyResponseEvent

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

def get_emotion_chain(event, context):
    """
    Function to get the emotion chain.
    """
    logger.info(f"Received event: {event}")
    event = APIGatewayProxyRequestEvent(**event)
    message = json.loads(event.body)
    logger.info(f"Parsed message from event body: {message}")
    response = agent.run(message)
    logger.info(f"Agent response: {response}")
    return response.model_dump()
