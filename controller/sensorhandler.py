# sensorhandler.py

import multiprocessing


class SensorHandler():
    def __init__(self, sensors:list, *args, **kwargs):
        self.p = multiprocessing.Pool(len(sensors))
        self.sensors = self._index_sensors(sensors)
    

    def _index_sensors(self, sensors):
        sensor_index = {}
        for s in sensors:
            sensor_index[s.sid] = s


    def _start_sensor(self, sensor):
        sensor.run()
    

    def _stop_sensor(self, sensor):
        sensor.stop()
    
    
    def _run_all(self):
        all_sensors = list(self.sensors.values())
        self.p.map(self._start_sensor, all_sensors)

    
    def _stop_all(self):
        all_sensors = list(self.sensors.values())
        self.p.map(self._stop_sensor, all_sensors())