import boto3
import base64
from botocore.exceptions import ClientError

# Define the name of the CMK and the name of the file to encrypt
cmk_name = 'my-cmk'
filename = 'file-to-encrypt.txt'

# Create a KMS client
kms = boto3.client('kms')

# Create a customer master key
try:
    # Create a new customer master key with the specified description
    # Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/create_key.html
    response = kms.create_key(Description='CMK for study')
    cmk_arn = response['KeyMetadata']['Arn']
    print("Created new customer master key with ARN: " + cmk_arn,"\n")
except ClientError as e:
    # If the key already exists, retrieve its ARN
    if e.response['Error']['Code'] == 'AlreadyExistsException':
        # Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/describe_key.html
        response = kms.describe_key(KeyId=cmk_name)
        cmk_arn = response['KeyMetadata']['Arn']
        print("Customer master key already exists with ARN: " + cmk_arn,"\n")
    else:
        # Print any other errors that occur
        print("Unexpected error: " + str(e))

# Retrieve an existing master key
try:
    # Retrieve an existing customer master key by its name
    response = kms.describe_key(KeyId=cmk_name)
    cmk_arn = response['KeyMetadata']['Arn']
    print("Retrieved customer master key with ARN: " + cmk_arn,"\n")
except ClientError as e:
    # Print any errors that occur
    print("Error retrieving customer master key: " + str(e),"\n")

# Create a data key
try:
    # Generate a new data key using the customer master key
    # Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/generate_data_key.html
    response = kms.generate_data_key(KeyId=cmk_arn, KeySpec='AES_256')
    ciphertext_blob = response['CiphertextBlob']
    plaintext_key = response['Plaintext']
    print("Created data key with ciphertext blob: " + base64.b64encode(ciphertext_blob).decode('utf-8'),"\n")
except ClientError as e:
    # Print any errors that occur
    print("Error creating data key: " + str(e),"\n")

# Encrypt a file
with open(filename, 'rb') as f:
    data = f.read()

try:
    # Encrypt the file using the customer master key
    # Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/encrypt.html
    response = kms.encrypt(KeyId=cmk_arn, Plaintext=data)
    ciphertext_blob = response['CiphertextBlob']
    with open(filename + '.encrypted', 'wb') as f:
        f.write(ciphertext_blob)
    print("File encrypted successfully!\n")
except ClientError as e:
    # Print any errors that occur
    print("Error encrypting file: " + str(e),"\n")

# Decrypt a data key
try:
    # Decrypt the data key using the customer master key
    # Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/decrypt.html
    response = kms.decrypt(CiphertextBlob=ciphertext_blob)
    decrypted_key = response['Plaintext']
    print("Decrypted data key: " + base64.b64encode(decrypted_key).decode('utf-8'),"\n")
except ClientError as e:
    # Print any errors that occur
    print("Error decrypting data key: " + str(e),"\n")

# Decrypt a file
with open(filename + '.encrypted', 'rb') as f:
    ciphertext_blob = f.read()

try:
    # Decrypt the file using the decrypted data key
    # Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/decrypt.html
    response = kms.decrypt(CiphertextBlob=ciphertext_blob)
    decrypted_data = response['Plaintext']
    with open(filename + '.decrypted', 'wb') as f:
        f.write(decrypted_data)
    print("File decrypted successfully!\n")
except ClientError
