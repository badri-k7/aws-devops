# CLI command to create EC2 instance

To create an EC2 instance using the AWS CLI, you can use the **run-instances** command. Here is an example:

```aws ec2 run-instances --region ap-southeast-1 --image-id ami-03f6a11788f8e319e --instance-type t2.micro --key-name aws-devops-ec2-access --security-group-ids sg-074cc48af6898208b  --subnet-id subnet-0d3ed57ca5e17e9da```

In this example, --region specifies the Singapore region (ap-southeast-1), --image-id specifies the ID of the Amazon Machine Image (AMI) to use for the instance, --instance-type specifies the instance type (t2.micro), --key-name specifies the name of the key pair to use for SSH access, --security-group-ids specifies the IDs of the security groups to associate with the instance, and --subnet-id specifies the ID of the subnet in which to launch the instance. Note that you should replace the example values for --image-id, --key-name, --security-group-ids, and --subnet-id with values that are appropriate for your specific setup.