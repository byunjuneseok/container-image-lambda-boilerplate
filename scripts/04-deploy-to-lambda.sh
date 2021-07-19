#!/bin/bash

aws lambda create-function \
    --role arn:aws:iam::"$AWS_ACCOUNT_ID":role/"$LAMBDA_ROLE_NAME" \
    --function-name "$SERVICE_NAME" \
    --package-type Image \
    --code ImageUri="$AWS_ACCOUNT_ID".dkr.ecr."$AWS_REGION".amazonaws.com/"$SERVICE_NAME":latest
