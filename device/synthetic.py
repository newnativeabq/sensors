# synthetic.py

import os
import time


class Timer():
    def __init__(self, **kwargs):
        self.setup_system()

    def setup_system(self):
        pass

    def read(self):
        return {'value': int(time.time())}
