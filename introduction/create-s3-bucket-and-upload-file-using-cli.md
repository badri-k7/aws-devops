# CLI commands to create S3 bucket and Upload files

To create an S3 bucket and upload files to it using the AWS CLI, you can use the **s3api** and **s3** commands. Here are the steps:

1. Create a new S3 bucket using the `s3api` command. Update LocationConstraint to the region you want to create S3 bucket and replace `my-bucket-name` with the name you want to give to your bucket:

    ```bash
    aws s3api create-bucket --bucket my-bucket-name --create-bucket-configuration LocationConstraint=ap-southeast-1
    ```

2. Upload a file to the S3 bucket using the `s3` command. Replace `file.txt` with the name of the file you want to upload, and replace `my-bucket-name` with the name of the bucket you created in step 1:

    ```bash
    aws s3 cp file.txt s3://my-bucket-name/
    ```

3. To upload multiple files at once, you can use the `sync` command. Replace `my-folder` with the path to the local folder containing the files you want to upload, and replace `my-bucket-name` with the name of the bucket you created in step 1:

    ```bash
    aws s3 sync my-folder/ s3://my-bucket-name/my-folder/
    ```