import os
from time import sleep
from kafka import KafkaProducer

KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')

if __name__ == '__main__':
    print (KAFKA_BROKER_URL)
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL)
    
    while True:
        message = 'HELLO'
        producer.send('queueing.transactions', value=message.encode())
        sleep(1000)