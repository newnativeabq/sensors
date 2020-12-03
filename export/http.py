# http.py

import requests
from .reporter import Reporter



class HTTP(Reporter):
    def __init__(self, **kwargs):
        self.setup(**kwargs)
 

    def setup(self, **kwargs):
        super().setup(**kwargs)
        self.target = _validate_url(kwargs['target'])
        self.auth = kwargs['auth']
        self.headers = {
            'Accept': "*/*",
            'Accept-Encoding': 'gzip, deflate, br',
        }


    def send(self, data):
        payload, files = self.translate(data)
        if files is not None:
            r = requests.post(self.target, 
                headers=self.headers, files=files, data=payload)
        else:
            r = requests.post(self.target, headers=self.headers, data=payload)
            

    def translate(self, data:dict):
        payload = super().translate(data)
        files = payload['files']
        payload.pop('files')
        return payload, files



def _validate_url(url: str) -> str:
    if url[-1] == '/':
        return url 
    else:
        return url + '/'