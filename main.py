"""
Main.py

Set up sensor collection and reading suite
"""

from device import W1Therm, Sensor
from export import HTTP


### Configure Sensors ###

therm = Sensor(
    device=W1Therm(),
    reporter=HTTP(target="192.168.1.1:8888/pi", auth=None),
    freq=2,
)


therm.read_one()
therm.report()

therm.run()