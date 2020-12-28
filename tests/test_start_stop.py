from device import Sensor, Timer
from export import Printer

import pytest


@pytest.fixture
def tsensor():
    s = Sensor(
        sid = 's',
        device = Timer,
        reporter = Printer,
        freq = 0.25,
        threaded = True
    )
    return s
    


def test_start_stop_sensor(tsensor):
    tsensor.start()  # Will spawn rogue process if no redis connection... TODO?
    tsensor.stop()  # this won't work with unthreaded start (blocks)