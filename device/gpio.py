# gpio.py

import os
import glob
import time


class W1Therm():
    def __init__(self, **kwargs):
        self.setup_system()

    def setup_system(self):
        device_folder = glob.glob('/sys/bus/w1/devices/' + '28*')[0]
        self.device_file = device_folder + '/w1_slave'

        if not os.path.isdir(device_folder):
            os.system('sudo modprobe w1-gpio')
            os.system('sudo modprobe w1-therm')
        

    def _validate_data(self, data):
        if 'YES' in data[0]:
            return self._strip_temp(data[1])
        else:
            raise ValueError(f'Issue with the data {data}')


    def _strip_temp(self, templine):
        epos = templine.find('t=')
        if epos != -1:
            return int(templine[epos+2:])


    def read(self):
        with open(self.device_file, 'r') as f:
            data = f.readlines()
        return {'value': self._validate_data(data)}
