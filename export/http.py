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
        payload = self.translate(data)
        requests.post(self.target, **payload)


    def translate(self, data):
        packet = self.template
        packet['value'] = data['value']
        payload = {'data': packet}

        if 'files' in data:
            payload['files'] = data['files']

        return payload