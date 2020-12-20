# sensorhandler.py

import multiprocessing as mp
from registry import Registry
from device import start_sensor, stop_sensor


class SensorHandler():
    def __init__(self, sensors:Registry, *args, **kwargs):
        self.sensors = sensors
        self.processes = []


    def __repr__(self):
        return f"<SensorHandler> {self.sensors}"
    

    def _get_sensors(self):
        return list(self.sensors.values())


    def initialize(self, data_registry):
        for s in self._get_sensors():
            s.data_registry = data_registry

    
    def _create_processes(self):
        for s in self._get_sensors():
            self.processes.append(
                mp.Process(target=start_sensor, args=(s,))
            )
        
    
    def _start_processes(self):
        for p in self.processes:
            p.start()


    def _stop_processes(self):
        # Add Listener to control signaling and process join.
        for p in self.processes:
            p.join()


    def run_all(self):
        self._create_processes()
        self._start_processes()
        self._stop_processes()


    def stop_all(self):
        self.p.map(stop_sensor, self._get_sensors())


    def start_single_sensor(self, sid):
        start_sensor(self.sensors[sid])


    def stop_single_sensor(self, sid):
        stop_sensor(self.sensors[sid])  ## TODO: check sensor registry for valid lookup