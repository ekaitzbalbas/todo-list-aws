import os
import json
import decimalencoder
import todoList

def get(event, context):
    id = event['pathParameters']['id']
    
    result = todoList.get_item(id)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result,
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
