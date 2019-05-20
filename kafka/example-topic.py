#!/usr/bin/python
from time import sleep
from json import dumps
from kafka import KafkaProducer

sleep(40)

producer = KafkaProducer(bootstrap_servers=['kafka:29092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

for nextNumber in range(1000):
    data = {'number' : nextNumber}
    producer.send('test', value=data)
    print(nextNumber)
    sleep(5)