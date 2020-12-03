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
        pass

    def send(self, data):
        pass

    def translate(self, data):
        def _get_value(data, key):
            if key in data:
                return data[key]

        payload = {}
        payload['sid'] = _get_value(data, 'sid')
        payload['value'] = _get_value(data, 'value')
        payload['files'] = _compose_files(
            _get_value(data, 'files')
        )
        return payload


def _compose_files(file_item: tuple):
    if file_item is not None:
        if len(file_item) == 3:
            return [
                ('file', file_item)
            ]
        else:
            raise ValueError("File Item length not equal 3.  \
                Use 3 tuple format (file_name, file_data, filetype)")
    return

                