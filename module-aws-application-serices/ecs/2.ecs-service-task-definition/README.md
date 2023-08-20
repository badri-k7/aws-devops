## Setting Up ECS Task Definition under Fargate Mode with CloudFormation

In this guide, you will learn how to create an ECS Task Definition for Fargate using a CloudFormation template.

### Prerequisites

- An active AWS account.
- AWS CLI installed and configured.
- An existing ECS cluster (like the one you've created in the previous steps).

### Instructions

#### 1. **Create the CloudFormation Template**:

Save the following content to a file named `ecs-fargate-task-definition.yml`.

```yaml
Resources:
  FargateTaskDefinition:
    Type: AWS::ECS::TaskDefinition
    Properties:
      Family: 'my-fargate-task-definition'
      NetworkMode: 'awsvpc'
      RequiresCompatibilities:
        - FARGATE
      Cpu: '256'
      Memory: '0.5GB'
      ExecutionRoleArn: !Ref EcsTaskExecutionRole
      ContainerDefinitions:
        - Name: 'my-container'
          Image: 'amazonlinux:2'
          Memory: 512
          Cpu: 256
          Essential: true
          PortMappings:
            - ContainerPort: 80
  FargateService:
    Type: AWS::ECS::Service
    Properties:
      ServiceName: 'my-fargate-service'
      Cluster: 'MyECSCluster' # Replace with your cluster name or ARN
      LaunchType: 'FARGATE'
      TaskDefinition: !Ref FargateTaskDefinition
      DesiredCount: 1
      NetworkConfiguration:
        AwsvpcConfiguration:
          AssignPublicIp: 'ENABLED'
          Subnets: 
            - 'subnet-xxxx' # Replace with your subnet ID
          SecurityGroups: 
            - 'sg-xxxx' # Replace with your security group ID            

  EcsTaskExecutionRole:
    Type: 'AWS::IAM::Role'
    Properties:
      RoleName: 'ecsTaskExecutionRole'
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: 'Allow'
            Principal:
              Service: 'ecs-tasks.amazonaws.com'
            Action: 'sts:AssumeRole'
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy'     
```

This CloudFormation template defines an ECS Task Definition for Fargate.

#### 2. **Deploy the CloudFormation Template**:

Execute the following command:

```bash
aws cloudformation create-stack --stack-name MyFargateTaskDefinition --template-body file://ecs-service-task-definition.yaml --capabilities CAPABILITY_NAMED_IAM
```

#### 3. **Verify the Task Definition**:

Go to the AWS Management Console:
- Navigate to CloudFormation.
- Look for the `MyFargateTaskDefinition` stack and verify its status is `CREATE_COMPLETE`.

Additionally, you can check in the ECS dashboard:
- Navigate to the Task Definitions on the ECS dashboard.
- You should see `my-fargate-task-definition` in the list of task definitions.

### Conclusion

Congratulations! You've successfully used CloudFormation to create and register a Fargate Task Definition under your ECS cluster. This task definition can now be used to launch containers under the Fargate launch type within your ECS cluster.
