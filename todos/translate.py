import os
import json
import logging
import decimalencoder
import boto3
import todoList

translate = boto3.client('translate')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def translate_text(event, context):
    id = event['pathParameters']['id']
    
    result = todoList.get_item(id)
    
    text = result['Item']['text']
    source_language = "auto"
    target_language = event['pathParameters']['lang']
    
    #extract text from response and translate      
    try:
        response_trans = translate.translate_text(
    	        Text = text,
    	        SourceLanguageCode = source_language, 
    	        TargetLanguageCode = target_language
            )
            
        # item = {
        #     'id': event['pathParameters']['id'],
        #     'text': text,
        #     'TranslatedText': str(response_trans.get('TranslatedText')),
        #     'SourceLanguageCode': str(response_trans.get('SourceLanguageCode')),
        #     'TargetLanguageCode': str(response_trans.get('TargetLanguageCode'))
        # }
    except Exception as e:
        logger.error(str(e))
        raise Exception("[ErrorMessage]: " + str(e))
    
    # create a response
    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(item)
    # }
    
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(response_trans)
    }

    return response