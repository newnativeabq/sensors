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
        # stream.seek(0)
        payload = {
            'value': 0,
            'files': ('img', stream.getvalue(), 'image/png'),
        }
        stream.close()
        return payload