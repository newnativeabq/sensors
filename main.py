"""
Main.py

Set up sensor collection and reading suite
"""

from device import GPIO, Sensor
from export import HTTP


### Configure Sensors ###

therm = Sensor(
    reader=GPIO(device="thermometer"),
    reporter=HTTP(target="192.168.1.1:8888/pi", auth=None)
)

print(therm)