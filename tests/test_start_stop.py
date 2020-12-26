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
        threaded = False
    )
    return s