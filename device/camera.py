#camera.py

from picamera import PiCamera 
import time 
import io 
# from PIL import Image



class Camera():
    def __init__(self, **kwargs):
        self.setup_system()


    def setup_system(self):
        self.camera = PiCamera()
        self.io = io.BytesIO()
        

    def _validate_data(self, data):
        return data


    def read(self):
        self.camera.capture(self.io, format='png')
        self.io.seek(0)
        return {
            'value': 1,
            'files': (
                str(time.time()).split('.')[0] + '.png', 
                self.io,
                'image/png')
            }