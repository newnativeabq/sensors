# sensor.py

import queue

class Sensor():
    def __init__(self, device, reporter, qsize=None, **kwargs):
        self.device = device 
        self.reporter = reporter
        self.cache = self._build_cache(qsize)


    def _build_cache(self, qsize):
        if qsize is None:
            self.rqueue = 1
        else:
            self.rqueue = qsize 
        return queue.Queue(self.rqueue)


    def read(self):
        self.cache.put(self.device.read())
    

    def get_one(self):
        if self.cache.empty():
            return None 
        else:
            return self.cache.get()


    def report(self):
        self.reporter.send(self.get_one())