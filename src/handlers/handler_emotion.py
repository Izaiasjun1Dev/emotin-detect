import json
import logging
from agent.base_agent.base import agent
from agent.domain.handler_emotion.input import APIGatewayProxyRequestEvent
from agent.domain.handler_emotion.output import APIGatewayProxyResponseEvent
from observability import tracer

logger = logging.getLogger(__name__)

def get_emotion_chain(event, context):
    """
    Function to get the emotion chain.
    """
    logger.info(f"Received event: {event}")
    with tracer.start_as_current_span("get_emotion_chain") as span:
        event = APIGatewayProxyRequestEvent(**event)
        message = json.loads(event.body)
        span.set_attribute("message", str(message))
        logger.info(f"Parsed message from event body: {message}")
        response = agent.run(message)
        span.set_attribute("emotions", str(response.emotions))
        logger.info(f"Agent response: {response}")
    return response.model_dump()
