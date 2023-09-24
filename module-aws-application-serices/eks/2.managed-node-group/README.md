## Hands-On: Adding Managed Node Groups to EKS Cluster with CloudFormation

In this hands-on workshop, you will be adding managed node groups to your existing EKS cluster using AWS CloudFormation.

### Prerequisites
- An existing EKS cluster deployed
- AWS CLI installed and configured
- `kubectl` installed
- AWS CloudFormation Template for managed node groups

### Step 1: Validate the CloudFormation Template

Before creating the stack, validate the CloudFormation template to ensure that it doesn't have errors.

```bash
aws cloudformation validate-template --template-body file://eks-managed-node-group.yaml
```

### Step 2: Create CloudFormation Stack

Create a new CloudFormation stack to deploy the managed node group into your existing EKS cluster.

```bash
aws cloudformation create-stack --stack-name eks-managed-node-group \
  --template-body file://eks-managed-node-group.yaml 
```

### Step 3: Monitor the Stack Creation

You can either monitor the stack creation from the AWS Management Console or use the AWS CLI as shown below:

```bash
aws cloudformation describe-stacks --stack-name eks-managed-node-group
```

### Step 4: Verify Node Group Addition in EKS

Once the CloudFormation stack shows a `CREATE_COMPLETE` status, verify that the managed node group has been added to the EKS cluster.

```bash
kubectl get nodes
```

Congratulations! You have successfully added a managed node group to your EKS cluster using CloudFormation.
