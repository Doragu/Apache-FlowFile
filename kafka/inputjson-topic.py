#!/usr/bin/python
import os
import json
from json import dumps
from time import sleep
from kafka import KafkaProducer


def connector():    
    result = False

    while result is False:
        try:
            producer = KafkaProducer(bootstrap_servers=['kafka:29092'], value_serializer=lambda x: dumps(x).encode('utf-8'))
            result = True   
        except:
            pass
        finally:
            sleep(0.5)

    return producer

def sendToKafka(file):
    with open(path+'/'+file) as f:
        try:
            data = json.load(f)
        except:
            pass

    for line in data:
        producer.send('json', value=line)
        sleep(0.1)

def checkForNewFiles(before):
    while 1:
        sleep (5)
        after = dict ([(f, None) for f in os.listdir (path)])
        added = [f for f in after if not f in before]
        if added:
            for file in added:
                if ".json" in file:
                    sendToKafka(file)
        before = after

if __name__ == "__main__":
    producer = connector()

    print("Connection passed")

    path = "./input_json"
    before = dict ([(f, None) for f in os.listdir (path)])

    for file in before:
        if ".json" in file:
            sendToKafka(file)

    checkForNewFiles(before)