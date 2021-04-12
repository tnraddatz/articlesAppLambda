import json
import pyjokes


def main(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfullys!",
        "joke": pyjokes.get_joke()
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Access-Control-Allow-Origin": "*"
        }
    }
    return response
