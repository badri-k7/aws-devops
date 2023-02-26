# Steps to launch EC2 instance using boto3

1. Install the Boto3 library using pip
```
pip install boto3
```

2. Import the necessary libraries
```
import boto3
```

3. Create an EC2 client 
```
ec2 = boto3.client('ec2')
```

4. Define the parameters for creating an EC2 instance. You can define parameters such as AMI ID, Instance type, Keypair, Securitygroup ID, User data and so on.
```
image_id = 'ami-0f2eac25772cd4e36'  # Amazon Linux 2 AMI
instance_type = 't2.micro'
key_name = 'intellipat-aws-devops-ec2-access'
security_group_ids = ['sg-074cc48af6898208b']
user_data = '''#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &
'''
```

5. Now launch the EC2 instance 
```
response = ec2.run_instances(
    ImageId=image_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=security_group_ids,
    UserData=user_data,
    MinCount=1,
    MaxCount=1
)
```

6. Wait for the instance to start up 
```
instance_id = response['Instances'][0]['InstanceId']
print('Instance ID:', instance_id)
```
7. Get the EC2 instance public IP address
```
response = ec2.describe_instances(InstanceIds=[instance_id])
ip_address = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
print('Public IP address:', ip_address)
```