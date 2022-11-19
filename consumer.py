import json
import pandas as pd
from datetime import datetime
from kafka import KafkaConsumer
import matplotlib.pyplot as plt

class Consumer(object):

    def __init__(self):
        self.IoT_consumer()
        
    def IoT_consumer(self):
        topic = '19270'
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers='lab10.alumchat.fun:9092',
            value_deserializer=lambda m: json.loads(m.decode('ascii'))
            )
        on = True
        while on:
            print('---waiting---')
            msg = next(consumer)
            time = datetime.fromtimestamp(int(msg.timestamp/1000))
            value_dic = self.deserializer(msg.value)
            temp = value_dic['temperatura']
            hum = value_dic['humedad']
            wind = value_dic['direccion_viento']

    def deserializer(self, json_mssg):
        json_dic = json.loads(json_mssg)
        
        return json_dic

I = Consumer()
