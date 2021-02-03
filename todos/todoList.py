import time
import os
import boto3

# dynamo
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def put_item(item):
    table.put_item(Item=item)

def get_all_items():
    scan = table.scan()
    return scan['Items']
    
def get_item(item_id):
    result = table.get_item(
        Key={
            'id': item_id
        }
    )
    return result['Item']

def update_item(item_id, data):
    timestamp = int(time.time() * 1000)
    result = table.update_item(
        Key={
            'id': item_id
        },
        ExpressionAttributeNames={
            '#todo_text': 'text',
        },
        ExpressionAttributeValues={
            ':text': data['text'],
            ':checked': data['checked'],
            ':updatedAt': timestamp,
        },
        UpdateExpression='SET #todo_text = :text, '
                         'checked = :checked, '
                         'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )
    return result['Attributes']

def delete_item(item_id):
    table.delete_item(
        Key={
            'id': item_id
        }
    )