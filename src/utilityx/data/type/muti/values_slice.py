from collections.abc import MutableSequence

class VeluesSlice():
    def __init__(self, values:MutableSequence, slc:slice):
        self._values:MutableSequence = values
        self._slice = slc

    def _get_slice(self):
        return self._slice

    def _get_values(self):
        return self._values

