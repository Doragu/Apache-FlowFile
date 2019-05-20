#!/usr/bin/python
import os
import json
from json import dumps
from time import sleep
from kafka import KafkaProducer

sleep(30)

path = "./input_json"
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

before = dict ([(f, None) for f in os.listdir (path)])

for file in before:
    if ".json" in file:
        with open(path+'/'+file) as f:
            data = json.load(f)

        for line in data:
            producer.send('json', value=line)
            sleep(0.1)

while 1:
    sleep (5)
    after = dict ([(f, None) for f in os.listdir (path)])
    added = [f for f in after if not f in before]
    if added:
        for file in added:
            if ".json" in file:
                with open(path+'/'+file) as f:
                    data = json.load(f)
                for line in data:
                    producer.send('json', value=line)
                    sleep(0.1)
    before = after