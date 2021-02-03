import json
import os
import decimalencoder
import todoList

def list(event, context):
    result = todoList.get_all_items()

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result, cls=decimalencoder.DecimalEncoder)
    }

    return response
