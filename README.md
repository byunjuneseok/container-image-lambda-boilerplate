# Deploy Python Lambda functions with container images.

![Small architecture](./readme-banner.png)

Build docker image lambda function wtih API Gateway. Just define a function and build your image you want.


# 👋 Prerequisite
- Install `awscli`: [Official Document for installation](https://docs.aws.ßamazon.com/cli/latest/userguide/cli-chap-install.html)
    ```bash
    # After installing awscli.
    aws configure
    ```

- Install `direnv`
    ```bash
    # Install `direnv` (macOS)
    brew install direnv

    ## Append to `~/.zshrc`
    eval "$(direnv hook zsh)"
    ```

- Fill `envrc`
- Relaunch your shell.
    ```bash
    # Relaunch your shell.
    # Check the variables with the command as below.
    printenv | grep <VARIABLE-NAME>
    ```

# 🎮 How to deploy 
```bash
# Login ECR.
# https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-login-password.html
./scripts/00-login-ecr.sh

# Create ECR repository.
# https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/create-repository.html
./scripts/01-create-ecr-repository.sh

# Build image and push to Amazon ECR.
./scripts/02-ecr-tag-and-push.sh

# Create and deploy lambda function.
# https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-role.html
# https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-role-policy.html
./scripts/03-create-iam-for-lambda.sh

# https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-function.html
./scripts/04-deploy-to-lambda.sh

# Provision API Gateway.
# https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-rest-api.html
# https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-resources.html
# https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-resource.html
# https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-method.html
# https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-method-response.html
# https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-integration.html
# https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-integration-response.html
# https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-deployment.html
./scripts/05-create-api-gateway.py
```

# 🦿 Update your function.
```bash
# after fix code at './lambda'
./scripts/10-update-function.sh
```

# Customize boilerplate 
- Policy generator : https://awspolicygen.s3.amazonaws.com/policygen.html


# Reference
- https://docs.aws.amazon.com/lambda/latest/dg/python-image.html
- https://awscli.amazonaws.com/v2/documentation/api/latest/index.html
