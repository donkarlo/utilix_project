from collections.abc import MutableSequence

class ValuesSlice():
    def __init__(self, values:MutableSequence, slc:slice):
        self._values:MutableSequence = values
        self._slice = slc

    def get_slice(self):
        return self._slice

    def get_values(self):
        return self._values

