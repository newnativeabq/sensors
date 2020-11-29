"""
Main.py

Set up sensor collection and reading suite
"""

from device import W1Therm, Sensor, Camera
from export import HTTP, Printer


### Configure Sensors ###

therm = Sensor(
    sid='therm1',
    device=W1Therm,
    reporter=HTTP,
    target="http://192.168.1.37:8080/api/data",
    auth=None,
    freq=2,
    template={'sid':None, 'value':None, 'files':{}},
)

camera = Sensor(
    sid='camera1',
    device=Camera,
    reporter=HTTP,
    target="http://192.168.1.37:8080/api/data",
    auth=None,
    freq=2,
    template={'sid':None, 'value':None, 'files':None}
)

# Example with printer
# therm = Sensor(
#     sid='therm1',
#     device=W1Therm,
#     reporter=Printer,
#     freq=2,
#     template={'sid':None,'value':None},
# )

# camera = Sensor(
#     sid='camera1',
#     device=Camera,
#     reporter=Printer,
#     freq=2,
#     template={'sid':None, 'value':None, 'files':None}
# )

# camera.read_one()
# therm.read_one()
# camera.report()
# therm.report()


camera.run()
# therm.run()