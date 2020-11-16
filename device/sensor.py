# sensor.py

import queue
import threading
import time

class Sensor():
    def __init__(self, device, reporter, freq=1, qsize=None, **kwargs):
        self.device = device 
        self.reporter = reporter
        self.cache = self._build_cache(qsize)
        self.freq = freq
        self.active = False


    def _build_cache(self, qsize):
        if qsize is None:
            self.qsize = 1
        else:
            self.qsize = qsize 
        return queue.Queue(self.qsize)


    def read_one(self):
        self.cache.put(self.device.read())

    
    def read_multiple(self):
        while True:
            self.cache.put(self.device.read())
            time.sleep(1/self.freq)
            if not self.active:
                break
    

    def get_one(self):
        if self.cache.empty():
            return None 
        else:
            return self.cache.get()


    def report(self):
        self.reporter.send(self.get_one())

    
    def report_multiple(self):
        while True:
            if self.cache.full():
                for _ in range(self.qsize):
                    self.reporter.send(self.get_one())
            time.sleep(self.qsize/self.freq)
            if not self.active:
                break


    def run(self):
        read_thread = threading.Thread(target=self.read_multiple)
        report_thread = threading.Thread(target=self.report_multiple)
        self.op_threads = [read_thread, report_thread]
        self.start()


    def start(self):
        self.active = True
        [t.start() for t in self.op_threads]


    def stop(self):
        self.active = False
        [t.join() for t in self.op_threads]
