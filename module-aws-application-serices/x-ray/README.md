# AWS X-Ray sample application deployment using cloudformation

## Prerequisites
1. An AWS account
2. Access to AWS management console

## Steps to deploy sample application
1. **Access the CloudFormation Console**: Open the AWS Management Console and navigate to the CloudFormation console at `https://ap-southeast-1.console.aws.amazon.com/cloudformation/home?region=ap-southeast-1`.
2. **Create a new CloudFormation stack**: Click on "Create stack" and select "With new resources (standard)".
3. **Specify the template URL**: In the "Create stack" page, select "Amazon S3 URL" under the "Template source" section. Copy and paste the following URL into the "Amazon S3 URL" field:
    ```bash
    https://s3.amazonaws.com/aws-xray-assets.ap-southeast-1/samples/aws-xray-scorekeep-app.yaml
    ```
    Click "Next" to proceed. 
4. **Specify stack details**: In the "Stack name" field, enter "xray-sample" (or any desired name for the stack). Keep the default parameter values, then click "Next".
5. **Configure stack options**: You can add any tags, specify additional permissions, or configure advanced options. However, for this tutorial, leave the default settings and click "Next".
6. **Review stack details**: Review the stack name, template, and parameters. Ensure everything is correct, then check the box "I acknowledge that AWS CloudFormation might create IAM resources with custom names" at the bottom of the page. Click "Create stack" to initiate the stack creation process. 
7. **Monitor the stack creation**: On the "Stacks" page, select the "xray-sample" stack (or the name you provided earlier). In the "Events" tab, you can monitor the progress of the stack creation. Wait for the stack creation to complete with the status "CREATE_COMPLETE".
8. **Retrieve the LoadBalancerUrl**: Once the stack creation is complete, navigate to the "Outputs" tab. Copy the value of the "LoadBalancerUrl" key. This URL points to the deployed sample application.
9. **Visit the web page**: Open a new browser window or tab and paste the copied "LoadBalancerUrl" to visit the sample application's web page.
10. **View generated traces**: After interacting with the sample application, go to the AWS X-Ray console at `https://ap-southeast-1.console.aws.amazon.com/xray/home?region=ap-southeast-1#/service-map` to view the generated traces and analyze the performance of the application.

You have now successfully deployed the AWS X-Ray sample application using a CloudFormation template and can analyze its performance using the X-Ray console.