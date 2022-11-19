import json
import time as t
from kafka import KafkaProducer
from sensors import Sensors as S

class Iot(object):

    def __init__(self, mu, sigma, time):
        # self.sim_running(mu,sigma, time)
        self.IoT_producer(mu,sigma, time)
        


    def sim_running(self, mu, sigma, time):
        on = True
        while on:
            data = S(mu, sigma)
            print(data.IoT_params)
            t.sleep(time)
    
    def IoT_producer(self,mu,sigma,time):
        topic = '19270'
        producer = KafkaProducer(
            bootstrap_servers='lab10.alumchat.fun:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
        on = True
        while on:
            data = S(mu, sigma)
            mssg = data.IoT_params
            certif = producer.send(topic, mssg)
            print(type(certif))
            t.sleep(time)

I = Iot(50,7,15)
# I.sim_running()
# I.IoT_producer()