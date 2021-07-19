#! /usr/bin/python3
import common

import os

stage_name = os.getenv('STAGE')
service_name = os.getenv('SERVICE_NAME')
aws_account_id = os.getenv('AWS_ACCOUNT_ID')
aws_region = os.getenv('AWS_REGION')
apigateway_http_method = os.getenv('APIGATEWAY_HTTP_METHOD')
apigateway_authorization_type = os.getenv('APIGATEWAY_AUTHORIZATION_TYPE')

cmd = [
    'aws', 'apigateway', 'create-rest-api', '--name', service_name, '--region', aws_region
]
result = common.run_cli(cmd)
apigateway_id = result.get('id')

cmd = [
    'aws', 'apigateway', 'get-resources', '--rest-api-id', apigateway_id, '--region', aws_region
]
result = common.run_cli(cmd)
resources = result.get('items')
root_resource_id = resources[0]['id']

cmd = [
    'aws', 'apigateway', 'create-resource', '--rest-api-id', apigateway_id, '--region', aws_region,
    '--parent-id', root_resource_id, '--path-part', '{proxy+}'
]
result = common.run_cli(cmd)
resource_id = result.get('id')

cmd = [
    'aws', 'apigateway', 'put-method', '--rest-api-id', apigateway_id, '--region', aws_region,
    '--resource-id', resource_id, '--http-method', apigateway_http_method, 
    '--authorization-type', apigateway_authorization_type
]
result = common.run_cli(cmd)

cmd = [
    'aws', 'apigateway', 'put-method-response', '--rest-api-id', apigateway_id, '--region', aws_region,
    '--resource-id', resource_id, '--http-method', apigateway_http_method, 
    '--status-code', '200'
]
result = common.run_cli(cmd)

lambda_arn = f'arn:aws:lambda:{aws_region}:{aws_account_id}:function:{service_name}'

cmd = [
    'aws', 'apigateway', 'put-integration', '--rest-api-id', apigateway_id, '--region', aws_region, 
    '--resource-id', resource_id, '--http-method', apigateway_http_method, '--type', 'AWS', '--integration-http-method', apigateway_http_method,
    '--uri', f'arn:aws:apigateway:{aws_region}:lambda:path/2015-03-31/functions/{lambda_arn}/invocations'
]
result = common.run_cli(cmd)

cmd = [
    'aws', 'apigateway', 'put-integration-response', '--rest-api-id', apigateway_id, '--region', aws_region, 
    '--resource-id', resource_id, '--http-method', apigateway_http_method, '--selection-pattern',  '', '--status-code', '200'
]
result = common.run_cli(cmd)

cmd = [
    'aws', 'lambda', 'add-permission', '--function-name', service_name, '--source-arn', f'arn:aws:execute-api:{aws_region}:{aws_account_id}:{apigateway_id}/*/{apigateway_http_method}/*',
    '--principal', 'apigateway.amazonaws.com', '--action', 'lambda:InvokeFunction', '--statement-id', f'invoke{apigateway_id}'
]
result = common.run_cli(cmd)

cmd = [
    'aws', 'apigateway', 'create-deployment', '--rest-api-id', apigateway_id, '--stage-name', stage_name
]
result = common.run_cli(cmd)


print('#' * 80)
print(f'https://{apigateway_id}.execute-api.ap-northeast-2.amazonaws.com/{stage_name}')
print('#' * 80)