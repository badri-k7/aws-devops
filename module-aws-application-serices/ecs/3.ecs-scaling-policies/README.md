## ECS Scaling and Monitoring

In this section, you will scale and monitor the ECS service that was previously set up.

### Step 1: Update your CloudFormation Template for Scaling

1. You'll be working with a CloudFormation template named `ecs-service-scaling.yaml`. If you're creating one from scratch or modifying an existing one, ensure it includes the following content. For the purpose of this workshop, a conveniently pre-configured template named "`ecs-scaling-policies.yaml`" is available for you to use.

```yaml
Parameters:
  ECSClusterName:
    Description: Name of the ECS Cluster
    Type: String

  ECSServiceName:
    Description: Name of the ECS Service
    Type: String

  EcsAutoScalingRoleName:
    Description: Name of the ECS Auto Scaling Role
    Type: String

Resources:

  EcsServiceScalableTarget:
    Type: 'AWS::ApplicationAutoScaling::ScalableTarget'
    Properties:
      MaxCapacity: 10
      MinCapacity: 1
      ResourceId: !Sub service/${ECSClusterName}/${ECSServiceName}
      RoleARN: !Sub arn:aws:iam::${AWS::AccountId}:role/${EcsAutoScalingRoleName}
      ScalableDimension: ecs:service:DesiredCount
      ServiceNamespace: ecs

  ECSServiceScalingPolicy:
    Type: 'AWS::ApplicationAutoScaling::ScalingPolicy'
    Properties:
      PolicyName: AStepPolicy
      PolicyType: StepScaling
      ScalingTargetId: !Ref EcsServiceScalableTarget
      StepScalingPolicyConfiguration:
        AdjustmentType: PercentChangeInCapacity
        CoolDown: 60
        MetricAggregationType: Average
        StepAdjustments:
          - MetricIntervalLowerBound: 0
            ScalingAdjustment: 1

  CloudWatchAlarmHighCPU:
    Type: 'AWS::CloudWatch::Alarm'
    Properties:
      AlarmDescription: Alarm if CPU too high or metric disappears indicating instance is down
      Namespace: AWS/ECS
      MetricName: CPUUtilization
      Statistic: Average
      Period: 300
      EvaluationPeriods: 2
      Threshold: 75
      ComparisonOperator: GreaterThanThreshold
      Dimensions:
        - Name: ServiceName
          Value: !Ref ECSServiceName
        - Name: ClusterName
          Value: !Ref ECSClusterName
      AlarmActions:
        - !Ref ECSServiceScalingPolicy
```

### Step 2: Update the CloudFormation Stack with Scaling Configurations

Using AWS CLI, apply the updated scaling template:

```bash
aws cloudformation deploy --template-file ecs-service-scaling.yaml --stack-name YourStackName --capabilities CAPABILITY_NAMED_IAM
```

Remember to replace `YourStackName` with the name of your CloudFormation stack

### Step 3: Monitoring with Amazon CloudWatch

After deploying the scaling configurations, you can monitor the ECS service's metrics with Amazon CloudWatch:

1. Open the **AWS Management Console**.
2. Navigate to the **Amazon CloudWatch** service.
3. In the navigation pane, select **Metrics**.
4. Choose the **ECS** namespace from the list.
5. Filter or search for metrics related to your ECS Cluster and Service. You can monitor various metrics like `CPUUtilization`, `MemoryUtilization`, and more.
6. Optionally, create a new CloudWatch Dashboard to visualize these metrics. Add widgets based on the metrics of interest for your service.

With these steps, you will be able to adjust the scaling of your ECS services based on demand and monitor their performance using CloudWatch.
