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
    target="http://192.168.1.37:8080/api/data",
    auth=None,
    freq=0.25,
    template={'sid':None, 'value':None},
    threaded=True
)
sensor_group.register(therm)


camera = Sensor(
    sid='camera1',
    device=Camera,
    reporter=HTTP,
    target="http://192.168.1.37:8080/api/data",
    auth=None,
    freq=0.1,
    template={'sid':None, 'value':None}
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
    camera.read_one()
    camera.report()

    # p = mp.Process(target=start_sensor, args=(sensor_group.values()[0],))
    # p.start()

    # # Initialize all sensors with their data queues
    # controller = SensorHandler(sensor_group)
    # controller.initialize(data_registry)
    
    # # Run Sensors in their own processes
    # controller.run_all()

