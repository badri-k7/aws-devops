# AWS KMS Python Script
This script demonstrates how to use the AWS KMS (Key Management Service) to create a customer master key, generate a data key, and use the data key to encrypt and decrypt a file. 

## Requirements
1. Python 3.x
2. Boto3 library
3. AWS credentials with appropriate permissions to use the AWS KMS API

## Usage
1. Open the kms_python_script.py file in a text editor.
2. Set the `cmk_name` and `filename` variables at the top of the file to the desired values.
3. Run the script using Python:
    ```bash
    python kms_python_script.py
    ```
4. The script will create a customer master key (CMK) with the specified name if it does not already exist, or retrieve the existing CMK if it does exist.
5. The script will generate a data key using the CMK and print the ciphertext blob of the encrypted key.
6. The script will encrypt the specified file using the data key and save the encrypted data to a new file with the `.encrypted` extension.
7. The script will decrypt the data key using the CMK and print the plaintext key.
8. The script will decrypt the encrypted file using the decrypted data key and save the decrypted data to a new file with the `.decrypted` extension.

