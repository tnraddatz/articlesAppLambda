import json
import boto3


def main(event, context):
    try:
        # parameters
        params = json.loads(event['body'])
        website_url = params['website_url']
        # ends

        # Connect to DB and record transaction
        ddb = boto3.resource('dynamodb')
        table = ddb.Table('DynamoDevNewsTable')  # TODO: Edit Table Name

        # scan_kwargs = {
        #     'FilterExpression': Key('year').between(*year_range),
        #     'ProjectionExpression': "#yr, title, info.rating",
        #     'ExpressionAttributeNames': {"#yr": "year"}
        # }

        ddb_response = table.scan()
        
        response = {
            "statusCode": 200,
            "body": json.dumps(ddb_response['Items']),
            "headers": {
                "Access-Control-Allow-Origin": "*"
            }
        }

        return response

    except Exception as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({
                "message": str(e)
            }),
            "headers": {
                "Access-Control-Allow-Origin": "*"
            }
        }
        return response
