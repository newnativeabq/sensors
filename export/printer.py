# printer.py

from .reporter import Reporter

class Printer(Reporter):
    def __init__(self, **kwargs):
        super().setup(**kwargs)


    def translate(self, data:dict):
        def _get_value(data, key):
            if key in data:
                return data[key]

        payload = {}
        
        payload['value'] = _get_value(data, 'value')
        payload['file'] = _get_value(data, 'file')

        return payload


    def send(self, data):
        payload = self.translate(data)
        print(payload)