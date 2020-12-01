# sensor.py

import time
import threading

class Sensor():
    def __init__(self, sid, device, reporter, freq=1, qsize=None, data_registry=None, 
                    threaded=False, **kwargs):
        self.sid = sid
        self.device = device(**kwargs)
        self.reporter = reporter(sid=sid, **kwargs)
    
        self.freq = freq
        self.active = False

        self._set_q_size(qsize)

        self.__name__ = sid

        self.threaded = threaded
        print(f'Sensor setup for {self.threaded}')


    def _set_q_size(self, qsize):
        if qsize is None:
            self.qsize = 1
        else:
            self.qsize = qsize


    def _fetch_cache(self):
        return self.data_registry[self.sid]


    def read_one(self):
        cache = self._fetch_cache()
        cache.put(self.device.read())

    
    def read_multiple(self):
        cache = self._fetch_cache()
        while True:
            cache.put(self.device.read())
            time.sleep(1/self.freq)
            if not self.active:
                break
    

    def get_one(self):
        cache = self._fetch_cache()
        if cache.empty():
            return None 
        else:
            return cache.get()


    def report(self):
        cache = self._fetch_cache()
        if not cache.empty():
            self.reporter.send(self.get_one())

    
    def report_multiple(self):
        cache = self._fetch_cache()
        while True:
            if cache.full():
                for _ in range(self.qsize):
                    self.reporter.send(self.get_one())
            self.sleep()
            if not self.active:
                break


    def sleep(self):
        time.sleep(self.qsize/self.freq)


    def _run_threaded(self):
        print('Creating read/report threads and starting operations.')
        read_thread = threading.Thread(target=self.read_multiple)
        report_thread = threading.Thread(target=self.report_multiple)
        self.op_threads = [read_thread, report_thread]
        [t.start() for t in self.op_threads]


    def _run_synchronous(self):
        print('Beginning synchronous operations.')
        while self.active:
            self.read_one()
            self.report()
            self.sleep()


    def start(self):
        self.active = True
        if self.threaded:
            self._run_threaded()
        else:
            self._run_synchronous()


    def stop(self):
        self.active = False
        if self.threaded:
            [t.join() for t in self.op_threads]
        else:
            pass




## Utility Class

class DataQueue():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.store = []
    
    def get(self):
        return self.store.pop()

    def put(self, value):
        self.store.append(value)

    def empty(self):
        return len(self.store) == 0
    
    def full(self):
        return len(self.store) >= self.maxsize



## Utility Functions

def start_sensor(sensor):
    sensor.start()


def stop_sensor(sensor):
    sensor.stop()