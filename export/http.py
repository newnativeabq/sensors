# http.py

import requests
from requests_toolbelt import MultipartEncoder
from .reporter import Reporter



class HTTP(Reporter):
    def __init__(self, **kwargs):
        self.setup(**kwargs)
 
    def setup(self, **kwargs):
        super().setup(**kwargs)
        self.target = kwargs['target']
        self.auth = kwargs['auth']


    def send(self, data):
        m = self.translate(data)
        print(m.content_type)
        requests.post(self.target, data=m, 
                        headers={'Content-Type': m.content_type})


    def translate(self, data:dict) -> MultipartEncoder:
        def _get_value(data, key):
            if key in data:
                return data[key]

        m = MultipartEncoder(
            fields = {
                'value': str(data['value']),
                'file': (
                    _get_value(data, 'filename'),
                    _get_value(data, 'file')
                    )
            }
        )

        return m