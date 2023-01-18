import base64

def encodeAndDecode(messageAttributes, operation):
    if operation == 'encode':
        #Converting to bytes like object
        bytes_encoded = messageAttributes.encode('ascii')
        #Converting to base64
        result = base64.b64encode(bytes_encoded).decode('ascii')
        return result
    elif operation == 'decode':
        result = base64.b64decode(messageAttributes).decode('ascii')
        return result