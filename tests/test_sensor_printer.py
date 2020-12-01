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
    threaded = True,
)

camera = Sensor(
    sid='camera1',
    device=Camera,
    reporter=HTTP,
    target="http://192.168.1.37:8080/api/data",
    auth=None,
    freq=2,
    template={'sid':None, 'value':None, 'files':None}
    threaded = True,
)

# # Example with printer
# therm = Sensor(
#     sid='therm1',
#     device=W1Therm,
#     reporter=Printer,
#     freq=0.25,
#     template={'sid':None,'value':None},
#     threaded=False,
# )

# camera = Sensor(
#     sid='camera1',
#     device=Camera,
#     reporter=Printer,
#     freq=2,
#     template={'sid':None, 'value':None, 'files':None},
    # threaded=False
# )

# camera.read_one()
# therm.read_one()
# camera.report()
# therm.report()


# camera.run()
# therm.run()