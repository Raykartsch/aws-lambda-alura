import json
import log as l

def lambda_handler(event, context):
    # TODO implement
    print(event)

    l.log_function("Log de Execução após configurar Github action " + event)

    return {
        'statusCode': 404,
        'body': event
    }


