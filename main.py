from confluent_kafka import Producer
from faker import Faker
import json
import time

def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        print(f'Produced message on topic {msg.topic()} with value of {msg.value().decode("utf-8")}')

def main():
    time.sleep(20) # Waiting for broker to load
    
    fake = Faker()
    producer=Producer({'bootstrap.servers':'broker:29092'})
    
    while True:
        messages = []
        
        for _ in range(2):
            data = { 'name': fake.name() }
            messages.append(json.dumps(data))
        
        producer.poll(0.25)
        
        for message in messages:
            producer.produce('Tutorial2.pets', message.encode('utf-8'), callback=receipt)
        
        producer.flush()
        
        time.sleep(2)
            
if __name__ == "__main__":
    main()