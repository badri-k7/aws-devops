# Workshop: Installing Docker on AWS Cloud Shell

In this hands-on workshop, we'll guide you through the process of installing Docker on AWS Cloud Shell. 

## Prerequisites

- An AWS account with access to the AWS Management Console.
- AWS Cloud Shell access.

## Installing Docker

### 1. Access AWS Cloud Shell
1. Log into your [AWS Management Console](https://aws.amazon.com/console/).
2. At the top-right corner of the console, locate and click on the Cloud Shell icon (`>_`).
3. Wait for Cloud Shell to initialize, providing you with a command-line interface.

### 2. Update the Package Database
Before installing Docker, it's a good practice to update the package database:
```bash
sudo yum update -y
```
### 3. Install Docker
To install Docker, use the following command:
```
sudo yum install docker -y
```
### 4. Start the Docker Service
Once the installation is complete, start the Docker service:
```bash
sudo service docker start
```
### 5. Verify Docker Installation
To ensure Docker is correctly installed and running, run the following command:
```bash
docker --version
```
You should see the Docker version printed, indicating a successful installation.

## Conclusion

Congratulations! You've successfully installed Docker on AWS Cloud Shell. Now you're ready to pull and run containers on your AWS Cloud Shell environment.
