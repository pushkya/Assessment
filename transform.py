from encodeAndDecode import encodeAndDecode
from datetime import datetime
import sys
import json

def transform(messages):
    #Transformed messages result to be stored
    transformed_messages = []
    
    try:
        if len(messages) == 0:
            raise IndexError('Message queue is empty')
    except IndexError as error:
        print("Error - " + str(error))
        sys.exit()

    for message in messages:
        messageBody = json.loads(message['Body'])
        #Get IP and device_id from messageBody
        try:
            ip = messageBody['ip']
            device_id = messageBody['device_id']
        except Exception as exception:
            print('Exception: '+ str(exception))
            continue
        
        # Reference: https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
        # Masking IP and device_id using base64 encoding technique
        encodedIP = encodeAndDecode(ip, 'encode')
        encodedDeviceID = encodeAndDecode(device_id, 'encode')
        
        #Replacing masked IP and device_id with the original attributes
        messageBody['ip'] = encodedIP
        messageBody['device_id'] = encodedDeviceID
        
        #Replacing None with 'None' to insert into postgres
        messageBody['locale'] = 'None' if messageBody['locale'] == None else messageBody['locale']
        
        #Adding create date
        messageBody['create_date'] = datetime.now().strftime("%Y-%m-%d")
        transformed_messages.append(messageBody)

    return transformed_messages