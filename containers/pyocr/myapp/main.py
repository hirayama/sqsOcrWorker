from myAWS import secretManager
from myAWS import session
import myOcr
import os
import json
env = os.getenv("ENV", "local")
kinesis_stream = os.getenv("KINESIS_STREAM", "test")
sqs_name = os.getenv("SQS_CHANNEL", "test")
secret_manager_name = os.getenv("SECRET_MANAGER", "test")

secret = secretManager.SecretManager(secret_manager_name)
session_tokyo = session.my_session(secret.access_key, secret.secret_key)
session_us = session.my_session(secret.access_key, secret.secret_key, 'us-east-1')

# SQS
sqs = session_tokyo.resource('sqs')
queue = sqs.get_queue_by_name(QueueName=sqs_name)
messages = queue.receive_messages(MaxNumberOfMessages=10)
lines = []
if messages:
  for message in messages:
    lines.append({
      'Data': json.dumps(myOcr.my_ocr(message.body)).encode('utf-8')
    })
print(lines)

# Kinesis
try:
  firehose = session_us.client('firehose')
  if len(lines) > 0:
    result=firehose.put_record_batch(
      DeliveryStreamName=kinesis_stream,
      Records=lines
    )
  print(result)
except ClientError as e:
  print(e)

