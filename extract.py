import boto3
import sys

def extract(url, queue_name, waitTime, numberOfMessages = 25):
    
    #Instantiating SQS client using boto3 to receive messages from queue
    sqsClient = boto3.client("sqs", endpoint_url = url)
    messages = []
    
    try:
        response = sqsClient.receive_message(
                QueueUrl = url + '/' + queue_name,
                WaitTimeSeconds = waitTime,
                MaxNumberOfMessages = numberOfMessages)
    except Exception as exception:
        #Print the exception occuring while receiving the response
        print("Error - " +str(exception) + '. Try again')
        sys.exit()
        
    #Appending response messages in the queue    
    messages = response['Messages']
    
    return messages