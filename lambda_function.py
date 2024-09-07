import json
import log as l
import os

def lambda_handler(event, context):
    # TODO implement
    print(event)
    minha_var = os.environ['MINHA_VAR']
    print("Testando config de variável de ambiente lambda AWS", minha_var)
    l.log_function("Log de Execução após configurar Github action " + event)

    return {
        'statusCode': 404,
        'body': event,
        'headers':{
            'content-type': 'text/html'
        }
    }


