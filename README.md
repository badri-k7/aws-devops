# Getting started
Welcome to the "Hands-On with AWS Application Services" repository! This repository is designed to help you explore and learn various AWS application services through practical examples and hands-on exercises using both Boto3 and AWS CLI.

- Clone the repository to your local machine.
- Follow the README files provided in each service folder for detailed instructions on using the examples.

**Table of Contents**

- [Introduction](https://github.com/badri-k7/aws-devops/tree/main/introduction)
  - [Prerequisites](https://github.com/badri-k7/aws-devops/blob/main/introduction/1.prerequesites)
    - [Install AWS CLI](https://github.com/badri-k7/aws-devops/blob/main/introduction/1.prerequesites/1.install-aws-cli.md)
    - [Install Python pip](https://github.com/badri-k7/aws-devops/blob/main/introduction/1.prerequesites/2.install-python-pip.md)
  - [Deploy EC2 using AWS CLI](https://github.com/badri-k7/aws-devops/blob/main/introduction/2.ec2/1.deploy-ec2-using-aws-cli.md)
  - [Deploy EC2 using boto3](https://github.com/badri-k7/aws-devops/blob/main/introduction/2.ec2/2.deploy-ec2-using-boto3.md)
  - [Create S3 buckets using CLI](https://github.com/badri-k7/aws-devops/blob/main/introduction/3.s3/1.create-s3-bucket-and-upload-file-using-cli.md)
  - [Create S3 bucket using boto3](https://github.com/badri-k7/aws-devops/blob/main/introduction/3.s3/2.create-s3-bucket-using-boto3.md)
- [AWS Application Services](https://github.com/badri-k7/aws-devops/tree/main/module-aws-application-serices)
  - [DynamoDB handson with Boto3](https://github.com/badri-k7/aws-devops/tree/main/module-aws-application-serices/dynamodb/boto3)
  - [IAM handson with Boto3](https://github.com/badri-k7/aws-devops/tree/main/module-aws-application-serices/iam/boto3)
  - [KMS handson with Boto3](https://github.com/badri-k7/aws-devops/tree/main/module-aws-application-serices/kms/boto3)
  - [SQS handson with Boto3](https://github.com/badri-k7/aws-devops/tree/main/module-aws-application-serices/sqs/boto3)
  - [SWF handson with Boto3](https://github.com/badri-k7/aws-devops/tree/main/module-aws-application-serices/swf/boto3)
  - [Codeguru handson with Boto3](https://github.com/badri-k7/aws-devops/tree/main/module-aws-application-serices/codeguru-profiler/boto3)
  - [X-Ray Handson](https://github.com/badri-k7/aws-devops/tree/main/module-aws-application-serices/x-ray)

# Introduction

  The "Introduction" directory consists of various markdown files, providing instructions for installing and deploying different AWS services using AWS CLI and Boto3.

  - `1.prerequisites/1.install-aws-cli.md`: Contains instructions for installing AWS CLI on your local machine.
  - `1.prerequisites/2.install-python-pip.md`: Contains instructions for installing Python pip on your local machine.
  - `2.ec2/1.deploy-ec2-using-aws-cli.md`: Provides guidelines for deploying an EC2 instance using AWS CLI.
  - `2.ec2/2.deploy-ec2-using-boto3.md`: Contains instructions for deploying an EC2 instance using Boto3.
  - `3.s3/1.create-s3-bucket-and-upload-file-using-cli.md`: Contains instructions for creating an S3 bucket and uploading a file using AWS CLI.
  - `3.s3/2.create-s3-bucket-using-boto3.md`: Provides guidelines for creating an S3 bucket using Boto3.


# Module AWS Application Services
  The "Module AWS Application Services" directory contains several subdirectories for different AWS services such as DynamoDB, IAM, KMS, SNS, SQS, and SWF. Each service directory contains markdown files with instructions for using the service with either AWS CLI or Boto3, as well as additional files and directories related to the service.

## DynamoDB
  The DynamoDB directory contains subdirectories for using DynamoDB with AWS CLI, Boto3, and for local development.

  - `dynamodb/boto3/1.create-table.md`: Contains instructions for creating a DynamoDB table using Boto3.
  
  - `dynamodb/boto3/2.crud-operations.md`: Provides guidelines for performing CRUD operations on a DynamoDB table using Boto3.

  - `dynamodb/cli/1.create-table.md`: This file contains instructions for creating a DynamoDB table using AWS CLI.

  - `dynamodb/cli/2.crud-operations.md`: This file contains instructions for performing CRUD operations on a DynamoDB table using AWS CLI.

## IAM
  The IAM directory contains subdirectories for using IAM with AWS CLI and Boto3.

  - `iam/boto3/hands-on-with-iam.py`: This file contains Python code that demonstrates creating an IAM user, group, and policy using Boto3.

  - `iam/cli/policy_document.json`: This file contains a JSON policy document that can be used to create an IAM policy.

  - `iam/cli/role_document.json`: This file contains a JSON role document that can be used to create an IAM role.

## KMS
  The KMS directory contains a subdirectory for using KMS with Boto3.

  - `kms/boto3/file-to-encrypt.txt`: This file is a sample file that can be encrypted using KMS.

  - `kms/boto3/hands-on-with-kms.py`: This file contains Python code that demonstrates encrypting and decrypting a file using KMS and Boto3.

## SNS
  The SNS directory contains a subdirectory for using SNS with Boto3

  - `sns/boto3/hands-on-with-sns.py`: This file contains a Python script for using SNS with Boto3 to send/receive a message from/to a topic.

## SWF
  The SWF directory contains a subdirectory with the readme instructions for using SWF with Boto3

## Codeguru Profiler
  The Codeguru-Profiler directory cotains a subdirectory for using Codeguru profiler with boto3

  - `codeguru-profiler/boto3/hands-on-with-profiler.py`: This file contains a Python script for using AWS Codeguru Profiler with the lambda function.

## X-Ray
  The x-ray directory contains the readme instructions to deploy a sample application to generate the necessary distributed traces. This allows you to understand and gain deeper understanding of x-ray capabilities.