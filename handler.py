# def scan_sudoku():
#     image = request.files['image']
#     print(image)
#     return {
#         "sudoku": []
#     }

import json


def hello(event, context):
    body = {
        "message": "Hello there!",
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
