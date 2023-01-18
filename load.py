import psycopg2
import sys
import configparser
from encodeAndDecode import encodeAndDecode

def load(transformed_messages):
    try:
        if len(transformed_messages) == 0:
            raise IndexError
    except IndexError as error:
        print('Error - '+ str(error))
        sys.exit()
    
    configuration = configparser.ConfigParser()

    # Read the config file
    configuration.read('config.ini')

    # Get config details
    username = configuration.get('postgres', 'username')
    password = configuration.get('postgres', 'password')
    host = configuration.get('postgres', 'host')
    database = configuration.get('postgres', 'database')

    con = psycopg2.connect(database = encodeAndDecode(database, 'decode'), user = encodeAndDecode(username,'decode'),
                            password = encodeAndDecode(password, 'decode'), host = encodeAndDecode(host, 'decode'))
    cursor = con.cursor()
    for i in range(len(transformed_messages)):
        data = list(transformed_messages[i].values())
        cursor.execute("INSERT into user_logins( \
                        user_id, app_version, device_type, masked_ip, locale, masked_device_id, create_date \
                        )VALUES(%s,%s,%s,%s,%s,%s,%s);",data)
        con.commit()
    con.close()
    return