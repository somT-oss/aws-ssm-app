import boto3
from pprint import pprint

client = boto3.client('ssm')
response = client.get_parameters(
    Names=[
        'db-url',
    ],
    WithDecryption=False
)

pprint(response)