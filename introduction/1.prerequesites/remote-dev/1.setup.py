import boto3
from botocore.exceptions import ClientError

def main():
    region_name = 'ap-southeast-1'
    ec2 = boto3.client('ec2', region_name=region_name)

    try:
        default_vpc = ec2.create_default_vpc()
        print("VPC ID: ", default_vpc['Vpc']['VpcId'])

        describe_subnets_and_sg(default_vpc['Vpc']['VpcId'], region_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'DefaultVpcAlreadyExists':
            print("Default VPC already exists. Describing its subnets and security group.")
            default_vpc = ec2.describe_vpcs(
                Filters=[
                    {
                        'Name': 'isDefault',
                        'Values': [
                            'true',
                        ]
                    },
                ]
            )
            vpc_id = default_vpc['Vpcs'][0]['VpcId']
            describe_subnets_and_sg(vpc_id, region_name)
        else:
            print("Unexpected error: %s" % e)

    try:
        response = ec2.create_key_pair(KeyName='awsug-workshop-keypair')
        print('KeyPair: ', response['KeyMaterial'])
    except ClientError as e:
        if e.response['Error']['Code'] == 'InvalidKeyPair.Duplicate':
            print("KeyPair 'awsug-workshop-keypair' already exists.")
        else:
            print("Unexpected error: %s" % e)

def describe_subnets_and_sg(vpc_id, region_name):
    ec2 = boto3.client('ec2', region_name=region_name)
    subnets = ec2.describe_subnets(
        Filters=[
            {
                'Name': 'vpc-id',
                'Values': [
                    vpc_id,
                ]
            },
        ]
    )
    print("Subnet IDs: ")
    for subnet in subnets['Subnets']:
        print(subnet['SubnetId'], "\n")

    security_groups = ec2.describe_security_groups(
        Filters=[
            {
                'Name': 'vpc-id',
                'Values': [
                    vpc_id,
                ]
            },
        ]
    )
    print("Security Group IDs: ")
    for sg in security_groups['SecurityGroups']:
        print(sg['GroupId'], "\n")

if __name__ == '__main__':
    main()
