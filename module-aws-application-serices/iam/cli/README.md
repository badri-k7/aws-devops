# Hands on with IAM using CLI

1. Create a new IAM user
    ```bash
    aws iam create-user --user-name study_iam_user
    ```
2. Create a new IAM policy
    ```bash
    aws iam create-policy --policy-name my-policy --policy-document file://policy.json
    ```
3. Create a new IAM role
    ```bash
    aws iam create-role --role-name study_iam_role --assume-role-policy-document file://role_document.json
    ```
4. Attach the policy to the role
    ```bash
    aws iam attach-role-policy --role-name study_iam_role --policy-arn <policy-arn>
    ```
5. Attach the policy to the user
    ```bash
    aws iam attach-user-policy --user-name study_iam_user --policy-arn <policy-arn>
    ```
6. To set an initial password for an IAM user
    ```bash
    aws iam create-login-profile --user-name <USER-NAME> --password <PASSWORD> --no-password-reset-required
    ```
7. To request temporary security credentials for a role you're authorized to assume

    ```bash
    aws sts assume-role --role-arn "arn:aws:iam::<ACCOUNT_ID>:role/<ROLE_NAME>" --role-session-name "MySession"
    ```

    Upon successful execution of the command, you'll receive a JSON response containing temporary security credentials, including an AccessKeyId, SecretAccessKey, and SessionToken. You can use these temporary credentials to make subsequent API requests

    To use the temporary credentials with the AWS CLI, you can set the following environment variables:

    ```bash
    export AWS_ACCESS_KEY_ID=<AccessKeyId>
    export AWS_SECRET_ACCESS_KEY=<SecretAccessKey>
    export AWS_SESSION_TOKEN=<SessionToken>
    ```

    With these environment variables set, the AWS CLI will use the temporary credentials for subsequent commands, allowing you to perform actions as the assumed role.

    Keep in mind that the temporary credentials have a limited duration, which by default is 1 hour, but can be set between 15 minutes and 12 hours using the `--duration-seconds` parameter when calling `assume-role`