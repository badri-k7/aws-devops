# Workshop Modules Overview

This workshop comprises various modules introducing you to AWS services and how to interact with them using the AWS CLI and Python's Boto3 library. 

## Prerequisites

Before starting with the modules, ensure that you have the necessary setups. Follow the instructions in the given order:

1. [Install AWS CLI](./1.prerequesites/1.install-aws-cli.md): Follow the instructions to install and configure AWS CLI on your local machine.

2. [Install Python, pip and Boto3](./1.prerequesites/2.install-python-pip.md): Python and pip are essential for running Boto3 scripts. Boto3 is the Amazon Web Services (AWS) SDK for Python, which allows Python developers to write software that makes use of AWS services like Amazon S3, Amazon EC2, etc.

3. [Setup Default VPC and Key Pair](./1.prerequesites/3.setup.py): This script will guide you through setting up a default VPC if it does not exist, or describing the default VPC if it already exists. It will also generate a key pair for accessing the EC2 instance.

After you've completed the prerequisites, proceed with the following modules:

## EC2 Module

1. [Deploy EC2 instance using AWS CLI](./2.ec2/1.deploy-ec2-using-aws-cli.md): Learn how to deploy an EC2 instance using AWS CLI in this module.

2. [Deploy EC2 instance using Boto3](./2.ec2/2.deploy-ec2-using-boto3.md): This module provides instructions to deploy an EC2 instance using Python's Boto3 library.

## S3 Module

1. [Create S3 bucket and upload file using CLI](./3.s3/1.create-s3-bucket-and-upload-file-using-cli.md): This module guides you on creating an S3 bucket and uploading a file using AWS CLI.

2. [Create S3 bucket using Boto3](./3.s3/2.create-s3-bucket-using-boto3.md): Learn how to create an S3 bucket using Python's Boto3 library in this module.
