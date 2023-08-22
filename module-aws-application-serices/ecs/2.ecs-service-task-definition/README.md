## Setting Up ECS Task Definition under Fargate Mode with CloudFormation

In this guide, you will learn how to create an ECS Task Definition for Fargate using a CloudFormation template.

### Prerequisites

- An active AWS account.
- AWS CLI installed and configured.
- An existing ECS cluster (like the one you've created in the previous steps).

### Instructions

#### 1. **Create the CloudFormation Template**:

Refer to the `ecs-fargate-task-definition.yaml` file in your current working directory. Take a moment to familiarize yourself with the content of the file before proceeding with the hands-on instructions below.

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
          Command:
            - "/bin/sh"
            - "-c"
            - "while true; do echo hello world; sleep 30; done"
          PortMappings:
            - ContainerPort: 80
          LogConfiguration:
            LogDriver: "awslogs"
            Options:
              awslogs-group: !Ref MyLogGroup
              awslogs-region: "ap-southeast-1" # Change this to your region
              awslogs-stream-prefix: "ecs"            
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
  
  MyLogGroup:
    Type: "AWS::Logs::LogGroup"
    Properties: 
      LogGroupName: "/ecs/my-log-group"
      RetentionInDays: 14 # This is optional; defines how long to keep logs. Adjust as necessary.
```

This CloudFormation template defines an ECS Task Definition and a Fargate service.

#### 2. **Deploy the CloudFormation Template**:

Execute the following command:

```bash
aws cloudformation create-stack --stack-name MyFargateTaskDefinition --template-body file://ecs-service-task-definition.yaml --capabilities CAPABILITY_NAMED_IAM
```

#### 3. **Verify the Task Definition**:

Go to the AWS Management Console:
- Navigate to CloudFormation.
- Look for the `MyFargateTaskDefinition` stack and verify its status is `CREATE_COMPLETE`.

Additionally, verify the setup in the ECS dashboard:
1. Navigate to the ECS dashboard in the AWS Management Console.
2. In the left sidebar, click on **Task Definitions**. You should see `my-fargate-task-definition` listed among the task definitions.
3. Next, click on **Clusters** in the left sidebar.
4. Select your cluster (e.g., `MyECSCluster`).
5. Within the **Services** tab, you should see your service (e.g., `my-fargate-service`) listed and running. This verifies that both your task definition and service have been created successfully.


### Conclusion

Congratulations! You've successfully used CloudFormation to create, register a Fargate Task Definition, and establish an ECS Service under your ECS cluster. This task definition and service combination enables you to seamlessly launch containers using the Fargate launch type within your ECS cluster.
