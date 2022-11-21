import json
import random

class Sensors(object):

    def __init__(self, mu, sigma):
        # Mean
        self.mu = mu
        # Standard Deviation
        self.sigma = sigma
        # Wind Direction
        self.wind_dir = [
            'N','NW','W','SW',
            'S','SE','E','NE'
        ]
        self.IoT_params = self.capsuler()
        
    
    def generator(self):
        # Gaussian Random Temperature Generator
        temp = random.gauss(self.mu, self.sigma)
        temp = float("{:.2f}".format(round(temp, 2)))
        #Gaussian Random Humidity Generator
        hum = int(random.gauss(self.mu, self.sigma))
        # Random Wind Direction Choice Generator
        wind = random.choice(self.wind_dir) 

        return [temp, hum, wind]

    def capsuler(self):
        temp, hum, wind = self.generator()
        json_aux = {}
        json_aux['temperatura'] = temp
        json_aux['humedad'] = hum
        json_aux['direccion_viento'] = wind
    
        return json.dumps(json_aux)
