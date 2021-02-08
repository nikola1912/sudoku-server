import json
import base64
import boto3
from requests_toolbelt.multipart import decoder

client = boto3.client('rekognition')


def scan_sudoku(event, context):
    base64_string = event['body']
    content_type = event['headers']['Content-Type']

    multipart_string = base64.b64decode(base64_string)
    multipart_data = decoder.MultipartDecoder(multipart_string, content_type)
    file_data = multipart_data.parts[0].content

    response = client.detect_text(Image={'Bytes': file_data})
    print(response)

    return {
        "statusCode": 200,
        "body": "Sudoku successfully scanned"
    }
