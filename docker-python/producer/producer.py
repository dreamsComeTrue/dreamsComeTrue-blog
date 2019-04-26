import os
import datetime
import socket
from json import dumps
from time import sleep
from kafka import KafkaProducer

KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')

if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER_URL], retries=5, 
                             value_serializer=lambda x: 
                             dumps(x).encode('utf-8'))
    
    while True:
        message = {'HELLO': str(datetime.datetime.now().time())}
        producer.send('sandbox', value=message)
        sleep(5)
        print ("Sent!")