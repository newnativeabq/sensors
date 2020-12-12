"""
Main.py

Set up sensor collection and reading suite
"""

from device import W1Therm, Sensor, Camera, DataQueue, start_sensor, stop_sensor
from export import HTTP, Printer
from registry import Registry
from controller import SensorHandler
import multiprocessing as mp 
import queue

sensor_group = Registry()
data_registry = Registry()

### Configure Sensors ###

therm = Sensor(
    sid='therm1',
    device=W1Therm,
    reporter=HTTP,
    target="http://192.168.1.37:8080/api/data/",  # Endpoint will redirect if trailing '/' not included!
    # target='https://httpbin.org/post',
    auth=None,
    freq=1/30,
    template={'sid':None, 'value':None},
    threaded=False,
)
sensor_group.register(therm)


camera = Sensor(
    sid='camera1',
    device=Camera,
    reporter=HTTP,
    target="http://192.168.1.37:8080/api/data/",
    # target='https://httpbin.org/post',
    auth=None,
    freq=1/60,
    template={'sid':None, 'value':None, 'files': None},
    threaded=False,
)
sensor_group.register(camera)

if __name__ == '__main__':

    # q = queue.Queue 
    # q = mp.Queue
    q = DataQueue

    # Create data queues
    for s in sensor_group.values():
        data_registry[s.sid] = q(maxsize=1)
        s.data_registry = data_registry

    # therm.read_one()
    # therm.report()
    # camera.read_one()
    # camera.report()

    # Initialize all sensors with their data queues
    controller = SensorHandler(sensor_group)
    controller.initialize(data_registry)
    
    # Run Sensors in their own processes
    controller.run_all()

