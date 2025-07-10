#!/bin/bash
AWS_REGION="us-east-1"
AWS_ACCOUNT_ID="<your_account_id>"

SERVICES=("booking" "payment" "user")

for service in "${SERVICES[@]}"; do
  docker build -t $service ./services/$service
  docker tag $service:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$service-service:latest
  aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
  docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$service-service:latest
done
