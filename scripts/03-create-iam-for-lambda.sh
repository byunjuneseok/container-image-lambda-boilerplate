#!/bin/bash

aws iam create-role --role-name "$LAMBDA_ROLE_NAME" --assume-role-policy-document file://iam/role.json
aws iam put-role-policy --role-name "$LAMBDA_ROLE_NAME" --policy-name "$LAMBDA_ROLE_NAME"-policy --policy-document file://iam/policy.json
