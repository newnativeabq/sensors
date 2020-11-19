# http.py

import requests
from .reporter import Reporter



class HTTP(Reporter):
    def __init__(self, **kwargs):
        self.setup(**kwargs)
 
    def setup(self, **kwargs):
        super().setup(**kwargs)
        self.target = kwargs['target']
        self.auth = kwargs['auth']


    def send(self, data):
        payload, stream = self.translate(data)
        requests.post(self.target, data=payload)


    def translate(self, data):
        packet = self.template
        packet['value'] = data['value']
        if 'attachment' in data:
            stream = data['attachhment'] # TODO: this can not be sent as is
        else:
            stream = None
        return packet, stream