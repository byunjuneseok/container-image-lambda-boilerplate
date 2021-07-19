#!/bin/bash

docker build -t "$SERVICE_NAME" .
docker tag "$SERVICE_NAME":latest "$AWS_ACCOUNT_ID".dkr.ecr."$AWS_REGION".amazonaws.com/"$SERVICE_NAME":latest
docker push "$AWS_ACCOUNT_ID".dkr.ecr."$AWS_REGION".amazonaws.com/"$SERVICE_NAME":latest

aws lambda update-function-code \
    --function-name "$SERVICE_NAME" \
    --image-uri "$AWS_ACCOUNT_ID".dkr.ecr."$AWS_REGION".amazonaws.com/"$SERVICE_NAME":latest
