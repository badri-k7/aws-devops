# Workshop: Creating a Dockerfile, Building an Image, and Pushing to Amazon ECR

In this hands-on activity, we'll walk you through creating a Dockerfile, building a Docker image from that file, and then pushing the image to Amazon Elastic Container Registry (ECR).

## Prerequisites

- A functional installation of Docker.
- An AWS Cloud9 or local development environment.
- AWS CLI installed and configured with the necessary permissions.
- An AWS account with permissions to use Amazon ECR.

## Steps

### 1. Create a Dockerfile
In your Cloud9 or local environment, create a new file named `Dockerfile`:

```bash
touch Dockerfile
```
Open the Dockerfile in an editor and add the following content:
```bash
# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory's contents into the container at /app
COPY . /app

# Define an environment variable
ENV NAME=World

# Run a simple Python script when the container launches
CMD ["python", "-c", "print(f'Hello, $NAME!')"]
```

This Dockerfile describes a simple container that prints "Hello, World!" using Python.

### 2. Build the Docker Image
Navigate to the directory containing your Dockerfile and run:

```bash
docker build -t hello-world .
```
This will build the Docker image with the tag hello-world.

### 3. Push the Image to Amazon ECR
First, ensure you have an ECR repository to push your image. If you don't, create one:
```bash
aws ecr create-repository --repository-name hello-world
```
Authenticate Docker to the ECR registry:
```bash
$(aws ecr get-login --no-include-email --region your-region-name)
```
Replace your-region-name with your AWS region, for example ap-southeast-1.
Tag your image for the ECR repository:
```bash
docker tag hello-world:latest your-account-id.dkr.ecr.your-region-name.amazonaws.com/hello-world:latest
```
Replace your-account-id with your AWS account ID and your-region-name with your AWS region.

Now, push the image:
```bash
docker push your-account-id.dkr.ecr.your-region-name.amazonaws.com/hello-world:latest
```

## Conclusion
Congratulations! You've successfully created a Dockerfile, built a Docker image from it, and pushed the image to Amazon ECR. Understanding this process is key for deploying containerized applications on AWS!