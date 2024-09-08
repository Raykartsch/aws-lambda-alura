import json
import log as l
import os

def lambda_handler(event, context):
    record = event.records[0]

    print(record)
    return {
        'statusCode': 404,
        'body': f'''<html><body>Dados da Requisição {str(event)}</html></body>''',
        'headers':{
            'content-type': 'text/html'
        }
    }


