# test_controller.py


import pytest
from controller import SensorHandler
from device import Sensor, Timer, DataQueue
from export import Printer
from registry import Registry



@pytest.fixture 
def sregistry():
    rg = Registry()
    s = Sensor(
        sid = 's',
        device = Timer,
        reporter = Printer,
        freq = 0.25,
        threaded = True
    )
    rg.register(s)
    return rg

@pytest.fixture 
def sdata():
    dg = Registry()
    dg['s'] = DataQueue(maxsize=1)
    return dg



def test_make_handler(sregistry, sdata):
    h = SensorHandler(sregistry)
    h.initialize(sdata)