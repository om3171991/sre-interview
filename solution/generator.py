import boto3
import random
sqs = boto3.client('sqs',region_name="ap-southeast-1",endpoint_url="http://localstack:4566")
sqs.create_queue(QueueName='test-queue')
count = random.randint(10, 100)
print(count)
while count > 0 :
    message_body="Test message {}".format(count)
    sqs.send_message(QueueUrl='http://localstack:4576/000000000000/test-queue',MessageBody=message_body)
    count-=1
   
print("completed")
