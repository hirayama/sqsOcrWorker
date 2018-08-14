 #! /bin/bash

set -xe

ECR_ENDPOINT=''
TAG=pyocr

docker tag ${TAG}_prod:latest ${ECR_ENDPOINT}/${TAG}:latest 
docker push ${ECR_ENDPOINT}/${TAG}:latest 
