import json
import time
import logging
import os
import decimalencoder
import todoList

def update(event, context):
    data = json.loads(event['body'])
    if 'text' not in data or 'checked' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")
    
    id = event['pathParameters']['id']
    
    result = todoList.update_item(id, data)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result,
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
    