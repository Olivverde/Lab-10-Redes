import json
import time as t
from kafka import KafkaProducer
from sensors import Sensors as S
import logging
import ast

class Producer(object):
    # logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s \n', level = logging.INFO)
    logging.basicConfig(format='%(message)s \n', level = logging.INFO)

    def __init__(self, mu, sigma, time):
        self.IoT_producer(mu,sigma, time)
        
    def IoT_producer(self,mu,sigma,time):
        topic = '19270'
        logging.info('Starting producer')
        producer = KafkaProducer(
            bootstrap_servers='lab10.alumchat.fun:9092',
            # value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
        on = True

        while on:
            data = S(mu, sigma)
            mssg = data.IoT_params
            mssg = ast.literal_eval(mssg)
            wind_options = ['N','NW','W','SW','S','SE','E','NE']

            temperature = int(mssg['temperatura'])
            humidity = mssg['humedad']
            wind = wind_options.index(mssg['direccion_viento']) + 100

            data = "{}{}{}".format(chr(temperature), chr(humidity), chr(wind))
            x = {}
            x =  data.encode('ASCII')

            # mssg = data.IoT_params
            

            certif = producer.send(topic, x)
            # mssg = ast.literal_eval(mssg)

            logging.info('Sending log: {}'.format(mssg))
            logging.info('Sending encoded: {}'.format(x))
            logging.info('---Delay---')
            t.sleep(time)

I = Producer(50,7,15)
