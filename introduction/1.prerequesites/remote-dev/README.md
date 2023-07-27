# Launching AWS CloudShell

AWS CloudShell is a browser-based shell that you can use to interact directly with your AWS resources. In this guide, we will walk you through how to launch AWS CloudShell from your laptop.

1. Log in to AWS Management Console

First, you will need to log in to the [AWS Management Console](https://aws.amazon.com/console/). 

2. Open AWS CloudShell

Once you are logged in to the AWS Management Console, you can launch CloudShell by clicking on the CloudShell icon in the upper right corner of the console.

The icon looks like a '>' symbol.

Clicking on the icon will open a new pane at the bottom of your screen. This is the AWS CloudShell.

3. Start using AWS CloudShell

Once CloudShell has launched, you can start using it to interact with your AWS resources.

You can type AWS CLI commands directly into the CloudShell. It comes pre-configured with AWS CLI, so there is no need for you to install or manage any software.

Note that AWS CloudShell is available at no extra charge, but standard rates for other AWS services used with CloudShell still apply.

If you are new to AWS CLI or CloudShell, AWS provides comprehensive guides and tutorials that you can follow. You can find these in the [official AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html).

4. Install pip and boto3

You will need to install pip and boto3 in your CloudShell environment. To do this, follow the instructions outlined in the [2.install-python-pip-boto3.md](../local-dev/2.install-python-pip-boto3.md) file.

5. Clone this repo
This repositoty contains the instructions needed to run this workshop

   ```bash 
   git clone https://github.com/badri-k7/aws-devops.git
   ```

6. [Setup Default VPC and Key Pair](./1.setup.py): This script will guide you through setting up a default VPC if it does not exist or describing the default VPC if it already exists. It will also generate a key pair for accessing the EC2 instance.

    Upon completion of this script, make sure to:

    - Copy and save the KeyPair name "awsug-workshop-keypair"; you'll need these for later modules.
    - Download the private key file for the key pair (`awsug-workshop-keypair.pem`), and keep it secure. This key file is necessary to connect to your EC2 instances if needed.
    - [Optional]Configure the private key in your local SSH configuration. If you're using a UNIX-like system (Linux, MacOS), you can generally do this by adding the private key to the SSH agent with the `ssh-add` command. If you're on Windows and using Putty, you'll need to convert the `.pem` file into a `.ppk` file using PuttyGen and then configure Putty to use it. If you're unsure about this step, just keep the key safe—you'll need it to access the EC2 instance later.

After you've completed the prerequisites, proceed with the following modules:

## EC2 Module

1. [Deploy EC2 instance using AWS CLI]( ../../2.ec2/1.deploy-ec2-using-aws-cli.md): Learn how to deploy an EC2 instance using AWS CLI in this module.

2. [Deploy EC2 instance using Boto3](../../2.ec2/2.deploy-ec2-using-boto3.md): This module provides instructions to deploy an EC2 instance using Python's Boto3 library.

## S3 Module

1. [Create S3 bucket and upload file using CLI](../../3.s3/1.create-s3-bucket-and-upload-file-using-cli.md): This module guides you on creating an S3 bucket and uploading a file using AWS CLI.

2. [Create S3 bucket using Boto3](../../3.s3/2.create-s3-bucket-using-boto3.md): Learn how to create an S3 bucket using Python's Boto3 library in this module.
