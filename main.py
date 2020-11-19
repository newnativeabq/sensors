"""
Main.py

Set up sensor collection and reading suite
"""

from device import W1Therm, Sensor
from export import HTTP, Printer


### Configure Sensors ###

therm = Sensor(
    sid='therm1',
    device=W1Therm(),
    reporter=HTTP,
    target="http://192.168.1.37:8080/api/data",
    auth=None,
    freq=2,
    template={'sid':None,'value':None},
)

# Example with printer
# therm = Sensor(
#     sid='therm1',
#     device=W1Therm(),
#     reporter=Printer,
#     freq=2,
#     template={'sid':None,'value':None},
# )

therm.read_one()
therm.report()

therm.run()