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