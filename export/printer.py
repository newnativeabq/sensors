# printer.py

from .reporter import Reporter

class Printer(Reporter):
    def __init__(self, **kwargs):
        super().setup(**kwargs)


    def translate(self, data:dict):
        return super().translate(data)


    def send(self, data):
        payload = self.translate(data)
        print(payload)