import json
import boto3
import html5lib
from webpreview import web_preview
from urllib.parse import urlparse


def main(event, context):
    try:
        # parameters
        params = json.loads(event['body'])
        website_url = params['website_url']
        # ends

        # --- Normalize incoming URLs ---

        # Parse website url and remove https:// and http://
        # Also help the user if they mis-typed scheme (http/https)
        website_object = urlparse(website_url)
        if (website_object.scheme):
            website_url = website_url.replace(
                website_object.scheme + "://", "", 1)
            website_url = website_url.replace(
                website_object.scheme + ":/", "", 1)
            website_url = website_url.replace(
                website_object.scheme + ":", "", 1)

        # Remove last char if url ends with / or .
        url_last_char = website_url[-1]
        if (url_last_char == "/" or url_last_char == "."):
            website_url = website_url[:-1]

        # Remove `www.` so we can normalize incoming url
        first_four_char = website_url[0:4]
        if (first_four_char == "www."):
            website_url = website_url[4:]

        title, description, image = web_preview(
            url=website_url, parser="html5lib")
        # -----------------------------

        # Connect to DB and record transaction
        ddb = boto3.resource('dynamodb')
        table = ddb.Table('DynamoDevNewsTable')  # TODO: Edit Table Name

        ddb_response = table.put_item(
            Item={
                'PostUrl': website_url,
                'Title': title,
                'Description': description,
                'ImageUrl': image
            }
        )

        response = {
            "statusCode": 200,
            "body": json.dumps(ddb_response),
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
