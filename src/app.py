import json
from handlers.handler_emotion import get_emotion_chain
import observability  # noqa: F401

if __name__ == "__main__":
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
    
    event ={
        "body": json.dumps(body), 
    }
    
    print(get_emotion_chain(event, None).get("emotions"))