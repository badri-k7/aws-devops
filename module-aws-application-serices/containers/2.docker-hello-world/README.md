# Workshop: Pulling and Running a Simple Container in AWS Cloud9

In this hands-on activity, we'll guide you through the process of accessing the AWS Cloud Shell, pulling a simple Docker container from Docker Hub, and running it on AWS Cloud Shell. We'll be using the classic `hello-world` container for demonstration.

## Prerequisites

- An AWS account with access to the AWS Management Console.
- AWS Cloud9 environment set up and running. If you haven't set it up, follow the "Getting Started" section below.

## Getting Started

### 1. Access AWS Cloud9
1. Log into your [AWS Management Console](https://aws.amazon.com/console/).
2. Navigate to the "Services" dropdown and select "Cloud9" under "Developer Tools".
3. Click on "Create environment". 
   - **Name and description**: Provide a name for your environment and an optional description.
   - For the purpose of this workshop, leave all other settings at their defaults. Once you've provided a name and description, proceed to "Create environment".
4. After a short wait, your Cloud9 environment will be ready. You'll be presented with an IDE interface along with a terminal at the bottom.

### 2. Pull the `hello-world` Container

With your Cloud9 terminal open, input the following command:

```bash
docker pull hello-world
```
This command fetches the `hello-world` container image from Docker Hub.

### 3. Verify the Image Has Been Pulled
To ensure the image has been downloaded, list the images on your Cloud9 system with:
```bash
docker images
```
Check for the `hello-world` image in the output list.

### 4. Run the `hello-world` Container
Now, initiate the pulled container:
```bash
docker run hello-world
```
This command should return a message confirming that your Docker installation is functioning correctly and detailing how the container operates.

## Conclusion

Great job! You've successfully accessed AWS Cloud9, pulled, and executed a simple container using Docker. This foundational knowledge will be pivotal as you delve deeper into the world of containers.