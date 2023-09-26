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

Before creating the stack, validate the CloudFormation template to ensure that it doesn't have errors. (Note: switch your directory to the `module-aws-application-services/eks/3.efs-integration` directory)

```bash
aws cloudformation validate-template --template-body file://eks-efs-integration.yaml
```

### Step 2: Deploy the CloudFormation Stack

Deploy the CloudFormation stack to create the EFS filesystem and other necessary resources.

```bash
aws cloudformation create-stack --stack-name eks-efs-integration --template-body file://eks-efs-integration.yaml
```

### Step 3: Deploy the EKS Add-ons CloudFormation Stack
Deploy the EKS add-ons CloudFormation stack to create the necessary add-ons, including the EFS CSI driver. Before deploying the EKS add-ons CloudFormation stack, ensure to replace the placeholders `OIDC_ENDPOINT` and `ACCOUNT_ID` in the `efs-addons-installation.yaml` template with appropriate values.


```bash
aws cloudformation create-stack --stack-name eks-addons --template-body file://efs-addons-installation.yaml --capabilities CAPABILITY_NAMED_IAM
```

### Step 4: Confirm Resources

Once the CloudFormation stack is successfully created, confirm that the EFS filesystem and related resources are created. This can be done either from the AWS Management Console or via AWS CLI.

### Step 5: Create Persistent Volume
First, create a Persistent Volume (PV) using the EFS filesystem ID that you get from the AWS EFS Dashboard. Create a YAML file named efs-pv.yaml with the following content:

```yaml
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: efs-pv
spec:
  capacity:
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  storageClassName: ""
  persistentVolumeReclaimPolicy: Retain
  csi:
    driver: efs.csi.aws.com
    volumeHandle: <REPLACE-WITH-EFS-FILE-SYSTEM-ID>
```

Apply the PV manifest:

```bash
kubectl apply -f efs-pv.yaml
```
### Step 6: Create Persistent Volume Claim
After successfully creating the PV, create a Persistent Volume Claim (PVC) to claim storage from the PV you just created. Create a YAML file named efs-pvc.yaml with the following content:

```yaml
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: efs-claim
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: ""
  resources:
    requests:
      storage: 5Gi
```

Apply the PVC manifest:

```bash
kubectl apply -f efs-pvc.yaml
```
### Step 7: Integrate EFS with EKS

Update your EKS cluster configurations or deployment manifests to use the EFS filesystem as a volume.

Example EKS Pod manifest snippet:

```yaml
---
apiVersion: v1
kind: Pod
metadata:
  name: efs-app
spec:
  containers:
  - name: app
    image: centos
    command: ["/bin/sh"]
    args: ["-c", "while true; do echo $(date -u) >> /data/out.txt; sleep 2; done"]
    volumeMounts:
    - name: persistent-storage
      mountPath: /data
  volumes:
  - name: persistent-storage
    persistentVolumeClaim:
      claimName: efs-claim
```

### Step 8: Deploy Manifests to EKS

Apply your updated manifests to your EKS cluster.

```bash
kubectl apply -f efs-pod.yaml
```

### Step 9: Confirm EFS Integration

Check if your EKS pods are running and confirm that they can read/write to the EFS filesystem.

```bash
kubectl exec -ti efs-app -- tail -f /data/out.txt
```

## Conclusion
Congratulations! You have successfully integrated an EFS filesystem with your EKS cluster using AWS CloudFormation and Kubernetes manifests. Your EKS pods now have shared storage that they can use.
