from typing import Iterable


class Iterablex(Iterable):
    def __init__(self):
        pass

    def isinstance(self, obj):
        return isinstance(obj, Iterable)

    def __next__(self):
        pass


    def __iter__(self):
        pass