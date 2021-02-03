import os
import todoList 

def delete(event, context):
    id = event['pathParameters']['id']

    todoList.delete_item(id)

    # create a response
    response = {
        "statusCode": 200
    }

    return response
