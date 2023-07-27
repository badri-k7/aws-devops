# Getting started
Welcome to the "Hands-On with AWS Application Services" repository! This repository is designed to help you explore and learn various AWS application services through practical examples and hands-on exercises using both Boto3 and AWS CLI.

- Clone the repository to your local machine.
- Follow the README files provided in each service folder for detailed instructions on using the examples.

**Table of Contents**

- [Introduction](./introduction)
  - [Prerequisites](./introduction/1.prerequesites)
    - [Local Development Environment Setup](./introduction/1.prerequesites/local-dev)
    - [Remote Development Environment Setup](./introduction/1.prerequesites/remote-dev)
  - [Deploy EC2 using AWS CLI](./introduction/2.ec2/1.deploy-ec2-using-aws-cli.md)
  - [Deploy EC2 using boto3](./introduction/2.ec2/2.deploy-ec2-using-boto3.md)
  - [Create S3 buckets using CLI](./introduction/3.s3/1.create-s3-bucket-and-upload-file-using-cli.md)
  - [Create S3 bucket using boto3](./introduction/3.s3/2.create-s3-bucket-using-boto3.md)
- [AWS Application Services](./module-aws-application-serices)
  - [DynamoDB handson with Boto3](./module-aws-application-serices/dynamodb/boto3)
  - [DynamoDB handson with CLI](./module-aws-application-serices/dynamodb/cli)
  - [SQS handson with Boto3](./module-aws-application-serices/sqs/boto3)


# Introduction

  The "Introduction" directory is your first step into this hands-on workshop. It offers a set of preliminary materials that prepare you for the rest of the modules. Please visit the "local-dev" directory for instructions on setting up your local AWS development environment or the "remote-dev" directory if you are planning to set up a remote environment.

 
# Module AWS Application Services
  The "Module AWS Application Services" directory contains several subdirectories for different AWS services such as DynamoDB and SQS. Each service directory contains markdown files with instructions for using the service with either AWS CLI or Boto3, as well as additional files and directories related to the service.

## DynamoDB
  The DynamoDB directory contains subdirectories for using DynamoDB with AWS CLI, Boto3, and for local development.

  - `dynamodb/boto3/1.create-table.md`: Contains instructions for creating a DynamoDB table using Boto3.
  
  - `dynamodb/boto3/2.crud-operations.md`: Provides guidelines for performing CRUD operations on a DynamoDB table using Boto3.

  - `dynamodb/cli/1.create-table.md`: This file contains instructions for creating a DynamoDB table using AWS CLI.

  - `dynamodb/cli/2.crud-operations.md`: This file contains instructions for performing CRUD operations on a DynamoDB table using AWS CLI.

## SQS
  The "SQS" directory contains a subdirectory for using SQS with Boto3

  - `sqs/boto3/1.create-sqs.md`: This markdown file contains instructions on how to create a new SQS queue using Boto3.
  
  - `sqs/boto3/2.send-messages-to-queue.md`: This markdown file provides guidelines on how to send messages to an SQS queue using Boto3.
  
  - `sqs/boto3/3.process-message-from-queue.md`: This markdown file demonstrates how to process messages from an SQS queue using Boto3.