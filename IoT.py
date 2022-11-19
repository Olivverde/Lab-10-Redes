import time
from sensors import Sensors as S

class Iot(object):

    def __init__(self, mu, sigma, time):
        self.sim_running(mu,sigma, time)


    def sim_running(self, mu, sigma):
        on = True
        while on:
            data = S(mu, sigma)
            print(data.IoT_params)
            time.sleep(time)

I = Iot(50,7,15)
I.sim_running()