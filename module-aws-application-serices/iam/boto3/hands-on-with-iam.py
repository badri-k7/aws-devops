import boto3
import json

# Create an IAM client
iam = boto3.client('iam')

# Define the name of the new user, policy, and role
user_name = 'study_iam_user'
policy_name = 'study_iam_policy'
role_name = 'study_iam_role'

# Create a new IAM user
# Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/create_user.html
response = iam.create_user(UserName=user_name)

# Print the response
print("Created new IAM user: ", response)

# Create a new IAM policy
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        }
    ]
}

# Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_policy
response = iam.create_policy(
    PolicyName=policy_name,
    PolicyDocument=json.dumps(policy_document)
)

# Print the response
print("Created new IAM policy: ", response)

# Get the policy ARN from the response
policy_arn = response['Policy']['Arn']


role_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "ec2.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }

# Create a new IAM role
# Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_role
response = iam.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument=json.dumps(role_document)
)


# Print the response 
print("Created new IAM role: ", response)

# Get the role ARN from the response
role_arn = response['Role']['Arn']

# Attach the policy to the role
# Documenation:https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.attach_role_policy

response = iam.attach_role_policy(
    RoleName=role_name,
    PolicyArn=policy_arn
)
# Print the response
print("Attached policy to role: ", response)


# Attach the policy to the user
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.attach_user_policy
# Attach the policy to the user
response = iam.attach_user_policy(
    UserName=new_username,
    PolicyArn=policy_arn
)

# Print the response
print("Attached policy to role: ", response)