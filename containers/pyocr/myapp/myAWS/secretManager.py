import boto3
import json
from botocore.exceptions import ClientError

class SecretManager():

  __endpoint_url= 'https://secretsmanager.ap-northeast-1.amazonaws.com'
  __region_name = 'ap-northeast-1'

  def __init__(self, name):
    secret = self._get_aws_keys(name=name)
    self.access_key = secret['AWS_ACCESS_KEY_ID']
    self.secret_key = secret['AWS_SECRET_ACCESS_KEY']
  
  def _get_aws_keys(self, name):
    endpoint_url = self.__endpoint_url
    region_name = self.__region_name

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
        endpoint_url=endpoint_url
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("The requested secret " + secret_name + " was not found")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)
    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            binary_secret_data = get_secret_value_response['SecretBinary']
            
        return json.loads(secret)

