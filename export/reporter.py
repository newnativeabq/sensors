# reporter.py

class Reporter():
    """
    Reporter
        Base class for reporting sensor data.
        Goal is to fill a 'template' that the specific implementation
            will translate.
    """
    def __init__(self, **kwargs):
        pass

    def setup(self, **kwargs):
        if 'sid' in kwargs:
            self.sid = kwargs['sid']
        if 'template' in kwargs:
            self.template = kwargs['template']
            self.template['sid'] = self.sid

    def send(self, data):
        pass

    def translate(self, data):
        return data



class Printer(Reporter):
    def __init__(self, **kwargs):
        super().setup(**kwargs)

    def translate(self, data):
        packet = self.template
        packet['value'] = data['value']
        payload = {'data': packet}

        if 'files' in data:
            payload['files'] = data['files']

        return payload

    def send(self, data):
        payload = self.translate(data)
        print(payload)