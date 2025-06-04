import json
from handlers.handler_emotion import get_emotion_chain

# OpenTelemetry imports
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)

# Configuração do tracer provider e exportador para console
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

if __name__ == "__main__":
    with tracer.start_as_current_span("main") as main_span:
        body = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "isBase64Encoded": False,
            "multiValueHeaders": {},
            "path": "/",
            "pathParameters": {},
            "queryStringParameters": {},
            "multiValueQueryStringParameters": {},
            "requestContext": {
                "accountId": "string",
                "apiId": "string",
                "domainName": "string",
                "domainPrefix": "string",
                "httpMethod": "POST",
                "requestId": "string",
                "resourceId": "string",
                "resourcePath": "/",
                "stage": "string",
            },
            "body": "{\"message\": \"I am happy\"}"
        }
        event = {
            "body": json.dumps(body),
        }

        with tracer.start_as_current_span("get_emotion_chain_call") as span:
            emotions = get_emotion_chain(event, None).get("emotions")
            span.set_attribute("emotions.count", len(emotions) if emotions else 0)

        print(emotions)
