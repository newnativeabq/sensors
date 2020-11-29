#camera.py

from picamera import PiCamera 
import io 
# from PIL import Image



class Camera():
    def __init__(self, **kwargs):
        self.setup_system()


    def setup_system(self):
        self.camera = PiCamera()


    def _validate_data(self, data):
        return data


    def read(self):
        stream = io.BytesIO()
        self.camera.capture(stream, format='png')
        payload = {
            'value': 1,
            'files': {'file': stream.getvalue()}
            }
        stream.close()
        return payload