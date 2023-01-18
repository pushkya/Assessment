import configparser
from extract import extract
from transform import transform
from load import load
import argparse

def main():
    
    #Reference: YouTube Data Engineering: Bootcamp By Alexi
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--endpoint-url', required = True ,help = "Endpoint URL")
    parser.add_argument('-q', '--queue-name', required = True ,help = "Queue Name")
    parser.add_argument('-t', '--wait-time', type = int, default = 5, help = "Wait time (default = 5)")
    parser.add_argument('-m', '--message-length', type = int, default = 25, help = "Maximum messages (default = 25)")
    
    #Argument parsing
    arguments = vars(parser.parse_args())

    #Getting value for each argument
    endpoint_url = arguments['endpoint_url']
    queue_name = arguments['queue_name']
    waitTime = arguments['wait_time']
    messageLength = arguments['message_length']

    #Extract messages
    print("Extracting messages from SQS Queue")
    messages = extract(endpoint_url, queue_name, waitTime, messageLength)
    
    #Transform IP and device_id, converting None to 'None' and adding datetime
    print("Transforming messages")
    transformed_messages = transform(messages)
    
    #Load data to Postgres
    print("Loading messages to Postgres...")
    load(transformed_messages)

    #Return from the main function
    return

if __name__ == '__main__':
    main()