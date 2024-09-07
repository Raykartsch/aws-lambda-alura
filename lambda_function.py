import json
import log as l

def lambda_handler(event, context):
    # TODO implement
    print(event)

    l.log_function("Função de Execução " + event)

    return {
        'statusCode': 404,
        'body': event
    }


