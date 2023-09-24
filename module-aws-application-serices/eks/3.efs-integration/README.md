# Workshop: Setting Up EFS and Integrating it with EKS using CloudFormation

## Introduction
In this workshop, you'll learn how to create an Elastic File System (EFS) and integrate it with an existing EKS cluster using AWS CloudFormation. This will allow your EKS pods to access shared storage.

## Prerequisites
- An AWS account
- Basic knowledge of EKS and CloudFormation
- AWS CLI and `kubectl` installed
- An existing EKS cluster

## Hands-On Instructions

### Step 1: Validate the CloudFormation Template

Before creating the stack, validate the CloudFormation template to ensure that it doesn't have errors.

```bash
aws cloudformation validate-template --template-body file://eks-efs-integration.yaml
```

### Step 2: Deploy the CloudFormation Stack

Deploy the CloudFormation stack to create the EFS filesystem and other necessary resources.

```bash
aws cloudformation create-stack --stack-name eks-efs-integration --template-body file://eks-efs-integration.yaml
```

### Step 3: Confirm Resources

Once the CloudFormation stack is successfully created, confirm that the EFS filesystem and related resources are created. This can be done either from the AWS Management Console or via AWS CLI.

### Step 4: Create Persistent Volume and Persistent Volume Claim

Before integrating EFS with EKS, create a Persistent Volume (PV) and a Persistent Volume Claim (PVC) for the EFS filesystem. Use the EFS filesystem ID outputted by the CloudFormation stack.

```yaml
# Create efs-pv-pvc.yaml file
apiVersion: v1
kind: PersistentVolume
metadata:
  name: efs-pv
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteMany
  nfs:
    server: <EFS_SERVER_ID> #EFS DNS name in the EFS dashboard under the filesystem details.
    path: "/"
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: efs-pvc
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 5Gi
```

Apply the PV and PVC manifests:

```bash
kubectl apply -f efs-pv-pvc.yaml
```

### Step 5: Integrate EFS with EKS

Update your EKS cluster configurations or deployment manifests to use the EFS filesystem as a volume.

Example EKS Pod manifest snippet:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-efs-pod
spec:
  volumes:
  - name: efs-volume
    persistentVolumeClaim:
      claimName: efs-pvc  # The PVC that's backed by EFS
  containers:
  - name: my-container
    image: nginx:1.19  # Using a specific version for better reproducibility
    volumeMounts:
    - mountPath: /shared-data  # Path inside the container where the EFS volume will be mounted
      name: efs-volume
```

### Step 6: Deploy Manifests to EKS

Apply your updated manifests to your EKS cluster.

```bash
kubectl apply -f my-efs-pod.yaml
```

### Step 7: Confirm EFS Integration

Check if your EKS pods are running and confirm that they can read/write to the EFS filesystem.

```bash
kubectl exec -it <your_pod_name> -- /bin/bash
# inside the pod
cd /shared-data
touch test-file
```

## Conclusion
Congratulations! You have successfully integrated an EFS filesystem with your EKS cluster using AWS CloudFormation and Kubernetes manifests. Your EKS pods now have shared storage that they can use.
