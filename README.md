# About this container

Get a jpg-url from SQS,
Get numbers displayed the bottom by py-ocr lib,
Post log datas to Kinesis Firehose.

* Assumed running on ECS.

# Usage

`ENV=local docker-compose up`

For a temporary script test,
`ENV=local docker-compose run --rm app python containers/pyOcr/myapp/main.py`

## Abount Env

When local, aws-cli tokens in `.env.local`.
When prod, aws-cli tokens in AWS SecretManager.
So the ECS containers need the IAM role with permissions of AWS SecretManager.

# Setup

## make image and push to ECR

`ENV=prod docker-compose build --force-rm`
You can find `pyocr:latest` image by `docker images`.
Then push this image to ECR.
`./push_ecr.sh`
* Image tags are set in docker-compose.yml

## AWS Services

- Make SQS channel, Kinesis Firehose stream, ECS Cluster.
- Register task definition for pyOcr
  - Need environments of sqs channel, kinesis, secret manager.
