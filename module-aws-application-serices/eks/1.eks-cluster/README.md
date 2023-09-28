## Setting Up EKS Cluster

---

#### Pre-requisites
- IAM roles
- VPC
- Subnets

#### Overview
In this section, we will go over how to create an EKS cluster using CloudFormation. AWS CloudFormation allows you to use programming languages or a simple text file to model and provision, in an automated and secure manner, all the resources needed for your applications across all regions and accounts.

---

## Setting Up Your Remote IDE

### 1. Access AWS Cloud9

1. Log into your [AWS Management Console](https://aws.amazon.com/console/).
2. Navigate to the "Services" dropdown and select "Cloud9" under "Developer Tools".
3. Click on "Create environment".
   - **Name and description**: Provide a name for your environment and an optional description.
   - For the purpose of this workshop, leave all other settings at their defaults. Once you've provided a name and description, proceed to "Create environment".
4. After a short wait, your Cloud9 environment will be ready. You'll be presented with an IDE interface along with a terminal at the bottom.


#### Step 1: Clone the Workshop Repository
Firstly, clone the GitHub repository that contains the CloudFormation templates.
```bash
git clone https://github.com/badri-k7/aws-devops.git
```

#### Step 2: Navigate to CloudFormation Template Directory
Navigate into the directory where the CloudFormation template for EKS setup is located.
```bash
cd <repository_directory>/module-aws-application-serices/eks/1.eks-cluster
```

#### Step 3: Validate the CloudFormation Template
Run this command to validate your CloudFormation template.
```bash
aws cloudformation validate-template --template-body file://eks-cluster-setup.yaml
```

#### Step 4: Create the EKS Cluster
Run the following command to create a CloudFormation stack that will provision your EKS cluster.
```bash
aws cloudformation create-stack --stack-name EKSCluster --template-body file://eks-cluster-setup.yaml --capabilities CAPABILITY_NAMED_IAM
```

Wait for the CloudFormation stack to reach the `CREATE_COMPLETE` state. You can monitor the stack creation from the AWS Management Console using;

```
aws cloudformation describe-stacks --stack-name EKSCluster
```

## Additional Post-Cluster Creation Steps

### Installing `kubectl`

Before configuring `kubectl` for EKS Cluster Access, make sure `kubectl` is installed. If it's not, follow these steps to install it:

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

### Configuring `kubectl` for EKS Cluster Access

1. Once your CloudFormation stack creation is complete and the EKS Cluster is ready, you'll need to update your `kubeconfig` to add the new EKS cluster. Open your Cloud9 terminal and execute:

   ```bash
   aws eks --region [REGION] update-kubeconfig --name [EKS_CLUSTER_NAME]
   ```
   - Replace `[REGION]` with the AWS region where your cluster is deployed.
   - Replace `[EKS_CLUSTER_NAME]` with the name of your new EKS cluster.

This command configures `kubectl` to use the new EKS cluster by updating the `kubeconfig` file, usually located in `~/.kube/config`.

2. To verify that your `kubeconfig` has been updated, you can run:
  
   ```bash
   kubectl config get-contexts
   ```
   Look for the name of your new EKS cluster in the output.
---

## Verifying Your EKS Cluster

### Step 5: Verify Your EKS Cluster

To ensure that your EKS cluster has been set up correctly, run the following command:

```bash
kubectl get svc
```

If everything has been configured correctly, you should see the Kubernetes services up and running.
---

That's the end of the EKS cluster setup section. Next, we will move on to the next part of the workshop.

