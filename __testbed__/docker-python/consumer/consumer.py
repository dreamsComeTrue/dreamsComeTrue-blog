import os
import json
from kafka import KafkaConsumer

KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')

if __name__ == '__main__':
    f = open("out.txt","w+")
    
    consumer = KafkaConsumer("sandbox", bootstrap_servers=[KAFKA_BROKER_URL], 
                             value_deserializer=lambda value: json.loads(value))
    
    for message in consumer:
        f.write (str(message))
        
    f.close()