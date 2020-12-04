import json


def lambda_handler(event, context):
    body = {
        "message": "This is hello2",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
