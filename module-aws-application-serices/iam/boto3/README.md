# Hands on with IAM

## Prerequisites

1. **Install pip**: Follow the [Instructions](https://github.com/badri-k7/aws-devops/blob/main/introduction/0.install-python-pip.md) to install `pip` 

## Instructions to execute the `hands-on-with-iam.py` script

1. **Install Boto3** : If you haven't already done so, you'll need to install `Boto3`, the Python library for working with AWS, by running the command pip install boto3 in your terminal or command prompt.

2. **Configure AWS credentials**: Before you can use Boto3 to interact with AWS, you'll need to configure your AWS credentials. There are several ways to do this, such as setting environment variables, using a credentials file, or using an IAM role. For more information on configuring AWS credentials, see the [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#configuring-credentials)

3. **Clone the git repo** : Once you are in the directory where you want to clone the repository, use the `git clone` command followed by the URL of the Git repository.

    ```bash
    git clone https://github.com/badri-k7/aws-devops.git
    ```
4. **Run the script** : Run the script by executing the command `python hands-on-with-iam.py` in your terminal or command prompt.

5. **Verify the results** : After the script has finished running, you can verify that the IAM user, policy, and role were created by logging in to the AWS Management Console, navigating to the IAM service, and check the Users, Policies, and Roles sections. You should see the new IAM user, policy, and role listed with the names you specified in the script.