#camera.py

from picamera import PiCamera 
import io 
# from PIL import Image



class Camera():
    def __init__(self, **kwargs):
        self.setup_system()


    def setup_system(self):
        pass

    
    def setup_camera(self, camera: PiCamera):
        camera.meter_mode = 'matrix'
        camera.flash_mode = 'auto'

    def _validate_data(self, data):
        return data


    def read(self):
        stream = io.BytesIO()
        with PiCamera() as camera:
            self.setup_camera(camera)
            camera.capture(stream, format='png')

        payload = {
            'value': 0,
            'files': ('img', stream.getvalue(), 'image/png'),
        }
        stream.close()
        return payload