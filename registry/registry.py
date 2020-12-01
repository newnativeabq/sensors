
"""
Registry

A mechanism of creating function lookups on import to avoid 
large dictionaries in the module.
"""


class Registry():
    """ Emulate dictionary with custom register function """
    def __init__(self, name=None):
        if name is None:
            self.name = __name__
        else:
            self.name = name
        self.store = {}


    def __repr__(self):
        return f'{self.store}'

    def __len__(self):
        return len(self.store)

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def values(self):
        return list(self.store.values())

    def register(self, obj, **kwargs):
        self.store[obj.__name__] = obj

