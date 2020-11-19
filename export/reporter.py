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

    def send(self, data):
        payload = self.template
        payload['value'] = data['value']
        print(payload)