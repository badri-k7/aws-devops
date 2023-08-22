## Deploying the ECS Cluster using CloudFormation

In this hands-on guide, you will deploy an ECS cluster using AWS CloudFormation.

### Prerequisites

- An active AWS account.
- AWS CLI installed and configured.
- A cloned copy of this repository or the CloudFormation template file saved locally.

#### 1. Navigate to your working directory:
If you have cloned this repository, navigate to its directory in your terminal or command prompt. If you have saved only the CloudFormation template, make sure you're in its directory.

```bash
cd path/to/your/directory
```

#### 2. Deploy the CloudFormation Stack:
Run the following command to deploy the ECS cluster. Replace `YourStackName` with a name for your CloudFormation stack:

```bash
aws cloudformation create-stack --stack-name YourStackName --template-body file://ecs-cluster.yaml
```

#### 3. Monitor Stack Creation:
To view the status of your stack as AWS CloudFormation creates it, you can use:

```bash
aws cloudformation describe-stacks --stack-name YourStackName
```
Wait for the `"StackStatus"` field to show `"CREATE_COMPLETE"`.

#### 4. Retrieve Outputs:
After the stack creation completes, retrieve the outputs (the ECS cluster name and ARN) using:

```bash
aws cloudformation describe-stacks --stack-name YourStackName --query 'Stacks[0].Outputs'
```

### Cleanup
After you're done with the ECS cluster and want to delete it and associated resources, run:

```bash
aws cloudformation delete-stack --stack-name YourStackName
```

### Conclusion

Congratulations! You've successfully deployed an ECS cluster using AWS CloudFormation. You can now move on to deploying task definitions or other resources associated with ECS.