#!/bin/bash
# Login and push Docker images to ECR
$(aws ecr get-login --no-include-email --region us-east-1)
docker tag booking-service:latest <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/booking-service
docker push <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/booking-service
