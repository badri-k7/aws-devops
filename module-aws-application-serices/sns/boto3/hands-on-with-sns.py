import boto3
import time


"""
    In this example, the script first creates an SNS client using the boto3.client() method. It then uses the create_topic() method to create a new SNS topic and retrieves the topic ARN from the response. Next, the script sends a message to the topic using the publish() method, passing in the topic ARN and the message to send. Finally, the script subscribes to the topic using the subscribe() method, specifying the protocol (in this case, email) and the endpoint (in this case, a sample email address).
"""

# Create an SNS client
sns = boto3.client('sns')

# Create an SNS topic
topic_arn = sns.create_topic(Name='my-topic')['TopicArn']

# Subscribe to the topic
protocol = 'email'
endpoint = 'user@example.com'
subscription_arn = sns.subscribe(TopicArn=topic_arn, Protocol=protocol, Endpoint=endpoint)['SubscriptionArn']

# Sleep for 120 seconds
time.sleep(120)

# Send a message to the topic
message = 'Hello, world!'
sns.publish(TopicArn=topic_arn, Message=message)
