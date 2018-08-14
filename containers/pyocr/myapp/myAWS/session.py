from boto3.session import Session
from botocore.exceptions import ClientError

def my_session(access_key, secret_key, region_name='ap-northeast-1'):
  return Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region_name)
